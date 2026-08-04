# ns/alignments/ — mappings to external vocabularies

`skos:exactMatch` / `owl:equivalentProperty` alignments between platform terms and external vocabularies (first target: the SDG indicators vocabulary in skos_SDG). Kept here so mappings are not scattered into the vocabularies themselves. See [ADR-0002 §7](../../docs/adr/0002-platform-semantic-artifact-inventory.md).

[`hed-hashgraph.ttl`](hed-hashgraph.ttl) maps the legacy `hed:` namespace to the Hashgraph Ontology, executing ADR-0002 §2's dissolution decision (issue #6) — the interpretation key for existing data that references `hed:` URIs.
