# A Worked Example

One change, traced end to end, twice.

The scenario is deliberately ordinary: **a vulnerability is reported in a library used by a production service, and someone has to fix it.** It is the most common piece of work a factory handles.

| | [A Change, End to End](connected.md) | [The Same Change, Air-Gapped](airgap.md) |
|---|---|---|
| **The setting** | Connected: registry, transparency log and identity provider all reachable | An enclave with no network path out -- no DNS, no registry pull, no transparency log |
| **What it traces** | Eleven steps from advisory to running container, showing at each step what is produced, who signs it, and what the next step actually checks | The same eleven steps, read as a diff against the connected flow |
| **Where it ends** | Ten signed documents -- eight bound to the image digest, two to the commit -- of which admission control reads exactly one | Two steps genuinely break -- the agent degrades by GPU count, and attestation discovery loses the referrers API. A third looks broken and isn't: keyless signing crosses fine if the bundle carries its own proof |

The air-gapped page assumes you've read the connected one. It's written as a diff and doesn't stand alone.
