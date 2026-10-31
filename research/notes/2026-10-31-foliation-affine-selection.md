# Foliation and affine-degree mechanisms for arbitrary pairs

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
see the [bounded audit](2026-10-31-foliation-affine-selection-audit.md).
This closes two bounded mechanism selections. It supplies neither an
unrestricted STCI obstruction nor a construction, and promotes no result.

## 1. Question and inherited evidence

Fix an algebraically closed field of characteristic zero and

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

The question is whether two arbitrary homogeneous equations can have sole
support C. The [complement-pencil assessment](2026-10-31-unrestricted-strategy-assessment.md#8-subsequent-selection-birational-transport-and-complement-pencils)
already identifies a morphism \(\mathbf P^3\setminus C\to\mathbf P^1\)
as an equivalent formulation. The
[affine-endpoint criterion](2026-10-30-four-streams-affine-endpoints.md)
already retains the ordinary degree filtration and full scheme at infinity.
The [Jacobian/contact result](2026-10-31-cyclic-cover-duality.md) and its
[Hamiltonian continuation](2026-10-31-contact-global-consequence.md) retain
actual ideal membership and explain why reduced characteristic-foliation
arguments do not automatically extend to thick structures. These are
reviewed provisional dependencies, not unrestricted exclusion theorems.

The new question was whether foliation residues or affine degree estimates
provide an additional implication for arbitrary pairs. Literature was
checked before deciding whether to expand either mechanism.

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
not justify the unit-times-exact argument. For general D, no bound on the
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

The [weighted-initial analysis](2026-10-26-weighted-initials-normal-boundary.md)
already retains cancellation, integral lattices and full transition maps.
Renaming its filtration as a semidegree does not recover missing data.

## 5. Decision, constructive meaning, and stopping conditions

Stop these bare applications. Neither finite non-Kupka counts nor the
checked affine inequalities currently supplies a new unrestricted
incompatibility or a sufficient boundary construction. This conclusion
concerns these applications, not all foliation or valuation geometry.

For nonexistence, a continuation needs a specified comparison controlling
the normalized foliation's actual curve contributions, or a
characteristic-zero lower bound forcing positive loss in §3 for all
supported affine pairs. For existence, the affine formulation instead
asks for actual equations attaining the equality in the fixed
compactification. A construction through a finite map must control both
gaps; finite-map existence alone is insufficient. The earlier
[paired elliptic construction](2026-10-31-paired-elliptic-construction.md)
remains positive evidence that nontrivial target data can be constructed,
while its failed node gluing is an independent condition, not a universal
obstruction.

Reopening requires a specified new mechanism to test, not a proof of its
success in advance. State the needed premise and what an outcome would
teach beyond the existing equivalent condition. For a derivative estimate,
first establish its actual subalgebra input or an applicable module-level
replacement. For a residue formula, first establish its component
hypotheses and treatment of the other singular curves. Stop when the
premise fails or only the existing degree budget is recovered. Do not
append local classifications, tame-pair lists, or adjacent elliptic targets
automatically. No next technical campaign is selected at this checkpoint.

Two fresh `gpt-6-astra/xhigh` workers completed the bounded selections.
A fresh `gpt-6.1-sol/high` reviewer independently reconstructed the
deductions, checked primary source hypotheses and challenged the proposed
allocation. The review added the exact reduced affine control, sharpened
the semidegree citation and retained the essential unit condition in the
residue argument. No material correction remains; all three workers have
completed their assignments. No new numerical computation,
canonical promotion, carrier construction or defining pair was produced.
