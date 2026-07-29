# ns/policies/ — Fluree policies and rules

Access policies and roles for the Fluree ledger (JSON-LD), loaded in bootstrap phase 2 before the API opens to users. **Security-sensitive**: every change requires review; no policy may block the propagator's own system identity (see [ii-backend#82](https://github.com/IndependentImpact/ii-backend/issues/82)). See [ADR-0002 §6](../../docs/adr/0002-platform-semantic-artifact-inventory.md).
