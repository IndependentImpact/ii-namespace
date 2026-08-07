# ii-namespace

This repo documents II's **entire semantic estate**: (a) it hosts II's own namespace — terms, classes and properties defined only where no domain ontology covers them — and (b) it identifies every external ontology and vocabulary II uses and how II applies it. II's namespace builds on and extends those external ontologies; it is not separate from them.

Home of the semantic web artifacts the Independent Impact Platform itself needs to operate, published under `https://independentimpact.org/ns/`.

## Repository contents

| Path                                       | Artifact                                                                          |
| ------------------------------------------ | --------------------------------------------------------------------------------- |
| [`CONTEXT.md`](CONTEXT.md)                 | Glossary of this repo's domain language                                            |
| [`ns/contexts.jsonld`](ns/contexts.jsonld) | JSON-LD list of all the contexts that users will encounter in II's Fluree ledger   |
| [`ns/contexts.md`](ns/contexts.md)         | Prose companion to `ns/contexts.jsonld`                                            |
| [`ns/vocab/`](ns/vocab/)                   | Platform vocabulary: classes and properties no domain ontology covers              |
| [`ns/config/`](ns/config/)                 | SKOS config concept schemes (controlled enumerations for UI and validation)        |
| [`ns/alignments/`](ns/alignments/)         | Mappings between platform terms and external vocabularies                          |
| [`reference/`](reference/)                 | Snapshots of the deployed legacy `/ns/` source; carry-forward input, deleted once conversion completes (#8) |
| [`docs/agents/`](docs/agents/)             | How agent skills use this repo (issue tracker, triage labels, domain docs)         |

### Content details

### `ns/contexts.jsonld` — JSON-LD list of all the contexts that users will encounter in II's Fluree ledger

Currently a stub. It is being rebuilt as the public external-ontology registry that `ns/catalog.ttl` provided before PR #19 moved the catalog to ii-backend — see issue #21.

### `ns/contexts.md`

How II uses each ontology/context/namespace; prose companion to `ns/contexts.jsonld`

### `ns/vocab/` — platform vocabulary

Classes and properties the platform needs that no domain ontology covers, e.g., platform users and roles. Define nothing that aiao, claimont, impactont, infocomm, Bhash (the Hashgraph Ontology — "hadeda" in the original review wording, see issue #5), or dcterms already provide. The legacy `hed:` namespace dissolves into reuse of Bhash.

### `ns/config/` — config concept schemes (SKOS)

One SKOS concept scheme per file: the controlled enumerations that populate UI elements and constrain values. Candidate schemes (settled per scheme during rebuild): user types, license scopes, workflow states, document/schema types, review outcomes, monitoring flags (impact intentionality, beneficial/adverse, monitored). This is the config-schemes entry of the ontology layer (formerly the "Config Concept Schemes" row of ts-0006).

### `ns/alignments/` — mappings to external vocabularies

`skos:exactMatch` / `owl:equivalentProperty` alignments between platform terms and external vocabularies (e.g. config concepts → SDG SKOS vocabulary). Exists so mappings are not scattered into the vocabularies themselves.

### `reference`

The JSON-LD currently served at `https://independentimpact.org/ns/` predates this repo's governance: its source lived in a personal repo with no releases or tags and diverged from what is served (a 28-node gap, one unparseable file), and it mixes vocabulary with inline SHACL. Its terms **carry forward** — they are being converted to governed Turtle here, pruned per-term. The [`reference/`](reference/) snapshots are the conversion input.

## Explicitly excluded from this repo

- Standard-specific extensions and SHACL — owned per-standard and hosted outside this repo (BE ts-0009; ownership model under amendment in BE #91)
- Instance data of any kind — lives in Fluree, arrives via HCS

## Related

- [IndependentImpact/ii-backend](https://github.com/IndependentImpact/ii-backend) — the platform backend whose ADRs and tech-specs source the artifacts here
- [IndependentImpact/skos_SDG](https://github.com/IndependentImpact/skos_SDG) — SDG indicators vocabulary and Indicator Ontology (pending w3id publication)
