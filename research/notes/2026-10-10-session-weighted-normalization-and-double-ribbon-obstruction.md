# Weighted normalization and the forbidden genus-seven double ribbon

Date: 2026-10-10. Author: `bisection_weighted_normalization`.
Status: **PROVED HERE, supplied for root acceptance**. This is a separate
structural record of the attempted weighted-incidence approach and the
stronger obstruction that supersedes it. No canonical frontier is edited.
All assertions below concern the fixed smooth rational quartic

    C0=[s^4:s^3t:st^3:t^4]

over an algebraically closed field of characteristic zero. The normal-bundle
calculation itself works in characteristic different from two. The proof
does not establish the unrestricted C0 or universal STCI question.

The root and another independent audit had already identified the same
ribbon obstruction when this author reported it. Agreement is not the
proof; the exact ring and conormal arguments below are the evidence. The
[child conormal audit](2026-10-10-session-weighted-ribbon-conormal-independent-audit.md)
checks the complete CM, Euler, derivative, and generic-immersion interfaces.

## 1. Accepted inputs and the original weighted-ring target

Let X be an integral nonnormal quartic whose normalization S has sectional
genus two, and let H be the pulled-back ambient hyperplane. Write
P=k[x0,x1,x2,x3], A=P/(F4), and

    B=direct-sum_{m>=0} H0(S,O_S(mH)).

The accepted entire-conductor theorem gives an actual line Gamma with
ambient ideal (l0,l1), and an exact sequence

    0 -> O_X -> nu_*O_S -> O_Gamma(-2) -> 0.

The two l_i are independent linear forms. Since H1(X,O_X(m))=0 for every
integer m (the quartic hypersurface restriction sequence on P3 proves
this), taking global sections gives an exact sequence of graded P-modules

    0 -> A -> B -> (P/(l0,l1))(-2) -> 0.

In particular B is generated as a P-module by 1 and any nonambient
quadratic section Q. The quotient generator is its image in degree two.
For a bisection mate, the audited second-pencil argument supplies an actual
section Q with complete Cartier divisor 2c_S and 2c_S~2H; it is nonambient
by the unique-quadric class obstruction. The ensuing ring calculation does
not assume a split or reduced upstairs conductor.

## 2. Exact two-generator P-module presentation

There are uniquely specified ambient cubics A3,B3 with

    l0 Q=A3,       l1 Q=B3

in B. Consequently l1 A3-l0 B3 vanishes in A, and hence equals a scalar
multiple of F4. That scalar is nonzero. If it were zero, unique
factorization and coprimality of l0,l1 would give

    A3=l0 C2,      B3=l1 C2.

The domain B would then imply Q=C2 from l0(Q-C2)=0, contradicting that Q
is nonambient. Scaling F4 gives l1 A3-l0 B3=F4.

The graded matrix

    P(-3)^2 -> P direct-sum P(-2),
    [[-A3,-B3],[l0,l1]]

is injective over the domain P, since its determinant is the nonzero
quartic F4. Its cokernel maps onto B, and its Hilbert series is

    (1+t^2-2t^3)/(1-t)^4.

The same series follows from the preceding conductor exact sequence:

    (1-t^4)/(1-t)^4 + t^2/(1-t)^2
       = (1+t^2-2t^3)/(1-t)^4.

Thus the surjection from the cokernel to B is an isomorphism degree by
degree. This proves the exact presentation and Cohen--Macaulayness of B,
without a separate vanishing theorem for negative twists. It also proves
that the quartic carrier equation is precisely the determinant of the
two cubic relations. This is an exact structural statement, not a generic
rank assertion.

## 3. The weighted Hilbert--Burch ideal

The cubics A3,B3 vanish on Gamma. Indeed their restrictions on the entire
upstairs conductor are l_i Q=0. The pullback of sections from Gamma to its
finite flat double cover is injective, so their downstairs restrictions
are zero. Choose quadratic forms a,b,c,d with

    A3=a l0+b l1,       B3=c l0+d l1.

For W=P[z], deg(z)=2, the weighted presentation of B is

    R0=z l0-A3,
    R1=z l1-B3,
    R2=z^2-(a+d)z+ad-bc.

The third relation follows in the domain B by multiplying by l0 and
using the first two, then canceling the nonzero l0. The two syzygies are

    (z-d)R0+b R1-l0 R2=0,
    c R0+(z-a)R1-l1 R2=0.

Equivalently R0,-R1,R2 are the maximal minors of

    [[z-d,c],[b,z-a],[-l0,-l1]].

The ideal has codimension two: away (l0,l1), it eliminates z and imposes
the nonzero quartic F4, while over (l0,l1) the monic relation R2 leaves
dimension two. Hilbert--Burch therefore gives the numerator

    1-2t^3-t^4+2t^5

over denominator (1-t)^4(1-t^2). The resulting series is precisely the
series of B, so the surjection W/(R0,R1,R2) -> B is an isomorphism.
Changing the quadratic decompositions of A3,B3 only changes R2 by the
first two relations and does not change B.

