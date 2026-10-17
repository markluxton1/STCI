# Smooth lifted curves can meet singular normalization points

Date: 2026-10-09. Author: `singular_local_lift`, subagent of
`singular_normalization_next_frontier`.

Status: **PROVED HERE**, by the explicit algebra below. The universal
STCI problem and the fixed rational quartic C0 problem remain open.
This note provides a local countershield and a surviving local class
group criterion. It makes no classification claim about quartic
normalizations.

## 1. Precise surviving criterion

Let (R,m) be a normal Noetherian local ring of dimension two, and let
P be a height-one prime such that R/P is regular of dimension one.
Thus the reduced curve c defined by P is smooth at the closed point.

**The curve c is Cartier at that point if and only if R is regular.**

For the forward implication, write P=(f). The maximal ideal of R/P
has one generator. Lift that generator to a in m. Then m=(a,f), so
the embedding dimension of R is at most two. Since dim R=2, R is
regular. Conversely a regular local ring of dimension two is a UFD,
so P is principal.

Suppose a mate reduction gives b c Cartier, for an integer b>0. At a
singular point of c, the local divisor class [c] is consequently a
nonzero torsion class, of order dividing b. In particular, if the
local class group is torsion free, c cannot pass through that point.
The same conclusion holds for a locally factorial normalization.

The relation bH=b c in the Weil divisor class group only proves that
[c-H] is killed by b. Without an argument controlling torsion, it does
not prove c is Cartier, c~H, or the existence of a section f with
div(f)=c. This is the exact limitation relevant to the remaining
singular-normalization frontier.

## 2. An affine quartic with isolated singular normalization

Work over an algebraically closed field k of characteristic zero.
Put

    B = k[x,g,v]/(v^2-4xg),
    y = x+g+v,
    w = y^2,
    F = (w+(x-g)^2)^2-4(x+g)^2 w,
    A = k[x,g,w]/(F).

The assignments x->x, g->g, w->(x+g+v)^2 identify A with a subring
of B. To see that the displayed hypersurface is integral, regard F as
a monic quadratic in w over k(x,g). Its discriminant is

    64 x g (x+g)^2,

which is not a square in k(x,g). Gauss's lemma makes F irreducible in
k[x,g,w]. Its image vanishes in B. Since x,g are algebraically
independent in B, the image has dimension two, so its defining prime
ideal is exactly (F).

In B the element y satisfies both

    y^2=w,
    y^2-2(x+g)y+(x-g)^2=0.

Thus B=A[y] is finite over A, with v=y-x-g. Moreover

    y = (w+(x-g)^2)/(2(x+g))

in the fraction field. The denominator is a nonzero element of A,
so Frac(A)=Frac(B): the map is birational.

The ring B is normal. The hypersurface equation v^2-4xg has gradient
(-4g,-4x,2v), so the only singular point is the origin. A hypersurface
is Cohen--Macaulay; here it is regular in codimension one. Serre's
criterion therefore proves normality. Its embedding dimension at the
origin is three and its dimension is two, so that point is singular.
This is the ordinary A1 surface singularity. Since B is normal,
integral over A, and has the same fraction field, it is the full
integral closure of A: an element of Frac(A) integral over A is also
integral over B and hence belongs to B.

Therefore Spec B is the finite birational normalization of the
integral affine quartic Spec A.

## 3. The smooth curve, full support, and mate

Let

    c = V(g,v) in Spec B,
    C = V(g,w-x^2) in Spec A.

Both coordinate rings are k[x], and the restriction of normalization
is the identity on x. Thus c and C are smooth, c->C is an
isomorphism, and C is an embedded smooth parabola in affine
three-space. At the origin its parametrization (x,g,w)=(t,0,t^2)
has nonzero derivative (1,0,0).

The full reduced inverse image of C is c. Indeed v^2=4xg gives
v in sqrt((g)), and

    w-x^2 = 2xv + g(6x+g+2v) in B.

Consequently sqrt((g,w-x^2)B)=(g,v). There is no second normalization
branch lying above C.

The scheme-theoretic inverse image is not asserted to be reduced:
its ideal is (g,xv). Modulo g its coordinate ring is
k[x,v]/(v^2,xv), which retains a nilpotent supported at the origin.
The support assertion and the isomorphism of reduced curves are the
precise statements used here.

