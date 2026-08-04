# ii-namespace

Home of the semantic web artifacts the Independent Impact Platform itself needs to operate, published under `https://independentimpact.org/ns/`.

Domain ontologies (AIAO, claimont, impactont, infocomm, the Indicator and Methodology ontologies) live in their own repos under w3id.org addresses; indicator and methodology content lives in its own repos and domains. This repo holds only the platform's own artifacts — and the catalog that maps the whole estate.

## Contents

| Path | Artifact |
| --- | --- |
| [`ns/catalog.ttl`](ns/catalog.ttl) | DCAT registry of every semantic artifact the platform recognizes, internal and external. The bootstrap root. |
| [`ns/vocab/`](ns/vocab/) | Platform vocabulary: classes and properties no domain ontology covers |
| [`ns/config/`](ns/config/) | SKOS config concept schemes (controlled enumerations for UI and validation) |
| [`ns/shapes/`](ns/shapes/) | Platform-level SHACL shapes (platform-only) |
| [`ns/contexts/`](ns/contexts/) | Published JSON-LD `@context` documents for HCS message payloads |
| [`ns/policies/`](ns/policies/) | Fluree access policies and roles (security-sensitive, platform-only) |
| [`ns/alignments/`](ns/alignments/) | Mappings between platform terms and external vocabularies |
| [`reference/`](reference/) | Snapshots of the deployed legacy `/ns/` source, pending conversion to Turtle |
| [`docs/adr/`](docs/adr/) | Architectural decision records for this repo |

The full inventory, with the ii-backend ADRs and tech-specs that determine each artifact's content, is in [ADR-0002](docs/adr/0002-platform-semantic-artifact-inventory.md).

## How artifacts are published and loaded

Every released artifact version is registered in `ns/catalog.ttl`, which records each artifact's access level (`dcterms:accessRights`). Public artifacts are pinned to IPFS — HTTPS URLs are human conveniences; CIDs are authoritative. Platform-only artifacts (shapes, policies) are not publicly pinned; a release hash may be anchored on Hedera, or pinned content encrypted. The storage service bootstrap ([ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82)) resolves the catalog first, fetches each artifact, loads it into Fluree, and validates it; Fluree policies load in a later phase, via the platform's private channel, before the API opens to users. Public artifacts travel the same HCS→IPFS→Fluree path used for all third-party content, which keeps the Fluree state rebuildable from HCS replay. Fluree data-level permissions filter catalog triples per requester, so API users see only the entries they may see.

## Legacy form

The JSON-LD currently served at `https://independentimpact.org/ns/` predates this repo's governance: it has no source under version control, no versioning, and mixes vocabulary with inline SHACL. Its terms **carry forward** — they are being converted to governed Turtle here, pruned per-term, per [ADR-0001](docs/adr/0001-rebuild-legacy-ns-vocabulary-in-governed-form.md). The [`reference/`](reference/) snapshots are the conversion input.

## Related

- [`docs/ontology-layer.md`](docs/ontology-layer.md) — how II uses each ontology; prose companion to `ns/catalog.ttl` (formerly ts-0006)
- [IndependentImpact/ii-backend](https://github.com/IndependentImpact/ii-backend) — the platform backend whose ADRs and tech-specs source the artifacts here
- [IndependentImpact/skos_SDG](https://github.com/IndependentImpact/skos_SDG) — SDG indicators vocabulary and Indicator Ontology (pending w3id publication)
