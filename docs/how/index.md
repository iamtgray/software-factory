# How It Works

Every hand-off in the factory is built from the same five things, and [The Five Primitives](primitives.md) names them: a digest-bound statement, a delegated verdict, a capability descriptor, trust configuration, and freshness state. Fix those five and the choice of tools becomes close to arbitrary -- swapping Syft for Trivy changes which binary emits an SBOM attestation, and nothing downstream of it.

[The Hand-offs](handoffs.md) spends the primitives on the boundaries that need them. Most boundaries inside a factory are ordinary function calls; five are trust-domain transitions, where the receiver can't verify what the sender did by inspection and has to rely on a signature. Those five are the architecture. Everything else is plumbing.

Then the contract. [Slots and Outcomes](slots.md) defines each component position by the outcome it owes -- a signed SBOM, a reviewed diff, a scanned artefact -- so the tool that fills it is an implementation detail; it also covers how an implementation declares machine-readably what it can actually do, and why that contract has to be a Kubernetes custom resource and not a 2,653-line values file.

!!! note "Three became five"
    The original formulation had three primitives. Adversarial verification found two more -- trust configuration and freshness state -- which had been quietly treated as fields in a manifest, when they're things the architecture has to carry everywhere. The five on the primitives page are the corrected set. See [What We Got Wrong](../start/corrections.md).
