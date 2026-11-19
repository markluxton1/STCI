# General coordinate boundary: contacts and toric compactification

## Scope

Let \(k\) be algebraically closed of arbitrary characteristic, trivially
valued. Fix the smooth quartic \(C=[s^4:s^3t:st^3:t^4]\), and choose four
independent hyperplanes \(L_i\), giving coordinates \(y_i\) on \(\mathbf P^3\).
Write \(f_i=L_i|_C\in H^0(\mathbf P^1,\mathcal O(4))\),
\(U=C\setminus\bigcup_i V(f_i)\), and
\(N=\mathbf Z^4/\mathbf Z(1,1,1,1)\), with coordinate classes \(e_i\).
This is a statement about each coordinate-torus embedding, not equations
realizing \(C\) as a set-theoretic complete intersection.

## Theorem: realized contact weights and a proper toric model

At each puncture \(q\), put \(a_q=(\operatorname{ord}_q f_i)_{i=0}^3\).
Use a local trivialization of \(\mathcal O(4)\). Since the coordinates have
no common zero, \(\min_i a_{qi}=0\); also \(a_q\ne0\) and
\(0\le a_{qi}\le4\). Let \(d_q=\gcd_i a_{qi}\). The vector
\(n_q=[a_q]/d_q\) is primitive in \(N\): subtract a zero coordinate to
identify \(N\) with \(\mathbf Z^3\), where this is the usual gcd test.

