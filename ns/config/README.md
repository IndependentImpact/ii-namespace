# ns/config/ — config concept schemes

One SKOS concept scheme per file: the controlled enumerations that populate UI elements and constrain values. See [ADR-0002 §3](../../docs/adr/0002-platform-semantic-artifact-inventory.md) for sources. Concepts carry `skos:notation` with the wire value (the string legacy data used) and `skos:prefLabel` for display; the shapes in [`ns/shapes/`](../shapes/) validate scheme membership.

| Scheme                                                         | Source                                                                             |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [`auth-proofs.ttl`](auth-proofs.ttl)                           | legacy `authProofShape`                                                            |
| [`technology-measure-types.ttl`](technology-measure-types.ttl) | legacy `techMeasTypeShape`                                                         |
| [`impact-intentionality.ttl`](impact-intentionality.ttl)       | legacy `impactIntentionalityShape`                                                 |
| [`beneficial-adverse.ttl`](beneficial-adverse.ttl)             | legacy `beneficialOrAdverseShape`                                                  |
| [`monitored.ttl`](monitored.ttl)                               | legacy `monitoredShape` (review: may become a boolean property)                    |
| [`hedera-networks.ttl`](hedera-networks.ttl)                   | legacy `hed:HederaNetworkNameShape` (review: may become `hgo:Network` individuals) |

Still to extract (sources not yet enumeration-complete): workflow states and step types (standard-specific per ts-0003 — may not be platform config at all), document/schema types, review outcomes.
