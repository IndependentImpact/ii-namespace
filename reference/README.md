# Reference: deployed /ns/ source snapshots

Verbatim snapshots of the JSON-LD documents deployed at `https://independentimpact.org/ns/`, taken 2026-07-29 (server reported `Last-Modified: Sun, 28 Sep 2025 19:29:59 GMT`). The source these files were generated from lived in a personal repo with no releases or tags and **diverged** from what is served (the deployed snapshot is 28 nodes richer), so the deployed documents are the authoritative carry-forward input — the **input for converting the vocabulary to governed Turtle form** (the carry-forward decision, PRs #3/#9). Once carry-forward into `ns/` is complete, this directory is deleted (git history preserves it) — see issue #8.

| File | Source URL | Size |
| --- | --- | --- |
| `ns.jsonld` | `https://independentimpact.org/ns/` | 27,570 bytes |
| `ns-hedera.jsonld` | `https://independentimpact.org/ns/hedera/` | 3,986 bytes |

`ns.jsonld` defines 69 nodes in the `indimp:` namespace: 12 classes, 48 properties, and 9 inline SHACL shapes (`PlatformUser`, `AgentLicense`, `Workflow`, `resourceIpfsUri`, …), referencing the Jellyfish data namespace (active work-in-progress). `ns-hedera.jsonld` defines the `hed:` namespace, which dissolves into reuse of the Hashgraph Ontology rather than carrying forward.
