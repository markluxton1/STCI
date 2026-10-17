# The entire conductor of a rational ADE degree-four del Pezzo normalization

Date: 2026-10-09. Author: `singular_local_lift`, for
`singular_normalization_next_frontier`.

Status: **PROVED HERE, independently audited**, under the hypotheses in Section 1. This note
concerns the actual conductor schemes, including reducible and
nonreduced cases. It does not assume the upstairs conductor is smooth
or avoids the normalization singularities. No canonical files are
edited, and no mate or universal STCI conclusion follows from this
structural reduction alone.

## 1. Hypotheses and conclusions

Work over an algebraically closed field k of characteristic zero.
Let X be an integral quartic surface in P3, and let nu:S->X be its
finite normalization. Assume S is a rational normal degree-four del
Pezzo surface with only ADE singularities and

    H=nu^*O_X(1)=-K_S,
    H ample and Cartier,       H^2=4.

ADE is used through its precise properties: S is Cohen--Macaulay and
Gorenstein, and its minimal resolution mu:M->S is rational and
crepant, so R^i mu_*O_M=0 for i>0 and K_M=mu^*K_S. No list of ADE
types, including 4A1 or A3+2A1, is required in the proof.

Let I=Ann_OX(nu_*O_S/O_X) be the conductor. Define the actual schemes

    Gamma=V_X(I),       D=V_S(I O_S),       p:D->Gamma.

Then:

1. I O_S is invertible and isomorphic to O_S(-H). Consequently D
   is an effective Cartier divisor with D~H.
2. Gamma is pure Cohen--Macaulay of dimension one and arithmetically
   Cohen--Macaulay in P3, with Hilbert polynomial 2m+1. Its ideal is
   a complete intersection of degrees (1,2). Thus the entire Gamma
   is a plane conic: smooth, two distinct lines, or a double line.
3. There is an exact sequence on Gamma

       0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,

   and omega_Gamma=O_Gamma(-1) is invertible. Therefore p is finite
   flat of degree two, on the entire schemes.
4. Trace gives a canonical global involution sigma of the O_Gamma
   algebra p_*O_D, with decomposition

       p_*O_D = O_Gamma direct_sum N,
       N=ker(trace) isomorphic to omega_Gamma.

   Locally N has a generator z with z^2 in O_Gamma and sigma(z)=-z.
   These statements retain nilpotents when Gamma or D is nonreduced.
5. D is a connected Gorenstein anticanonical curve with
   omega_D=O_D, H^0(D,O_D)=k, and Hilbert polynomial 4m. Its
   arithmetic genus is one. Smoothness and reducedness are not
   asserted.

## 2. Finite absolute duality identifies the actual upstairs conductor

The quartic hypersurface X is Gorenstein with omega_X=O_X. Finite
absolute duality, together with Cohen--Macaulay concentration on
the equal-dimensional schemes, gives

    nu_*omega_S = Hom_OX(nu_*O_S,omega_X).

This is an identity of canonical modules, not a use of relative
duality requiring nu to be flat. Locally write A for the domain of
X, B for its finite birational normalization and K for their common
fraction field. Every A-linear homomorphism B->A is multiplication
by an element r in K, because it becomes multiplication after
tensoring with K. Since 1 belongs to B, such r belongs to A, and

    Hom_A(B,A)={r in A:rB subset A}=I.

This identifies the right side with the actual conductor ideal,
also as a B-module. Since S is Gorenstein and K_S=-H,

    I=nu_*omega_S,
    I O_S=omega_S=O_S(-H)

as B-ideals after using the duality identification. The inclusion
into O_S is a nonzero inclusion of an invertible sheaf into the
structure sheaf of an integral scheme. Its zero scheme is an
effective Cartier divisor D with O_S(-D)=I O_S. Therefore D~H.
This remains valid when D passes through an ADE point.

## 3. All twists have the required H1 vanishing

Put A_M=mu^*H. It is nef and big, and K_M=-A_M by crepancy. For
n>=0,

    n A_M-K_M=(n+1)A_M

is nef and big. Kawamata--Viehweg vanishing on the smooth resolution
therefore gives H^1(M,O_M(n A_M))=0. Rationality of the ADE
resolution and the projection formula identify this group with
H^1(S,O_S(nH)). Thus the latter vanishes for n>=0.

For n<=-1, Serre duality on the projective Gorenstein surface gives

    H^1(S,O_S(nH))^* = H^1(S,O_S((-n-1)H)).

