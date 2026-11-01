//! Research adapter only. All semantic identities and causal judgments are Adva's.
use adva_ir::{
    CompilationArtifact, GraftFrameKind, NodeId, OccurrenceId, SharedProgramDiagram, SourceId,
    WireProducer,
};
use adva_lisp::{
    advance_causal_cut, analyze_program_slice_with_graft, compile_function, import_diagram_json,
    link_modules, parse_module,
};
use serde_json::{Value, json};
use std::collections::BTreeSet;
use std::sync::atomic::{AtomicUsize, Ordering};
static ADVANCE_ATTEMPTS: AtomicUsize = AtomicUsize::new(0);

const SPINE: &str = include_str!("../fixtures/spine.adva");
const EXPANDED: &str = include_str!("../fixtures/expanded.adva");
const TREE: &str = include_str!("../fixtures/tree.json");
const REV: &str = "87a1a6933bca3fdb5c176cbf612729e278d172f7";
type Check<T> = Result<T, String>;

fn require(ok: bool, reason: &str) -> Check<()> {
    if ok { Ok(()) } else { Err(reason.to_owned()) }
}

fn compile(source: &str, module: &str) -> CompilationArtifact {
    let linked = link_modules(vec![parse_module(source).expect("parse fixed module")])
        .expect("link fixed module");
    let a = compile_function(&linked, module, "root").expect("compile fixed root");
    assert!(a.certificate.certified() && a.graft_trace.certificate.certified());
    a
}

fn revalidate(a: &CompilationArtifact) -> Check<()> {
    let imported = import_diagram_json(&a.result.to_json().map_err(|e| e.to_string())?)
        .map_err(|e| e.to_string())?;
    require(imported.certificate.certified(), "import not certified")?;
    let all: Vec<_> = imported.result.nodes.iter().map(|n| n.id).collect();
    let slice =
        analyze_program_slice_with_graft(&imported.result, &a.graft_trace.result, &[], &all)
            .map_err(|e| e.to_string())?;
    require(slice.certificate.certified(), "graft slice not certified")
}

fn bind_source(candidate: &CompilationArtifact, expected: &CompilationArtifact) -> Check<()> {
    revalidate(candidate)?;
    require(candidate == expected, "source_artifact_binding_mismatch")
}

fn permutations(xs: &[NodeId]) -> Vec<Vec<NodeId>> {
    if xs.is_empty() {
        return vec![vec![]];
    }
    let mut out = vec![];
    for (i, x) in xs.iter().enumerate() {
        let mut rest = xs.to_vec();
        rest.remove(i);
        for mut suffix in permutations(&rest) {
            suffix.insert(0, *x);
            out.push(suffix);
        }
    }
    out
}

fn replay(d: &SharedProgramDiagram, word: &[NodeId]) -> Check<Vec<Value>> {
    let mut done = vec![];
    let mut steps = vec![];
    for event in word {
        require(
            ADVANCE_ATTEMPTS.fetch_add(1, Ordering::Relaxed) < 4500,
            "native_advance_budget",
        )?;
        let a = advance_causal_cut(d, &done, *event).map_err(|e| e.to_string())?;
        require(a.certificate.certified(), "step not certified")?;
        done = a.result.after.completed.clone();
        steps.push(serde_json::to_value(a).unwrap());
    }
    require(done.len() == d.nodes.len(), "incomplete_schedule")?;
    Ok(steps)
}

fn inv(word: &[NodeId], corner: &[NodeId]) -> usize {
    let position = |id| word.iter().position(|v| *v == id).unwrap();
    (0..corner.len())
        .map(|i| {
            ((i + 1)..corner.len())
                .filter(|j| position(corner[i]) > position(corner[*j]))
                .count()
        })
        .sum()
}

fn corner_visit(d: &SharedProgramDiagram, id: NodeId, out: &mut Vec<NodeId>) {
    assert!(
        !out.contains(&id),
        "this finite corner reader excludes sharing"
    );
    out.push(id);
    let node = d.nodes.iter().find(|n| n.id == id).unwrap();
    for wire in &node.inputs {
        if let WireProducer::Node { node } = wire.producer {
            corner_visit(d, node, out);
        }
    }
}

