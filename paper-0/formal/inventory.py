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
    mappings = [mapping, appendix]
    for reviewed in mappings:
        if digest(ROOT / reviewed["source"]) != reviewed["source_sha256"]:
            raise ValueError("reviewed formal correspondence has source drift: " + reviewed["source"])
    claims = []
    for path in sources():
        # Preserve newlines so navigation locations remain useful.
        text = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text())
        for match in ENV.finditer(text):
            labels = re.findall(r"\\label\{([^}]+)\}", match[3])
            line = text[:match.start()].count("\n") + 1
            attached = [s["id"] for s in statements if s["source"] == str(path.relative_to(ROOT)) and s["label"] in labels]
            lean = sorted({name for reviewed in mappings for row in reviewed["mapping"]
                           if str(path.relative_to(ROOT)) == reviewed["source"] and set(labels) & set(row["source_labels"])
                           for name in row["formal"]})
            claims.append({"source": str(path.relative_to(ROOT)), "line": line,
                           "environment": match[1], "title": match[2], "labels": labels,
                           "formal_status": "component-map-supplied" if lean else "fragment-certificate-supplied" if attached else "not-yet-formalized",
                           "certificates": attached, "lean_components": lean})
    return {"schema": "aeg.paper0.formal.inventory.v3",
            "scope": "Theorem-like environments in recursively included TeX files; prose/equation coverage and dependencies require review. No proof truth is assigned by this inventory.",
            "sources": {str(path.relative_to(ROOT)): digest(path) for path in sources()},
            "definition_map_sha256": digest(HERE / "definition-map.json"),
            "appendix_map_sha256": digest(HERE / "appendix-map.json"),
            "claims": claims}


if __name__ == "__main__":
    (HERE / "inventory.json").write_text(json.dumps(generate(), indent=2) + "\n")