The exponent on the right is nonnegative. Consequently

    H^1(S,O_S(nH))=0       for every integer n.

The exact conductor preimage sequence on P3 is

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0,

where J_Gamma is the ideal sheaf of the actual downstairs scheme.
After twist m, both intermediate cohomology groups H^1 and H^2 of
O_P3(m-4) vanish. The long exact sequence therefore identifies

    H^1(P3,J_Gamma(m)) = H^1(S,O_S((m-1)H)) = 0

for every integer m.

## 4. Purity, the Hilbert polynomial, and the entire plane conic

The conductor I is maximal Cohen--Macaulay as an O_X-module.
Locally this follows from its identification with the canonical
module of the finite Cohen--Macaulay normalization. More explicitly,
a system of parameters of the two-dimensional local ring A is a
system of parameters at all finite normalization points above it;
it is regular on their canonical modules. Hence depth_A(I)=2.
The depth lemma applied to

    0 -> I -> O_X -> O_Gamma -> 0

gives depth at least one for O_Gamma at its closed points. The
conductor is a nonzero rank-one ideal, so its quotient has dimension
at most one. It follows that Gamma is a pure Cohen--Macaulay curve;
there are no embedded or isolated zero-dimensional components.

Riemann--Roch on the rational crepant resolution, and rationality
of the resolution, give for every integer n

    chi(O_S(nH))=1+2n(n+1).

The quartic hypersurface sequence gives

    chi(O_X(m))=2m^2+2.

Using I=nu_*O_S(-H) in the conductor sequence yields

    chi(O_Gamma(m))
      =(2m^2+2)-(1+2(m-1)m)=2m+1.

Thus Gamma has degree two and arithmetic genus zero. The H^1
ideal vanishing from Section 3 makes its saturated homogeneous
coordinate ring Cohen--Macaulay of dimension two.

To retain the scheme classification, take an Artinian reduction
by two general regular linear forms. Its nonnegative Hilbert
function h has h0=1, sum h_i=degree(Gamma)=2, and
sum i h_i=1 from arithmetic genus zero. Thus h=(1,1). The degree-one
piece of the coordinate ring has dimension 2+1=3, so exactly one
linear form belongs to the ideal in P3. Gamma lies in a plane.
In degree two its coordinate ring has dimension five, while that
of the plane has dimension six. Thus a nonzero plane quadratic
equation Q_2 belongs to its ideal. The plane quotient by Q_2 and
Gamma have the identical Hilbert series (1+t)/(1-t)^2. Their graded
surjection is consequently an isomorphism in every degree. This
proves that the entire saturated ideal is

    I_Gamma=(ell,Q_2),       degrees (1,2).

This excludes extra embedded structures. Over k the equation is a
smooth conic, a product of
two distinct linear forms, or a square of a linear form. The double
line here is the actual plane double-line scheme, not an arbitrary
ribbon supported on a line. In every case Gamma is Gorenstein, and
adjunction gives omega_Gamma=O_Gamma(-1).

## 5. The quotient is the dualizing sheaf and forces finite flatness

Work again over a Gorenstein local surface ring A, with B its
normalization and I the conductor. The modules B and I are maximal
Cohen--Macaulay. Duality on that category gives

    I=Hom_A(B,A),       Hom_A(I,A)=B,
    Ext_A^j(B,A)=Ext_A^j(I,A)=0 for j>0.

Apply Hom_A(-,A) to 0->I->A->C->0, where C=A/I. Since A is a domain
and I contains a nonzero element, Hom_A(C,A)=0. The resulting
exact sequence is

    0 -> A -> B -> Ext_A^1(C,A) -> 0.

The last module is the canonical module of the pure codimension-one
Cohen--Macaulay scheme C. Globalizing with omega_X=O_X therefore
gives

    nu_*O_S/O_X = omega_Gamma.

Since the same conductor I is an ideal of both A and B, quotienting
the inclusion A subset B by I gives, on the actual conductor schemes,

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

The right-hand line bundle is locally free of rank one over every
local ring of Gamma, including a node or a double-line point. The
sequence therefore splits as a sequence of modules locally: a
generator of omega_Gamma lifts, and the resulting middle module is
free of rank two. Because p is finite, this proves that p is finite
flat of degree two. No smoothness, generic reducedness or separate
flatness assertion has been inserted here.

## 6. Trace constructs an involution on the entire algebra