This was a finite prospective parameter incidence: for a fixed actual
length-two secant/tangent Gamma, A3 and B3 lie in I_C0(3) intersect I_Gamma,
and the determinant quartic also vanishes along C0. However this incidence
is unnecessary for the mate question because the actual double section
already yields the obstruction below.

## 4. The actual double section would be an embedded CM ribbon

Since B is generated by x0,...,x3,Q and Q is killed, B/(Q) is generated
in degree one. Its Proj is therefore closed embedded in P3. It is also
the actual Cartier zero scheme Y=div(Q) on S, whose reduced scheme is
the smooth embedded lift c_S~=C0 and whose generic multiplicity is two.
In the preceding presentation its ambient ideal is

    (A3,B3,ad-bc).

The Hilbert--Burch degrees are (3,3,4), with two degree-five syzygies.
Consequently this would be a degree-eight Cohen--Macaulay double curve
of arithmetic genus seven supported on C0.

The ribbon statement does not rely solely on this graded calculation.
A normal surface is Cohen--Macaulay, and cutting by the nonzero section
Q makes Y a CM curve. Let J be the kernel of O_Y -> O_C0. At the generic
point J has rank one and J^2=0. Globally J^2 is supported at finitely many
points and is a subsheaf of O_Y. A one-dimensional CM scheme has no
nonzero finite-support subsheaf of O_Y, so J^2=0 everywhere. J is then
an O_C0-module and has no torsion for the same reason. Smoothness of C0
implies that J is a line bundle. Thus Y is a ribbon, including every
point lying above the conductor and every ADE point on c_S.

The accepted rational resolution gives, for every integer m,

    chi(O_S(mH))=2m^2+m+1.

The Cartier sequence for Q yields

    chi(O_Y(mH))=chi(O_S(mH))-chi(O_S((m-2)H))=8m-6.

Since O_C0(H)=O_P1(4) and chi(O_C0(mH))=4m+1,

    chi(J(mH))=4m-7,
    J=O_P1(-8).

In particular the sign of the linear term of chi(O_S(mH)) matters.
Replacing it with the dualizing polynomial would give the wrong degree.

## 5. Exact normal-bundle obstruction

Let N=N_C0/P3. To calculate H0(N(-8)), dual Euler and cotangent sequences
identify its dual obstruction with the map

    K -> H0(P1,O(4)),
    K=ker[H0(O(2))^4 -> H0(O(6))],
    (P0,...,P3) |-> sum P_i d f_i,

where (f0,f1,f2,f3)=(s^4,s^3t,st^3,t^4). The first map sends P to sum P_i
f_i and is surjective, since the four degree-four monomials multiplied
by all degree-two monomials span all seven degree-six monomials. Hence
K has dimension five. A basis is

    (st,-s^2,0,0), (t^2,-st,0,0), (0,t^2,-s^2,0),
    (0,0,st,-s^2), (0,0,t^2,-st).

Dividing their differential expressions by t ds-s dt gives respectively

    s^4, s^3t, 2s^2t^2, st^3, t^4.

The map is therefore an isomorphism in characteristic different from
two. Exactness and Serre duality give

    H0(P1,N(-8))=0.

Since deg(N)=14, the splitting theorem gives N=O(7) direct-sum O(7).
Only the vanishing, rather than the full splitting, is needed below.

For any embedded ribbon Y in P3 with reduction C0 and nilideal J, the
ambient ideal I_C0 pulls back into J. Since J^2=0, this induces a
surjection

    I_C0/I_C0^2=N^* -> J=O(-8).

No nonzero map exists: Hom(N^*,O(-8))=H0(N(-8))=0. This contradicts
the actual embedded ribbon obtained from B/(Q). Thus no such quadratic
section Q with complete divisor 2c_S can exist.

An equivalent proof avoids the weighted ring completely. The Cartier
ribbon Y=div(Q) maps by normalization to P3 and extends C0. Pullback of
I_C0 again gives a global conormal map to O(-8), which is generically
nonzero because normalization is an isomorphism off the actual conductor
line and Y has nonzero generic nilpotents. The same vanishing contradicts
this. This second proof applies to any actual Cartier equivalence
2c_S~2H, even before checking whether Q is the extra quadratic generator.

## 6. Mathematical consequence and retained scope

Under the audited genus-two bisection second-pencil input, 2c_S~2H is
an actual Cartier equivalence. The obstruction therefore excludes the
entire bisection mate stratum, without any root-of-unity order bound,
conductor splitting, local fiber enumeration or reduced-cover assumption.
The split-conductor power-descent and blowup-partition reductions remain
valid intermediate results; they are superseded as a research target by
this stronger obstruction.

The genus-two section/trisecant stratum is separate. If an endpoint or
other section analysis supplies the same actual Cartier equivalence,
this obstruction applies there too. No such equivalence is asserted here
from a numerical or merely rational divisor relation. Higher carrier
degrees and the unrestricted problems remain open.

No CAS execution, new historical verifier count, literature novelty claim
or canonical-file acceptance is attached to this record. The five
displayed differential identities are exact hand computations with an
independent written audit.
