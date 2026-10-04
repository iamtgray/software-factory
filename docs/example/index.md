# A worked example

One change, traced end to end twice: a vulnerability is reported in a library used by a production service, and someone has to fix it.

| | [A Change, End to End](connected.md) | [The Same Change, Air-Gapped](airgap.md) |
|---|---|---|
| **The setting** | Connected: registry, transparency log and identity provider all reachable | An enclave with no network path out (no DNS, no registry pull, no transparency log) |
| **What it traces** | Eleven steps from advisory to running container -- what each step produces, who signs it, and what the next step checks | The same eleven steps, read as a diff against the connected flow |
| **Where it ends** | Ten signed documents (eight bound to the image digest, two to the commit), of which admission control reads exactly one | The agent degrades by GPU count, and attestation discovery loses the referrers API. Keyless signing crosses intact, as long as the bundle carries its own proof |

Read the connected page first, because the air-gapped one won't stand up alone. Its trace comes from what the tools document and what the standards claim, not from a run in a real enclave.
