# II Namespace

The governed home of Independent Impact's semantic estate: the platform's own vocabulary, published under `https://independentimpact.org/ns/`, and the record of which external ontologies II uses and how. Everything here is RDF authored as Turtle; instance data never lives here.

## Language

### The estate

**Semantic estate**:
Everything semantic II publishes or depends on — the platform's own namespace plus every external ontology and vocabulary II uses, and how each is applied.

**Namespace**:
The URI space `https://independentimpact.org/ns/` and the artifacts published under it, with the repo path mirroring the URI.
_Avoid_: ns folder, website

**Governed form**:
An artifact that is version-controlled, reviewed and released from this repo, as opposed to the legacy hand-edited JSON-LD that was deployed without source control discipline.

**Context**:
An ontology, vocabulary or JSON-LD context a user of II's Fluree ledger will encounter; each is registered with its prefix, namespace URI and status.
_Avoid_: schema (overloaded), bounded context (that is a DDD term, not this)

### Platform artifacts

**Platform vocabulary** (`iiplat:`):
Classes and properties the Independent Impact Platform needs that no domain ontology covers. Defined only where aiao, claimont, impactont, infocomm, Bhash or dcterms have nothing.
_Avoid_: II ontology, platform schema

**Config scheme**:
A SKOS concept scheme, one per file, holding a controlled enumeration that populates UI elements and constrains values. Renaming to "enums" is under discussion (#15).
_Avoid_: lookup table, code list

**Wire value**:
The literal string legacy data used for an enumerated value (e.g. `EDDSA_SIGNATURE`), carried on a concept as `skos:notation`.

**Alignment**:
A mapping (`skos:exactMatch`, `skos:closeMatch`, `owl:equivalentProperty`) between a platform or legacy term and an external vocabulary, kept in `ns/alignments/` so mappings never scatter into the vocabularies themselves.

**Bootstrap catalog**:
The DCAT/VANN catalog the backend loads at bootstrap, listing the platform's semantic artifacts. It lives in ii-backend (`assets/storage-service/`), not here; this repo's public external-ontology registry is being rebuilt separately (#21).
_Avoid_: catalog.ttl "in this repo" (moved by PR #19)

### Carry-forward

**Carry-forward**:
Converting a legacy term into governed Turtle, preserving it per-term rather than deprecating wholesale; the form was the problem, not the content.
_Avoid_: deprecation, rewrite

**Legacy namespace**:
The pre-governance JSON-LD served at `/ns/` (`indimp:`) and `/ns/hedera/` (`hed:`) before this repo existed. `hed:` dissolves into reuse of the Hashgraph Ontology; `indimp:` terms carry forward into the platform vocabulary.

**Reference snapshot**:
A verbatim copy of a deployed legacy JSON-LD document, kept purely as carry-forward input and deleted once conversion completes (#8).
_Avoid_: archive, backup

**Prune candidate**:
A carried-forward term whose retention is in question, flagged with a `skos:editorialNote` beginning "Carry-forward review:" and removed or kept per-term during review — never silently.

**Term-URI continuity**:
The open decision on whether platform terms keep the legacy base URI (`…/ns/` + `indimp:`) or move to `…/ns/vocab/` + `iiplat:`. Existing ledger data references the legacy URIs.

### External ontologies

**AIA Ontology Suite**:
The four ontologies aiao, claimont, impactont and infocomm taken together; the platform's primary domain-modelling layer for agents, activities, claims and information.

**Hashgraph Ontology** (`hgo:`, "Bhash"):
The external ontology modelling Hedera entities (accounts, topics, consensus messages). `hgo` is II's local prefix convention; the ontology declares none itself.
_Avoid_: hadeda (a misheard review term — resolved to mean this ontology), hed: (the dissolved legacy namespace)

**Consensus timestamp**:
A Hedera instant in the mirror-node string form `<seconds>.<nanoseconds>` (nine zero-padded nanosecond digits). A string, not an `xsd:dateTime` (#23).

### Standards

**Standard**:
A methodology standard hosted on the II platform (e.g. NIAS, TPTS), owned by its standards body, with its own ontology and SHACL that extend the platform's and domain ontologies.

**Standards body**:
The organization that owns and publishes a standard — the tenant of the platform.
_Avoid_: standard registry (a Guardian-era remnant)

**Tenant standard**:
A standard viewed as a platform tenant, with its own namespace whose location (body-owned domain vs a reserved platform path) is an open policy question (#31).
