# Challenge 2: Does Verification Deter Participation?

**Complexity:** Medium

## The Question

Is there a trade-off between verification stringency and treaty membership? Two competing hypotheses exist: strong verification might *deter* participation by creating vulnerabilities for states, or it might *enable* participation by building mutual confidence. Which does the data support?

## Why It Matters

This is one of the foundational puzzles in international cooperation. If intrusive oversight drives actors away, then designing strong governance regimes means accepting smaller coalitions. If oversight builds confidence, then the fear of "regulatory competition" may be overstated. The answer has direct implications for whether mandatory AI oversight would push developers to non-cooperative jurisdictions.

## Your Task

Test the relationship between verification intensity and state participation across arms control agreements. You will need to construct or approximate a measure of verification stringency and examine whether it correlates with the number of state parties, controlling for relevant agreement characteristics (weapon type, era, scope, bilateral vs. multilateral).

Be careful about causal claims: correlation between verification design and participation could reflect many things. Consider what confounders might be at play.

**Datasets to start with:** `agreement_info`, `vercom`, `weapons_facilities`

**Tip:** `nr_states_parties_total` and `nr_states_parties_ratification` in `agreement_info` give you participation counts. `verified_compliance_mechanism_nr` gives a simple verification intensity measure, though you may want to construct something more nuanced from `vercom`.

## AI Governance Extension (Optional)

If strict verification deters participation, what does this imply for mandatory AI oversight regimes? Could it push labs to less regulated jurisdictions? If there is no deterrence effect, are "race to the bottom" fears in AI governance overstated?
