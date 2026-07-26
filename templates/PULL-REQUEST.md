# Pull Request — <Change Title>

> Explain not only what changed, but why the change was made, how it was verified, and what remains uncertain.
>
> Remove sections that are not relevant. Do not replace missing evidence with confident language.

---

## Summary

<!--
Describe the change in a few direct sentences.
Focus on the problem solved and the outcome.
-->

---

## Problem

<!--
What user, system, or business problem does this pull request address?
Do not describe only the implementation.
-->

---

## Scope

### Included

- 

### Not Included

<!--
State what this pull request intentionally does not solve.
-->

- 

---

## Related Work

- **Issue / ticket:** `<link or identifier>`
- **Feature brief:** `<path or link>`
- **Engineering handoff:** `<path or link>`
- **Decision record:** `<path or link or not applicable>`

---

## Selected Approach

<!--
Describe the implemented approach in concrete terms.
-->

---

## Why This Approach

<!--
Explain why this approach fits the current requirement, repository, and constraints.
Avoid vague statements such as "cleaner", "better", or "more scalable"
without defining what they mean in this context.
-->

- 

---

## Alternatives Considered

### Alternative 1 — <Name>

- **Benefits:**
- **Costs / risks:**
- **Why it was not selected:**

### Alternative 2 — <Name>

- **Benefits:**
- **Costs / risks:**
- **Why it was not selected:**

<!--
If there was no meaningful alternative, explain why instead of inventing one.
-->

---

## Decision Costs

<!--
What complexity, coupling, maintenance, performance, migration,
or operational cost are we deliberately accepting?
-->

- 

---

## Behavior Changes

### Before

<!--
What happened before this pull request?
-->

---

### After

<!--
What happens after this pull request?
-->

---

## Failure Modes

<!--
List realistic failure scenarios tied to the actual change.
-->

| Scenario | Expected Behavior | Protection / Handling | Residual Risk |
|---|---|---|---|
|  |  |  |  |

---

## Tests

### Tests Added or Updated

| Test | What It Proves | Result |
|---|---|---|
|  |  | Passed / Failed / Not Run |

### Tests Not Added

| Missing Test | Reason | Accepted Risk | Follow-up |
|---|---|---|---|
|  |  |  |  |

---

## Verification

<!--
Report only checks that were actually executed.
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

## Security and Privacy

<!--
Complete when the change affects authentication, authorization,
personal data, secrets, permissions, or trust boundaries.
-->

- [ ] No new security or privacy impact
- [ ] Security or privacy impact is documented below

Details:

- 

---

## Data, Migration, and Compatibility

<!--
Complete when the change affects database schemas, stored data,
external contracts, public APIs, or backward compatibility.
-->

- [ ] No migration required
- [ ] Migration required and documented
- [ ] Backward compatible
- [ ] Breaking change approved and documented

Details:

- 

---

## Operational Impact

<!--
Complete when relevant.
-->

### Configuration

- 

### Deployment

- 

### Rollback

- 

### Observability

- 

---

## Files Changed

<!--
List meaningful files or areas. Group generated files when appropriate.
-->

| File / Area | Change | Reason |
|---|---|---|
|  |  |  |

---

## Known Limitations

<!--
Do not minimize or hide current limitations.
-->

- 

---

## Open Decisions

| Decision | Why It Remains Open | Impact | Owner |
|---|---|---|---|
|  |  |  |  |

---

## Reviewer Focus

<!--
Tell the reviewer where judgment is needed.
Do not ask only for syntax or style review.
-->

Please focus on:

1. 
2. 
3. 

---

## Questions the Author Must Be Able to Answer

1. Why was this implementation chosen?
2. What viable alternative was considered?
3. Where can this solution fail?
4. Which cost or limitation are we accepting?
5. Which verification evidence supports the change?
6. What remains unverified?
7. Under what future condition should this approach change?

### Change-Specific Questions

1. 
2. 
3. 

---

## Author Checklist

### Ownership

- [ ] I can explain the problem without reading the implementation.
- [ ] I can explain why this approach was selected.
- [ ] I can name at least one viable alternative.
- [ ] I understand the main failure modes.
- [ ] I can defend the accepted trade-offs.

### Scope

- [ ] The pull request addresses one coherent problem.
- [ ] Unrelated refactoring is excluded.
- [ ] Scope changes are documented.
- [ ] Non-goals remain outside the implementation.

### Quality

- [ ] Acceptance criteria are met or exceptions are documented.
- [ ] Relevant tests were added or intentionally deferred.
- [ ] Verification results are reported honestly.
- [ ] No secret, debug code, or unresolved placeholder was committed.
- [ ] Documentation matches the final behavior.

### Handoff

- [ ] `STAR-HANDOFF.md` was created or updated when required.
- [ ] Known limitations remain visible.
- [ ] Open decisions have an owner or follow-up.
- [ ] The reviewer knows where engineering judgment is needed.

---

## Reviewer Checklist

- [ ] The problem and scope are clear.
- [ ] The selected approach fits the repository.
- [ ] Alternatives and trade-offs are credible.
- [ ] Failure modes are specific to the change.
- [ ] Verification evidence supports the claims.
- [ ] Missing tests and residual risks are visible.
- [ ] The author can defend the decision.
- [ ] Approval does not rely only on the code compiling or tests passing.

---

## Final Ownership Statement

AI may have assisted with analysis, implementation, tests, or documentation.

The author remains responsible for:

- the problem,
- the decisions,
- the trade-offs,
- the verification,
- the unresolved risks,
- and the consequences.
