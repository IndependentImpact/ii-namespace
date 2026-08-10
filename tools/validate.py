#!/usr/bin/env python3
"""Validate the repo's semantic artifacts.

- Every ns/**/*.ttl must parse as Turtle.
- ns/contexts.jsonld must parse as JSON (and as JSON-LD once it is no longer a stub).
- In ns/config/, every skos:Concept must be in a skos:ConceptScheme defined in
  the same file, every scheme must have at least one concept, and every
  concept must carry skos:notation (the wire value) and skos:prefLabel.

Scheme-membership validation against the platform shapes lives in ii-backend
(assets/storage-service/shacl-shapes/); this script only guards what this
repo can check on its own.
"""

import json
import sys
from pathlib import Path

from rdflib import Graph, RDF, Namespace

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
ROOT = Path(__file__).resolve().parent.parent

errors = []


def check_turtle(path: Path) -> Graph | None:
    try:
        return Graph().parse(path, format="turtle")
    except Exception as e:
        errors.append(f"{path.relative_to(ROOT)}: does not parse as Turtle: {e}")
        return None


def check_config_scheme(path: Path, g: Graph) -> None:
    rel = path.relative_to(ROOT)
    schemes = set(g.subjects(RDF.type, SKOS.ConceptScheme))
    concepts = set(g.subjects(RDF.type, SKOS.Concept))
    if not schemes:
        errors.append(f"{rel}: no skos:ConceptScheme defined")
    for c in concepts:
        in_schemes = set(g.objects(c, SKOS.inScheme))
        if not in_schemes:
            errors.append(f"{rel}: concept {c} has no skos:inScheme")
        elif not in_schemes & schemes:
            errors.append(f"{rel}: concept {c} is only in schemes not defined in this file")
        if (c, SKOS.notation, None) not in g:
            errors.append(f"{rel}: concept {c} has no skos:notation (wire value)")
        if (c, SKOS.prefLabel, None) not in g:
            errors.append(f"{rel}: concept {c} has no skos:prefLabel")
    for s in schemes:
        if not any(g.subjects(SKOS.inScheme, s)):
            errors.append(f"{rel}: scheme {s} has no concepts")


def check_contexts_jsonld(path: Path) -> None:
    rel = path.relative_to(ROOT)
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        errors.append(f"{rel}: not valid JSON: {e}")
        return
    if isinstance(data, dict) and "todo" in data:
        print(f"  {rel}: stub (#21), JSON well-formed — skipping JSON-LD parse")
        return
    try:
        Graph().parse(path, format="json-ld")
    except Exception as e:
        errors.append(f"{rel}: not valid JSON-LD: {e}")


def main() -> int:
    ttl_files = sorted((ROOT / "ns").rglob("*.ttl"))
    if not ttl_files:
        errors.append("no Turtle files found under ns/ — wrong working directory?")
    for path in ttl_files:
        g = check_turtle(path)
        print(f"  {path.relative_to(ROOT)}: {'parse ok' if g is not None else 'PARSE FAILED'}")
        if g is not None and path.parent.name == "config":
            check_config_scheme(path, g)

    contexts = ROOT / "ns" / "contexts.jsonld"
    if contexts.exists():
        check_contexts_jsonld(contexts)

    if errors:
        print(f"\n{len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    print(f"\nAll checks passed ({len(ttl_files)} Turtle files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
