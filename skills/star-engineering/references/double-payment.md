# Everyday case: One order, two payments

> Illustrative scenario for learning and Reels. This is **not** a report of a real incident, a tested fix, or a claim about payment providers.

## The ordinary problem

A customer orders dinner. The payment screen seems frozen, so they tap **Pay** twice. The app shows one order, but the card can be charged twice if duplicate requests are processed as independent payments.

The development request looks simple:

```text
Ödeme butonuna iki kez basılınca ikinci ödemeyi engelle.
```

A coding assistant might immediately disable the UI button. That improves the screen but does **not**, by itself, prevent duplicate server requests caused by network retries, two devices, or webhook re-delivery.

## STAR's questions before changing code

1. **Behavior / acceptance criteria:** Does the same logical checkout produce at most one successful charge even if the client retries? What response should a retry receive?
2. **Decision owner:** How is the logical purchase identified? Who defines retry windows and what happens when the provider returns an unknown/timeout state?
3. **Alternatives:** UI-only button lock vs. server-side idempotency key tied to an order and persisted payment state. UI locking is useful, but server-side deduplication is a stronger boundary.
4. **Failure scenarios:** Two concurrent requests; payment provider succeeds but the app times out; callback arrives twice; database write fails after external charge; the customer intentionally makes a new order.
5. **Verification:** Simultaneous submissions, repeated callback, retry after timeout, and a distinct new order should have separately asserted outcomes.

## Example answer before code (illustrative)

```markdown
Problem: A second click or network retry can create a second charge for
one intended purchase.

Blocking decision: Which identifier represents one logical payment?
The server cannot decide a purchase's identity from a button click alone.

Recommended direction: Enforce idempotency on the server using an agreed
operation key and durable payment state. Disable the button as UX only.
Confirm the payment provider's idempotency and reconciliation semantics.

Required tests:
- Two concurrent requests with the same key do not create two charges.
- Retry after a timeout returns or reconciles the existing outcome.
- Duplicate callbacks cannot finalize the same order twice.
- A genuinely new purchase is still possible.
```

## What STAR actually changes

**Without STAR:** The assistant may solve only the visible UI symptom.

**With STAR:** It makes the hidden backend requirements, owner decisions, and failure tests visible *before* implementation. It does not guarantee that code will be correct; evidence still requires executable tests and review.

## Reels demonstration (about 25–35 seconds, suggested script)

- **Hook:** “Yemek siparişinde Öde'ye iki kez bastın. Kartından iki kere para çekildi.”
- **Problem:** “AI'a 'butonu kilitle' dedin. Çalışıyor gibi görünüyor.”
- **Reveal:** “Ama internet kopup istek tekrar gönderilince? Butonun kilitli olması sunucuyu korumuyor.”
- **Payoff:** “STAR, koddan önce şu soruyu sorduruyor: Aynı ödeme isteği iki kez gelirse ne olacak?”
- **CTA:** “Yazılım projenizde bu kontrol akışını denemek için yoruma **STAR** yazabilirsiniz.”

## Honest distribution note

The repository provides the **skill and installation instructions**. Instagram comment-to-DM delivery is a separate Meta/third-party messaging automation and is **not** implemented by this repository. Do not promise an automatic link until that integration has been configured and tested.