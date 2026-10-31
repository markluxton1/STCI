# Normalized foliations and the two affine boundary losses

Fix the smooth quartic C0=[s^4:s^3t:st^3:t^4] over an algebraically closed characteristic-zero field. The following are independently reviewed provisional deductions about arbitrary proper supported homogeneous pairs and arbitrary affine radical pairs. They supply neither an unrestricted obstruction nor equations. The review reconstructed the normalized and entirely non-Kupka alternatives, localized residues, both nonnegative affine losses and the reduced-pair control; the unit-times-exact and primary-source hypotheses below were essential. Existing [contact/Jacobian identities](contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity) are ideal-membership statements, not automatically subalgebra membership.

## 2. The foliation must be normalized, and its Kupka hypotheses retained

Analytic foliation and residue statements are read over the complex
numbers after descent to a finitely generated field of definition.

For a hypothetical supported proper CI \((F_a,G_b)\), put

\[
\omega_0=bG\,dF-aF\,dG,\quad
D=\gcd(\text{coefficients of }\omega_0),\quad
\omega=\omega_0/D,\quad e=a+b-\deg D.
\]

Euler's identity makes \(\omega\) a section of
\(\Omega^1_{\mathbf P^3}(e)\); it defines the normalized foliation of the
equalized pencil. Its normal determinant is \(O(e)\). The removal of D
cannot be omitted when discussing the degree or the singular set.

C remains in the singular locus after this normalization. If the
foliation were regular at a point of C, analytic Frobenius coordinates
would make its meromorphic first integral a meromorphic function of one
transverse coordinate. Its zero and pole divisors could not both pass
through that point without sharing a local hypersurface component. This
contradicts proper intersection of F and G. This argument is over the
complex numbers; descent and faithful base change give the stated
characteristic-zero conclusion.

There is a direct useful limitation on the classical Kupka mechanism.
If D does not vanish identically on C, then **every point of C is
non-Kupka** for this normalized foliation. Indeed,

\[
d\omega_0=-(a+b)dF\wedge dG.
\]

At the generic point of C, the transverse regular local ring has dimension
two and \((F,G)\) has length \(m=ab/4>1\). If the classes of dF and dG
were independent there, F,G would generate the maximal ideal and this
length would be one. Their wedge therefore vanishes on the reduced
curve. On the dense open where D is a unit, both \(\omega|_C\) and
\(d\omega|_C\) vanish. They vanish on all of reduced C by extension.
Here dω along its singular set is independent of local trivialization.
The inequality m>1 follows already from the known low-degree exclusions.
If D contains C, this argument does not apply to the normalized form.

