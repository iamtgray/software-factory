# Why these fail

The software factory idea isn't new. I've traced four serious attempts since 1968, and none ended well. Almost none of the post-mortem is technical -- the diagnoses are organisational. One of them describes modern platform engineering, forty years early.

## Four attempts, and the rejection that came first

The 1968 entry sits outside the four. Before anyone had built anything the field was told this wouldn't work, and most of what it objected to has since stopped being a problem.

| When | What | Outcome |
|---|---|---|
| **1968** | A Honeywell engineer proposes software factories at the NATO conference | **Rejected as unworkable** -- reusable modules cannot be both general and efficient; machine dependence; no way to catalogue components |
| **1969 onward** | **Hitachi**, then NEC, Toshiba and Fujitsu from 1976-77 | Ran two decades, then faded |
| **1975-78** | **SDC** -- a US defence contractor, first to build and trademark "The Software Factory", ~200 programmers centralised in one building | **Abandoned** after about ten projects |
| **1986-93** | **Eureka Software Factory** -- a publicly funded European platform programme | Forgotten |
| **2003-08** | **Microsoft Software Factories** -- model-driven development, domain-specific languages | Faded |

**Hitachi predates SDC.**

And after 1978 the term "became an anathema to both managers and programmers". I haven't found a US firm that claimed a software factory for roughly the next twenty years.

## Diagnosis 1: SDC's failure was organisational

Cusumano's account, in his order of importance:

1. **Too much product variety** for a centralised, standardised facility.
2. **Middle management refused to cede delivery control**, and were *"not required by top management to use the Software Factory, leading to a decline in the flow of work."*
3. Infrastructure imposed *"without adequate analysis or anticipation of the work flow and the reactions of its personnel."*

**Developer resistance comes third**, folded into the infrastructure complaint.

**Schedule and budget accuracy "improved dramatically."** It was abandoned anyway -- it lost a political contest about control, starved of work because nobody was required to use it.

!!! danger "The same funding shape shows up today"
    RAND finds that current defence software factories are mostly **customer-funded** -- each one must win its customers' budgets.

    That's SDC's failure mode in the budget line: optional adoption, leading to a decline in the flow of work. What to do about it is a funding decision, and it sits on [Mandate vs Adoption](../tradeoffs/mandate-vs-adoption.md).

### The compromise they retreated to

The compromise was to *"maintain the factory procedures and some of the tools, but **decentralize the factory workers**."*

That surviving half is platform engineering, written down in 1978, and the industry arrived there again forty years later without citing SDC on the way; it's the half this project builds.

## Diagnosis 2: Japan's long fade

1. **No study I've found demonstrates the advantage statistically.**
2. The enabling conditions were local (captive customers, lifetime employment, high volumes of similar mainframe software).
3. The product mix changed underneath it.

Cusumano and Kemerer, *Management Science* 1990, n=40: **no statistically significant difference between US and Japanese organisations on productivity, quality or reuse.** Reused code costs about 64% of new.

And Toshiba's own productivity curve: **+22% in year one, +70% by year five, then +8% across the next four** -- the explanation offered is a practical reuse ceiling around 50%.

Reuse **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%.** So the modification rate of shared assets is the number to watch: a slot implementation every programme forks by 40% leaves you worse off than an empty shelf, because you pay the coordination cost and get none of the benefit.

## Does the modern version repeat them?

**Solved:** the 1968 objections about machine dependence and component cataloguing.

**Shifted ground:** the objection that reusable modules cannot be both general and efficient. The *assurance machinery* (SBOMs, provenance, signing, control evidence) looks uniform across applications. *Application architecture* varies with the system it serves, which is why [scope](../start/scope.md) gets a page of its own.

**Avoided:** centralising people. I've not seen anyone propose 200 programmers in one building.

**At risk of repeating:**

- **optional adoption**, via the customer-funded model above
- **no workflow analysis** before imposing infrastructure
- **developer experience** -- secondary in 1978; in a classified environment a workaround becomes a security incident
- **product variety**, if scope is drawn too broadly

The recent material adds failure modes the older attempts don't show:

!!! quote "SEI, 2026"
    Organisations "collapsed under the weight of their own tooling... until no one can explain their own deployment path."

!!! quote "RAND, 2025"
    "Limited movement toward implementation of continuous authority to operate" -- despite three years of enabling policy.

The RAND line bears on this project directly: the economic case rests on control inheritance, and if that inheritance isn't happening in practice the case is theoretical. From the outside I can't tell how much of it is happening.

### What might be genuinely new this time

The binding constraint may have moved from code production to evidence production. If it has, a factory sits on a compliance chokepoint teams can't easily opt out of, unlike SDC, whose customers could decline.

## The modern case study: Kessel Run

**Created:** 2017, after a programme cancellation that had run from $374m to $745m in development against a lifecycle estimate over $3.5bn.

**Delivered:** real applications, including one used during the Kabul evacuation of 123,000 people, and durable policy change -- continuous authorisation and a new software acquisition pathway exist partly because of it.

**Never delivered:** the system replacement it was created to produce.

Its co-founder, in 2025: it was **"failing"** and **"not doing its mission"** -- though he puts the blame elsewhere, *"It's the Air Force that failed Kessel Run."* The structural cause he names: *"We were turning over 50 percent of our staff every six months"*, and *"What software company... turns over their entire C suite every two years?"*

In March 2025 it reverted to a government-led, vendor-managed model with a single vendor per portfolio. A serving engineer, anonymously: *"It's back to the future."*

In February 2026 it opened a new programme for the same capability, ten years after the cancellation it was created to fix.

His account is the only one I've got, and he has a reason to tell it that way. But if the turnover figure is the cause, a factory whose operation depends on institutional memory is in trouble at the organisations that need it most.

## Why not just build the apps?

From the person who coined the modern term:

!!! quote
    "If you want to make toast, you don't go build a toaster... Just build the apps."

What's being built here is the evidence that the toast is safe to eat -- the apps can't produce it themselves, and twelve regulatory regimes now require it.
