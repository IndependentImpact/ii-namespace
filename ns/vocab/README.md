# ns/vocab/ — II Platform vocabulary

Classes and properties the platform needs that no domain ontology covers. [`vocab.ttl`](vocab.ttl) carries forward the legacy `/ns/` vocabulary in governed Turtle form — all 12 classes and 48 properties entered carry-forward, and pruning has since run per-term (11 classes and 44 properties today), with `skos:editorialNote "Carry-forward review: …"` marking terms whose retention is still open. Design rule: define nothing that aiao, claimont, impactont, infocomm, dcterms, or Bhash (the Hashgraph Ontology) already provides.
