# How it works

[The Five Primitives](primitives.md) names what every hand-off in the factory reduces to: a digest-bound statement, a delegated verdict, a capability descriptor, trust configuration, and freshness state. Swap Syft for Trivy and the only change is which binary emits the SBOM attestation -- downstream still reads the same format.

Most boundaries inside a factory are ordinary function calls. Five are trust-domain transitions, where the receiver's only evidence about what the sender did is a signature, and each of those five needs its own key, policy and audit trail. [The Hand-offs](handoffs.md) covers each one.

[Slots and Outcomes](slots.md) defines each component position by the outcome it owes: a signed SBOM, a reviewed diff, a scanned artefact. It also covers how an implementation declares machine-readably what it can do, and why that declaration belongs in a Kubernetes custom resource. The API server rejects a bad slot declaration on admission, and the core can ask the cluster which implementation is installed and how to call it. Big Bang spreads the same information across a 2,653-line values file, the template conditionals that read it, and whatever those templates rendered, so nothing validates it on admission and there's nothing left to query afterwards.
