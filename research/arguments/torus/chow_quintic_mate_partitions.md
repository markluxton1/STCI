# Small multiplicity partitions for a quartic–quintic pair

**Review.** The \((2,2,1)\) and invariant-pair exclusions were independently
reconstructed by the correctness and algebraic-geometry reviewers during
the November 23 first-moment synthesis. This is bounded degree coverage,
not a proof of UM1 in arbitrary degree.

Over an algebraically closed field, let \(Z=V(F_4,G_5)\) be a proper
homogeneous CI whose entire cycle consists of translated quartics with
nonzero parameters. Group equal components, so distinct components have
pairwise distinct parameter pairs. The total multiplicity is five.

## 1. There is no invariant pair, in any characteristic

Invariant ideals have eigenform generators of degrees four and five.
The missing middle vertices force pure powers of \(x_1\) and \(x_2\)
in different generators. The weight pairs are consequently \((4,15)\)
or \((12,5)\), for weights \((0,1,3,4)\).
Every degree-five weight-fifteen monomial is one of
\[
                x_2^5,\quad x_1x_2^2x_3^2,\quad x_0x_2x_3^3.
\]
Thus that quintic is divisible by \(x_2\). In the reversed case it is
divisible by \(x_1\). Properness makes the intersection of this plane
factor with the quartic a nonempty plane curve. No translated quartic
lies in a plane, contradicting the entire-cycle hypothesis.

## 2. Partition \((2,2,1)\) is empty, in any characteristic

Let \(Y\) be the union of the three distinct reduced components and
\(D\) the union of the two doubled ones. Linkage makes \(D\) residual
to \(Y\), and gives \(p_a(Y)=p_a(D)+10\).
Write \(e=[u_1=u_2]\), \(f=[h_1=h_2]\), \(g=[\eta_1=\eta_2]\),
where \(h_i=v_i^2/u_i^3\) and \(\eta_i=u_i^2/v_i\).
The [two-component calculation](chow_moment_residual_speciality.md#4-the-exact-two-double-residual-in-degree-one)
gives
\[
 p_a(D)=5+e+f,\qquad h^1(\mathcal O_D(1))=e+f+g.
\]
For three distinct translates each endpoint delta invariant is in
\(\{7,9,12\}\), by the
[three-branch evaluation calculation](chow_moment_residual_speciality.md#5-one-tripled-component-in-every-degree-in-characteristic-zero).
These ranks use only the basis lists \((1,u,v)\), \((1,u,u^2)\),
and \((1,v,v^2)\), so remain valid in every characteristic.
Thus \(p_a(Y)=\delta_0+\delta_\infty-2\).

If \(e+f=0\), the required genus fifteen is impossible. If \(e+f=1\),
genus sixteen forces endpoint deltas \((9,9)\); both the \(u_i\)'s
and the \(h_i\)'s are then pairwise distinct, a contradiction.
If \(e=f=1\), distinctness is impossible in characteristic two. Otherwise
\(v_2=-v_1\), so \(g=0\). Genus seventeen forces deltas \((12,7)\)
or \((7,12)\), hence all three components lie on a common eigen-cubic.
Its linear multiples give \(\dim(I_Y)_4\ge4\). But the
[exact linkage source identity](chow_moment_residual_speciality.md#1-a-low-degree-symmetry-criterion-from-linkage)
gives \(\dim(I_Y)_4=1+h^1(\mathcal O_D(1))=3\), again a contradiction.

### Single double and triple partitions in every characteristic

The partitions \((2,1,1,1)\) and \((3,1,1)\) are also empty in every
characteristic. The extension concerns this bidegree, not the all-degree
one-triple theorem.

First, every actual \(F_4\) is irreducible: a factor \(P\) gives a proper
subpair \((P,G_5)\) with an entire translated cycle, hence
\(4\mid5\deg P\) and \(\deg P=4\). For one double the residual is the
smooth quartic itself. Its \(H^1(\mathcal O_C(1))\) vanishes, so the
all-characteristic linkage criterion makes \(F_4\) an eigenform.
The regular-initial-sequence construction then gives a proper invariant
pair with the same cycle, contradicting Section 1. That construction is
characteristic-free; its usual characteristic-zero qualification concerns
the subsequent moment consequence.

For one triple, let \(\mathcal O_{\mathbf P^1}(\ell)\) be the nilideal
of the residual double. The [conormal splitting](../../results/quartic_conormal_characteristic_jump.md)
gives \(\ell\ge-7\) outside characteristic two and \(\ell\ge-8\)
in characteristic two. If \(\ell\ge-5\), the same cohomology argument
applies. If \(\ell=-6\), linkage requires reduced-support genus fifteen,
excluded by the endpoint table above. If \(\ell=-7\), the
[irreducible-extreme argument](chow_moment_residual_speciality.md#5-one-tripled-component-in-every-degree-in-characteristic-zero)
is characteristic-free: genus sixteen forces the two affine parameter
relations; their nonzero intercepts give the irreducible extreme quartics
\(E_4,E_{12}\). Their proper invariant initial pair contradicts Section 1.

The additional case \(\ell=-8\) requires genus seventeen, hence endpoint
deltas \((7,12)\) or \((12,7)\). The three curves lie on a common
eigen-cubic \(H\). Thus \(HS_1\subseteq(I_Y)_4\) has dimension four.
The nilideal sequence twisted by one gives
\[
h^1(\mathcal O_R(1))\le h^1(\mathcal O_{\mathbf P^1}(-4))=3.
\]
The exact linkage identity gives \(\dim(I_Y)_4\le4\), so
\((I_Y)_4=HS_1\), contradicting irreducibility of \(F_4\).

This bounded extension was independently reconstructed by the correctness
and generalizations reviewers during the renewed November 23 reassessment.

## 3. The characteristic-zero frontier

Every actual \(F_4\) is irreducible: any factor \(P\) gives the proper
subpair \((P,G_5)\) with only translated components, so
\(4\mid5\deg P\), and necessarily \(\deg P=4\).
A reduced fundamental cycle (partition \((1,1,1,1,1)\)) forces the
unmixed CI ideal to be reduced and invariant, impossible by Section 1.
The single-double and single-triple exclusions above apply in every
characteristic.
Sole partition \((5)\) is excluded by the
[quartic-carrier theorem](../../results/quartic_carrier_exclusion.md).

Only \((4,1)\) and \((3,2)\) remain unexcluded here. Neither is asserted
nonempty. These are finite-degree probes; their exclusion alone would
not resolve the all-degree first-moment conjecture.