Let E=p_*O_D. It is a locally free O_Gamma algebra of rank two.
The trace of multiplication satisfies trace(1)=2. In characteristic
zero this gives the canonical splitting

    E=O_Gamma direct_sum N,       N=ker(trace).

The line bundle N maps isomorphically onto E/O_Gamma=omega_Gamma.
Locally choose a generator z of N. Its rank-two multiplication
matrix has trace zero. Cayley--Hamilton gives

    z^2=-det(multiplication_by_z) in O_Gamma.

Thus the O_Gamma-linear map fixing 1 and sending z to -z is an
algebra automorphism. It squares to the identity and is independent
of the trace-zero generator, so these maps glue to a global
involution sigma. Its invariant algebra is O_Gamma, and its
anti-invariant module is N=omega_Gamma.

These are statements about all sections of the entire schemes.
They remain true if the base conic is a double line, if D is
nonreduced, or if the local algebra has equation z^2=0. No branch
point, function-field sign ratio or decomposition into reduced
components is required to construct sigma.

For the later quadratic descent calculation, this gives an exact
description of the entire restriction space. Since O_D(H)=p^*O_Gamma(1),
the invariant and anti-invariant summands of p_*O_D(2H) are

    O_Gamma(2),       omega_Gamma tensor O_Gamma(2)=O_Gamma(1).

Their spaces of global sections have dimensions five and three,
respectively, for every plane conic scheme classified above. In a
local trace-zero generator, a quadratic restriction can be written
a+z h, with a an invariant degree-two section and h a degree-one
section in the anti-invariant summand. It descends exactly when the
entire anti-invariant component is zero. This is a full module
statement even for a double line, not a test at generic points.
The multiplication N tensor N->O_Gamma is equivalently a global
section of omega_Gamma^(-2)=O_Gamma(2), including when that section
defines a nonreduced or singular upstairs curve.

## 7. Upstairs arithmetic data and limits of this reduction

Since D is Cartier and S is Gorenstein,

    omega_D=(omega_S tensor O_S(D))|D=O_D.

The sequence 0->O_S(-H)->O_S->O_D->0, together with the all-twist
H^1 vanishing and H^0(S,O_S(-H))=0, gives H^0(D,O_D)=k. Thus D
is connected. Its Hilbert polynomial is

    chi(O_D(mH))
      =chi(O_S(mH))-chi(O_S((m-1)H))=4m.

In particular its arithmetic genus is one. The same formula follows
from p_*O_D=O_Gamma direct_sum omega_Gamma and chi(O_Gamma(m))=2m+1,
which provides an independent consistency check of the twists.

The structural reduction leaves the following possibilities in
scope: D may pass through an ADE point, have singularities, split
into components, or be nonreduced; Gamma may be two lines or a
double line. It supplies the global trace involution in all of those
cases. It does not by itself show that a section Q with divisor
2c is invariant under that involution, nor that such a section
descends to X. Arguments using a smooth elliptic conductor or a
simple ramification parameter must separately justify those
hypotheses before being applied to the entire lane.

## 8. Primary inputs and provenance

The independent scheme-theoretic audit is saved in
`research/notes/2026-10-09-session-delpezzo-entire-conductor-independent-audit.md`.
It accepts the canonical-module identifications, entire conic scheme
classification, finite flatness and trace involution, while retaining
the singular/nonreduced-D descent boundary. Independent agreement is
audit evidence; the proof is the argument above.

Finite absolute duality is the
[Stacks Project finite-ring dualizing lemma](https://stacks.math.columbia.edu/tag/0AX0),
combined with
[Cohen--Macaulay concentration](https://stacks.math.columbia.edu/tag/0AWQ).
The local conductor identification and the maximal-Cohen--Macaulay
dual sequence are written out above. The projective-space
cohomology vanishing is the
[Stacks Project computation](https://stacks.math.columbia.edu/tag/01XS).

The vanishing input is the standard characteristic-zero
Kawamata--Viehweg theorem, used on the smooth resolution with
(n+1)mu^*H nef and big. Its original primary reference is
[Kawamata, Mathematische Annalen 261 (1982), 43--46](https://link.springer.com/article/10.1007/BF01456407).
The publisher's bibliographic record was freshly inspected; its
full text is subscription-only. The author-hosted link to Viehweg's
1982 paper returned HTTP 410. No fresh full-text verification of
those original vanishing papers is claimed. The use and hypotheses
of the standard vanishing theorem are explicit in Section 3.

No symbolic test is used as a substitute for these scheme-theoretic
proofs. No classification or novelty claim is made.
