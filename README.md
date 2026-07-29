# ii-namespace

Home of the semantic web artifacts the Independent Impact Platform itself needs to operate, published under `https://independentimpact.org/ns/`.

Domain ontologies (AIAO, claimont, impactont, infocomm, the Indicator and Methodology ontologies) live in their own repos under w3id.org addresses; indicator and methodology content lives in its own repos and domains. This repo holds only the platform's own artifacts — and the catalog that maps the whole estate.

## Contents

| Path | Artifact |
| --- | --- |
| [`ns/catalog.ttl`](ns/catalog.ttl) | DCAT registry of every semantic artifact the platform recognizes, internal and external. The bootstrap root. |
| [`ns/vocab/`](ns/vocab/) | Platform vocabulary: classes and properties no domain ontology covers |
| [`ns/config/`](ns/config/) | SKOS config concept schemes (controlled enumerations for UI and validation) |
| [`ns/shapes/`](ns/shapes/) | Platform-level SHACL shapes |
| [`ns/contexts/`](ns/contexts/) | Published JSON-LD `@context` documents for HCS message payloads |
| [`ns/policies/`](ns/policies/) | Fluree access policies and roles (security-sensitive) |
| [`ns/alignments/`](ns/alignments/) | Mappings between platform terms and external vocabularies |
| [`archive/`](archive/) | Verbatim snapshots of the deprecated legacy `/ns/` vocabulary |
| [`docs/adr/`](docs/adr/) | Architectural decision records for this repo |

The full inventory, with the ii-backend ADRs and tech-specs that determine each artifact's content, is in [ADR-0002](docs/adr/0002-platform-semantic-artifact-inventory.md).

## How artifacts are published and loaded

Every released artifact version is pinned to IPFS and registered in `ns/catalog.ttl` with its CID. The storage service bootstrap ([ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82)) resolves the catalog first, fetches each artifact by CID — HTTPS URLs are human conveniences; CIDs are authoritative — loads it into Fluree, and validates it. Fluree policies load in a later phase than vocabularies, schemes, and shapes, before the API opens to users. This is the same HCS→IPFS→Fluree path used for all third-party content, which keeps the entire Fluree state rebuildable from HCS replay.

## Deprecation notice

Everything served at `https://independentimpact.org/ns/` before this repo took over belongs to a previous architecture and is **deprecated** — see [ADR-0001](docs/adr/0001-deprecate-legacy-ns-vocabulary.md). Do not reference its terms (e.g. `indimp:PlatformUser`) in new work; the [`archive/`](archive/) snapshots are the reference for what they meant.

## Related

- [`ts-0006-semantic-web-ontologies.md`](ts-0006-semantic-web-ontologies.md) — migrated inventory of the ontology layer; superseded by `ns/catalog.ttl` as entries are confirmed
- [IndependentImpact/ii-backend](https://github.com/IndependentImpact/ii-backend) — the platform backend whose ADRs and tech-specs source the artifacts here
- [IndependentImpact/skos_SDG](https://github.com/IndependentImpact/skos_SDG) — SDG indicators vocabulary and Indicator Ontology (pending w3id publication)
