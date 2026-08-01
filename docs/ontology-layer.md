# The ontology layer: how II uses each ontology

The authoritative, machine-readable inventory of II's semantic estate — every internal artifact and external ontology, with namespace, prefix, status, access level, and per-release CIDs — is [`ns/catalog.ttl`](../ns/catalog.ttl). This document is its prose companion: it explains *how* the platform uses each ontology, which entity types each one models, and where the open gaps are.

(Formerly `ts-0006-semantic-web-ontologies.md`, migrated from ii-backend. Its inventory table is superseded by the catalog; issue #2.)

## Which ontology models which entity type

- **Agent** — AIAO (`aiao:Agent`) for identity/interaction modelling; the Bhash Core Ontology (`hgo:Account`) for the agent's on-chain account representation (see [`ns/alignments/hed-hashgraph.ttl`](../ns/alignments/hed-hashgraph.ttl) for the legacy `hed:` mapping).
- **Activity** — AIAO (`aiao:Activity`) for the activity itself; the Impact Ontology (`impactont:Event`, `impactont:Process`) for the causal/process layer connecting an activity to its impact outcomes (see [BE ts-0003](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md)'s workflow/process-step examples, which are AIAO/Impact Ontology nodes in practice).
- **Claim** — the Claims Ontology (`claimont:Claim`, `claimont:Attestation`, `claimont:hasSubject`, `claimont:hasPropertyPredicate`, `claimont:hasObject`, `claimont:hasClaimant`, `claimont:isSupportedBy`), built on RDF reification.
- **Indicator** — the Indicator Ontology and, for SDG-aligned indicators specifically, the SDG Indicators SKOS vocabulary.
- **Methodology** — the Methodology Ontology (not yet published; see [Methodology Management](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/capabilities/methodology-management.md)).
- **Standard** — the Standard Ontology (not yet published). Each onboarded standard additionally gets its own OWL extension of AIAO plus a SKOS concept scheme built from AIAO, DC Terms, and Schema.org classes/properties, reusing existing terms and minting new ones only where the standard genuinely needs them (see [Standards Management](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/capabilities/standards-management.md)).
- **Platform concerns no domain ontology covers** — [`ns/vocab/`](../ns/vocab/) (platform users, licenses, workflows-as-records, resource↔storage provenance), constrained to define nothing the domain ontologies or dcterms already provide (ADR-0002 §2).

`aiao`, `claimont`, `impactont`, and `infocomm` are modelled in `ii-arch` as one bundled suite (the AIAO Ontology Suite); the others are separate, standalone vocabularies.

Note: `nias:` (as in `nias:ProjectDesign`, seen in [BE ts-0003](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md)'s examples) is not itself a published ontology — it is a worked example of what a standard's own onboarded, standard-specific extension of the Standard Ontology looks like once instantiated.

## Reused third-party vocabularies

II reuses classes/properties from existing vocabularies where possible rather than minting new ones, and encodes constraints and workflows using standard semantic-web tooling:

- **DC Terms** (`dcterms:`) — provenance/versioning (`dcterms:source`, `dcterms:isVersionOf`, `dcterms:isReplacedBy`, `dcterms:replaces`, `dcterms:isFormatOf`), plus titles, descriptions, and access metadata throughout the catalog. Catalogued as `#vocab-dcterms`.
- **Schema.org** — candidate reusable vocabulary for standard-specific classes/properties, before a standard mints new ones of its own; also `schema:domainIncludes`/`schema:rangeIncludes` in `ns/vocab/`.
- **SKOS** — concept schemes for a standard's own vocabulary (enables broader/narrower comparison across standards); also underlies the SDG Indicators vocabulary and the platform's own config schemes in [`ns/config/`](../ns/config/).
- **RDF** (`rdf:`) — base reification (`rdf:Statement`, `rdf:subject`, `rdf:predicate`, `rdf:object`) that claims (`claimont:Claim`) are built on top of.
- **SHACL** — not a domain ontology, but the constraint/shape language used throughout (see [BE ts-0003](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md)) to validate instances of the above; the platform's own shapes live in [`ns/shapes/`](../ns/shapes/) (platform-only, ADR-0002).
- **VANN, DCAT, PROV-O, W3C VCDM, OWL-Time** — annotation/catalog/provenance/credential/temporal vocabularies used where the artifacts need them (the catalog itself is DCAT + VANN; `iiplat:AgentLicense` subclasses `vcdm:VerifiableCredential`; `iiplat:CreditingPeriod` subclasses `time:Interval`).

`LegalRuleML` is flagged in `ii-arch` as a candidate for future use (e.g. for standards' rule-based provisions) but is not yet integrated.

## Open gaps

- The **Standard Ontology** and **Methodology Ontology** have no published URI yet — both are marked planned/under-development in `ii-arch`, and remain so in II's own model (and in the catalog). A concrete namespace and publication location should be decided before either is relied on for cross-standard interoperability.
- The **Information Communication Ontology** (`infocomm`) is referenced only via its w3id link in `ii-arch` — no concrete class or property from it appears in any worked example. Its actual coverage (documents, questions, information corpora — the "infotrip"/"infocorp" vocabulary described in [BE ts-0003](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md)) is inferred, not confirmed from source.
- **Bhash account→network link**: `hgo:registeredIn` relates Artefacts (topics) to a network, but `hgo:Account` is an Actor — no property links an account to its network (issues #5/#6; candidate upstream fix in Bhash).
- **"hadeda" naming**: the review wording named "hadeda" as a domain ontology; no such semantic namespace exists (`NovaInstitute/Hadeda` is an R SDK for Hedera). Resolved as meaning Bhash — pending Alex's confirmation on issue #5.

## Related Documentation

- [ADR-0002 — Inventory of the platform's own semantic web artifacts](adr/0002-platform-semantic-artifact-inventory.md)
- [BE ADR-0005 — One Fluree ledger, private standard-specific SHACL and FSF named graphs](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/adrs/adr-0005-a-one-fluree-ledger-private-standard-shacl-graphs.md)
- [BE ts-0003 — Workflow definition and enforcement](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/tech-specs/ts-0003-workflows.md)
- [Standards Management](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/capabilities/standards-management.md), [Methodology Management](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/capabilities/methodology-management.md), [Indicator Management](https://github.com/IndependentImpact/ii-backend/blob/develop/docs/capabilities/indicator-management.md)
