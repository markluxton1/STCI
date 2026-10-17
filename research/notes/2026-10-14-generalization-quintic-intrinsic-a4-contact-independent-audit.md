# Independent audit: intrinsic A4 contact and the h2 common-root condition

Date: 2026-10-14, completed after local midnight on October 15.

Status: **PASS for the new contact bound and the resulting homogeneous
h2 condition Res(H,Q6)=0 on every surviving mate candidate.** This does
not prove the remaining resultant locus empty or prove conductor power
descent.

The reviewed proposal is
[the intrinsic A4 contact-bound note](2026-10-14-generalization-quintic-intrinsic-a4-contact-bound.md).
The actual conductor octic, the complete A4 target-fiber criterion and
the accepted exclusion of G=Jbar=0 are premises. No accepted verifier
was replayed. This audit checks the new deductions directly and reads
the new coefficient-extraction source and its captured execution.

## 1. Actual A4 fibers force the needed nonvanishing

Work on the accepted admissible finite birational nonendpoint quintic
projection family, in characteristic zero, with delta nonzero. Write
j=Jbar and let SUP mean full inverse support. The accepted A4 target
fiber criterion at j=0 states that an off-c point exists exactly when

    D0=delta^2/2+B is nonzero,       G=-2D0.

For G nonzero, put L=delta^2+2B+G=2D0+G. If L=0, then
D0=-G/2 is nonzero and the displayed criterion produces an actual
off-c point. Thus

    j=0, G nonzero, SUP implies L nonzero.              (1)

This implication respects the D0=0 exception: that exception cannot
occur when L=0 and G is nonzero. No affine/projective denominator is
discarded in the argument.

## 2. Exact contact one or two

Let F(p) be the accepted actual conductor octic, with intrinsic A4
point p=0. The new coefficient identities are

    F(0)|_(j=0)=0,
    [p]F|_(j=0)=-2G L(3delta^2+G)^2,
    [p^2]F|_(j=0,G=-3delta^2)
        =-108delta^5(delta^2-B).                        (2)

The new source reads the accepted primitive polynomial directly and
asserts precisely these identities; it reconstructs neither the
conductor determinant nor the accepted fiber theorem. Its
[attempt-01 execution record](../validation/2026-10-14-quintic-intrinsic-a4-contact/attempt-01/execution-record.json)
records the accepted input digest, source digest, exit zero and empty
stderr. This is a new coefficient-extraction check, not a rerun of an
accepted verifier.

On j=0, G nonzero, SUP, equation (1) makes the factors G and L in
the first coefficient nonzero. If G+3delta^2 is nonzero, F has exact
order one at p=0. If G=-3delta^2, the first coefficient vanishes and

    L=2(B-delta^2),
    [p^2]F=54delta^5 L,                                 (3)

which is nonzero by (1). F therefore has exact order two. Since p is
a uniformizer of the smooth curve C0 at this point and c maps
isomorphically to C0, these orders are the actual conductor-contact
orders on c. Thus the new all-parameter conclusion is

    j=0, G nonzero, SUP implies ord_A4(F) in {1,2}.      (4)

The new argument does not apply (4) to G=0. For mate candidates, that
lane is removed by the separate accepted G=j=0 theorem. Only its
mate-exclusion conclusion is needed here; no new assertion about its
full-support scope is required.

## 3. The h2 resultant condition

Use the independently audited factorization Fsrc=H Q6, with H the
complete homogeneous conormal gcd of degree two, Q6 nonzero of degree
six, and source coordinates x=T/S=r/delta. The intrinsic A4 point
is S=0. The accepted leading-coefficient identities imply

    S divides H implies G=j=0.

Consequently H avoids A4 on all surviving mate candidates after the
accepted G=j=0 closure.

For j nonzero, SUP requires support(Q6) contained in support(H).
A nonzero homogeneous sextic over the algebraically closed field has
a root; hence Q6 and H have a common root and Res(H,Q6)=0.

For j=0, suppose instead that Res(H,Q6) is nonzero. This is the
homogeneous resultant, so H and Q6 have no common projective root,
including infinity and repeated-root cases. SUP permits support(Q6)
only in support(H) together with A4. Disjointness from H therefore
forces

    Q6=c S^6,       c nonzero.

Since H avoids A4, this would give ord_A4(Fsrc)=6. Equation (4)
gives a contradiction. Therefore

    every surviving actual h2 mate candidate satisfies
    Res(H,Q6)=0, for either value of j.                  (5)

This is a necessary incidence condition. It does not assert that the
quadratic and sextic have precisely one common root, that any root is
simple, or that conductor support or descent follows from the
resultant. On a rational finite inverse-map chart, a previously
captured exact factorization of this resultant may now be imposed
for j=0 as well as j nonzero, subject to that capture's denominator,
content and projection restrictions. No boundary chart is eliminated
by the proof of (5).

The accepted proofs remain premises. The new mathematical content
reviewed here consists only of (1), the deductions (3)-(5) from the
literal new coefficients, and their precise geometric scope.
