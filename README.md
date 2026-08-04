# ii-namespace

This repo documents II's **entire semantic estate** (see the repo README): (a) it hosts II's own namespace — terms, classes and properties defined only where no domain ontology covers them — and (b) it identifies every external ontology and vocabulary II uses and how II applies it. II's namespace builds on and extends those external ontologies; it is not separate from them.

Home of the semantic web artifacts the Independent Impact Platform itself needs to operate, published under `https://independentimpact.org/ns/`.

## Repository contents

| Path                               | Artifact                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------ | --- |
| [`ns/catalog.ttl`](ns/catalog.ttl) | DCAT registry of every semantic artifact the platform recognizes, internal and external. The bootstrap root. |
| [`ns/vocab/`](ns/vocab/)           | Platform vocabulary: classes and properties no domain ontology covers                                        |
| [`ns/config/`](ns/config/)         | SKOS config concept schemes (controlled enumerations for UI and validation)                                  |     |
| [`ns/alignments/`](ns/alignments/) | Mappings between platform terms and external vocabularies                                                    |
| [`reference/`](reference/)         | Snapshots of the deployed legacy `/ns/` source, pending conversion to Turtle                                 |
| [`docs/adr/`](docs/adr/)           | Architectural decision records for this repo                                                                 |

### Content details

### `ns/contexts.jsonld` — JSON-LD list of all the contexts that users will encounter in II's Fluree ledger

Currently empty. TODO.

### `ns/contexts.md`

How II uses each ontology/context/namespace; prose companion to `ns/contexts.jsonld`

### `ns/vocab/` — platform vocabulary

Classes and properties the platform needs that no domain ontology covers, e.g., platform users and roles. Define nothing that aiao, claimont, impactont, infocomm, Bhash (the Hashgraph Ontology — "hadeda" in the original review wording, see issue #5), or dcterms already provide. The legacy `hed:` namespace dissolves into reuse of Bhash.

### `ns/config/` — config concept schemes (SKOS)

One SKOS concept scheme per file: the controlled enumerations that populate UI elements and constrain values. Candidate schemes (settled per scheme during rebuild): user types, license scopes, workflow states, document/schema types, review outcomes, monitoring flags (impact intentionality, beneficial/adverse, monitored). This is the config-schemes entry of the ontology layer (formerly the "Config Concept Schemes" row of ts-0006).

### `ns/alignments/` — mappings to external vocabularies

`skos:exactMatch` / `owl:equivalentProperty` alignments between platform terms and external vocabularies (e.g. config concepts → SDG SKOS vocabulary). Exists so mappings are not scattered into the vocabularies themselves.

### `reference`

The JSON-LD currently served at `https://independentimpact.org/ns/` predates this repo's governance: it has no source under version control, no versioning, and mixes vocabulary with inline SHACL. Its terms **carry forward** — they are being converted to governed Turtle here, pruned per-term. The [`reference/`](reference/) snapshots are the conversion input.

## Explicitly excluded from this repo

- Standard-specific extensions and SHACL — per-standard, private graphs (BE ADR-0005, BE ts-0009)
- Instance data of any kind — lives in Fluree, arrives via HCS

## Related

- [IndependentImpact/ii-backend](https://github.com/IndependentImpact/ii-backend) — the platform backend whose ADRs and tech-specs source the artifacts here
- [IndependentImpact/skos_SDG](https://github.com/IndependentImpact/skos_SDG) — SDG indicators vocabulary and Indicator Ontology (pending w3id publication)
