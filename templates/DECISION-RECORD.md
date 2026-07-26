# Decision Record — <Decision Title>

> Use this document for decisions that are persistent, costly to reverse, architecturally significant, or likely to be questioned later.
>
> Record the decision that was actually made. Preserve trade-offs, uncertainty, and the conditions under which the decision should change.

---

## Status

- **Decision ID:** `ADR-0001`
- **Status:** `Proposed | Accepted | Superseded | Rejected | Deprecated`
- **Date:** `YYYY-MM-DD`
- **Decision owner:** `<name or role>`
- **Related feature / issue:** `<path, link, or identifier>`
- **Supersedes:** `<decision ID or none>`
- **Superseded by:** `<decision ID or none>`

---

## 1. Decision Summary

<!--
State the decision in one or two direct sentences.
-->

We will:

---

## 2. Context

<!--
Describe the situation that made this decision necessary.
Include relevant business, technical, operational, and repository constraints.
Do not describe the solution yet.
-->

### Current Situation

---

### Problem or Pressure

---

### Constraints

- 

---

## 3. Decision Drivers

<!--
List the factors that materially influenced the decision.
Order them by importance where possible.
-->

1. 
2. 
3. 

---

## 4. Options Considered

### Option A — <Name>

**Description**

---

**Benefits**

- 

**Costs / Risks**

- 

**Best fit when**

- 

---

### Option B — <Name>

**Description**

---

**Benefits**

- 

**Costs / Risks**

- 

**Best fit when**

- 

---

### Option C — <Name>

**Description**

---

**Benefits**

- 

**Costs / Risks**

- 

**Best fit when**

- 

<!--
Remove unused options.
Do not invent alternatives merely to fill the template.
-->

---

## 5. Decision

<!--
State the selected option clearly.
-->

We selected:

---

## 6. Why This Decision Was Made

<!--
Explain why this option is the best fit for the current problem and constraints.
Do not rely on vague language such as "cleaner", "better", or "more scalable"
without defining what those terms mean here.
-->

- 

---

## 7. Trade-offs Accepted

<!--
Record what we are deliberately giving up or making more expensive.
-->

| Accepted Cost | Why It Is Acceptable Now | Risk |
|---|---|---|
|  |  |  |

---

## 8. Consequences

### Positive Consequences

- 

### Negative Consequences

- 

### Neutral or Operational Consequences

- 

---

## 9. Assumptions

<!--
List assumptions that must remain true for the decision to stay valid.
-->

| Assumption | Why It Matters | Evidence | Risk If False |
|---|---|---|---|
|  |  |  |  |

---

## 10. Failure Modes and Risks

### Risk 1 — <Scenario>

- **Consequence:**
- **Current mitigation:**
- **Residual risk:**
- **Verification / monitoring:**

### Risk 2 — <Scenario>

- **Consequence:**
- **Current mitigation:**
- **Residual risk:**
- **Verification / monitoring:**

---

## 11. Security, Privacy, and Data Impact

<!--
Complete when the decision affects trust boundaries, personal data,
authentication, authorization, secrets, retention, or compliance.
-->

- 

---

## 12. Operational Impact

### Deployment

- 

### Migration

- 

### Rollback

- 

### Observability

- 

### Ownership

- 

---

## 13. Verification Evidence

<!--
Record the evidence used to support the decision.
Examples: benchmark, test result, spike, production incident, repository analysis.
Do not cite assumptions as evidence.
-->

| Evidence | Method / Source | Result | Limitations |
|---|---|---|---|
|  |  |  |  |

---

## 14. Reconsideration Triggers

<!--
Define concrete conditions that should cause this decision to be reviewed.
Avoid vague language such as "if scale increases."
-->

Review this decision when one or more of the following becomes true:

- 
- 
- 

---

## 15. Rejected Alternatives

<!--
Summarize why each non-selected option was rejected.
-->

| Alternative | Why Rejected Now | When It Could Become Viable |
|---|---|---|
|  |  |  |

---

## 16. Implementation Notes

<!--
Describe only the implementation consequences of the decision.
Do not duplicate the feature implementation plan.
-->

- 

---

## 17. Related Files and Documentation

- 

---

## 18. Questions the Developer Must Be Able to Answer

1. What problem made this decision necessary?
2. Which alternatives were considered?
3. Why is the selected option the best fit for the current constraints?
4. Which cost or limitation are we deliberately accepting?
5. Which assumptions must remain true?
6. Where can this decision fail?
7. Which evidence supports the decision?
8. Under what concrete condition should the decision be reconsidered?
9. What would be required to reverse or replace it?

---

## 19. Decision Review Checklist

- [ ] The decision is stated clearly.
- [ ] The context is separated from the solution.
- [ ] Real alternatives were considered.
- [ ] Trade-offs are explicit.
- [ ] Assumptions are visible.
- [ ] Risks and failure modes are documented.
- [ ] Evidence is distinguished from opinion.
- [ ] Operational consequences are recorded.
- [ ] Reconsideration triggers are concrete.
- [ ] The decision can be defended to another engineer.

---

## Final Ownership Statement

AI may have assisted with analysis or implementation.

The decision owner remains responsible for:

- the selected option,
- the accepted trade-offs,
- the assumptions,
- the evidence,
- the risks,
- and the consequences.
