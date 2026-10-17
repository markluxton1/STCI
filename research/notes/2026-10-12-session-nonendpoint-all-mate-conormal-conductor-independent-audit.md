# Nonendpoint quintics: independent all-mate conormal/conductor audit

Date: 2026-10-12. Auditor:
`oct11_endpoint_support_global_audit/two_root_contact_audit`.

Status: **PASS: direct independent geometric proof of a necessary locus in
every mate degree.** This sharpens the generic degree-eight restriction,
but does not exclude the remaining resultant and A4 cotangent loci, all
nonendpoint projections, all quintic carriers, or fixed C0 itself.

The audited cubic data are in
[the corrected conormal reduction](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md),
as read with SHA-256
`3576392d41d4f64db506291f7cd0609a6930a80296eeedd7c9ccdfa92352c3f5`.
This new note also audits root's proposed geometric extension, which is
written out below rather than inferred from the earlier numerical bound.
No prior note, canonical record or seal-bound file was changed. No new
CAS execution was needed to resolve an identity gap.

## 1. Hypotheses and the precise all-mate conclusion

Work over an algebraically closed field k of characteristic zero, for the
fixed curve C0 and the accepted genus-one degree-five A4 normalization pair
`(S,c)` of the
[intrinsic classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md).
Retain the nonendpoint parameters `delta!=0,a,b,g,d`, and actual center
avoidance. The resulting projection

    nu:S -> X subset P3

is finite birational and is the normalization of its integral quintic
image. Its restriction `c->C0` is an isomorphism. These admissibility
statements are justified explicitly in the
[pole-filtration audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md).

