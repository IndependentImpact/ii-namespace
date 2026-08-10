# Author Turtle, generate JSON-LD

Status: accepted (decision stated by @AlexIvanHoward in issue #17)

All RDF artifacts in this repo are **authored in Turtle**. JSON-LD — Fluree's native language — is **generated** from the Turtle and is what Fluree loads; the two are semantically equivalent serializations of the same RDF graph, so nothing is lost in conversion. These artifacts are inserted into Fluree exactly once but read and reviewed by humans continually, so the source format optimizes for human readability.

## Why not author JSON-LD directly

It is Fluree-native, but the legacy estate demonstrated the failure modes of hand-authored JSON-LD twice over:

- **All nine deployed inline shapes were invalid SHACL as served**: `sh:in` written as a JSON array does not produce the RDF list SHACL requires, so every enumeration constraint silently constrained nothing.
- **One source file was unparseable JSON** (a trailing comma) — an error class that cannot survive authoring in an RDF syntax that is parsed as RDF.

Authoring both by hand was also rejected: two hand-maintained serializations drift.

## Consequences

- Releases need a serialization step (any RDF library: rdflib, Jena riot) producing the JSON-LD distribution from the Turtle source. CI already parses every Turtle file on push (PR #33).
- **Exception**: `ns/contexts.jsonld` stays authored JSON-LD, because its consumer requires that exact format (recorded in `ns/README.md` conventions).
- **Deliberately not decided here**: which serialization carries an artifact's canonical CID when pinned — pinning the Turtle while Fluree loads generated JSON-LD means loaded bytes ≠ pinned bytes. Candidate answer: pin both as `dcat:distribution`s of one dataset. Belongs to the DCAT decision (#18) and the registry rebuild (#21).

## Numbering note

ADR-0001 and ADR-0002 were retired in PR #19 (their substance folded into `README.md`). Numbering continues at 0003 rather than reusing numbers that appear in merged history.
