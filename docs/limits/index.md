# Limitations

What this approach cannot do, what cannot be known, what nobody thought to ask, and what has already been tried.

**[What Nobody Asked](unasked.md)** -- Three critics were pointed at the research and asked what was missing. There is no named buyer, no operating model, no cost in money, and no response in the architecture to either of the two failure modes the research itself ranked highest. Also a correctness defect: restoring the high side from backup silently defeats the anti-rollback guarantee. Start here if you are deciding whether to fund this.

**[What We Cannot Answer](unanswerable.md)** -- Questions that aren't answerable from public sources, most of them about how real cross-domain guards actually behave. Six of seven things you'd need to design a transfer format are controlled information. Designing against a guess is worse than not designing.

**[What Has Failed Before](history.md)** -- The idea has failed four times since 1968, and the diagnoses are consistent and unflattering. The compromise the 1978 attempt retreated to is modern platform engineering, forty years early.

**[Ecosystem Health](ecosystem.md)** -- Twelve projects under 300 stars on the critical path, well-known tools that are dead despite their star counts, and a licence pattern where the paid tier is reliably the feature a regulated deployment needs.
