"""Inventory current theorem-like environments, without assigning proof truth."""

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ENV = re.compile(r"\\begin\{(theorem|proposition|lemma|corollary|definition|example|convention|remark|warning)\}(?:\[([^\]]*)\])?(.*?)\\end\{\1\}", re.S)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources():
    """Follow the manuscript's input order, including nested subsection inputs."""
    result, seen = [], set()

    def walk(path):
        if path in seen:
            raise ValueError("duplicate/cyclic manuscript input: " + str(path))
        seen.add(path)
        result.append(path)
        # Commented installation examples are not manuscript inputs.
        active = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text())
        for name in re.findall(r"\\input\{([^}]+)\}", active):
            candidate = ROOT / "paper-0" / name
            if not candidate.suffix:
                candidate = candidate.with_suffix(".tex")
            walk(candidate)

    walk(ROOT / "paper-0/aeg-paper-0.tex")
    return result


def generate():
    statements = json.loads((HERE / "statements.json").read_text())
    mapping = json.loads((HERE / "definition-map.json").read_text())
    appendix = json.loads((HERE / "appendix-map.json").read_text())
    evaluability = json.loads((HERE / "evaluability-map.json").read_text())
    chapter03 = json.loads((HERE / "chapter03-map.json").read_text())
    analysis = json.loads((HERE / "analysis-map.json").read_text())
    chapter04 = json.loads((HERE / "chapter04-map.json").read_text())
    apollonius = json.loads((HERE / "apollonius-map.json").read_text())
    projective = json.loads((HERE / "projective-map.json").read_text())
    pgl = json.loads((HERE / "pgl-map.json").read_text())
    affine_generation = json.loads((HERE / "affine-generation-map.json").read_text())
    arithmetic = json.loads((HERE / "arithmetic-map.json").read_text())
    bruhat = json.loads((HERE / "bruhat-map.json").read_text())
    fixed_points = json.loads((HERE / "fixed-points-map.json").read_text())
    cardinality = json.loads((HERE / "cardinality-map.json").read_text())
    normalization = json.loads((HERE / "normalization-map.json").read_text())
    geometry = json.loads((HERE / "geometry-map.json").read_text())
    mappings = [mapping, appendix, evaluability, chapter03, analysis, chapter04, apollonius, projective, pgl, affine_generation, arithmetic, bruhat, fixed_points, cardinality, normalization, geometry]
    for reviewed in mappings:
        if digest(ROOT / reviewed["source"]) != reviewed["source_sha256"]:
            raise ValueError("reviewed formal correspondence has source drift: " + reviewed["source"])
        for source, expected in reviewed.get("additional_sources", {}).items():
            if digest(ROOT / source) != expected:
                raise ValueError("reviewed formal correspondence has source drift: " + source)
    claims = []
    for path in sources():
        # Preserve newlines so navigation locations remain useful.
        text = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text())
        for match in ENV.finditer(text):
            labels = re.findall(r"\\label\{([^}]+)\}", match[3])
            line = text[:match.start()].count("\n") + 1
            attached = [s["id"] for s in statements if s["source"] == str(path.relative_to(ROOT)) and s["label"] in labels]
            lean = sorted({name for reviewed in mappings for row in reviewed["mapping"]
                           if str(path.relative_to(ROOT)) == row.get("source", reviewed["source"]) and set(labels) & set(row["source_labels"])
                           for name in row["formal"]})
            claims.append({"source": str(path.relative_to(ROOT)), "line": line,
                           "environment": match[1], "title": match[2], "labels": labels,
                           "formal_status": "component-map-supplied" if lean else "fragment-certificate-supplied" if attached else "not-yet-formalized",
                           "certificates": attached, "lean_components": lean})
    # Some certified components belong to a numbered equation and surrounding
    # prose, not a theorem-like environment. Keep their navigation separate so
    # the environment counts are not inflated by an invented theorem.
    equations = {}
    for reviewed in mappings:
        for row in reviewed["mapping"]:
            if row.get("anchor_kind") != "equation":
                continue
            source = row.get("source", reviewed["source"])
            text = re.sub(r"(?<!\\)%[^\n]*", "", (ROOT / source).read_text())
            for label in row["source_labels"]:
                match = re.search(r"\\begin\{equation\}(?:(?!\\end\{equation\}).)*?\\label\{" +
                                  re.escape(label) + r"\}", text, re.S)
                if match is None:
                    raise ValueError("reviewed equation anchor missing: " + label)
                key = (source, label)
                target = equations.setdefault(key, {"source": source, "label": label,
                    "line": text[:match.start()].count("\n") + 1,
                    "formal_status": "component-map-supplied", "lean_components": [], "coverage": []})
                target["lean_components"] = sorted(set(target["lean_components"]) | set(row["formal"]))
                target["coverage"].append(row["coverage"])
    return {"schema": "aeg.paper0.formal.inventory.v3",
            "scope": "Theorem-like environments in recursively included TeX files; prose/equation coverage and dependencies require review. No proof truth is assigned by this inventory.",
            "sources": {str(path.relative_to(ROOT)): digest(path) for path in sources()},
            "definition_map_sha256": digest(HERE / "definition-map.json"),
            "appendix_map_sha256": digest(HERE / "appendix-map.json"),
            "evaluability_map_sha256": digest(HERE / "evaluability-map.json"),
            "chapter03_map_sha256": digest(HERE / "chapter03-map.json"),
            "analysis_map_sha256": digest(HERE / "analysis-map.json"),
            "chapter04_map_sha256": digest(HERE / "chapter04-map.json"),
            "apollonius_map_sha256": digest(HERE / "apollonius-map.json"),
            "projective_map_sha256": digest(HERE / "projective-map.json"),
            "pgl_map_sha256": digest(HERE / "pgl-map.json"),
            "affine_generation_map_sha256": digest(HERE / "affine-generation-map.json"),
            "arithmetic_map_sha256": digest(HERE / "arithmetic-map.json"),
            "bruhat_map_sha256": digest(HERE / "bruhat-map.json"),
            "fixed_points_map_sha256": digest(HERE / "fixed-points-map.json"),
            "cardinality_map_sha256": digest(HERE / "cardinality-map.json"),
            "normalization_map_sha256": digest(HERE / "normalization-map.json"),
            "geometry_map_sha256": digest(HERE / "geometry-map.json"),
            "equation_components": list(equations.values()),
            "claims": claims}


if __name__ == "__main__":
    (HERE / "inventory.json").write_text(json.dumps(generate(), indent=2) + "\n")
