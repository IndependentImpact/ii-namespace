# Technical Specification 0006: Semantic Web Ontology Layer

TODO: This document was migrated as-is from ii-backend/docs/tech-specs/. It needs to be reviewed and updated. And it should not be presented as a "tech spec."


## Overview

[ADR-0005](../adrs/adr-0005-one-fluree-ledger-private-standard-shacl-graphs.md) decides that II's default graph holds "the ordinary RDF relationships" connecting activities, agents, projects, standards, methodologies, indicators, instruments, evidence, reviews, claims, and reputation — but does not name which ontologies define those relationships. This tech-spec names them.

## Ontologies and vocabularies in use

| Ontology / vocabulary                           | URI                                                                                     | Coverage                                                           | Core entity type(s)                              | Status            |
| ----------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------ | ----------------- |
| AIAO Ontology Suite (`aiao`)                    | `https://w3id.org/aiao`                                                                 | Actors, interactions, activities, outcomes/artifacts               | agent, activity                                  | prototype         |
| Claims Ontology (`claimont`)                    | `https://w3id.org/claimont`                                                             | Claims and attestations                                            | claim                                            | prototype         |
| Impact Ontology (`impactont`)                   | `https://w3id.org/impactont`                                                            | Impact events/processes; causal state-change                       | activity (impact/process layer)                  | prototype         |
| Information Communication Ontology (`infocomm`) | `https://w3id.org/infocomm`                                                             | Information/communication concepts (documents, questions, corpora) | — (referenced, never instantiated in an example) | prototype         |
| Standard Ontology                               | none published yet                                                                      | Classes/properties for standards                                   | standard                                         | planned           |
| Indicator Ontology                              | `https://github.com/IndependentImpact/skos_SDG/blob/main/ontologies/core/indicator.ttl` | Indicators, metrics                                                | indicator                                        | prototype         |
| Methodology Ontology                            | none published yet                                                                      | Methodologies (procedures, rules, controls)                        | methodology                                      | under development |
| SDG Indicators vocabulary                       | `https://github.com/IndependentImpact/skos_SDG/tree/main/ontologies/vocabularies`       | SKOS vocabulary of SDG indicators                                  | indicator                                        | under development |
| Config Concept Schemes                          | `https://independentimpact.org/ns/`                                                     | System configuration concepts                                      | — (infrastructure, not a core entity)            | prototype         |
| Hedera Ontology ("Hashgraph Ontology")          | `https://hashgraphontology.xyz/`                                                        | Hedera accounts, transactions, tokens, topics, smart contracts     | agent (account representation)                   | prototype         |

`aiao`, `claimont`, `impactont`, and `infocomm` are modelled in `ii-arch` as one bundled suite (the AIAO Ontology Suite); the other six are separate, standalone vocabularies.

### Reused third-party vocabularies

II reuses classes/properties from existing vocabularies where possible rather than minting new ones, and encodes constraints and workflows using standard semantic-web tooling:

- **DC Terms** (`dcterms:`) — provenance/versioning: `dcterms:source`, `dcterms:isVersionOf`, `dcterms:isReplacedBy`, `dcterms:replaces`, `dcterms:isFormatOf`.
- **Schema.org** — candidate reusable vocabulary for standard-specific classes/properties, before a standard mints new ones of its own.
- **SKOS** — concept schemes for a standard's own vocabulary (enables broader/narrower comparison across standards); also underlies the SDG Indicators vocabulary above.
- **RDF** (`rdf:`) — base reification (`rdf:Statement`, `rdf:subject`, `rdf:predicate`, `rdf:object`) that claims (`claimont:Claim`) are built on top of.
- **SHACL** — not a domain ontology, but the constraint/shape language used throughout (see [ts-0003](./ts-0003-workflows.md)) to validate instances of the above.

`LegalRuleML` is flagged in `ii-arch` as a candidate for future use (e.g. for standards' rule-based provisions) but is not yet integrated.

## Which ontology models which entity type

- **Agent** — AIAO (`aiao:agent`) for identity/interaction modelling; the Hedera Ontology for the agent's on-chain account representation.
- **Activity** — AIAO (`aiao:Activity`) for the activity itself; the Impact Ontology (`impactont:Event`, `impactont:Process`) for the causal/process layer connecting an activity to its impact outcomes (see [ts-0003](./ts-0003-workflows.md)'s workflow/process-step examples, which are AIAO/Impact Ontology nodes in practice).
- **Claim** — the Claims Ontology (`claimont:Claim`, `claimont:Attestation`, `claimont:hasSubject`, `claimont:hasPropertyPredicate`, `claimont:hasObject`, `claimont:hasClaimant`, `claimont:isSupportedBy`), built on RDF reification.
- **Indicator** — the Indicator Ontology and, for SDG-aligned indicators specifically, the SDG Indicators SKOS vocabulary.
- **Methodology** — the Methodology Ontology (not yet published; see [Methodology Management](../capabilities/methodology-management.md)).
- **Standard** — the Standard Ontology (not yet published). Each onboarded standard additionally gets its own OWL extension of AIAO plus a SKOS concept scheme built from AIAO, DC Terms, and Schema.org classes/properties, reusing existing terms and minting new ones only where the standard genuinely needs them (see [Standards Management](../capabilities/standards-management.md)).

Note: `nias:` (as in `nias:ProjectDesign`, seen in [ts-0003](./ts-0003-workflows.md)'s examples) is not itself a published ontology — it is a worked example of what a standard's own onboarded, standard-specific extension of the Standard Ontology looks like once instantiated.

## Open gaps

- The **Standard Ontology** and **Methodology Ontology** have no published URI yet — both are marked planned/under-development in `ii-arch`, and remain so in II's own model. A concrete namespace and publication location should be decided before either is relied on for cross-standard interoperability.
- The **Information Communication Ontology** (`infocomm`) is referenced only via its w3id link in `ii-arch` — no concrete class or property from it appears in any worked example. Its actual coverage (documents, questions, information corpora — the "infotrip"/"infocorp" vocabulary described in [ts-0003](./ts-0003-workflows.md)) is inferred, not confirmed from source.

## Related Documentation

- [ADR-0005 — One Fluree ledger, private standard-specific SHACL and FSF named graphs](../adrs/adr-0005-one-fluree-ledger-private-standard-shacl-graphs.md)
- [ts-0003 — Workflow definition and enforcement](./ts-0003-workflows.md)
- [Standards Management](../capabilities/standards-management.md)
- [Methodology Management](../capabilities/methodology-management.md)
- [Indicator Management](../capabilities/indicator-management.md)
