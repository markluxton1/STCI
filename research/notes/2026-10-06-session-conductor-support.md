# Full inverse-image support and asymptotic conductor descent

Date: 2026-10-06. Status: **PROVED under the stated hypotheses;
independently audited by the frontier auditor and a separate local-algebra
auditor**.
This note corrects a missing support hypothesis in the historical P-032
formulation and gives a conditional construction valid in every
characteristic. It is not a resolution of the universal STCI problem.

Let X=V(F) be an integral hypersurface in P3 over an algebraically closed
field, C an integral curve in X, and nu:S->X the finite normalization.
Write H=nu*O_X(1), Q=nu_*O_S/O_X, and c=Ann(Q). Let

    W=(nu^{-1}(C))_red

denote the **entire** reduced inverse image, including possible isolated
points. A finite morphism does not ensure that W is pure dimensional.

## 1. An obstruction before divisor classes or descent

If X has an STCI mate G for C, the nonzero pullback of G is a section
of O_S(bH) whose zero set is exactly W. Its zero scheme is an effective
Cartier divisor on the integral normal surface S. Every minimal prime
of a nonzero principal ideal in a Noetherian domain has height one.
Consequently W has no isolated zero-dimensional irreducible component.

Thus an isolated point in the full inverse image of C excludes **every
mate degree on this fixed carrier**. It does not exclude C as an STCI
on a different carrier.

The historical P-032 notation implicitly replaced W by the union of its
curve components. That replacement requires a purity check. Finiteness
rules out exceptional divisors over closed points, but does not rule out
isolated inverse-image points.

The fixed-degree corrected criterion is: there exists an effective
Cartier divisor A on S with |A|=W, an isomorphism O_S(A)=O_S(bH), and
descent of its canonical section to O_X(b). Equivalently the canonical
section must match a section on the full conductor scheme. The proof
of P-032 then applies verbatim. If W is pure dimensional, A can be
written as a positive integer combination of **all** curve components
of W; if W is not pure dimensional, no such A exists.

## 2. Asymptotic descent when all nonnormality lies on C

**Conditional theorem.** Assume Supp(Q) is contained in C. Then the
following are equivalent:

1. C has an STCI mate on X, of some positive degree;
2. there are b>0 and an effective Cartier divisor A on S such that
   |A|=W and O_S(A) is isomorphic to O_S(bH).

Necessity follows by pulling back a mate. For sufficiency transport
the canonical section of A to s in H0(S,O_S(bH)). The conductor c is
an ideal both in O_X and in nu_*O_S: locally for A subset B,
c={a in A : aB subset A} satisfies cB=c, hence nu_*c_S=c.
Its ideal on S, denoted c_S,
has zero set contained in W, since Supp(Q) is contained in C.

Let I_A=O_S(-A). Since V(c_S) is contained in V(I_A), locally
I_A is contained in radical(c_S). Noetherianity and quasi-compactness
give a single positive N with

    I_A^N contained in c_S.

In each trivialization of O_X(b), the coefficient of s^N therefore
belongs to the conductor. It belongs to O_X; these coefficients glue
because the trivializations are pulled back from X. Hence s^N descends
to t in H0(X,O_X(Nb)). The restriction map

    H0(P3,O(Nb)) -> H0(X,O_X(Nb))

is surjective, since H1(P3,O(Nb-deg F))=0. An ambient lift G has zero
set C on X, by finite surjectivity and |V(s^N)|=W. This is the required
pair (F,G). The proof uses no Frobenius and works in all characteristics.

This removes the **existence of some mate** conductor obstruction for
carriers whose nonnormal locus is entirely supported on C. It does
not remove conductor descent at a prescribed degree and does not
produce the requisite positive Cartier divisor or its linear equivalence.
Additional nonnormal curves away from C remain a genuine loophole.

## 3. Exact control example already present in the checkout

The retained characteristic-zero verifier verify_general_conductor_power.py reconstructs
the cubic pinch surface

    X: x^2 w-y^2 z=0

and its smooth-scroll normalization with affine chart

    (x,y,z,xi,w)=(u,ur,1,r,r^2).

For the indicated twisted cubic C, the full pulled-back ideal on this
chart is

    (h u,h(r+1))=(h) intersect (u,r+1),
    h=r-1-u(1+r).

The two factors are comaximal because h(0,-1)=-2. This example requires
characteristic different from two; the verifier works over Q. Thus the preimage
contains the divisor h=0 and an isolated reduced point (u,r+1).
The obstruction in section 1 already excludes this fixed carrier.
The verifier also checks that this same twisted cubic is STCI on
another carrier by the standard degree-(2,3) pair. Its existence must
remain visible: the obstruction is carrier-specific.

The verifier's docstring points to the 2026-10-05 literature note for
the unit-ratio example, but that explanation is absent from the retained
version of the note. This present support proof does not rely on the
missing explanatory text or on a sampled power calculation.

## 4. Primary-source background and continuation boundary

The Stacks Project effective-Cartier discussion supplies the standard
local nonzerodivisor and pure-codimension-one facts:
https://stacks.math.columbia.edu/tag/01WQ and
https://stacks.math.columbia.edu/tag/0B3Q.
The conductor argument above is proved here directly; no novelty claim
is made.

For future thick-carrier work, first test purity of W, then decide
whether Supp(Q) is contained in C. If it is, the remaining global
task is positive Cartier support and hyperplane linear equivalence
upstairs. If it is not, keep the full nonreduced conductor square and
residue-unit gluing data. Normalization does not by itself supply either.