The Weil divisor of g in Spec B is exactly 2c. Its zero set has only
the prime (g,v). At that prime x is a unit and v is a uniformizer:
g=v^2/(4x). Hence the valuation is exactly two.

Downstairs the plane g=0 is a mate, since

    F(x,0,w)=(w-x^2)^2.

The surface is smooth at the generic point of C. Substituting g=0,
w=x^2 into the gradient of F gives

    (F_x,F_g,F_w)|C = (0,-16x^3,0).

Thus this example also has carrier order one at the generic point of
C. It does not rely on C being a component of a generic nonnormal
locus. Nevertheless c meets the isolated singular point of the
normalization and its ambient image remains smooth and immersed.

Finally c is not Cartier at the origin. The prime ideal (g,v) needs
two generators there: their independent degree-one classes survive
modulo m(g,v), whose homogeneous terms start in degree two. A
principal ideal in a local ring has at most one generator. Therefore
the local class [c] is nonzero. The relation div(g)=2c shows that
its order is exactly two.

## 4. Projective quartic countershield, with degree explicitly retained

The homogenization in P3 with coordinates [x:g:w:t] is

    F_h = (wt+(x-g)^2)^2-4(x+g)^2 wt.

It is an integral quartic: its affine chart t=1 is integral by the
argument above, and t is not a factor of F_h. The plane g=0 cuts

    F_h|g=0 = (wt-x^2)^2.

The reduced intersection is the smooth projective conic
g=0, wt=x^2. Its gradient on that plane is (-2x,t,w), which never
vanishes at a projective point. The normalization of this projective
quartic restricts on t=1 to Spec B, so the lifted conic certainly
passes through the isolated singular normalization point established
above, while mapping isomorphically in its affine neighbourhood.

The curve here has degree **two**, not degree four. In particular this
is not a mate for the fixed rational quartic C0. We do not assert that
the projective full inverse image of the conic has a single smooth
component at the point t=0; the verified local countershield already
invalidates a local smooth-lift avoidance claim. The explicit plane
mate for the projective conic is, however, an actual global STCI.

## 5. Consequence for the continuation frontier

The implication

    smooth lifted curve + embedded smooth image + full mate support
    + order-one generic carrier  =>  avoidance of Sing(normalization)

is false as a local statement, even for an affine quartic. An
argument specifically using degree four for C0, its global divisor
class, or a classification of the possible normalization singularities
may still exclude the remaining cases. It must supply that additional
input explicitly. The accepted smooth F0/F2 normalization results do
not acquire a singular-normalization extension from this local step.

## 6. Exact verification and sources

The paired checker
`computations/verify_singular_local_lift_countershield_2026_10_09.py`
verifies the literal normalization relations, birational recovery
identity, discriminant, pulled-back curve equation, mate restriction,
generic gradient and projective homogenization. The geometric proofs
above supply normality, finiteness, divisor valuation and the local
Cartier criterion; the script does not label those conclusions proved
merely because a polynomial identity passed.

Terminal replay on 2026-10-09 returned exit 0 and `status: PASS` with
the isolated exact runtime `/private/tmp/stci-cas-venv/bin/python`.
The output is
`research/scratch/session-singular-local-lift-countershield-2026-10-09.json`.
Source SHA256:
`edb3a209b026fd2cbde4a11335087fce7430b291e6380b4774f62ca2415aa503`.
Output SHA256:
`fbc741cde69ab4b33b808711a228b6381fbe7ff2210872dcdec8a4c363475c9b`.
The separate adversarial proof is saved in
`research/notes/2026-10-09-singular-normalization-local-countershield-audit.md`;
it accepts the example and explicitly checks the nonreduced inverse
image scheme. Independent agreement is additional audit evidence;
the mathematical proof remains the explicit argument above.

Normality uses the primary
[Stacks Project, Serre's criterion](https://stacks.math.columbia.edu/tag/031S).
The normalization identification also uses the definition of a normal
domain as integrally closed in its fraction field in the
[Stacks Project, normal rings](https://stacks.math.columbia.edu/tag/037B). All other
algebra in the countershield is explicit in this note. No novelty claim
is made.
