# ADR-0001: Deprecate the legacy /ns/ vocabulary and rebuild from scratch

**Status:** accepted — 2026-07-29

## Context

`https://independentimpact.org/ns/` and `/ns/hedera/` serve JSON-LD vocabulary documents (last modified 2025-09-28) that predate the current architecture defined in ii-backend's ADRs and the Protocol design principles. They mix classes, properties, and inline SHACL shapes in one flat document, reference the retired `jellyfiiish.xyz` namespace, and have no source under version control — the deployed files are the only copy.

Meanwhile the platform's architecture has settled on: content on IPFS, approval and ordering signalled via HCS, the storage service loading artifacts into Fluree from a content-addressed catalog (see [ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82)).

## Decision

- Everything currently served under `https://independentimpact.org/ns/` is **deprecated** as belonging to a previous architecture. No new work may reference its terms.
- The deployed documents are archived verbatim in [`archive/`](../../archive/) for the record, since existing data may still reference their term URIs.
- The platform's semantic artifacts (config concept schemes, vocabulary, SHACL shapes) will be rebuilt from scratch in this repo, following ii-backend's ADRs and the Protocol design principles, published as content-addressed (IPFS-pinned) releases registered in `catalog.ttl`.

## Consequences

- Term URIs from the legacy documents (e.g. `indimp:PlatformUser`) may resurface in old data; the archive is the reference for what they meant.
- The nginx deployment at `/ns/` must eventually be replaced by publication from this repo; until then the live documents and this repo disagree, with this repo authoritative on intent.
- The new artifacts start with no backwards-compatibility obligation to the legacy vocabulary.
