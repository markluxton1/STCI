# Every quartic ancestor in the quadric quotient direction is excluded

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]` in characteristic
zero. Status: **PROVED, conditional on the accepted ancestor-to-canonical-
triple reduction and P-037.** This removes a specific conormal direction
for **every** second-defect divisor. It does not remove an entire
positive-D2 degree stratum. The d2=4 Gorenstein possibility outside this
direction is retained.

Let `Q=(q=0)`, with `q=x0*x3-x1*x2`. It is the smooth Segre quadric.
Up to interchange of the two rulings, C0 has class `(1,3)` on Q:
its two projection degrees are three and one. In the balanced finite
normal frame

```text
V=x2-z^3, U=q-z*V/2,
```

the quotient direction `A=-z/2,B=1` is exactly the conormal quotient
of C0 inside Q, of degree -6. Indeed the transverse path
`U=-(z/2)*epsilon,V=epsilon` has q identically zero. Thus its canonical
double is the double divisor `2C0` on Q. This identification uses only
the first quotient; positive D2 and any higher degeneration do not
change the canonical double.

Suppose a common quartic ancestor exists in this direction. Both F and
G contain its canonical triple, hence contain this canonical double.
Their restrictions to Q therefore belong to

```text
H0(Q, O_Q(4,4)(-2C0))=H0(Q,O_Q(2,-2))=0.
```

The last equality follows from the product cohomology of P1 times P1:
a negative degree on either ruling has no global sections. Consequently
both quartics restrict to zero on Q and are divisible by q. Write
`F=q*F2,G=q*G2`. The original equations give

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This contradicts the all-stage degree-two common-ancestor exclusion
P-037. The nonzero target u ensures `q*alpha` is nonzero. The proof
uses neither a mate supported on C0 nor a false assertion that F
annihilates the quadruple.

In particular the proof includes the otherwise retained `e=1,d2=d3=4`
Gorenstein boundary **when its first quotient is this quadric direction**.
It also includes quartics with zero first-normal symbol. No assumption
that the canonical triple is primitive is made.

The independent exact coefficient check
[`verify_session_localcoh_quadric_direction_2026_10_08.py`](../computations/verify_session_localcoh_quadric_direction_2026_10_08.py)
reconstructs all 35 ambient degree-four monomials and imposes both
vanishing on C0 and the first derivative along the actual Q path. The
combined matrix has rank 25. Its complete ten-dimensional kernel is
`q*H0(P3,O(2))`, checked against ten independent homogeneous quadratic
monomials. This matches the divisor proof and rules out any omitted
quartic first-symbol kernel member.

The rank check is a separate exact verification of the complete quartic
space; the global divisor proof supplies the defect-independent reason.
The two already excluded cubic-factor endpoint directions and four
one-dimensional endpoint fibres are recorded separately in
[`2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md`](2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md).