The accepted
[quintic conductor audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
gives the entire upstairs conductor as the actual invertible ideal

    I_cond,S=O_S(-2H) subset O_S.

Its effective zero divisor `D_cond` is Cartier and linearly equivalent to
`2H`, not merely a numerical conductor cycle. In particular

    deg O_c(D_cond)=2H.c=8.

Let P,J be the corrected cubic numerators in the owner note and let
`Ph,Jh` be their degree-three homogeneous forms on c. Set

    Jbar=d-2g+2b-a.

Then any actual mate, in **any** positive degree, necessarily satisfies

    Res_h(Ph,Jh)*Jbar=0.                     (A)

Equivalently, the locus where the homogeneous pair is coprime and
`Jbar!=0` has no mate in any degree. The proof uses no socle-degree
inequality and does not depend on a bound for the mate exponent.

## 2. P,J detect every smooth-source rank drop along c

On `S\ell=A2`, the coordinates `(r,T)` are regular, c is `T=0`, and
the restriction of the four projection sections is

    (r^4,r^3(r-delta),r(r-delta)^3,(r-delta)^4).

For `r!=0`, use the target chart `x0!=0` and set

    y=x1/x0, z2=x2/x0, w=x3/x0,
    V=z2-y^3, U=w-(3/2)y*z2+(1/2)y^4.

The ideal `(V,U)` equals `(z2-y^3,w-y^4)`; hence its differentials
are an actual basis of the normal cotangent space to C0 at every finite
value of y. In particular there is no extra exceptional finite y at which
this first-symbol test loses a normal direction.

The T derivatives of the actual four sections on c are

    L0=a-2r^2-r,
    L1=b-2r^2-r+delta*r,
    L2=g-2r^2-r+3delta*r,
    L3=d-2r^2-r+4delta*r.

Direct quotient and chain differentiation gives

    V_T=P/r^7, U_T=J/(2r^7),
    P=r^3 L2-3r(r-delta)^2 L1+2(r-delta)^3 L0,
    J=2r^3 L3-3r^2(r-delta)L2+(r-delta)^3 L1.

Thus these expressions include movement of y; they are not derivatives
taken with the image curve parameter artificially held fixed. Expansion
gives exactly the corrected cubics in the owner note. This audit uses
the corrected J, not the earlier rejected expansion.

The image tangent along c is nonzero: for `r!=0`, its y derivative is
`delta/r^2`. If at least one of P,J is nonzero at the source point,
the image of the transverse tangent vector is not in that tangent line.
Consequently the differential from the smooth surface S has rank two,
equivalently the target cotangent map onto the source cotangent space
is surjective.

The point `r=0` is not discarded. There `x3=delta^4!=0`, so use the
reversed target coordinates. If their raw balanced coordinates are
`Vraw,Uraw`, put `Uop=Vraw/2,Vop=2Uraw`. On the overlap, writing
`z2=y^3+V,w=y^4+(3/2)yV+U` and retaining terms modulo `(U,V)^2`
gives

    Uop=y^(-7)U, Vop=y^(-7)V.

Their actual T derivatives therefore extend as

    (Uop)_T=J/[2(r-delta)^7],
    (Vop)_T=P/(r-delta)^7.

Both denominators are nonzero at r=0. The reverse image curve parameter
is `r/(r-delta)`, whose derivative is `-delta/(r-delta)^2`, also
nonzero there. Hence the same rank-two conclusion holds at r=0 whenever
P,J are not simultaneously zero. Explicitly the zero condition there
is `a=b=0`, since `P(0)=-2a delta^3` and `J(0)=-b delta^3`.

Every source point of c except its A4 point is one of these finite r
points. Homogeneous coprimality of Ph,Jh therefore implies immersion at
every smooth-source point of c, with no missing projection rank-one point
or missing opposite target frame.

## 3. The actual A4 cotangent matrix, including its full embedding dimension

At A4 use the accepted chart `Z0=1`, with

    alpha=Z1, beta=Z2, chi=Z3,
    dZ=alpha*beta-chi^2,
    eZ=beta^2-alpha*beta*chi+chi^3.

The local surface equation is

    beta*(chi-alpha^2)+alpha*chi^2=0.

It has no linear term, so the classes of alpha,beta,chi form a basis of
the full three-dimensional cotangent space at this singular point. Both
dZ and eZ lie in the square of its maximal ideal. Thus this calculation
does not replace the singular cotangent space by a smooth normal direction
or discard torsion in a curve conormal sheaf.

Here `U4=1-alpha`, `U3=-alpha`, `U2=chi`, `U1=dZ`,
`U0=eZ`, and `h=beta+chi`. The actual section X0 has value one, so
the target affine ratios are valid at this point. With `B=b-a`, the
linear parts of `Xi/X0-1`, for i=1,2,3, have coefficient matrix

    [ delta,  B,    B                ]
    [3delta,  g-a,  g-a+3delta^2     ]
    [4delta,  d-a,  d-a+6delta^2     ].

Subtracting three and four times the first row from the second and third
gives its determinant directly as

    -3delta^3*(d-2g+2b-a)=-3delta^3 Jbar.

Since `delta!=0` and the characteristic is zero, `Jbar!=0` makes the
target cotangent map surjective at A4 as well. It factors through the
cotangent space of X, because every equation of X pulls back to zero
on S. The singularity of S poses no obstruction to this implication.

## 4. Finite local cotangent lemma: where full inverse support is essential

**Lemma.** Let `A subset B` be a finite inclusion of Noetherian local
rings, with maximal ideals m,n, with equal residue fields. If the map
`m/m^2 -> n/n^2` is surjective, then `A=B`.

Indeed surjectivity gives

    n=mB+n^2.

The finite B-module `n/mB` therefore equals its product with n. Nakayama
over B implies `n=mB`. Equality of residue fields gives `B=A+n`, so

    B=A+mB.

The finite A-module `B/A` now equals `m(B/A)`. Nakayama over A gives
`B/A=0`. These are the ordinary finite-module forms of
[Nakayama's lemma, Stacks 00DV](https://stacks.math.columbia.edu/tag/00DV),
freshly inspected for this audit. No analytic inverse-function theorem,
formal power-series approximation or conductor flatness is used.

For application at a closed point `x in C0`, the finite algebra
`B=(nu_*O_S)_x` is initially allowed to be semilocal. A hypothetical
mate forces the **entire reduced inverse support**

    (nu^(-1)(C0))_red=c.

Because `c->C0` is an isomorphism, there is consequently exactly one
preimage point over x, including no extra isolated point. Thus B has one
maximal ideal and is the local ring of S at that point. Its residue field
and that of `A=O_X,x` are both k. Finiteness over A is retained.

This single-preimage step is indispensable. Localizing one branch of a
multi-preimage fiber and applying the lemma without proving finiteness
would not justify a normalization isomorphism. The mate's full support
supplies precisely the missing hypothesis here.

Under homogeneous coprimality and `Jbar!=0`, Sections 2 and 3 give the
required cotangent surjectivity at every such source point. The lemma
therefore makes nu a local isomorphism at every closed point of C0.
In particular the full actual conductor ideal is the unit ideal at
every point of c.

## 5. The conductor contradiction uses an actual restricted section

The actual effective Cartier conductor `D_cond~2H` would now have support
disjoint from c. Its canonical section restricts to a nowhere-vanishing
section of `O_c(2H)`. This would trivialize that line bundle, whereas

    deg O_c(2H)=2*deg H|c=8.

This is impossible on the complete smooth curve c. It does not require
c itself to be Cartier in S, reduced conductor branches, a smooth
downstairs conductor, or a rank-two flat conductor cover. It uses the
accepted entire invertible conductor ideal, not a replacement cycle.

The contradiction proves (A) in every possible mate degree. It is not
a first-normal upper bound on a later contact multiplicity: first
derivatives here prove cotangent surjectivity, and the finite local
lemma plus full support converts that into an exact ring equality.

## 6. Properness, retained exceptional loci and evidence

The necessary locus is proper. At

    delta=1, a=1, b=g=d=0

the corrected cubics homogenize to

    Ph=2(R^3-4R^2S+4RS^2-S^3), Jh=2R^2S,

and `Jbar=-1`. Their homogeneous roots have no common point. Hence
the product in (A) is a nonzero polynomial. This specific point need
not be asserted admissible: center avoidance is a nonempty open set,
so the complementary nonempty open intersects it in the irreducible
nonendpoint parameter family. The accepted center point lies outside
S, and the bad line extensions are the image of the two-dimensional
S in the four-dimensional extension space, which proves that assertion.

The homogeneous common-root-at-infinity locus already lies in
`Jbar=0`: the two leading coefficients give
`g=3b-2a,d=4b-3a`, hence Jbar vanishes. Thus one may equivalently
retain the A4 cotangent hypersurface together with the finite common-root
incidence. The proposed product formulation remains correct and keeps
all homogeneous frames explicit.

The remaining resultant and A4 cotangent loci are **OPEN** in this audit.
No assertion that they admit a mate is made. The earlier entire-line
ramification conditions satisfy `R3-2R2=Jbar`; their separate all-power
exclusion addresses a subfamily of this retained A4 hypersurface.

I inspected the corrected supporting source, its captured seven-condition
PASS stream and the separate corrected twelve-check conormal output. Those
records support the cubic identities and opposite-frame transition;
their successful execution alone does not prove the new geometric theorem.
The independent new evidence is the explicit finite-point rank argument,
A4 matrix, two-step local lemma and actual conductor-section contradiction
written here. No additional CAS execution was necessary or claimed.
