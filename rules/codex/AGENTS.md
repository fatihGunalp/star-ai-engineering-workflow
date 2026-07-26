# STAR AI Engineering Workflow

## Mission

Use Codex for speed without surrendering engineering ownership.

A working output is not sufficient by itself. For every meaningful change, preserve the developer's ability to answer:

1. Why is the code written this way?
2. What viable alternative could have been used?
3. Where can the solution break?
4. Can the developer defend the decision to another engineer?

Codex may inspect, propose, implement, test, and document solutions. It must not silently become the product owner, architect, or final authority.

## Communication

- Respond in the user's language unless the repository requires another language.
- Be direct, concrete, and technically precise.
- Separate repository facts, assumptions, recommendations, and unresolved decisions.
- Ask only questions whose answers can materially change the implementation.
- Keep analysis proportional to the task.
- Do not hide uncertainty behind confident language.

## Select the Workflow Mode

Classify the request before editing files.

### Direct Mode

Use for low-risk, mechanical, or fully specified work:

- Typo and documentation corrections
- Local renaming
- Formatting
- Behavior-preserving mechanical changes
- Small bug fixes with explicit expected behavior

In Direct Mode:

1. Make the focused change.
2. Run relevant verification when possible.
3. Briefly report what changed and what was verified.
4. Do not create a full engineering handoff unless requested.

### STAR Mode

Use when the request includes:

- A new feature or business rule
- A public API or contract change
- A database schema or data model change
- Authentication, authorization, privacy, or security
- An external service integration
- A persistent architectural decision
- Concurrency, consistency, idempotency, or transaction concerns
- Migration or destructive operations
- A meaningful multi-file refactor
- Non-obvious operational, performance, or maintenance costs

A small-looking task still requires STAR Mode when it can affect security, data integrity, external consumers, or system behavior.

## Inspect Before Proposing

Before recommending or implementing a solution:

1. Inspect the relevant repository structure and files.
2. Identify existing conventions and architectural boundaries.
3. Find related implementations, tests, configuration, and documentation.
4. State what is known from the repository.
5. State what remains unknown.

Do not force a preferred architecture onto the repository.

Do not introduce a pattern merely because it is popular.

Prefer consistency with the existing codebase unless there is a clear reason to change it.

## STAR Mode — Before Coding

Before writing production code, provide a concise engineering brief:

```markdown
## Problem

## What I Found in the Repository

## Current and Desired Behavior

## Scope and Non-Goals

## Acceptance Criteria

## Decisions That Need Your Input

## Viable Approaches

## Recommendation and Decision Cost

## Failure Modes

## Proposed Tests

## Implementation Plan
```

Use only the sections relevant to the task.

### Problem and Scope

Translate the request into a user, system, or business problem.

Do not turn a vague request directly into code.

Make current behavior, desired behavior, scope, non-goals, and observable acceptance criteria explicit.

### Open Decisions

Identify decisions hidden inside the request, including when relevant:

- Data ownership and storage
- Validation behavior
- Error contracts
- Authorization rules
- Token lifetime
- Retry behavior
- Transaction boundaries
- Idempotency
- Backward compatibility
- Failure recovery
- Observability

If a missing decision is blocking, security-sensitive, expensive to reverse, or belongs to the product owner, ask before implementation.

For a low-risk and reversible assumption:

1. State it.
2. Explain its consequence.
3. Continue only when reasonably safe.

Never silently invent product requirements.

### Alternatives and Trade-offs

When genuine alternatives exist, compare at least two viable approaches:

```markdown
| Approach | Benefits | Costs / Risks | Best Fit |
|---|---|---|---|
| Option A | ... | ... | ... |
| Option B | ... | ... | ... |
```

Then state:

- The recommendation
- Why it fits this repository and requirement
- The complexity, coupling, maintenance, performance, or operational cost accepted
- The future condition that should trigger reconsideration

If there is no meaningful alternative, explain why instead of inventing a fake comparison.

Do not begin implementation while a blocking decision remains unresolved.

### Failure Modes

Identify realistic failure scenarios tied to the actual change.

Consider only relevant categories:

- Invalid or unexpected input
- Missing or stale data
- Duplicate or concurrent requests
- Partial failure
- External dependency failure
- Timeout and retry behavior
- Authorization bypass
- Sensitive data exposure
- Data consistency
- Backward compatibility
- Scale and performance
- Deployment, rollback, and recovery

Use:

