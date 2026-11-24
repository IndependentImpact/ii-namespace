# ns/vocab/ — II Platform vocabulary

Classes and properties the platform needs that no domain ontology covers. Design rule: define nothing that aiao, claimont, impactont, infocomm, dcterms, or Bhash (the Hashgraph Ontology) already provides.

Two vocabularies live here, both authored in Turtle (ADR-0003) and published under `https://independentimpact.org/ns/vocab/`:

- [`vocab.ttl`](vocab.ttl) — the platform vocabulary, `iiplat:` (`https://independentimpact.org/ns/vocab/`). It carries forward the legacy `/ns/` JSON-LD vocabulary in governed form — all 12 classes and 48 properties entered carry-forward, and pruning has since run per-term, with `skos:editorialNote "Carry-forward review: …"` marking the terms whose retention is still open (6 at the time of writing) — and has since grown with what the platform's design needed: workflows and their tests, standards and their kinds, namespaces and the catalogue annotations (BE TS-0030), Hedera links, and reputation — domains, triggers, rules, contracts and tokens (BE TS-0006). As of 2026-11-25 it declares 23 classes and 68 properties.
- [`bounties.ttl`](bounties.ttl) — the bounty vocabulary, `iibount:` (`https://independentimpact.org/ns/vocab/bounties/`): the bounty, its tasks, seats, rewards and the records II writes on them (BE TS-0001). As of 2026-11-25 it declares 6 classes and 30 properties.

## Conventions

- Every term carries `rdfs:label` and, where it is more than a name, `skos:definition`; `schema:domainIncludes` / `schema:rangeIncludes` state the intended subjects and values without the entailment `rdfs:domain` / `rdfs:range` would carry.
- `skos:editorialNote` records why a term exists or what is still open about it, and names the ii-backend document (BE TS-00xx, ADR-00xx) that decided it.
- Classes whose instances are concepts of a standard's own scheme — `iiplat:ReputationDomain`, `iiplat:ReputationAction`, `iiplat:ReputationEvent` — are declared `rdfs:subClassOf skos:Concept`, and an instance is typed with **both** the class and `skos:Concept`, explicitly: the platform's validators apply no `rdfs:subClassOf` entailment, so the axiom states the invariant for readers and reasoners rather than doing the typing. The same holds for the kinds of `iiplat:Standard` and of `iiplat:ReputationRule`: a node is typed with the base class and exactly one kind.
- Enumerated values (the legacy shapes' `sh:in` lists) are not here: they are SKOS concept schemes under [`../config/`](../config/) (issue #7). Mappings to external vocabularies are under [`../alignments/`](../alignments/).
- The platform SHACL shapes that constrain these terms live in ii-backend (`assets/storage-service/shacl-shapes/`), which pins the commit of this file it validates against in its bootstrap catalog.

The counts above are a snapshot; `grep -c ' a rdfs:Class'` and `grep -c ' a rdf:Property'` over a file give the current ones.
