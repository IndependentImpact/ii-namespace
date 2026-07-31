# ADR-0001: Rebuild the /ns/ vocabulary in governed form (prune and carry forward)

**Status:** proposed — 2026-07-31 (supersedes the 2026-07-29 draft that framed this as deprecation)

## Context

`https://independentimpact.org/ns/` and `/ns/hedera/` serve JSON-LD vocabulary documents (last modified 2025-09-28) whose **form** predates the current architecture: they have no source under version control — the deployed files are the only copy — no versioning or release discipline, and they mix classes, properties, and inline SHACL shapes in one flat document. Their **content** is another matter: many of the terms, classes and properties were purposely created for the new architecture and remain valid; the Jellyfish data namespace they reference is an active work-in-progress, not retired.

Meanwhile the platform's architecture requires semantic artifacts to be governed: authored in git where their evolution is transparent, reviewed via PRs, released with versions, pinned to IPFS with canonical CIDs, and registered in a catalog the storage service resolves at bootstrap (see [ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82)).

## Decision

- The vocabulary is rebuilt **in the correct form, not from scratch**: converted to Turtle in this repo, where source, history, review, releases, versioning and canonical CIDs are all governed by the git process.
- Terms, classes and properties **carry forward**. During conversion each term is assessed individually; only terms irrelevant under the new architecture are removed, and removal is a per-term review decision, not a blanket rule.
- [`reference/`](../../reference/) holds verbatim snapshots of the deployed documents as the input to this conversion. Once carry-forward is complete the snapshots are deleted — git history preserves them.
- The deployed JSON-LD at `/ns/` remains in place until publication from this repo replaces it; from then on the served documents are generated from this repo's source.

## Consequences

- There is no deprecation of the legacy term URIs; existing data that references them remains valid. Continuity of term URIs across the conversion is an open question settled during carry-forward review.
- The nginx deployment at `/ns/` must eventually serve this repo's published releases; until then the live documents and this repo may disagree, with this repo authoritative on intent.
- Inline SHACL shapes from the legacy documents are separated from the vocabulary during conversion and handled under the shapes artifact class (ADR-0002).
