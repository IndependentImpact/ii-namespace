# ADR-0002: Inventory of the platform's own semantic web artifacts

**Status:** proposed — 2026-07-31 (revised after review; the visibility model in §"Repo visibility and per-artifact access" is under discussion)

## Context

This repo documents II's **entire semantic estate** (see the repo README): (a) it hosts II's own namespace — terms, classes and properties defined only where no domain ontology covers them — and (b) it identifies every external ontology and vocabulary II uses and how II applies it. II's namespace builds on and extends those external ontologies; it is not separate from them. [ADR-0001](./0001-rebuild-legacy-ns-vocabulary-in-governed-form.md) governs how the existing `/ns/` vocabulary carries forward into this repo.

All artifacts here are loaded into Fluree at bootstrap ([ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82)): public artifacts are pinned to IPFS per release and registered by CID in the catalog, with the catalog CID anchored via HCS; platform-only artifacts follow a private channel (see the visibility section below). The bootstrap loads them in phases — see the [phasing comment on #82](https://github.com/IndependentImpact/ii-backend/issues/82).

Source documents below live in ii-backend under [`docs/adrs/`](https://github.com/IndependentImpact/ii-backend/tree/develop/docs/adrs) and [`docs/tech-specs/`](https://github.com/IndependentImpact/ii-backend/tree/develop/docs/tech-specs) (develop branch), abbreviated here as `BE ADR-…` and `BE ts-…`.

## Decision

This repo contains seven artifact classes, published under `https://independentimpact.org/ns/` with the path mirroring the URI.

### 1. `ns/catalog.ttl` — registry of the semantic estate

The catalog with one entry per artifact, internal and external: namespace URI, preferred prefix (VANN), version, source repo, access level, and per-version IPFS CID. It is the concrete form of the external-ontology mapping this repo exists for — each external entry records the ontology's namespace, prefix, landing page, and a description of how II uses it. The bootstrap root: the storage service resolves the catalog first, then fetches everything else by CID. Loaded in bootstrap phase 1.

Currently expressed in DCAT (with VANN annotations). *Open question: whether DCAT/VoID is the right vocabulary for it is not yet agreed.*

Sources:

- [ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82) — bootstrap procedure; catalog role and CID discipline
- [BE ts-0011 storage service](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0011-storage-service.md) — the component that consumes the catalog
- [BE ADR-0006 IPFS via Lighthouse](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0006-a-ipfs-via-lighthouse-public-file-storage.md) — pinning infrastructure
- [BE ADR-0015 ledger integrity anchoring](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0015-a-ledger-integrity-anchoring.md) — anchoring pattern the catalog CID follows
- [`ts-0006-semantic-web-ontologies.md`](../../ts-0006-semantic-web-ontologies.md) (this repo) — the inventory table that seeds the external entries

### 2. `ns/vocab/` — platform vocabulary

Classes and properties the platform needs that no domain ontology covers, e.g., platform users and roles. Define nothing that aiao, claimont, impactont, infocomm, hadeda, or dcterms already provide. The legacy `hed:` namespace dissolves into reuse of the Hashgraph Ontology. Loaded in phase 1.

Sources:

- [`reference/ns.jsonld`](../../reference/ns.jsonld) — the deployed vocabulary; carry-forward source per ADR-0001
- [`ts-0006-semantic-web-ontologies.md`](../../ts-0006-semantic-web-ontologies.md) (this repo) — which ontology models which entity type; reuse-before-minting rules
- [BE CONTEXT.md](https://github.com/IndependentImpact/ii-backend/blob/develop/CONTEXT.md) — actors and system flow the vocabulary must describe
- [BE ADR-0002 DIDs as primary identifiers](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0002-use-dids-as-primary-ii-identifiers.md) and [BE ADR-0016 DID method](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0016-did-method.md) — identifier model for user/agent terms
- [BE ADR-0010 Hedera topic structure](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0010-hedera-topic-structure.md) and [BE ts-0007 Hedera interaction patterns](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0007-hedera-interaction-patterns.md) — entity↔topic/account link semantics
- [BE docs/capabilities/identity.md](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/capabilities/identity.md) — licenses, credentials, user lifecycle

### 3. `ns/config/` — config concept schemes (SKOS)

One SKOS concept scheme per file: the controlled enumerations that populate UI elements and constrain values. Candidate schemes (settled per scheme during rebuild): user types, license scopes, workflow states, document/schema types, review outcomes, monitoring flags (impact intentionality, beneficial/adverse, monitored). This is the "Config Concept Schemes" row of ts-0006. Loaded in phase 1.

Sources (tech specs name the enumerations; capability docs give context only):

- [BE ts-0003 workflows](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md) — workflow states and step types
- [BE ts-0010 endpoint visibility tiers](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0010-endpoint-visibility-tiers.md) — visibility-tier enumeration
- [`reference/ns.jsonld`](../../reference/ns.jsonld) — legacy enumerations carried forward per ADR-0001

### 4. `ns/shapes/` — platform-level SHACL shapes (platform-only)

Shapes validating: config-conforming data (a property takes its value from a given concept scheme), workflow definitions, and the JSON-LD payloads carried in HCS messages. Boundaries: standard-specific SHACL lives in private per-standard graphs, not here; the CloudEvents envelope is JSON, validated by JSON Schema in ii-backend — only the semantic payload's shapes belong here. **Access: platform-only** (see the visibility section). Loaded in phase 1.

Sources:

- [BE ts-0003 workflows](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md) — SHACL as the workflow definition/enforcement language
- [BE ADR-0005 one Fluree ledger, private standard SHACL graphs](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0005-a-one-fluree-ledger-private-standard-shacl-graphs.md) (+ [addendum](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0005-b-addendum.md)) — the platform-vs-standard shape boundary
- [BE ts-0002 HCS message structure](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0002-a-hcs-message-structure.md) (+ [addendum](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0002-b-addendum-1.md)) — payload structure the payload shapes validate
- [BE ts-0009 standard onboarding pipeline](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0009-standard-onboarding-pipeline.md) — where standard-specific shapes come from (i.e. what to exclude here)

### 5. `ns/contexts/` — published JSON-LD `@context` documents

Every HCS payload is JSON-LD (BE ts-0002); the contexts those payloads use must be published, versioned, CID-pinned artifacts so any historical message remains interpretable — a precondition for the rebuild-from-HCS guarantee. Distinct from the catalog: a `@context` document maps a payload's JSON keys to term URIs so the payload can be read as RDF; the catalog (class 1) is the registry of which artifacts exist and where their released versions live. Loaded in phase 1.

Sources:

- [BE ts-0002 HCS message structure](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0002-a-hcs-message-structure.md) — CloudEvents envelope with JSON-LD payload and inline `@context`
- [BE ADR-0012 use CloudEvents](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0012-TODO-use-cloudevents.md) — envelope decision
- [BE ts-0005 HCS publication ordering](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0005-hedera-hcs-publication-ordering.md) — replay semantics the contexts must survive

### 6. `ns/policies/` — Fluree policies and rules (JSON-LD, platform-only)

Access policies and roles for the Fluree ledger. They are catalogued like every other artifact but are **platform-only** (see the visibility section): their content is not publicly pinned, and they load in bootstrap phase 2, before the API opens to users. Security-sensitive: changes require mandatory review; a policy must never be able to block the propagator's own system identity (see the [#82 phasing comment](https://github.com/IndependentImpact/ii-backend/issues/82)).

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

## Repo visibility and per-artifact access

*This section records a position under discussion, not a settled decision.*

The repo remains **private**; what varies is the access level of each artifact, recorded in the catalog:

- Every artifact the platform loads has a catalog entry — the catalog's purpose is that the system and its administrators know the entire estate. No artifact is uncatalogued because it is sensitive.
- Each internal entry carries `dcterms:accessRights`: `"public"` (vocab, config schemes, contexts, alignments, the catalog itself) or `"platform-only"` (shapes, policies).
- Public artifacts are exposed through the API and pinned to IPFS per release (CIDs authoritative; HTTPS URLs are human conveniences).
- Platform-only artifacts are **not** pinned as plaintext to public IPFS. A hash of each release may be anchored on Hedera for integrity, or pinned content may be encrypted; they load through the platform's private channel (phase 2 for policies).
- Once the catalog is loaded into Fluree, Fluree data-level permissions filter catalog triples per requester, so an API user sees only the entries they may see. This reuses the policy machinery the platform needs anyway, rather than splitting artifacts across repos.

Acknowledged trade-offs of this model:

- The repo cannot later be made public without rewriting history, since security-sensitive content will be in it. This challenges the original intent that the repo be private only until first release.
- GitHub has no per-directory access control: anyone with read access to the repo can read the policies. The collaborator set must be managed accordingly, including if external vocabulary contributors are ever invited.
- If the catalog *document* is publicly pinned (it is the bootstrap root), the *metadata* of platform-only artifacts — existence, title, description — is world-readable even though their content is not. Whether the catalog document itself is publicly pinned or operator-only is an open question.
- The fallback model, if this position does not hold: platform-only artifacts are authored in ii-backend and only *catalogued* here — the same "catalogued here, authored elsewhere" pattern already used for the external ontologies.

### Explicitly excluded from this repo

- Domain ontologies (aiao, claimont, impactont, infocomm, hadeda, Indicator Ontology, Methodology Ontology) — w3id-hosted, own repos
- Standard-specific extensions and SHACL — per-standard, private graphs (BE ADR-0005, BE ts-0009)
- Instance data of any kind — lives in Fluree, arrives via HCS
- Genesis config (topic IDs, trusted keys) — deliberately out-of-band, in ii-backend deployment (#82)

## Consequences

- The storage-service bootstrap (ii-backend#82) has a definite artifact list.
- Every release of a public artifact must be pinned to IPFS and registered in `ns/catalog.ttl` with its CID before the platform can use it; platform-only artifacts are registered in the catalog but delivered through the private channel, which #82's phasing must reflect.
- The ii-backend documents cited above are inputs to each artifact's content; when they change, the corresponding artifact here must be reviewed.
- Semantic-artifact review and security review converge on this repo's PR process, since platform-only security artifacts live here.
