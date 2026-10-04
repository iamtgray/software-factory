# How It Works

The mechanism, in three pages.

**[The Five Primitives](primitives.md)** -- Every hand-off in the factory is built from five things: a digest-bound statement, a delegated verdict, a capability descriptor, trust configuration, and freshness state. Fix these five and the choice of tools becomes close to arbitrary.

**[The Hand-offs](handoffs.md)** -- Five transitions where the receiver cannot verify what the sender did by inspection and must rely on a signature. Those five are the architecture. Everything else is plumbing.

**[Slots and Outcomes](slots.md)** -- How a component position is defined by the outcome it must produce rather than the tool that fills it, how an implementation declares what it can actually do, and why the interface has to be a Kubernetes API rather than a configuration file.
