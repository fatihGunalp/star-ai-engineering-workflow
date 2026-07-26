# Feature Brief — <Feature Name>

> Complete this document before production code is written for a meaningful change.
>
> Keep it concise. Record only decisions, risks, and constraints that can materially affect the implementation.

---

## Status

- **Feature slug:** `<feature-slug>`
- **Owner:** `<name or role>`
- **Status:** `Draft | Ready for Implementation | In Progress | Completed`
- **Created:** `YYYY-MM-DD`
- **Last updated:** `YYYY-MM-DD`
- **Related issue / ticket:** `<link or identifier>`

---

## 1. Problem

<!--
Describe the user, system, or business problem.
Do not describe the solution here.
-->

What problem are we solving?

---

## 2. Current Behavior

<!--
What happens today?
Include the relevant existing behavior, limitation, or failure.
-->

---

## 3. Desired Behavior

<!--
What should become possible after this change?
Describe observable behavior.
-->

---

## 4. Scope

### Included

<!--
List what this feature will include.
-->

- 

### Non-Goals

<!--
List what is intentionally excluded.
This protects the implementation from scope drift.
-->

- 

---

## 5. Acceptance Criteria

<!--
Write observable and testable conditions.
Avoid vague statements such as "works correctly" or "is user-friendly."
-->

- [ ] 
- [ ] 
- [ ] 

---

## 6. Repository Context

<!--
Record what was found in the existing codebase before proposing a solution.
-->

### Relevant Existing Components

- 

### Existing Conventions to Preserve

- 

### Related Tests

- 

### Constraints Found in the Repository

- 

---

## 7. Assumptions

<!--
List assumptions that are currently being used.
Each assumption should be visible and revisable.
-->

| Assumption | Why It Is Reasonable | Consequence If Wrong |
|---|---|---|
|  |  |  |

---

## 8. Open Decisions

<!--
List unanswered questions that can materially change the implementation.
Do not begin implementation while a blocking decision is unresolved.
-->

| Decision | Why It Matters | Owner | Blocking? | Status |
|---|---|---|---|---|
|  |  |  | Yes / No | Open |

---

## 9. Viable Approaches

<!--
Compare real alternatives only.
If there is no meaningful alternative, explain why.
-->

| Approach | Benefits | Costs / Risks | Best Fit |
|---|---|---|---|
| Option A |  |  |  |
| Option B |  |  |  |

---

## 10. Recommendation

<!--
State the recommended approach and why it fits this repository and requirement.
-->

### Selected Approach

---

### Why This Approach

---

### Decision Cost

<!--
What complexity, coupling, maintenance, performance, or operational cost are we accepting?
-->

- 

### Change Trigger

<!--
Under which future condition should this decision be reconsidered?
-->

- 

---

## 11. Failure Modes

<!--
Tie each failure mode to the actual feature.
Avoid generic checklist items.
-->

### Failure Mode 1 — <Scenario>

- **Consequence:**
- **Expected behavior:**
- **Verification:**

### Failure Mode 2 — <Scenario>

- **Consequence:**
- **Expected behavior:**
- **Verification:**

### Failure Mode 3 — <Scenario>

- **Consequence:**
- **Expected behavior:**
- **Verification:**

---

## 12. Test Plan

### Required Tests

<!--
Tests required for the acceptance criteria and core business behavior.
-->

- [ ] 

### Risk Tests

<!--
Tests for boundaries, concurrency, security, integrations, or failure recovery.
-->

- [ ] 

### Deferred Tests

<!--
For every deferred test, record the reason and accepted risk.
-->

| Test | Reason Deferred | Accepted Risk |
|---|---|---|
|  |  |  |

---

## 13. Implementation Plan

<!--
Describe small, coherent implementation steps.
Do not include unrelated refactoring.
-->

1. 
2. 
3. 

---

## 14. Expected File Changes

<!--
This is a forecast, not a guarantee.
Update it if the implementation scope changes.
-->

| File / Area | Expected Change | Reason |
|---|---|---|
|  |  |  |

---

## 15. Verification Plan

<!--
List the checks that should be executed after implementation.
Do not mark them as passed before they are actually run.
-->

- [ ] Build
- [ ] Unit tests
- [ ] Integration tests
- [ ] Static analysis / linting
- [ ] Formatting
- [ ] Targeted manual verification
- [ ] Final diff review

Additional project-specific checks:

- [ ] 

---

## 16. Handoff Target

After implementation, create or update:

```text
docs/features/<feature-slug>/STAR-HANDOFF.md
```

The handoff must reflect the actual work, verification evidence, remaining risks, known limitations, and questions the developer must be able to answer.

---

## 17. Questions the Developer Must Be Able to Answer

<!--
Write implementation-specific ownership questions.
Do not use generic questions such as "Is the code clean?"
-->

1. Why is this approach appropriate for the current problem and repository?
2. What viable alternative was considered, and why was it not selected?
3. Where can this solution fail?
4. Which cost or limitation are we deliberately accepting?
5. Under what future condition should this decision change?

---

## Readiness Check

The feature is ready for implementation only when:

- [ ] The problem is explicit.
- [ ] Scope and non-goals are clear.
- [ ] Acceptance criteria are observable.
- [ ] Repository context has been inspected.
- [ ] Blocking decisions are resolved.
- [ ] Alternatives and trade-offs are visible.
- [ ] Relevant failure modes are defined.
- [ ] Required tests are planned.
- [ ] The implementation plan is focused.
