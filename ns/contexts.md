# How II uses the different semantic artefacts

This document explains _how_ the platform uses each ontology, which entity types each one models, and where the open gaps are.

## Which ontology models which entity type

- **Agent** — AIA (`aiao:Agent`) for identity/interaction modelling; the Bhash Core Ontology (`hgo:Account`) for the agent's on-chain account representation (see [`ns/alignments/hed-hashgraph.ttl`](./alignments/hed-hashgraph.ttl) for the legacy `hed:` mapping).
- **Activity** — AIA (`aiao:Activity`) for the activity itself; the Impact Ontology (`impactont:Event`, `impactont:Process`) for the causal/process layer connecting an activity to its impact outcomes.
- **Claim** — the Claims Ontology (`claimont:Claim`, `claimont:Attestation`, `claimont:hasSubject`, `claimont:hasPropertyPredicate`, `claimont:hasObject`, `claimont:hasClaimant`, `claimont:isSupportedBy`), built on RDF reification.
- **Indicator** — the Indicator Ontology and, for SDG-aligned indicators specifically, the SDG Indicators SKOS vocabulary.
- **Methodology** — the Methodology Ontology (not yet published).
- **Standard** — Placeholder (none published yet). Each onboarded standard additionally gets its own OWL extension of AIA plus a SKOS concept scheme built from AIA, DC Terms, and Schema.org classes/properties, reusing existing terms and defining new ones only where the standard genuinely needs them.
- **Platform concerns no domain ontology covers** — [`/vocab`](./vocab).

`aiao`, `claimont`, `impactont`, and `infocomm` collectively make up the AIA Ontology Suite; the others are separate, standalone vocabularies.

## Reused third-party vocabularies

II reuses classes/properties from existing vocabularies where possible rather than defining new ones, and encodes constraints and workflows using standard semantic-web tooling:

- **DC Terms** (`dcterms:`) — provenance/versioning (`dcterms:source`, `dcterms:isVersionOf`, `dcterms:isReplacedBy`, `dcterms:replaces`, `dcterms:isFormatOf`), plus titles, descriptions, and access metadata throughout the estate's catalogued artifacts (registry entry pending the `contexts.jsonld` rebuild, #21).
- **Schema.org** — candidate reusable vocabulary for standard-specific classes/properties, before a standard defines new ones of its own; also `schema:domainIncludes`/`schema:rangeIncludes` in `/vocab`.
- **SKOS** — concept schemes for a standard's own vocabulary (enables broader/narrower comparison across standards); also underlies the SDG Indicators vocabulary and the platform's own config schemes in [`/config`](./config).
- **RDF** (`rdf:`) — base reification (`rdf:Statement`, `rdf:subject`, `rdf:predicate`, `rdf:object`) that claims (`claimont:Claim`) are built on top of.
- **SHACL** — not a domain ontology, but the constraint/shape language used throughout to validate instances of the above; the platform's own shapes live in ii-backend (`assets/storage-service/shacl-shapes/`) since PR #19.
- **VANN, DCAT, PROV-O, W3C VCDM, OWL-Time** — annotation/catalog/provenance/credential/temporal vocabularies used where the artifacts need them (the bootstrap catalog in ii-backend is DCAT + VANN; `iiplat:AgentLicense` subclasses `vcdm:VerifiableCredential`; `iiplat:CreditingPeriod` subclasses `time:Interval`).

`LegalRuleML` is flagged as a candidate for future use (e.g. for standards' rule-based provisions) but is not yet integrated.

## Open gaps

- The **Standard Ontology** and **Methodology Ontology** have no published URI yet.
- The **Information Communication Ontology** (`infocomm`) is referenced only via its w3id link in II backend documentation — no concrete class or property from it appears in any worked example. Its actual coverage (documents, questions, information corpora — the "infotrip"/"infocorp" vocabulary described) is inferred, not confirmed from source.
- **Bhash account→network link**: `hgo:registeredIn` relates Artefacts (topics) to a network, but `hgo:Account` is an Actor — no property links an account to its network (issues #5/#6; candidate upstream fix in Bhash).
- **"hadeda" naming**: the review wording named "hadeda" as a domain ontology; no such semantic namespace exists (`NovaInstitute/Hadeda` is an R SDK for Hedera). Resolved as meaning Bhash — pending confirmation on issue #5.
