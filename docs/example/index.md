# A Worked Example

One change, traced end to end, twice.

The scenario is deliberately ordinary: **a vulnerability is reported in a library used by a production service, and someone has to fix it.** No novel architecture, no exotic requirement -- just the most common piece of work a factory handles.

**[A Change, End to End](connected.md)** -- The connected case. Eleven steps from advisory to running container, showing at each step what is produced, who signs it, and what the next step actually checks. By the end there are ten signed documents bound to one image digest, and admission control reads exactly one of them.

**[The Same Change, Air-Gapped](airgap.md)** -- The same fix, delivered into a disconnected enclave. What survives the crossing, what does not, which steps gain a second implementation, and the three places the connected flow silently assumed a network it no longer has.

!!! tip "Read them in order"
    The second page only makes sense as a diff against the first. Three steps break in the air-gapped flow, and two of them aren't the obvious ones.
