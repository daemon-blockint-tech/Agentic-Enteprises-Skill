# Financial mathematics foundations

## Table of contents

1. [Interest theory](#interest-theory)
2. [Annuities certain](#annuities-certain)
3. [Loans and amortization](#loans-and-amortization)
4. [Bonds, yield, duration](#bonds-yield-duration)
5. [Notation and exam habits](#notation-and-exam-habits)
6. [Bridges](#bridges)

## Interest theory

| Concept | Definition / relation |
|---|---|
| Effective rate \(i\) | Growth per period: \(1+i\) |
| Nominal rate \(i^{(m)}\) | Compounded \(m\) times per year: \(1+i=(1+i^{(m)}/m)^m\) |
| Discount rate \(d\) | \(d=i/(1+i)\) |
| Force of interest \(\delta\) | Continuous compounding; \(a(t)=e^{\delta t}\) |
| Equivalence | Compare cashflows at same point in time via discounting |

**Unknowns**: Solve for rate, time, or amount using **time value of money** equations—always draw a timeline.

## Annuities certain

| Annuity | Payment timing | Standard symbol (awareness) |
|---|---|---|
| Immediate | End of period | \(a_{\overline{n}\mid}\) |
| Due | Beginning of period | \(\ddot{a}_{\overline{n}\mid}\) |
| Perpetuity | Infinite | \(a_{\overline{\infty}\mid}=1/i\) |

Relationships to memorize at foundation level:

- \(\ddot{a}_{\overline{n}\mid} = (1+i)\, a_{\overline{n}\mid}\)
- Present value of level payment stream ↔ loan payment (see below)

## Loans and amortization

- **Payment** \(P\) that amortizes principal with interest rate \(i\) over \(n\) periods
- **Outstanding balance** after \(k\) payments = PV of remaining payments
- **Yield** problems: find \(i\) given price and cashflows (may need numerical methods)

Actuarial link: same machinery as **premium financing** and **asset cashflows** at intro level.

## Bonds, yield, duration

| Topic | Foundation goal |
|---|---|
| Price vs yield | Inverse relationship; premium/discount par |
| Macaulay duration (intro) | Weighted average time of cashflows; sensitivity sketch |
| Convexity (intro) | Curvature of price–yield; why duration alone fails for large \(\Delta i\) |

Full ALM and asset strategy → `asset-liability-management` (not this skill).

## Notation and exam habits

- Define **payment period** vs **valuation date**
- State whether rates are **effective annual** or **nominal with compounding**
- Check **sign convention** (lender vs borrower) once per problem
- Verify answer with **alternate method** (e.g., PV of each cashflow)

## Bridges

| Foundation | Next skill |
|---|---|
| Annuities certain + survival (later) | Life annuities → `advanced-long-term-actuarial-mathematics` |
| Interest + statistics | Pricing present values of random cashflows |
| Duration intro | ALM and immunization overview → `asset-liability-management` |
