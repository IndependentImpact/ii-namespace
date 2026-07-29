# ADR-0002: Inventory of the platform's own semantic web artifacts

**Status:** proposed — 2026-07-29

## Context

[ADR-0001](./0001-deprecate-legacy-ns-vocabulary.md) deprecates the legacy `/ns/` vocabulary and commits to rebuilding the platform's semantic artifacts from scratch. This repo hosts exactly those artifacts: the semantic web resources the Independent Impact Platform itself needs to operate — as distinct from domain ontologies (w3id-hosted, own repos), indicator/methodology libraries (own repos and domains), and standard-specific extensions.

All artifacts here are loaded into Fluree through the same HCS→IPFS pipeline as third-party content ([ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82)): pinned to IPFS per release, registered by CID in the catalog, catalog CID anchored via HCS. The bootstrap procedure loads them in phases — see the [phasing comment on #82](https://github.com/IndependentImpact/ii-backend/issues/82).

Source documents below live in ii-backend under [`docs/adrs/`](https://github.com/IndependentImpact/ii-backend/tree/develop/docs/adrs) and [`docs/tech-specs/`](https://github.com/IndependentImpact/ii-backend/tree/develop/docs/tech-specs) (develop branch), abbreviated here as `BE ADR-…` and `BE ts-…`.

## Decision

This repo contains seven artifact classes, published under `https://independentimpact.org/ns/` with the path mirroring the URI.

### 1. `ns/catalog.ttl` — registry of the semantic estate

DCAT/VoID catalog with one entry per artifact (internal and external): namespace URI, preferred prefix (VANN), version, source repo, and per-version IPFS CID. The bootstrap root: the storage service resolves the catalog first, then fetches everything else by CID. Loaded in bootstrap phase 1.

Sources:

- [ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82) — bootstrap procedure; catalog role and CID discipline
- [BE ts-0011 storage service](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0011-storage-service.md) — the component that consumes the catalog
- [BE ADR-0006 IPFS via Lighthouse](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0006-a-ipfs-via-lighthouse-public-file-storage.md) — pinning infrastructure
- [BE ADR-0015 ledger integrity anchoring](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0015-a-ledger-integrity-anchoring.md) — anchoring pattern the catalog CID follows
- [`ts-0006-semantic-web-ontologies.md`](../../ts-0006-semantic-web-ontologies.md) (this repo) — the inventory table that seeds the external entries

### 2. `ns/vocab/` — platform vocabulary

Classes and properties the platform needs that no domain ontology covers: platform users and roles, agent licenses, resource↔storage provenance (`resourceIpfsUri`, `resourceHederaMessageId`), entity↔Hedera-account/topic links. Mint nothing that AIAO, claimont, impactont, or the Hedera Ontology already provides; the legacy `hed:` namespace dissolves into reuse of the Hedera Ontology. Loaded in phase 1.

Sources:

- [`archive/ns.jsonld`](../../archive/ns.jsonld) — the deprecated vocabulary; evidence of what the platform needed, **not** a design to copy
- [`ts-0006-semantic-web-ontologies.md`](../../ts-0006-semantic-web-ontologies.md) (this repo) — which ontology models which entity type; reuse-before-minting rules
- [BE CONTEXT.md](https://github.com/IndependentImpact/ii-backend/blob/develop/CONTEXT.md) — actors and system flow the vocabulary must describe
- [BE ADR-0002 DIDs as primary identifiers](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0002-use-dids-as-primary-ii-identifiers.md) and [BE ADR-0016 DID method](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0016-did-method.md) — identifier model for user/agent terms
- [BE ADR-0010 Hedera topic structure](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0010-hedera-topic-structure.md) and [BE ts-0007 Hedera interaction patterns](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0007-hedera-interaction-patterns.md) — entity↔topic/account link semantics
- [BE docs/capabilities/identity.md](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/capabilities/identity.md) — licenses, credentials, user lifecycle

### 3. `ns/config/` — config concept schemes (SKOS)

One SKOS concept scheme per file: the controlled enumerations that populate UI elements and constrain values. Candidate schemes (settled per scheme during rebuild): user types, license scopes, workflow states, document/schema types, review outcomes, monitoring flags (impact intentionality, beneficial/adverse, monitored). This is the "Config Concept Schemes" row of ts-0006. Loaded in phase 1.

Sources:

- [BE docs/capabilities/](https://github.com/IndependentImpact/ii-backend/tree/develop/docs/capabilities) — each capability doc (identity, indicator-, methodology-, standards-, project-management, peer-review, bounty-management) names the enumerations that capability needs
- [BE ts-0003 workflows](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md) — workflow states and step types
- [BE ts-0010 endpoint visibility tiers](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0010-endpoint-visibility-tiers.md) — visibility-tier enumeration
- [`archive/ns.jsonld`](../../archive/ns.jsonld) — legacy enumerations as candidates for carry-over

### 4. `ns/shapes/` — platform-level SHACL shapes

Shapes validating: config-conforming data (a property takes its value from a given concept scheme), workflow definitions, and the JSON-LD payloads carried in HCS messages. Boundaries: standard-specific SHACL lives in private per-standard graphs, not here; the CloudEvents envelope is JSON, validated by JSON Schema in ii-backend — only the semantic payload's shapes belong here. Loaded in phase 1.

Sources:

- [BE ts-0003 workflows](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md) — SHACL as the workflow definition/enforcement language
- [BE ADR-0005 one Fluree ledger, private standard SHACL graphs](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0005-a-one-fluree-ledger-private-standard-shacl-graphs.md) (+ [addendum](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0005-b-addendum.md)) — the platform-vs-standard shape boundary
- [BE ts-0002 HCS message structure](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0002-a-hcs-message-structure.md) (+ [addendum](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0002-b-addendum-1.md)) — payload structure the payload shapes validate
- [BE ts-0009 standard onboarding pipeline](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0009-standard-onboarding-pipeline.md) — where standard-specific shapes come from (i.e. what to exclude here)

### 5. `ns/contexts/` — published JSON-LD `@context` documents

Every HCS payload is JSON-LD (BE ts-0002); the contexts those payloads use must be published, versioned, CID-pinned artifacts so any historical message remains interpretable — a precondition for the rebuild-from-HCS guarantee. Loaded in phase 1.

Sources:

- [BE ts-0002 HCS message structure](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0002-a-hcs-message-structure.md) — CloudEvents envelope with JSON-LD payload and inline `@context`
- [BE ADR-0012 use CloudEvents](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0012-TODO-use-cloudevents.md) — envelope decision
- [BE ts-0005 HCS publication ordering](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0005-hedera-hcs-publication-ordering.md) — replay semantics the contexts must survive

### 6. `ns/policies/` — Fluree policies and rules (JSON-LD)

Access policies and roles for the Fluree ledger. They are JSON-LD and load through the same pipeline (bootstrap phase 2, before the API opens to users), so they are catalogued and pinned like every other artifact. Security-sensitive: changes require mandatory review; a policy must never be able to block the propagator's own system identity (see the [#82 phasing comment](https://github.com/IndependentImpact/ii-backend/issues/82)). Placement here rather than in ii-backend is a deliberate choice — they are semantic artifacts the platform loads — and may warrant its own ADR if contested.

Sources:

- [BE ADR-0009 Fluree storage mode](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0009-fluree-storage-mode.md) — ledger configuration the policies attach to
- [BE ADR-0005 one Fluree ledger](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0005-a-one-fluree-ledger-private-standard-shacl-graphs.md) — graph layout the policies must protect
- [BE ADR-0011 private storage setup](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0011-TODO-private-storage-setup.md) — private-data boundary
- [BE ADR-0014 Fluree backup and disaster recovery](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0014-fluree-backup-and-disaster-recovery.md) — the rebuild guarantee policy-loading must preserve
- [ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82) — phase 2 ordering, signature verification, self-lockout constraint

### 7. `ns/alignments/` — mappings to external vocabularies

`skos:exactMatch` / `owl:equivalentProperty` alignments between platform terms and external vocabularies (e.g. config concepts → SDG SKOS vocabulary). Empty at first; exists so mappings are not scattered into the vocabularies themselves. Loaded in phase 1.

Sources:

- [`ts-0006-semantic-web-ontologies.md`](../../ts-0006-semantic-web-ontologies.md) (this repo) — reused third-party vocabularies (DC Terms, Schema.org, SKOS)
- [skos_SDG](https://github.com/IndependentImpact/skos_SDG) — SDG indicators vocabulary, first alignment target

### Explicitly excluded from this repo

- Domain ontologies (aiao, claimont, impactont, infocomm, Indicator Ontology, Methodology Ontology) — w3id-hosted, own repos
- Indicator and methodology content — own repos and domains; approved via HCS, content on IPFS
- Standard-specific extensions and SHACL — per-standard, private graphs (BE ADR-0005, BE ts-0009)
- Instance data of any kind — lives in Fluree, arrives via HCS
- Genesis config (topic IDs, trusted keys) — deliberately out-of-band, in ii-backend deployment (#82)

## Consequences

- The storage-service bootstrap (ii-backend#82) has a definite artifact list: phase 1 loads classes 1–5 and 7; phase 2 loads class 6.
- Every release of any artifact here must be pinned to IPFS and registered in `catalog.ttl` with its CID before the platform can use it.
- The ii-backend documents cited above are inputs to each artifact's content; when they change, the corresponding artifact here must be reviewed.
- `ns/policies/` living here (not in ii-backend) means semantic-artifact review and security review converge on this repo's PR process.