The tropical support consists of the rays \(\rho_q=\mathbf R_{\ge0}n_q\),
with weight
\[
 w_\rho=\sum_{q:\rho_q=\rho}d_q.
\]
These weights are balanced: \(\sum_\rho w_\rho n_\rho=0\).
There is a smooth toric variety \(X_\Delta\), with fan consisting of zero
and these realized rays, in which the scheme-theoretic closure \(C'\) of
\(U\) is isomorphic to \(C\), hence proper. Multiplication
\(T\times C'\to X_\Delta\) is faithfully flat, and is smooth if and only
if every \(d_q=1\). The complete ambient refinement used to construct this
model is distinct from the ray-only fan \(\Delta\).

This gives a complete formula for **each realized frame**, not a classification
of which contact assignments the restricted linear system can realize.

## Proof

Normalization valuations give the stated rays; the embedding has generic
degree one, so there is no parametrization-degree factor. We prove the
weight formula through boundary intersection lengths below. Balancing follows
from the four degree-four divisors:
\[
 \sum_q[a_q]=[(4,4,4,4)]=0.
\]

### Closure and properness

Choose a smooth complete refinement \(\Sigma\) of the fan of \(\mathbf P^3\)
containing all \(\rho_q\). Insert the finitely many rational rays and then
smoothly subdivide, retaining them. The proper toric map
\(X_\Sigma\to\mathbf P^3\) is the identity on the torus \(T\).
The map from \(U\) lifts uniquely across each discrete valuation ring
\(\mathcal O_{C,q}\) by properness. The lifts glue to a closed immersion
\(C\to X_\Sigma\): its graph is a section of the separated morphism
\(C\times_{\mathbf P^3}X_\Sigma\to C\), followed by the closed base-change
immersion into \(X_\Sigma\). Its image \(C'\) is the strict transform.

At \(q\), the valuation is in the relative interior of \(\rho_q\).
In its ray chart \(\mathbf A^1\times\mathbf G_m^2\), a character pairing
to one with \(n_q\) pulls back as \(z=\tau^{d_q}u(\tau)\), with \(u\)
a unit; the two annihilator characters pull back to units. Thus \(q\)
lies in that ray's open divisor orbit, not a higher-codimension orbit.
Consequently \(C'\) lies in the toric open \(X_\Delta\) whose fan has just
zero and the realized rays. The curve \(C'\) is proper over \(k\), since \(C'\simeq\mathbf P^1\). Omitted higher-codimension orbits are
harmless precisely because they miss the curve. Moreover, \(U\) is a dense
open subset of the integral scheme \(C'\), so it is schematically dense.
As \(C'\) is closed in \(X_\Delta\), its defining ideal is exactly the
ideal of the scheme-theoretic closure of \(U\), not merely a set-theoretic
image. The valuation/orbit correspondence also agrees with
[Tevelev, Lemma 2.2](https://arxiv.org/html/math/0412329v3).

### Flatness on the affine ray charts

The multiplication map \(\mu:T\times C'\to X_\Delta\) is surjective:
\(U\) meets the torus, and each included ray orbit contains a puncture;
translations fill each orbit. Fix the affine ray chart
\(X_\rho=\operatorname{Spec}k[Z,U_1^{\pm1},U_2^{\pm1}]\).
Its inverse image \(C_\rho=C'\cap X_\rho\) is closed affine integral
and open in \(C'\). Write the restrictions as \((z,u_1,u_2)\).
The element \(z\) is nonzero and nonconstant: it vanishes at a puncture
on this ray, but nowhere on the dense open \(U\). Hence
\(k[Z]\to\Gamma(C_\rho,\mathcal O),\ Z\mapsto z\), is injective and
its target is torsion-free as a \(k[Z]\)-module. Over this PID it is flat;
thus \(z:C_\rho\to\mathbf A^1\) is flat.

Because the chart is torus invariant, \(\mu^{-1}(X_\rho)=T\times C_\rho\).
In the acting torus coordinates \((a,b_1,b_2)\), multiplication is
\((a,c,b_1,b_2)\mapsto(az(c),b_1u_1(c),b_2u_2(c))\).
Replacing \(b_i\) by \(b_i u_i(c)\) is an invertible change of source
coordinates. It leaves the product of the identity on \(\mathbf G_m^2\)
with \(f:\mathbf G_m\times C_\rho\to\mathbf A^1\), \(f(a,c)=az(c)\).
The map \((a,c)\mapsto(a,z(c))\) is the flat base change of \(z\) by
\(\mathbf G_m\times\mathbf A^1\to\mathbf A^1\). Compose it with the
isomorphism \((a,b)\mapsto(a,ab)\), whose inverse is
\((a,b)\mapsto(a,a^{-1}b)\), then with the flat projection to the second
factor. This proves flatness of \(f\), and hence of \(\mu\) on this chart.
On the dense torus multiplication is smooth. These charts cover \(X_\Delta\),
so \(\mu\) is faithfully flat.

### Smoothness and multiplicities

At a divisor orbit, torus tangent directions span its two tangent directions.
The remaining derivative is that of \(\tau^{d_q}u(\tau)\), nonzero at
\(q\) exactly when \(d_q=1\). Smooth source and target over the perfect
field \(k\) therefore give
\[
 \mu\text{ is smooth}\quad\Longleftrightarrow\quad d_q=1\text{ for every }q.
\]
Properness and faithful flatness now verify the hypotheses of
[Tevelev's Definition 1.1](https://arxiv.org/html/math/0412329v3): this is a
tropical compactification. By his Definition 1.3 it is a schön
compactification precisely in the primitive-contact case. The assertion is
about this model; the full complete ambient fan is not the tropical curve.
Intersection with \(z=0\) at \(q\) has length \(d_q\), giving the weight
formula by [Sturmfels–Tevelev, Section 3, Definition 3.1/Lemma 3.2](https://arxiv.org/abs/0704.3471).
Summing these lengths over punctures on the same orbit gives \(w_\rho\).

## Retained witnesses

Nonprimitive contacts occur even for a smooth embedded curve. The independent
sections \((1,1+x,1+x^3,x^4)\) in the affine parameter \(x=t/s\) have order
vector \((0,0,0,4)\) at zero in every characteristic. Multiplication is not
smooth there, although the underlying curve remains smooth.

## Edge loci and the simple collision example

Each of the six equations \(\operatorname{Res}(f_i,f_j)=0\) detects exactly
incidence with the edge \(V(y_i,y_j)\). Off these loci and the individual
discriminants, there are 16 distinct punctures and four rays of weight four.
If exactly one pair shares one simple root, with all other roots simple and
disjoint, there are 15 punctures: weights \(3,3,4,4\) on the four axes,
and weight one on \(e_i+e_j\). After dehomogenizing by a coordinate nonzero at the collision, locally
\(y_i=\tau a(\tau)\),
\(y_j=\tau b(\tau)\), with units \(a,b\). Blowing up the edge inserts
\(e_i+e_j\); the strict transform meets the exceptional divisor transversely
at unit ratio \(b/a\), away from both strict coordinate divisors.

## Exact characteristic-zero witness

In x=t/s take:

    f0=x+x^3+x^4
    f1=2x+3x^3+5x^4
    f2=1+x+2x^3+3x^4
    f3=2+3x+x^3+4x^4.

The coefficient matrix in (1,x,x^3,x^4) has determinant 9. All leading
coefficients are nonzero, so no root is at infinity. The discriminants are
-31, -11664, 2677, 58568. The only nonconstant pair gcd is gcd(f0,f1)=x.
The other pair resultants, ordered 02,03,12,13,23, are
17,242,541,19240,31. Moreover

    Res_x(f0,f1+u)=u(u^3+11u^2+6u+29).

The derivative at u=0 is 29, so this is a transverse one-parameter slice of
the simple edge wall. These integer identities were recomputed with SymPy;
they demonstrate nonemptiness in characteristic zero, not a uniform witness
in every characteristic.

## Finite parameter stratification, not a global fan

The frame space maps to \((\operatorname{Sym}^4\mathbf P^1)^4\) by its
four root divisors. Pull back the finite root-labeling maps. Exact equality
partitions of the 16 labeled roots are locally closed (equalities within
blocks, inequalities between them); their finite permutation-orbit unions
descend to constructible subsets of frame space. Each block specifies one
order vector \(a_q\), so the weighted fan is constant on each such part.
Empty patterns are discarded. This is not a realizability classification:
we have not characterized which partitions meet the frame space of the
restricted system \(\langle s^4,s^3t,st^3,t^4\rangle\).
After a finite base change labeling roots in a specialization, blocks can
coalesce and their vectors add. This does not assert that every coarsening
occurs or that partition order equals the closure order of realized strata.

All possible orders lie in the finite set \(\{0,\ldots,4\}^4\) with a zero
coordinate. One smooth complete refinement containing all their primitive
rays provides a common ambient modification for every frame. The ray-only
open must still use each frame's realized rays: unused rays would destroy
surjectivity of multiplication. This is not a canonical parameter-space fan.

## Relevance and remaining scope

For any hypothetical homogeneous pair \((F,G)\) with sole reduced support
\(C\), this curve geometry applies after any independent coordinate change.
It describes only \(C\cap T\) and its closure. It does not compute the
individual tropicalizations of the two surfaces, their common initial ideals,
or the scheme-theoretic multiplicities of their intersection. Consequently
it supplies no new obstruction to STCI and no criterion for two-equation
realization. No additional interface with the unidentified H17 diagram,
Chow-cycle degenerations, or residual visibility is asserted here.

The contact/weight/toric-model formulas are complete for every realized frame;
realizability of all root partitions is not classified. Historical recovery is
also incomplete: a “global fan over parameter space” remains undefined without
a parameter lattice, moduli problem, and notion of wall. Resultant incidence
divisors are not automatically polyhedral chambers. The original transcript
was not recovered, so exact historical equivalence is not claimed. The
[special two-ray compactification](tropical_thickenings_and_endpoint_duality.md)
is a different coordinate choice, not a contradiction.