fn orders(a: &CompilationArtifact) -> Value {
    revalidate(a).unwrap();
    let d = &a.result;
    assert!((1..=6).contains(&d.nodes.len()));
    assert_eq!(d.signature.inputs.len(), 1);
    assert_eq!(d.outputs.len(), 1);
    let ids: Vec<_> = d.nodes.iter().map(|n| n.id).collect();
    let mut edges = BTreeSet::new();
    for n in &d.nodes {
        for wire in &n.inputs {
            if let WireProducer::Node { node } = wire.producer {
                edges.insert((node, n.id));
            }
        }
    }
    let mut closure = edges.clone();
    loop {
        let mut next = closure.clone();
        for (u, v) in &closure {
            for (w, x) in &closure {
                if v == w {
                    next.insert((*u, *x));
                }
            }
        }
        if next == closure {
            break;
        }
        closure = next;
    }
    let WireProducer::Node { node: root } = d.outputs[0].producer else {
        panic!("no event root")
    };
    let mut corner = vec![];
    corner_visit(d, root, &mut corner);
    assert_eq!(corner.len(), ids.len());
    let candidates = permutations(&ids);
    let mut legal = vec![];
    let mut rejected = 0;
    for word in &candidates {
        let by_poset = closure
            .iter()
            .all(|(u, v)| word.iter().position(|x| x == u) < word.iter().position(|x| x == v));
        let native = replay(d, word).is_ok();
        assert_eq!(native, by_poset, "native/poset discrepancy on {word:?}");
        if native {
            legal.push(word.clone());
        } else {
            rejected += 1;
        }
    }
    let best = legal.iter().map(|w| inv(w, &corner)).min().unwrap();
    let minimizers: Vec<_> = legal
        .iter()
        .filter(|w| inv(w, &corner) == best)
        .cloned()
        .collect();
    assert_eq!(minimizers.len(), 1);
    let canonical = &minimizers[0];
    json!({"event_ids":ids, "dependency_edges":edges, "strict_order":closure,
        "corner_order":corner, "linear_extensions":legal, "schedule_count":legal.len(),
        "permutations_tested":candidates.len(), "rejected_permutations":rejected,
        "canonical_schedule":canonical, "canonical_inversions":best,
        "canonical_steps":replay(d, canonical).unwrap()})
}

// Parse only the contract's multiplication-by-minus-one single-spine grammar.
// This is a syntactic profile check, not a semantic identity allocator.
fn tree_contexts(t: &Value, out: &mut Vec<Value>) -> Check<()> {
    if t.get("hole").is_some() {
        return require(t == &json!({"hole":"x"}), "unsupported hole");
    }
    require(t["op"] == "mul", "unsupported context operation")?;
    let (inner, constant, slot) = if t["left"].get("constant").is_some() {
        (&t["right"], &t["left"], 2)
    } else {
        (&t["left"], &t["right"], 1)
    };
    require(
        constant == &json!({"constant":-1}),
        "branching_or_unsupported_parameter",
    )?;
    tree_contexts(inner, out)?;
    out.push(json!({"tree_vertex":t["id"], "operation":"mul", "constant":-1, "slot":slot}));
    Ok(())
}