[Calvo-Andrade–Corrêa–Fernández-Pérez, Theorem 2](https://arxiv.org/pdf/1506.05438)
instead assumes a connected lci component Z of the codimension-two
singular set with only finitely many non-Kupka points. It identifies their
divisor with the zeros of a section of
\(\omega_Z^{-1}\otimes K_{\mathcal F}|_Z\). If C satisfied those
hypotheses, its degree would be

\[
\deg D_{\rm NK}=\deg K_{\mathcal F}|_C-\deg\omega_C=4e-14.
\]

For smooth C there is also a direct extension that does not require it
to be a connected component disjoint from other singular curves. Either
\(d\omega|_C\) is identically zero, or C is generically Kupka. In the
second case the two-form belongs on the Kupka open set to
\(\det N_C^*\otimes O_C(e)\). This is a line subbundle of
\(\Omega^2_{\mathbf P^3}|_C\otimes O_C(e)\), so membership extends
across the omitted points of smooth C. Its nonzero section has an
effective zero divisor of degree \(4e-14\). In particular e≥4 and the
divisor is nonempty. This smooth-component deduction extends the formula's
scope, but still gives no finite divisor in the entirely non-Kupka case.

The same source's Baum–Bott formula retains every singular curve:

\[
e^2=4\operatorname{BB}(\mathcal F,C)
  +\sum_{T\ne C}\operatorname{BB}(\mathcal F,T)\deg T.
\]

Isolated points do not contribute to this degree-four cohomology identity.
One specialization can be evaluated without classifying transverse types.
If D=1, then off C the actual form is locally a unit times an exact
differential. For example, on a sufficiently small complex neighborhood
where G≠0,

\[
\omega_0=bG^{1+a/b}\,d(FG^{-a/b}).
\]

The logarithmic derivative of this unit is a closed Bott connection, so
the off-C curve residues vanish. The analogous expression applies where
F≠0. Equivalently, the exact transverse form has a Hamiltonian vector
field of zero divergence; [Corrêa–Lourenço, Theorem 1.2](https://arxiv.org/pdf/1612.05787)
identifies its Grothendieck residue with the curve's Baum–Bott residue
without the older genericity restriction. Thus

\[
D=1\quad\Longrightarrow\quad
\operatorname{BB}(\mathcal F,C)=(a+b)^2/4.
\]

This is compatible with C being entirely non-Kupka: vanishing of the
two-form on the reduction does not make its localized residue vanish.
After arbitrary factor removal, a holomorphic first integral alone does
not justify the unit-times-exact argument. For the explicit local control h=xy², removing the coefficient factor from dh gives y dx+2x dy. Its tangent vector field has eigenvalues 2 and −1, and its c1² residue is (2−1)²/(2·(−1))=−1/2, nonzero. Thus saturation really can destroy the vanishing-residue premise. For general D, no bound on the
remaining actual residues has been supplied here.

The algebraic Kupka scheme \((J(\omega):\operatorname{coeff}(d\omega))\)
must also be distinguished from the closure of classical Kupka points.
[Massri–Molinuevo–Quallbrunn, *The Kupka Scheme and Unfoldings*](https://arxiv.org/pdf/1509.07231)
imposes radical or additional genericity hypotheses for the relevant
identifications; a supported nonreduced CI supplies none automatically.
Thus a nonzero scheme supported on C would not prove that C has a
classical Kupka open set.

**Geometric extraction.** A pencil with a thick base curve can have
vanishing transverse differential along its entire reduced support. A
formula counting exceptional points in a generically nondegenerate
foliation then misses the relevant geometry. This is a general statement
about thick CI base curves under the stated condition on D, not a new
obstruction peculiar to the quartic. It neither classifies the possible D
nor disposes of the cases in which D contains C. The residue specialization
adds an exact compatibility condition, not an incompatibility. No general
residue evaluation or local foliation classification was completed.

## 3. Affine projection separates two boundary losses

On \(x_0=1\), write the coordinates as z,y,w. The triangular change

\[
Y=y-z^3,\qquad W=w-zy
\]

identifies C with the line \(Y=W=0\). Let P,Q be any polynomial pair
with radical \((Y,W)\), and let f,g be the corresponding actual
polynomials in z,y,w. Write a,b for their ordinary degrees and m for
their generic transverse colength. No coordinate-pair or power-generation
hypothesis is imposed.

Choose a general affine linear form ℓ with nonzero w coefficient. Its
restriction to C is a degree-four polynomial in z. Put

\[
B=k[z,y,w]/(f,g),\qquad H=(f,g,\ell):\mathbf A^3\to\mathbf A^3.
\]

The algebra B is finite over \(k[\ell]\): its reduction is finite and
the nilradical is nilpotent. It is Cohen–Macaulay with unique associated
prime \(I_C\); hence it is torsion-free, therefore free, over
\(k[\ell]\). Its rank is 4m, by multiplying the degree-four function
field extension on the reduction by its generic length m. Every fiber
over the distinguished target axis consequently has length 4m.

These finite fibers also make H dominant and generically finite. Write μ
for its generic degree. Conservation of isolated multiplicities, followed
by affine Bézout, gives

\[
\boxed{4m\le\mu\le ab},\qquad
\boxed{ab-4m=(ab-\mu)+(\mu-4m)}.
\]

The term \(\mu-4m\) counts sheets lost as a generic target approaches
the distinguished axis; \(ab-\mu\) records loss at infinity already
present for a generic target in this projective presentation. Their sum
is the degree of the residual cycle at infinity for the original pair.
They need not vanish together merely because H is finite.

The existing reduced affine presentation already illustrates this
distinction, without choosing another family. Take f=Y and g=W, so
a=3, b=2, m=1. Substitution gives
\(y=f+z^3\), \(w=g+zf+z^4\); hence ℓ makes z satisfy a quartic
with constant nonzero leading coefficient over \(k[f,g,\ell]\).
Thus H is finite of degree four. Here \(\mu-4m=0\) but
\(ab-\mu=2\). Its leading forms \(-z^3,-zy\) share the boundary
line z=0. Properness of this affine map leaves a genuine projective
residual curve. This is a direct check on the inherited affine equations,
not a new counterexample search.

This extraction generalizes: replace C by an integral affine curve with
projective closure of degree d, and choose ℓ whose extension to its
normalization has poles at all points at infinity. For general ℓ its
degree is d. A supported affine CI of generic length m then gives
\(dm\le\mu\le ab\) by the same argument. The coefficient four is thus
the degree of the embedded curve, not a characteristic-zero obstruction.

## 4. What the affine literature does and does not add

[Jelonek, Proposition 6 and Theorem 15](https://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf)
identifies properness at a target through equality of its finite-fiber
multiplicity with μ, and bounds the degree of the nonproperness locus by
\(ab-\mu\) for this H. That locus is empty or a hypersurface.
Consequently \(ab=4m\) forces H finite. Finiteness alone does not make
its generic degree equal ab. The theorem does not force either loss in
§3 to be positive. Its complex application transfers to characteristic
zero through a finitely generated field of definition and faithful base
change.

[Mondal, *General Bezout-type theorems*, Theorem 3.1 and Example 3.4](https://arxiv.org/pdf/1111.0614)
gives the corresponding semidegree intersection bound and an equality
criterion when the completion preserves intersection at infinity. With
ordinary degree, equality for \((f,g,\ell)\) says that their highest
homogeneous parts have no common projective zero. For general ℓ, this
holds exactly when the highest parts of f,g have no common curve in the
boundary plane. This recovers the existing endpoint criterion. Changing
completion also changes the intersection bound; it does not prove the
needed equality in the original \(\mathbf P^3\).

[Vénéreau, *A parachute for the degree of a polynomial in algebraically independent ones*](https://arxiv.org/pdf/0704.1561)
provides characteristic-zero derivative estimates for elements of the
subalgebra \(k[f,g]\). For example, if
\(\Delta=a+b-2-\max_{i<j}\deg(f_{x_i}g_{x_j}-f_{x_j}g_{x_i})\),
then

\[
\deg R(f,g)\ge\deg R_V(f,g)+b-\Delta
\]

when the displayed derivative is nonzero. Sole support supplies ideal
power containments with ambient coefficients, not the necessary
subalgebra membership. The existing homogeneous contact identity is
likewise ideal membership. No comparison from this estimate to m that
forces a positive quartic-specific loss has been obtained.

The weighted-initial analysis
already retains cancellation, integral lattices and full transition maps.
Renaming its filtration as a semidegree does not recover missing data.
## What remains to be proved

For nonexistence, a continuation needs a comparison controlling actual normalized curve residues, or a characteristic-zero lower bound forcing positive affine boundary loss for every pair. For existence, actual equations attaining equality in the fixed projective compactification suffice. Finiteness alone does not attain it. The derivative route first needs its actual subalgebra hypothesis or a proved module-level replacement; the residue route first needs the singular-component hypotheses and all other curve contributions. No local classification, adjacent-target enumeration, or new numerical computation is implied by these interfaces. The full question remains open.

## Characteristic boundary

The normalized-foliation/Frobenius-coordinate and analytic residue arguments above are retained in characteristic zero, with the stated descent to complex numbers. They are not transferred to characteristic p: coefficients a,b or a+b can vanish, differentials of p-th powers vanish, and the meromorphic first-integral and separability arguments can change. The elementary affine rank and ordinary-degree budget retain their algebraic meaning, but the cited complex properness and derivative estimates are used only at their checked characteristic-zero scope. No inequality forcing positive loss in characteristic p is claimed; the every-prime quartic-carrier construction in the [positive-characteristic construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-a-quartic-carrier) supplies actual pairs with zero residual loss, consistent with the exact boundary criterion.