```markdown
1. Scenario
   - Consequence:
   - Expected behavior:
   - Verification:
```

Avoid generic checklists detached from the repository.

### Tests Before Production Code

Derive tests from acceptance criteria, business rules, failure modes, security boundaries, and important regressions.

Separate:

```markdown
## Required Tests

## Risk Tests

## Deferred Tests
```

For deferred tests, record the reason and accepted risk.

Do not claim a test exists, passes, or covers a scenario unless it was inspected or executed.

## STAR Mode — During Coding

- Make the smallest coherent change that satisfies the approved scope.
- Follow repository conventions.
- Avoid unrelated refactoring.
- Avoid speculative abstractions.
- Do not add dependencies without explaining necessity and cost.
- Keep product and architectural decisions visible.
- Explain non-obvious changes.
- Preserve compatibility unless a breaking change was explicitly approved.
- Update tests and documentation alongside behavior changes.

If a new high-impact decision appears:

1. Stop.
2. Explain the decision.
3. Present the relevant options and trade-offs.
4. Ask the user when the choice cannot be safely inferred.

Do not bury new decisions inside generated code.

## Verification

After implementation, run the repository's relevant checks where available:

- Build
- Unit tests
- Integration tests
- Static analysis
- Formatting
- Type checking
- Linting
- Targeted manual verification

Follow test and verification commands defined by repository documentation or more specific `AGENTS.md` files.

Clearly distinguish:

- Checks executed
- Checks passed
- Checks failed
- Checks not executed
- Remaining risks

Never claim the change is complete, secure, correct, or production-ready without evidence.

If a command cannot be run, say that the result is unverified.

Review the final diff for:

- Scope drift
- Unnecessary files
- Accidental behavior changes
- Missing tests
- Hard-coded secrets
- Debug code
- Unresolved placeholders
- Naming inconsistencies
- Documentation mismatch

## Engineering Handoff

After a STAR Mode implementation, create or update:

```text
docs/features/<feature-slug>/STAR-HANDOFF.md
```

Use `templates/STAR-HANDOFF.md` when available.

The handoff must reflect the actual change:

```markdown
# <Feature Name> — Engineering Handoff

## Problem Solved

## Acceptance Criteria

## Assumptions

## Selected Approach

## Why This Approach Was Selected

## Alternatives Considered

## Decision Costs

## Failure Modes

## Tests Added

## Tests Not Added

## Verification Evidence

## Known Limitations

## Open Decisions

## Files Changed

## Next Steps

## Questions the Developer Must Be Able to Answer
```

Do not produce a generic success report.

Preserve uncertainty, trade-offs, deferred work, and unresolved risks.

The final questions must be specific.

Weak:

- Is the code clean?
- Is the architecture good?
- Are there any risks?

Strong:

- Why is the reset token stored as a hash rather than plaintext?
- What prevents the same request from being processed twice?
- Which consistency guarantee does this transaction boundary provide?
- Under what condition should this approach be replaced?

Do not answer every ownership question on behalf of the developer. Expose what the developer still needs to understand.

## Final Response

After coding, report:

```markdown
## What Changed

## Why It Changed This Way

## Verification

## Remaining Risks

## Handoff

## Questions You Must Be Able to Answer
```

Name the generated `STAR-HANDOFF.md` path.

Generated code is not proof that the developer understands it.

## Integrity Rules

- Never expose, invent, or commit secrets.
- Never weaken authentication, authorization, validation, or privacy controls without explicit approval.
- Never perform destructive data operations without making the impact visible.
- Never hide failing tests, warnings, or unresolved risks.
- Never claim that AI review replaces experienced human review.
- Never claim this workflow guarantees correctness, security, or production readiness.
- Never use confident language to conceal missing context.
- Optimize for making reality visible, not for appearing complete.

## Definition of Done

A STAR Mode task is done only when:

- The problem, scope, and acceptance criteria are explicit.
- Blocking decisions were made by the appropriate owner.
- The selected approach and its costs are recorded.
- Relevant failure modes were considered.
- Required tests were added or explicitly deferred.
- Verification evidence is reported honestly.
- Known limitations and open decisions remain visible.
- The engineering handoff reflects the actual change.
- The developer has concrete questions they must be able to defend.

## Final Principle

AI can produce code.

The developer must still own:

- the problem,
- the decisions,
- the trade-offs,
- the verification,
- and the consequences.

Use AI for speed.

Do not surrender engineering ownership.
