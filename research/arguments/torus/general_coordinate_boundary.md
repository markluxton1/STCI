# General coordinate boundary and a single edge collision

## Scope

Let k be algebraically closed with trivial valuation, and let
C=[s^4:s^3t:st^3:t^4] be the fixed smooth embedded quartic. Choose four
independent hyperplanes L_i, giving projective coordinates y_i=L_i(x).
Their restrictions f_i=L_i(s^4,s^3t,st^3,t^4) are binary quartics.
Write N=Z^4/Z(1,1,1,1), with e_i the coordinate classes.
The geometric argument below works in every characteristic under the stated
simple-root hypotheses. The explicit numerical witness is characteristic zero.

## Edge loci and the general configuration

For each of the six unordered pairs i,j, the binary homogeneous resultant
Res(f_i,f_j) vanishes exactly when C meets the coordinate edge V(y_i,y_j).
This is an incidence equation on the parameter space of independent ordered
hyperplanes, not a claim about real chambers or a global fan on that space.
Off these six loci and the four individual discriminant loci, the divisors
(f_i=0) are reduced, disjoint, and each has degree four. Thus C intersected
with the coordinate torus is P^1 minus 16 distinct points.

At a puncture choose a nonvanishing coordinate to trivialize O(4). The orders
of the four sections, modulo a common order, give its valuation vector in N.
Each of the four points of (f_i=0) contributes e_i. The standard normalization
formula for a parametrized tropical curve (here the parametrization is an
embedding, so its generic degree is one) sums the primitive-vector indices.
Consequently the four rays have weight four. Balancing is 4 sum_i e_i=0.

## Exactly one shared simple root

Assume f_i and f_j have exactly one common root q, simple in both; every other
root is simple, the other two f's do not vanish at q, and there are no other
pair collisions. There are then 15 punctures. The valuation vectors are:
three copies of e_i; three of e_j; four of each remaining e; one e_i+e_j.
All these vectors are primitive in N. The tropical fan therefore has five
rays, of respective weights 3,3,4,4,1. Their weighted sum is again zero.
This is a precise bounded statement about the curve at that incidence locus;
it does not assert a flat family of tropical fans or schemes across it.

Blow up the torus-invariant edge V(y_i,y_j). Near q, dehomogenize by another
coordinate and choose a parameter tau on C. Then y_i=tau a(tau),
y_j=tau b(tau), where a,b are units. In the blowup chart with ratio
v=y_j/y_i, the strict transform has v=b/a, a unit. The exceptional equation
y_i has order one on this curve. Hence the strict transform meets the
exceptional divisor transversely, away from both strict coordinate divisors.
The ambient fan operation is the star subdivision inserting e_i+e_j in
cone(e_i,e_j). This does not by itself say the entire ambient blowup is a
Tevelev tropical compactification: its multiplication map need not hit the
unused toric orbits. The relevant toric open subset must be specified for
that stronger terminology.

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

## Verification, sources, and limits

An independent mathematical reviewer checked the valuation weights,
primitivity, balancing, blowup chart, and exact scope. Source inputs:

- Repository audit: https://github.com/markluxton1/STCI/blob/9b7f30757eab14a5d4815c8682184399a35c7c32/research/cross_conversation_recovery_audit.md
- The existing special-coordinate model, which is different: https://github.com/markluxton1/STCI/blob/9b7f30757eab14a5d4815c8682184399a35c7c32/research/arguments/torus/tropical_thickenings_and_endpoint_duality.md
- Tevelev, *Compactifications of subvarieties of tori*, Definition 1.1 and
  Lemma 2.2 for terminology and the orbit/valuation relation:
  https://arxiv.org/html/math/0412329v3
The argument and numerical witness were checked afresh in the recovery audit.

Tangencies, triple or simultaneous collisions, higher contact weights,
compatibility of successive blowups, a global parameter-space fan, and exact
identity with the original historical claim remain unverified. Nothing here
constructs or obstructs a proper sole-support homogeneous pair for C.

### Additional checked multiplicity reference

Sturmfels–Tevelev, *Elimination Theory for Tropical Varieties*, §§2–3,
Definition 3.1/Lemma 3.2: https://arxiv.org/abs/0704.3471 . For this case take
the open toric subfan consisting of the origin and the five rays in the
ambient blowup fan. The strict curve is still proper in this open. Its
boundary intersections are transverse, and the torus orbit tangent vectors
together with the curve's transverse tangent span the ambient tangent space.
Thus the multiplication map is smooth and surjective; ray multiplicities
are the corresponding orbit-intersection lengths. This supplies a second
geometric justification of the valuation weights without misidentifying
the full complete ambient fan with the tropical curve.
