# ns/ — the platform's semantic artifacts

Everything under this directory is published under `https://independentimpact.org/ns/`, with the path mirroring the URI (so `ns/vocab/vocab.ttl` serves `…/ns/vocab/`). [ADR-0002](../docs/adr/0002-platform-semantic-artifact-inventory.md) defines the artifact classes; [`docs/ontology-layer.md`](../docs/ontology-layer.md) explains how these artifacts relate to the external ontologies II reuses.

| Path | Artifact | Access |
| --- | --- | --- |
| [`catalog.ttl`](catalog.ttl) | DCAT registry of the whole semantic estate — every internal artifact and external ontology, with namespace, prefix (VANN), status, access level, and per-release IPFS CIDs. The bootstrap root: the storage service resolves this first (ii-backend#82). | public |
| [`vocab/`](vocab/) | Platform vocabulary (`iiplat:`): classes and properties no domain ontology covers, carried forward from the legacy `/ns/` JSON-LD per [ADR-0001](../docs/adr/0001-rebuild-legacy-ns-vocabulary-in-governed-form.md). Prune candidates flagged with `skos:editorialNote`. | public |
| [`config/`](config/) | SKOS concept schemes, one per file: the controlled enumerations that populate UI elements and constrain values. Concepts carry the legacy wire string as `skos:notation`. | public |
| [`contexts/`](contexts/) | Published, versioned JSON-LD `@context` documents for HCS message payloads — pinned by CID so historical messages stay interpretable. *(Empty; not started.)* | public |
| [`alignments/`](alignments/) | Mappings between platform terms and external vocabularies, e.g. the legacy `hed:` → Bhash alignment. | public |
| [`shapes/`](shapes/) | Platform-level SHACL shapes: config-conformance, workflow definitions, payload validation. | platform-only |
| [`policies/`](policies/) | Fluree access policies and roles (security-sensitive). *(Empty; not started.)* | platform-only |

## Access levels

Each artifact's access level is recorded in the catalog as `dcterms:accessRights` (`"public"` / `"platform-only"`) — see the visibility section of ADR-0002 (under discussion). Public artifacts are pinned to IPFS per release and exposed via the API; CIDs are authoritative, HTTPS URLs are conveniences. Platform-only content is never publicly pinned (a release hash may be anchored on Hedera, or pinned content encrypted) and loads through the platform's private channel. Fluree data-level permissions filter catalog triples per requester.

## Conventions

- Turtle for all RDF artifacts; JSON-LD only for `contexts/` and `policies/` where the consumer requires it.
- Every artifact validates with rdflib before commit; every release is registered in `catalog.ttl` before the platform can use it (entries without a `dcat:distribution` are not loadable).
- Terms whose retention or modelling is unsettled carry `skos:editorialNote "Carry-forward review: …"` rather than being changed or dropped silently.
