# Password Reset — STAR engineering handoff

> Illustrative example of a completed handoff, written with the
> [handoff template](../../skills/star-engineering/assets/handoff-template.md).
> The project, file names, and stack (ASP.NET Core, EF Core, PostgreSQL) are fictional.
> The decisions behind it are recorded in [`request.md`](request.md).

## Problem and accepted behavior
- User/system problem: Users who forgot their password had no self-service way back in and had to contact support.
- Before → after: Manual reset by support → user requests an emailed link and sets a new password.
- In scope / out of scope: Request and confirm endpoints, token storage, reset email, session sign-out / rate limiting, MFA reset, UI redesign.
- Acceptance criteria and state:
  - Registered user can request a link — **met**
  - Same response for unknown emails — **met**
  - Token is single-use and expires after 30 minutes — **met** (single-use under concurrency: **partial**, see gaps)
  - Old password stops working after a reset — **met**

## Decisions and trade-offs
- Decision owner and approved choices: Developer approved a 30-minute lifetime, invalidating older tokens on a new request, and signing out all sessions.
- Selected approach and why: A 32-byte random token is emailed; only its SHA-256 hash is stored. Single-use is enforced by a conditional update (`WHERE used_at IS NULL`) in the same transaction as the password change, so revocation and single-use come from the database.
- Alternative considered and why not chosen: Signed stateless token. It needs no storage, but it cannot be revoked individually, and single-use would need stored state anyway.
- Cost accepted / trigger for reconsideration: One new table, database access on every reset, cleanup job still missing. Reconsider if reset traffic makes database load measurable or if passwordless login replaces this flow.

## Failure paths
| Realistic scenario | Expected behavior | Test or verification | Residual risk |
|---|---|---|---|
| Same token submitted twice in parallel | Exactly one request succeeds | Not tested; protected by the conditional update | Low, but unverified |
| Email service fails | Generic response; failure logged without the token | `RequestReset_EmailSenderFails_ReturnsGenericResponse` | User is not told to retry |
| Unlimited reset requests | Requests should be throttled | None | **High** until rate limiting exists |
| Token expires during submission | Rejected without revealing details | `Confirm_ExpiredToken_IsRejected` | None known |

## Verification evidence
| Check or test | Actually run? | Outcome and evidence |
|---|---|---|
| Build | Yes | `dotnet build` passed |
| Relevant unit / integration tests | Yes | `dotnet test`: 8 tests passed (5 unit, 3 integration with Testcontainers PostgreSQL) |
| Boundary / concurrency / failure tests | Partly | Expiry, reuse, unknown email, and email failure passed; parallel use **not run** |
| Focused diff review | Yes | No unrelated changes, secrets, or debug code found |

## Gaps and ownership
- Tests missing / intentionally deferred: Parallel use of the same token (no concurrent test harness yet, issue `#43`); response timing for known vs. unknown emails (unreliable in CI).
- Known limits and unverified claims: No rate limiting; expired tokens are never deleted; response time may reveal whether an email is registered; only a local SMTP server was used, not the production provider.
- Open decisions and owner: Rate limiting strategy (product + backend); token cleanup schedule (backend).
- Changed files: `src/Auth/PasswordReset/*`, `src/Data/Migrations/*`, `src/Auth/SessionService.cs` (`RevokeAllForUser`), `tests/Auth/PasswordReset/*`.
- Follow-up / rollback considerations: Apply the migration before deploying. Rolling back the application is safe because the old version does not use the new table.

## Developer's four questions
1. Why was the selected approach appropriate for this problem?
   *Single-use and revocation were requirements; a stored, hashed token provides both without exposing usable links if the database leaks.*
2. What viable alternative exists, and which trade-off did we accept?
   *A signed stateless token. We accepted database access and a cleanup job in exchange for revocation and single-use.*
3. Where can it fail, and what did we do to test that?
   *Parallel token use (designed against, not tested), missing rate limiting (not protected), email failure (tested).*
4. What was **actually verified**, and which claims remain assumptions?
   *Verified: build, 8 tests, local manual flow. Assumptions: concurrency safety, production email delivery, timing behavior.*

> Question 3 has an honest gap: the parallel case is protected by design but has not been proven by a test. It stays open until issue `#43` is closed.
