# ns/ — the platform's semantic artifacts

Everything under this directory is publicly published under `https://independentimpact.org/ns/`, with the path mirroring the URI (so `ns/vocab/vocab.ttl` serves `…/ns/vocab/`). [`contexts.md`](contexts.md) explains how these artifacts relate to the external ontologies II reuses.

| Path                                 | Artifact                                                                                                                                                                                                                                                                 | Access |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| [`contexts.jsonld`](contexts.jsonld) | A JSON-LD list of every artifact and external ontology used in II's Fluree ledger, with namespace, prefix (VANN), status, and per-release IPFS CIDs.                                                                                                                     | public |
| [`contexts.md`](contexts.jsonld)     | The prose companion to `contexts.jsonld`.                                                                                                                                                                                                                                | public |
| [`vocab/`](vocab/)                   | Platform vocabulary (`iiplat:`): classes and properties no domain ontology covers, carried forward from the legacy `/ns/` JSON-LD per [ADR-0001](../docs/adr/0001-rebuild-legacy-ns-vocabulary-in-governed-form.md). Prune candidates flagged with `skos:editorialNote`. | public |
| [`config/`](config/)                 | SKOS concept schemes, one per file: the controlled enumerations that populate UI elements and constrain values. Concepts carry the legacy wire string as `skos:notation`.                                                                                                | public |
| [`alignments/`](alignments/)         | Mappings between platform terms and external vocabularies, e.g. the legacy `hed:` → Bhash alignment.                                                                                                                                                                     | public |

## Conventions

- Turtle for all RDF artifacts; JSON-LD only for `contexts.jsonld` where the consumer requires it.
