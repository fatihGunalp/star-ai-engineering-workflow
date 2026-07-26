# <Feature Name> — Engineering Handoff

> This document records what was actually built, why it was built this way, how it was verified, and what remains unresolved.
>
> Do not use generic success language. Preserve trade-offs, uncertainty, deferred work, and known risks.

---

## Status

- **Feature slug:** `<feature-slug>`
- **Owner:** `<name or role>`
- **Status:** `Implemented | Partially Implemented | Blocked | Deferred`
- **Completed:** `YYYY-MM-DD`
- **Related issue / ticket:** `<link or identifier>`
- **Related feature brief:** `<path or link>`

---

## 1. Problem Solved

<!--
Describe the actual user, system, or business problem addressed.
Do not describe only the code that was changed.
-->

---

## 2. Final Scope

### Included

<!--
List what was actually implemented.
-->

- 

### Excluded

<!--
List what remained outside the implementation.
-->

- 

### Scope Changes

<!--
Record any difference between the original plan and the final implementation.
Explain why the scope changed.
-->

- 

---

## 3. Acceptance Criteria

<!--
Reflect the final state honestly.
-->

| Acceptance Criterion | Status | Evidence |
|---|---|---|
|  | Met / Partial / Not Met |  |

---

## 4. Assumptions

<!--
List assumptions that influenced the implementation.
-->

| Assumption | Impact on the Solution | Risk If Wrong |
|---|---|---|
|  |  |  |

---

## 5. Selected Approach

<!--
Describe the implemented approach in concrete terms.
-->

---

## 6. Why This Approach Was Selected

<!--
Explain why this approach fit the problem, repository, constraints, and current scale.
-->

- 

---

## 7. Alternatives Considered

### Alternative 1 — <Name>

- **Benefits:**
- **Costs / Risks:**
- **Why it was not selected:**

### Alternative 2 — <Name>

- **Benefits:**
- **Costs / Risks:**
- **Why it was not selected:**

<!--
If there was no meaningful alternative, explain why instead of inventing one.
-->

---

## 8. Decision Costs

<!--
What complexity, coupling, maintenance, performance, migration, or operational cost did this decision introduce?
-->

- 

---

## 9. Change Triggers

<!--
Under which future conditions should the selected approach be reconsidered?
-->

- 

---

## 10. Failure Modes

### Failure Mode 1 — <Scenario>

- **Consequence:**
- **Expected behavior:**
- **Current protection:**
- **Verification evidence:**
- **Residual risk:**

### Failure Mode 2 — <Scenario>

- **Consequence:**
- **Expected behavior:**
- **Current protection:**
- **Verification evidence:**
- **Residual risk:**

### Failure Mode 3 — <Scenario>

- **Consequence:**
- **Expected behavior:**
- **Current protection:**
- **Verification evidence:**
- **Residual risk:**

---

## 11. Tests Added

<!--
List only tests that were actually added.
-->

| Test | What It Proves | Result |
|---|---|---|
|  |  | Passed / Failed / Not Run |

---

## 12. Tests Not Added

<!--
Record intentionally missing tests.
Every omission must include a reason and accepted risk.
-->

| Missing Test | Reason | Accepted Risk | Owner / Follow-up |
|---|---|---|---|
|  |  |  |  |

---

## 13. Verification Evidence

<!--
Report what was actually executed.
Do not report planned checks as completed.
-->

| Check | Command / Method | Result | Notes |
|---|---|---|---|
| Build |  | Passed / Failed / Not Run |  |
| Unit tests |  | Passed / Failed / Not Run |  |
| Integration tests |  | Passed / Failed / Not Run |  |
| Static analysis / linting |  | Passed / Failed / Not Run |  |
| Formatting |  | Passed / Failed / Not Run |  |
| Manual verification |  | Passed / Failed / Not Run |  |
| Final diff review |  | Passed / Failed / Not Run |  |

### Unverified Areas

<!--
List anything that could not be verified and why.
-->

- 

---

## 14. Known Limitations

<!--
List current limitations without minimizing them.
-->

- 

---

## 15. Open Decisions

<!--
List decisions intentionally left unresolved.
-->

| Decision | Why It Remains Open | Impact | Owner |
|---|---|---|---|
|  |  |  |  |

---

## 16. Files Changed

<!--
List the meaningful files or areas changed.
Avoid dumping every generated file when a grouped description is clearer.
-->

| File / Area | Change | Reason |
|---|---|---|
|  |  |  |

---

## 17. Operational Notes

<!--
Include only what is relevant:
configuration, environment variables, migrations, deployment order,
rollback, observability, cleanup, or external dependencies.
-->

### Configuration

- 

### Migration / Deployment

- 

### Rollback

- 

### Observability

- 

---

## 18. Security and Privacy Notes

<!--
Complete this section when the change affects authentication, authorization,
personal data, secrets, permissions, or trust boundaries.
-->

- 

---

## 19. Next Steps

<!--
List concrete follow-up work.
Do not hide incomplete work behind vague language.
-->

- [ ] 
- [ ] 
- [ ] 

---

## 20. Questions the Developer Must Be Able to Answer

<!--
These questions must be specific to the implementation.
They are not a summary generated on behalf of the developer.
They expose what the developer must understand and defend.
-->

1. Why was this implementation chosen for this problem and repository?
2. What viable alternative was considered, and why was it rejected?
3. Where can this implementation fail?
4. Which cost or limitation are we deliberately accepting?
5. Which verification evidence supports the current result?
6. What remains unverified?
7. Under what future condition should this approach change?
8. What would break if one of the core assumptions were false?

### Feature-Specific Questions

1. 
2. 
3. 

---

## 21. Final Ownership Check

Before closing the task:

- [ ] I can explain the problem without reading the code.
- [ ] I can explain why the selected approach was used.
- [ ] I can name at least one viable alternative.
- [ ] I understand the main failure modes.
- [ ] I know which tests were added and which were not.
- [ ] I can distinguish verified facts from assumptions.
- [ ] I know the current limitations and open decisions.
- [ ] I can defend the decision to another engineer.
- [ ] I know when this decision should be reconsidered.

---

## Final Statement

AI may have helped produce the implementation.

The developer still owns:

- the problem,
- the decisions,
- the trade-offs,
- the verification,
- the unresolved risks,
- and the consequences.