fn spine_mapping(a: &CompilationArtifact) -> Check<Value> {
    revalidate(a)?;
    let d = &a.result;
    require(d.nodes.len() == 3, "expected_three_native_events")?;
    // Recover the chain backward through exact wires, independent of node numbering.
    let mut current = d.outputs[0].clone();
    let mut backwards = vec![];
    while let WireProducer::Node { node } = current.producer {
        let n = d
            .nodes
            .iter()
            .find(|n| n.id == node)
            .ok_or("missing event")?;
        require(
            n.operation.name == "neg" && n.inputs.len() == 1,
            "unsupported_unary_realization",
        )?;
        backwards.push(node);
        current = n.inputs[0].clone();
    }
    require(
        current.producer == WireProducer::Input { index: 0 },
        "wrong_hole",
    )?;
    backwards.reverse();
    let tree: Value = serde_json::from_str(TREE).unwrap();
    let mut contexts = vec![];
    tree_contexts(&tree, &mut contexts)?;
    require(
        backwards.len() == contexts.len(),
        "context_event_cardinality",
    )?;
    let mut rows = vec![];
    for (event, mut context) in backwards.into_iter().zip(contexts) {
        let frames: Vec<_> = a
            .graft_trace
            .result
            .frames
            .iter()
            .filter(|f| f.kind == GraftFrameKind::Call && f.body_region == vec![event])
            .collect();
        require(frames.len() == 1, "context_frame_not_unique")?;
        let frame = frames[0];
        require(frame.holes.len() == 1, "context_hole_arity")?;
        let slot = match frame.callee.function.as_str() {
            "mul-m1-s1" => 1,
            "mul-m1-s2" => 2,
            _ => return Err("unknown_context_signature".to_owned()),
        };
        require(context["slot"] == slot, "slot_mismatch")?;
        context["event"] = json!(event);
        context["frame_id"] = json!(frame.id);
        context["callee"] = json!(frame.callee);
        rows.push(context);
    }
    Ok(json!(rows))
}

fn negative_controls(a: &CompilationArtifact) -> Value {
    let mut controls = vec![];
    let mut reject = |name: &str, layer: &str, result: Check<()>| {
        let reason = result.expect_err("negative control unexpectedly accepted");
        controls.push(json!({"name":name,"layer":layer,"outcome":"rejected","reason":reason}));
    };
    let wrong_slot = compile(
        &SPINE.replace("(call mul-m1-s2 ", "(call mul-m1-s1 "),
        "oq1007-spine",
    );
    revalidate(&wrong_slot).unwrap(); // A valid different program; not an invalid Adva diagram.
    assert_eq!(wrong_slot.result.nodes, a.result.nodes); // same numeric carrier is insufficient
    reject(
        "wrong_slot_same_event_graph",
        "research_signature_binding",
        spine_mapping(&wrong_slot).map(|_| ()),
    );
    let ids: Vec<_> = a.result.nodes.iter().map(|n| n.id).collect();
    reject(
        "wrong_execution_order",
        "native_causal_step",
        replay(&a.result, &[ids[1], ids[0], ids[2]]).map(|_| ()),
    );
    reject(
        "duplicate_event",
        "native_causal_step",
        replay(&a.result, &[ids[0], ids[0], ids[1], ids[2]]).map(|_| ()),
    );
    reject(
        "missing_event",
        "research_complete_schedule",
        replay(&a.result, &ids[..2]).map(|_| ()),
    );
    reject(
        "unknown_event",
        "native_causal_step",
        replay(&a.result, &[NodeId(u32::MAX)]).map(|_| ()),
    );
    let mut occurrence = a.clone();
    occurrence.result.nodes[0].inputs[0].lineage[0] = OccurrenceId::explicit("occurrence:wrong");
    reject(
        "occurrence_substitution",
        "native_diagram_import",
        revalidate(&occurrence),
    );
    let mut source = a.clone();
    source.result.occurrences[0].source = SourceId::explicit("source:wrong");
    reject(
        "source_substitution",
        "native_diagram_import",
        revalidate(&source),
    );
    let foreign = compile(
        &SPINE.replace("oq1007-spine", "oq1007-foreign"),
        "oq1007-foreign",
    );
    revalidate(&foreign).unwrap();
    assert_eq!(
        foreign
            .result
            .nodes
            .iter()
            .map(|n| n.id)
            .collect::<Vec<_>>(),
        ids
    );
    reject(
        "valid_foreign_program_same_node_numbers",
        "research_source_binding",
        bind_source(&foreign, a),
    );
    let mut graft = a.clone();
    let f = graft
        .graft_trace
        .result
        .frames
        .iter_mut()
        .find(|f| f.kind == GraftFrameKind::Call)
        .unwrap();
    f.holes[0].entry_wire.output_index = 99;
    reject(
        "graft_hole_substitution",
        "native_graft_revalidation",
        revalidate(&graft),
    );
    json!(controls)
}

