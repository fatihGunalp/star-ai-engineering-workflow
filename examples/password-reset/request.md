# Example — Password Reset: From Request to Decisions

> Illustrative example. The project, file names, and stack (ASP.NET Core, EF Core, PostgreSQL) are fictional.
> It shows how a STAR conversation is expected to flow **before** production code is written.
> The outcome is recorded in [`completed-handoff.md`](completed-handoff.md).

---

## 1. The developer's request

```text
/star-engineering Add a password reset feature to this project.
```

In Codex the same request starts with `$star-engineering`. Without the prefix, the agent may still select the Skill on its own because the task touches authentication; automatic selection is not guaranteed.

---

## 2. The agent's response before coding

The request affects authentication, a new data model, and an external service (email), so the agent uses **STAR mode** instead of generating code immediately.

```markdown
## Problem

Users who forget their password cannot regain access without contacting
support. They need to set a new password through email, securely, without
knowing the current one.

## What I found in the repository

- Authentication: `src/Auth/AuthService.cs` (cookie sessions)
- Users: `src/Users/User.cs`, PostgreSQL via EF Core
- Email: `src/Notifications/IEmailSender.cs` already exists
- Tests: xUnit; integration tests use a Testcontainers PostgreSQL instance
- Not found: any rate limiting infrastructure

## Acceptance criteria

1. A registered user can request a reset link.
2. The response is identical whether or not the email is registered.
3. A token works only once and expires.
4. After a reset, the old password no longer works.

## Blocking decisions (yours to make)

1. Token lifetime: 15 minutes, 30 minutes, or 1 hour?
2. Should a new request invalidate older active tokens?
3. Should all active sessions be signed out after a reset?

## Recommended path and trade-off

Random token, stored only as a hash in the database.
A signed stateless token needs no storage, but it cannot be revoked or
made single-use without adding database state anyway.
Accepted cost: one new table and a cleanup job for expired tokens.

## Failure tests

- The same token submitted twice in parallel: exactly one request succeeds.
- The email service fails: the user still gets the generic response; nothing leaks.
- The token expires during submission: rejected without revealing details.

## Plan

1. Token entity and migration
2. Request endpoint (generic response)
3. Confirm endpoint (hash lookup, expiry, single-use)
4. Tests for each acceptance criterion and failure test
5. Handoff: `docs/features/password-reset/STAR-HANDOFF.md`
```

Only the three product and security decisions block the work. Everything else is stated as an assumption so the work can continue.

---

## 3. The developer's decisions

```text
1. 30 minutes.
2. Yes, invalidate older tokens.
3. Yes, sign out all sessions.

Rate limiting is out of scope for now; record it as a known limitation.
```

The agent did not make these decisions silently. The developer made them and now owns them.

---

## 4. What happens next

The agent implements the approved scope in small steps, runs the available checks, and records the result in [`completed-handoff.md`](completed-handoff.md).
