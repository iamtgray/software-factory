# A Worked Example

One change, traced end to end, twice.

The scenario is deliberately ordinary, and I'd guess it's about the commonest piece of work a factory handles: **a vulnerability is reported in a library used by a production service, and someone has to fix it.**

| | [A Change, End to End](connected.md) | [The Same Change, Air-Gapped](airgap.md) |
|---|---|---|
| **The setting** | Connected: registry, transparency log and identity provider all reachable | An enclave with no network path out (no DNS, no registry pull, no transparency log) |
| **What it traces** | Eleven steps from advisory to running container, showing at each step what is produced, who signs it, and what the next step actually checks | The same eleven steps, read as a diff against the connected flow |
| **Where it ends** | Ten signed documents (eight bound to the image digest, two to the commit), of which admission control reads exactly one | The agent degrades by GPU count, and attestation discovery loses the referrers API. Keyless signing crosses intact, as long as the bundle carries its own proof |

The air-gapped page is written as a diff against the connected one, so it won't stand up on its own.

The enclave column is the half I'm least confident about. It's traced from what the tools document and what the standards claim, with no run in a real enclave behind it, so the failures named above are the ones I managed to find, which isn't the same as them being the only ones.

Which column matters to you comes down to your own delivery path: does anything in it have to cross a boundary that won't pass bytes back?