fn produce() -> Value {
    let spine = compile(SPINE, "oq1007-spine");
    let expanded = compile(EXPANDED, "oq1007-expanded");
    let report = orders(&spine);
    let expansion_report = orders(&expanded);
    // Record, do not quotient away, extra constant events.
    let mul_ids: BTreeSet<_> = expanded
        .result
        .nodes
        .iter()
        .filter(|n| n.operation.name == "mul")
        .map(|n| n.id)
        .collect();
    let projections: BTreeSet<Vec<NodeId>> = expansion_report["linear_extensions"]
        .as_array()
        .unwrap()
        .iter()
        .map(|w| {
            let ids: Vec<NodeId> = serde_json::from_value(w.clone()).unwrap();
            ids.into_iter().filter(|id| mul_ids.contains(id)).collect()
        })
        .collect();
    let controls = negative_controls(&spine);
    let attempts = ADVANCE_ATTEMPTS.load(Ordering::Relaxed);
    json!({"native_advance_attempts":attempts, "schema":"aeg.oq1007.native-sequential.v1", "adva_revision":REV,
        "tree":serde_json::from_str::<Value>(TREE).unwrap(),
        "spine":{"artifact":spine, "mapping":spine_mapping(&spine).unwrap(), "orders":report},
        "expanded":{"artifact":expanded,"orders":expansion_report,"arithmetic_event_projections":projections},
        "negative_controls":controls,
        "status":{"theorem_5_2":"proved_abstract_sequential_only","this_fixture":"computationally_verified_example",
            "conjecture_5_3":"open","oq100_7":"open_partial_fixture","full_193_native_census":"not_run","carrier_check":"not_run"}})
}

fn receive(path: &str) -> Check<()> {
    require(
        std::fs::metadata(path).map_err(|e| e.to_string())?.len() <= 1024 * 1024,
        "candidate_size_budget",
    )?;
    let bytes = std::fs::read(path).map_err(|e| e.to_string())?;
    require(bytes.len() <= 1024 * 1024, "candidate_size_budget")?;
    let saved: Value = serde_json::from_slice(&bytes).map_err(|e| e.to_string())?;
    let expected = produce();
    for name in ["spine", "expanded"] {
        let candidate: CompilationArtifact =
            serde_json::from_value(saved[name]["artifact"].clone()).map_err(|e| e.to_string())?;
        let fresh: CompilationArtifact =
            serde_json::from_value(expected[name]["artifact"].clone()).unwrap();
        bind_source(&candidate, &fresh)?;
        require(
            saved[name]["orders"] == expected[name]["orders"],
            "stored_order_report_mismatch",
        )?;
    }
    require(saved == expected, "candidate_report_mismatch")
}

fn main() {
    let args: Vec<_> = std::env::args().collect();
    match args.get(1).map(String::as_str) {
        Some("produce") if args.len() == 2 => {
            println!("{}", serde_json::to_string_pretty(&produce()).unwrap())
        }
        Some("receive") if args.len() == 3 => match receive(&args[2]) {
            Ok(()) => println!(
                "accepted: fresh native import, graft check, source binding and exhaustive replay"
            ),
            Err(e) => {
                eprintln!("rejected: {e}");
                std::process::exit(1);
            }
        },
        _ => {
            eprintln!("usage: aeg-oq1007-native produce | receive FILE");
            std::process::exit(2);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn branching_is_refused_by_the_spine_adapter() {
        let leaf = json!({"id":"v", "op":"mul","left":{"hole":"x"},"right":{"constant":-1}});
        let branching = json!({"id":"r","op":"mul","left":leaf,"right":leaf});
        assert_eq!(
            tree_contexts(&branching, &mut vec![]),
            Err("branching_or_unsupported_parameter".to_owned())
        );
    }
    #[test]
    fn finite_native_counts_and_mutations() {
        let ev = produce();
        assert_eq!(ev["spine"]["orders"]["schedule_count"], 1);
        assert_eq!(ev["spine"]["orders"]["canonical_inversions"], 3);
        assert_eq!(ev["expanded"]["orders"]["schedule_count"], 15);
        assert_eq!(ev["negative_controls"].as_array().unwrap().len(), 9);
    }
}
