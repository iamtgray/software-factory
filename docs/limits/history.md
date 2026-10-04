# What Has Failed Before

The software factory idea has been tried four times and has failed four times. The diagnoses are consistent and unflattering, and they contain the best positioning argument available.

## Four attempts, and the rejection that came first

The 1968 entry isn't one of the four. It's the field being told, before anyone built anything, that this wouldn't work -- and two of its three objections have since been solved.

| When | What | Outcome |
|---|---|---|
| **1968** | A Honeywell engineer proposes software factories at the NATO conference | **Rejected as unworkable** -- reusable modules cannot be both general and efficient; machine dependence; no way to catalogue components |
| **1969 onward** | **Hitachi**, then NEC, Toshiba and Fujitsu from 1976-77 | Ran two decades, then faded |
| **1975-78** | **SDC** -- a US defence contractor, first to build and trademark "The Software Factory", ~200 programmers centralised in one building | **Abandoned** after about ten projects |
| **1986-93** | **Eureka Software Factory** -- a publicly funded European platform programme | Forgotten |
| **2003-08** | **Microsoft Software Factories** -- model-driven development, domain-specific languages | Faded |

**Hitachi predates SDC.** The Japanese movement wasn't a response to American practice.

And after 1978 the term "became an anathema to both managers and programmers". No US firm claimed a software factory for roughly twenty years.

## Diagnosis 1: SDC, and it wasn't technology

Cusumano's account, in his order of importance:

1. **Too much product variety** for a centralised, standardised facility.
2. **Middle management refused to cede delivery control**, and were *"not required by top management to use the Software Factory, leading to a decline in the flow of work."*
3. Infrastructure imposed *"without adequate analysis or anticipation of the work flow and the reactions of its personnel."*

Two details change how you read this.

**Developer resistance is explicitly downgraded to secondary.** The comfortable story (engineers hated it, engineers always hate change) isn't the finding.

**Schedule and budget accuracy "improved dramatically."** SDC's factory was *partly working* when it was abandoned. It didn't fail to deliver; it lost a political contest about control, starved of work because nobody was required to use it.

!!! danger "This failure is encoded in modern funding models"
    RAND finds that current defence software factories are mostly **customer-funded** -- each one must win its customers' budgets.

    That's SDC's exact failure mode written into the budget line: optional adoption, leading to a decline in the flow of work. **Fund as a product, or buy. Do not fund as a project with customer-recovered costs.**

### The best positioning argument available

The compromise SDC retreated to was to *"maintain the factory procedures and some of the tools, but **decentralize the factory workers**."*

!!! success "That is modern platform engineering, described in 1978."
    The surviving half of the 1978 failure is the thing the industry independently reinvented forty years later.

    So the honest framing isn't "this time it will work". It's: **the part that survived is the part we're building, and we're deliberately not building the part that died.**

## Diagnosis 2: Japan faded rather than collapsed

1. **The advantage was never statistically demonstrated.**
2. The enabling conditions were local (captive customers, lifetime employment, high volumes of similar mainframe software).
3. The product mix changed underneath it.

The headline claim of the entire movement doesn't survive its own best study. Cusumano and Kemerer, *Management Science* 1990, n=40: **no statistically significant difference between US and Japanese organisations on productivity, quality or reuse.** Reused code costs about 64% of new.

And Toshiba's own productivity curve is the cautionary one: **+22% in year one, +70% by year five, then +8% across the next four** -- because they hit a practical reuse ceiling of about 50%.

!!! quote "The single most prescriptive finding in the research"
    Reuse **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%.** A step function, not a gradient.

    So measure the modification rate of shared assets. A slot implementation every programme forks by 40% is worse than having no shared asset -- you pay the coordination cost and get none of the benefit.

## Does the modern version repeat them?

**Solved:** the 1968 objections about machine dependence and component cataloguing.

**Shifted rather than solved:** the objection that reusable modules cannot be both general and efficient. The *assurance machinery* -- SBOMs, provenance, signing, control evidence -- genuinely is uniform across applications. *Application architecture* is not. Which is why [scope](../start/scope.md) is the most important decision on this site.

**Avoided:** centralising people. Nobody is proposing 200 programmers in one building.

**At risk of repeating:**

- **optional adoption**, via the customer-funded model above
- **no workflow analysis** before imposing infrastructure
- **developer experience** -- secondary in 1978, but in a classified environment a workaround is a security incident
- **product variety**, if scope is drawn too broadly

**Two new failure modes, both recent:**

!!! quote "SEI, 2026"
    Organisations "collapsed under the weight of their own tooling... until no one can explain their own deployment path."

!!! quote "RAND, 2025"
    "Limited movement toward implementation of continuous authority to operate" -- despite three years of enabling policy.

That second one matters because the project's economic leverage rests on control inheritance. If that mechanism isn't actually happening, the leverage is theoretical.

### The one genuinely new condition, in our favour

The binding constraint has moved from **code production to evidence production.** That puts a factory on a compliance chokepoint no team can opt out of -- which is structurally stronger than SDC's position, because SDC's customers could simply decline.

But the dependency is explicit: if control inheritance is weak, that leverage vanishes and you're back in SDC's losing position.

## The modern case study, honestly

The most-cited success story.

**Created** 2017, after a programme cancellation that had run from $374m to $745m in development against a lifecycle estimate over $3.5bn.

**Delivered:** real applications, including one used during the Kabul evacuation of 123,000 people, and durable policy change -- continuous authorisation and a new software acquisition pathway exist partly because of it.

**Did not deliver:** the system replacement it was created to produce.

Its co-founder, in 2025: it was **"failing"** and **"not doing its mission"** -- but pointedly, *"It's the Air Force that failed Kessel Run."* The structural cause he names: *"We were turning over 50 percent of our staff every six months"*, and *"What software company... turns over their entire C suite every two years?"*

In March 2025 it reverted to a government-led, vendor-managed model with a single vendor per portfolio. A serving engineer, anonymously: *"It's back to the future."*

**In February 2026 it opened a new programme for the same capability -- ten years after the cancellation it was created to fix.**

!!! tip "Design against operator rotation"
    Fifty per cent turnover every six months was the proximate cause of death. A factory whose operation depends on institutional memory won't survive contact with the organisations that need it most.

## The objection to have an answer for

From the person who coined the modern term, and it's a good objection:

!!! quote
    "If you want to make toast, you don't go build a toaster... Just build the apps."

The answer isn't that he's wrong. It's that the thing being built isn't a toaster -- it's the evidence that the toast is safe to eat, which the apps can't produce for themselves and which twelve regulatory regimes now require.

If that answer doesn't convince you, the objection stands.
