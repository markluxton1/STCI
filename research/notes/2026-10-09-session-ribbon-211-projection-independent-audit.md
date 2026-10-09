# The entire conductor-contact partition [2,1,1] is excluded

Date: 2026-10-09. Author: `normal_global_adversarial`.
Status: **PROVED HERE under the accepted genus-one ribbon-net reduction**.
This rules out the entire binary-quartic multiplicity partition [2,1,1]
for a hypothetical genus-one quartic mate, in characteristic zero.
It does not yet exclude the partitions [4], [3,1], or [2,2].
No canonical frontier file is edited.

Inputs are the [independent ribbon-net proof](2026-10-09-session-genus-one-ribbon-net-independent-audit.md)
and the [uniform actual-coordinate fiber conditions](2026-10-09-session-genus-one-uniform-projection-adversarial.md).
The ribbon-net proof was read in this audit; its local Cohen--Macaulay
ribbon argument and direct conormal-kernel calculation supply a uniform
net, rather than an assumption that either toric family is exhaustive.

## 1. Actual net and omitted-coordinate derivatives

Use the six quadrics E0,...,E5 in the ordered basis

    (q01,q02,q03,q12,q13,q23).

For coefficient vector c=(c0,...,c5), the ribbon direction eta is killed
by the symmetric matrix

    M(c)=[[c0,c1,c2],[c1,c2+c3,c4],[c2,c4,c5]].

The accepted net is M(c) eta=0, with eta outside the intrinsic conic
eta1^2=eta0 eta2. The fixed projection still deletes Y2. Its derivative
restriction is

    W_c=c0 s^4-c1 s^3t-2c3 s^2t^2-c4 st^3+c5 t^4,

and its Y2^2 coefficient is -c3. This derivative map is injective on
the net: its only possible kernel in the full six-dimensional space
is q03, and M(q03)=[[0,0,1],[0,1,0],[1,0,0]] is invertible.

On eta0 nonzero, scale eta=(1,u,v), with v!=u^2. The following actual
net basis has derivative quartics G0,G1,G2:

    D=u^2 E0-u E1+E3,
    E=2uv E0-v E1-u E2+u E3+E4,
    F=v^2 E0-v E2+v E3+E5,

    G0=s^2(us-t)(us+2t),
    G1=s(2us+t)(v s^2-t^2),
    G2=(v s^2-t^2)^2.

In this basis a net quadric dD+eE+fF has Y2^2 coefficient
-(d+ue+vf). These identities are direct substitutions into M(c)
and into the omitted-coordinate derivative formula.

Let phi:P1 --> P2 be the map defined by this derivative space, after
removing its common base divisor. Let N be the surface pencil in the
net. It has two independent derivative forms. At every zero of the
linear-coefficient section L_c, full singleton fibers force both
surface derivatives to vanish. Therefore, away from the common base
divisor, all these zeros belong to one geometric fiber of phi: its
image is the common point of the two independent derivative lines.
This remains a necessary support condition at singular source points;
no tangent or isolated-rank assertion is used.

## 2. Every fiber has at most two points when the derivative space has
no common basepoint

On s=1, the rational ratio

    G1/G2=(t+2u)/(v-t^2)

has degree at most two. For any phi image point whose G2 coordinate is
nonzero, its inverse points belong to a fiber of that rational function
and hence number at most two. The locus G2=0 consists of at most two
points as well. Thus every geometric fiber of the basepoint-free phi
has at most two points. This argument includes degree-two conic maps
and birational quartic maps, without needing their separate classification.

The only direction not covered by eta0 nonzero and coordinate reversal
is eta=(0,1,0). There the derivative space is
<s^4,2s^2t^2,t^4>, and the map factors through [s^2:t^2]; again each
geometric fiber contains at most two points. Reversal fixes the omitted
middle coordinate, so using it does not change the actual projection.

Partition [2,1,1] has three distinct zeros. With no derivative basepoint,
they cannot all lie in one fiber. This excludes every such direction.

## 3. The unique common-basepoint locus

In the eta=(1,u,v) chart, a common zero of all G_i must have s nonzero
and t^2=v after s=1. The zeros of G0 are t=u and t=-u/2.
The first gives v=u^2, which is the excluded intrinsic conic. Thus the
only common-basepoint directions are

    v=u^2/4,       u nonzero,

with a single simple common basepoint t=-u/2. It is simple because G0
has a simple zero there. Every other direction is basepoint free.

A diagonal change of the curve parameter, which preserves the omitted
middle coordinate, normalizes this locus to eta=(1,1,1/4). Its basepoint
is t=-1/2. After dividing by t+1/2, the affine cubic-map coordinates are

    g0=-2(t-1),
    g1=-(t+2)(t-1/2),
    g2=(t-1/2)^2(t+1/2).

The divided map is basepoint free. Its point at infinity is [0:0:1]
and has no finite companion, since g0 and g1 have no common zero.

For two distinct finite parameters x,y with the same cubic-map image,
the first two cross-product equalities, divided by x-y, are

    2(x+y)-2xy+1=0,
    -2(x+y)^2+2(x+y)xy+(x+y)+xy+1/4=0.

Writing p=x+y and q=xy gives q=p+1/2 and then 3p+3/4=0.
Thus the only possible double fiber is

    p=-1/4,       q=1/4,
    {x,y}=zeros of N(t)=t^2+t/4+1/4.

The third cross product vanishes for these values, so this is indeed
the unique double fiber. Its two parameters are distinct because the
quadratic discriminant is -15/16. Neither is the common basepoint.

If L_c had three distinct zeros satisfying full singleton support,
one would have to be the basepoint, and the other two would have to be
this unique double fiber. No other configuration can fit the fiber
bound already proved.

## 4. The center condition forces an additional, distinct zero

The zero Y2^2 coefficient imposes d+e+f/4=0. For eta=(1,1,1/4),
reduce G0,G1,G2 modulo N(t). The resulting coefficient conditions for
N to divide dG0+eG1+fG2, together with the center condition, have matrix

    [[3/2,15/16,15/64],
     [3/2,15/16,15/64],
     [1,  1,    1/4 ]].

Its kernel is the one-dimensional space (d,e,f)=(0,-1/4,1).
Consequently the only linear-coefficient section whose zeros include
the double fiber is proportional to

    G2-G1/4
      =(2t-1)(2t+1)(4t^2+t+1)/16.

This has four distinct zeros: the basepoint -1/2, the two double-fiber
parameters, and an extra parameter +1/2. The extra parameter is not
a derivative basepoint and is not in that double fiber. Its image is
[1:0:0], different from the double-fiber image. Hence full singleton
fibers fail even in this last possible common-basepoint configuration.

This completes the exclusion of the entire [2,1,1] contact partition.
The proof handles every net direction and carries the fixed projection
center throughout. It does not infer singularity merely from an isolated
rank-one projection point.

## 5. Evidence and continuation scope

The [independent exact checker](../computations/verify_session_genus_one_projection_2026_10_09.py)
verifies the actual net basis, its omitted-coordinate coefficients and
derivatives, the divided cubic, both cross-product equations, the double
fiber, the remainder matrix, its unique kernel, and the final four-root
factorization. The resulting [JSON record](../scratch/session-genus-one-projection-checks-2026-10-09.json)
records these identities separately from the earlier displayed-family
checks. It does not substitute finite testing for the geometric fiber
argument.

Combined with the uniform necessary repeated-root condition, a remaining
hypothetical genus-one mate must have conductor-contact partition [4],
[3,1], or [2,2]. Those partitions are assigned to a separate owner;
their status is not asserted here. Genus-two normalizations and higher
carrier degrees remain outside this proof.
