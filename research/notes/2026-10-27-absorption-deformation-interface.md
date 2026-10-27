# Partial residual absorption through Cartier multiples

Date: 2026-10-27. Author: smooth-carrier construction agent.
Status: **independently reviewed provisional construction and uniform corollary**.
No canonical promotion or literature novelty is claimed. The construction uses
classical linear systems, Bertini and hypersurface restriction; its purpose is to
replace degree-by-degree experiments by one operation valid in arbitrary
multiplicity and sufficiently large mate degree.

## 1. Question and retrieved inputs

Fix

\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]

For proper actual pairs containing \(C\), ask how residual cycle mass can become
additional thickness on \(C\), without assuming the residual must disappear.
The construction below is over an algebraically closed field of characteristic
zero. The numerical floor in §4 works in any characteristic for this fixed
smooth embedded curve and the stated carrier hypothesis.

Retrieval followed [INDEX](../INDEX.md), [MAP](../MAP.md), and
[the contribution checklist](../CONTRIBUTING_AGENT.md). The relevant inherited
facts are:

- The ideal \(I_C(3)\) is globally generated. The
  [October 19 exceptional-cycle note, §2](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md)
  and [independent audit, §3](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md)
  already prove this from
  \[
  0\to\mathcal O_{\mathbf P^3}(1)\to I_C(3)
  \to\mathcal O_Q(2,0)\to0.
  \]
  The same input is used in the [all-degree intersection note](2026-10-27-global-containing-intersections.md).
  These are reviewed provisional evidence rather than a separate promoted
  record. No inherited verifier was replayed.
- The smooth quartic has degree four and genus zero. Its unique smooth
  containing quadric and the displayed ideal generators are recorded in that
  evidence. No balanced normal-bundle assumption is needed in this note.
- The accepted [R-0001](../results/quartic_carrier_exclusion.md) supplies a
  characteristic-zero low-degree STCI boundary, but it is **not an input** to
  either proof below. No closed low-degree case is reopened.

A targeted repository search found the inherited nef residual estimates and
fixed-degree degeneration examples, but not this particular arbitrary
\((m,n)\) construction paired with the uniform smooth-along-\(C\) residual
fraction. Their standard ingredients and lack of literature novelty claim
remain explicit.

## 2. A general positive construction in characteristic zero

**Proposition.** Let \(S=V(F_a)\subset\mathbf P^3_k\) be a smooth integral surface
containing \(C\), let \(H=\mathcal O_S(1)\), choose integers \(1\le m<n\), and
choose \(b\ge3n+1\). There are actual degree-\(b\) homogeneous forms
\(G_b(t)=G_n+tG_m\) such that:

1. Every finite fiber \(Y_t=V(F_a,G_b(t))\) is a proper complete intersection.
2. For every \(t\ne0\), the generic multiplicity of \(Y_t\) on \(C\) is exactly
   \(m\), while at \(t=0\) it is exactly \(n\).
3. For general \(t\ne0\),
   \[
   Y_t=mC+D_t
   \]
   as Cartier divisors on \(S\), with \(D_t\) smooth integral and not containing
   \(C\). At zero,
   \[
   Y_0=nC+D_n
   \]
   with \(D_n\) also smooth integral and not containing \(C\).
4. The residual family obtained by removing the **fixed lower** divisor \(mC\)
   is flat, and its special divisor is
   \[
   \mathscr D_0=(n-m)C+D_n.
   \tag{1}
   \]
   Thus \(4(n-m)\) units of residual cycle degree move onto \(C\) in the special
   fiber, with actual Cartier gluing.

Here smoothness and integrality of \(D_t\) are asserted for general parameter,
not every nonzero parameter. The numerical threshold is sufficient; optimality
is not claimed.

**Proof.** The curve \(C\) is an effective Cartier divisor on the smooth \(S\).
The quotient \(I_C(3)/I_S(3)\) is the pushforward of
\(\mathcal O_S(3H-C)\), so

\[
L=3H-C
\]

is globally generated. For \(r=m,n\),

\[
bH-rC=rL+(b-3r)H
\]

is very ample, because \(b-3r\ge1\), \(H\) is very ample, and tensoring a very
ample bundle with a globally generated one remains very ample. This last
fact can be seen by the graph map to the product of the two projective spaces,
followed by the Segre embedding. It uses actual global sections.

By Bertini smoothness and irreducibility, choose

\[
\tau_r\in H^0(S,\mathcal O_S(bH-rC)),\qquad
D_r=V(\tau_r),\quad r=m,n,
\]

with \(D_r\) smooth integral and not containing \(C\). Let \(s_C\) be the
canonical section of \(\mathcal O_S(C)\), and put

\[
\sigma_r=s_C^r\tau_r\in H^0(S,\mathcal O_S(bH)).
\]

These two sections are linearly independent, because their exact vanishing
orders along \(C\) differ. Consequently

\[
\sigma(t)=\sigma_n+t\sigma_m
=s_C^m\bigl(s_C^{n-m}\tau_n+t\tau_m\bigr)
\tag{2}
\]

is nonzero for every finite \(t\). Its divisor gives a proper intersection with
the integral surface \(S\). For \(t\ne0\), the bracket restricts on \(C\) to
\(t\tau_m|_C\), which is not identically zero, so the generic order is exactly
\(m\). At zero the exact order is \(n\).

The bracket in (2) is a family of sections of the **fixed** line bundle
\(\mathcal O_S(bH-mC)\). Its nonzero fibers are effective Cartier divisors.
They form a flat relative Cartier divisor over \(\mathbf A^1\). Alternatively,
on the product with the parameter line, a fiberwise nonzerodivisor has a
flat quotient by the local criterion for flatness. The same argument gives
flatness of the total CI family.

The residual pencil extends to \(\mathbf P^1\). At parameter infinity its
divisor is precisely the smooth integral \(D_m\). Smoothness and geometric
integrality are open in this proper flat family, so the generic member, and
therefore general finite nonzero members, are smooth integral. The special
member is exactly the Cartier sum (1), not merely a cycle equality.

Finally,

\[
0\to\mathcal O_{\mathbf P^3}(b-a)
\xrightarrow{\cdot F_a}\mathcal O_{\mathbf P^3}(b)
\to\mathcal O_S(bH)\to0
\]

and \(H^1(\mathbf P^3,\mathcal O(b-a))=0\) lift \(\sigma_m,\sigma_n\) to
homogeneous forms \(G_m,G_n\) with constant coefficients in \(k\). Their
linear combination lifts the entire family. Since its restriction to \(S\)
is nonzero in every fiber, \(F_a\) never divides \(G_b(t)\); integrality of
\(S\) gives properness. This proves all assertions. ∎

This is a general operation on actual global equations. It does not use
function-field-valued equation coefficients, a formal-algebraization
assumption, or a list of degree pairs.

The operation itself is more general than this quartic. For any smooth
connected curve \(C\subset\mathbf P^3\) whose ideal \(I_C(\delta)\) is globally
generated, the identical proof works on a smooth integral containing surface,
with \(b\ge\delta n+1\). Thus the number three enters only as a generation
degree for this particular ideal. No special quartic equations are needed in
the deformation mechanism.

## 3. Why full primary extraction must change in this family

On \(S\), the full \(C\)-primary component of \(Y_t\) is \(mC\) for \(t\ne0\),
and \(nC\) at zero. Its degree jumps from \(4m\) to \(4n\); it cannot be a flat
family with fixed Hilbert polynomial. The closure of the generic residual,
on the other hand, is the flat fixed-line-bundle family \(\mathscr D\), whose
specialization contains \((n-m)C\).

Thus the residual after removing the entire primary component at zero is
\(D_n\), whereas the specialization of the generic residual is
\((n-m)C+D_n\). Primary extraction and specialization do not commute.
Keeping these two residual operations separate is necessary even in this
ordinary smooth-carrier setting.

The [formal lifting interface](2026-10-27-absorption-formal-lifting-interface.md)
describes the distinction between a fixed-Hilbert-polynomial lower witness
and the full primary component. The [attachment-module interface](2026-10-27-absorption-attachment-module.md)
gives fiberwise information for the latter; no flatness of its equation
module across (2) follows automatically.

## 4. A uniform residual floor when a carrier is smooth along C

**Proposition.** Let \(S=V(F_a)\) now be any **integral** surface smooth at every
point of \(C\), possibly singular away from \(C\). Let \(G_b\) give a proper
intersection, and let \(m\) be its exact generic multiplicity along \(C\).
Write the effective Cartier divisor on \(S\) as

\[
V(G_b|_S)=mC+D,
\]

where \(D\) has no component \(C\). Then

\[
m\le\frac{b(3a-4)}{4a-2},
\qquad
\frac{4m}{ab}\le
\frac{4(3a-4)}{a(4a-2)}\le\frac23,
\qquad
\boxed{\deg D=ab-4m\ge\frac{ab}{3}.}
\tag{3}
\]

**Proof.** Because \(S\) is smooth along \(C\), the curve is Cartier there;
off \(C\) its ideal is the unit ideal. Hence it is a global Cartier divisor
on \(S\), regardless of singularities away from it. The line bundle
\(L=3H-C\) remains globally generated, as above. It consequently has
nonnegative degree on every integral curve, and \(L\cdot D\ge0\).

The normal sequence along \(C\) gives

\[
\deg N_{C/S}
=\deg N_{C/\mathbf P^3}-\deg\mathcal O_C(a)
=14-4a.
\]

Here \(\deg N_{C/\mathbf P^3}=4\deg C+2g(C)-2=14\) follows from the Euler and
tangent sequences; no splitting hypothesis is used. This is \(C^2\), since
\(C\) is Cartier. With \(H^2=a\) and \(H\cdot C=4\),

\[
0\le(3H-C)\cdot(bH-mC)
=b(3a-4)-m(4a-2).
\]

This proves the first inequality. The curve is nonplanar, so \(a\ge2\).
For integer \(a\ge2\),

\[
\frac23-\frac{4(3a-4)}{a(4a-2)}
=\frac{8(a-2)(a-3)}{3a(4a-2)}\ge0.
\]

The remaining assertions follow. Intersection degrees of Cartier line
bundles and effective curves are well-defined on the possibly singular
projective \(S\); smoothness away from \(C\) is not required. ∎

The constant \(1/3\) is sharp as a uniform bound. On the unique smooth
quadric \(Q\), put \(A=x_0^2x_2-x_1^3\). Its divisor on \(Q\) is \(C+2\ell\)
for a ruling line \(\ell\): in Segre coordinates
\((x_0,x_1,x_2,x_3)=(su,sv,tu,tv)\) one has
\(A=s^2(tu^3-sv^3)\), where \(tu^3-sv^3\) cuts out \(C\) and \(s=0\)
cuts out \(\ell\). This factorization, rather than divisor classes alone,
specifies the double line. The actual pairs \((q,A^n)\) of degrees \((2,3n)\) have cycle
\(n[C]+2n[\ell]\); residual degree \(2n=(2\cdot3n)/3\).
This elementary powering control tests sharpness and is not claimed as a
new construction or a separate low-degree research program.

More generally, for a smooth connected curve of degree \(e\), genus \(g\),
and globally generated \(I_C(\delta)\), the same carrier calculation gives

\[
0\le b(\delta a-e)
-m\bigl(e(a+\delta-4)-(2g-2)\bigr).                 \tag{4}
\]

One can solve (4) for an upper bound on \(m\) only when its displayed
coefficient of \(m\) is positive. No universal residual fraction is claimed
for arbitrary curves. The fixed quartic yields (3) upon substituting
\((e,g,\delta)=(4,0,3)\).

## 5. What this mechanism teaches

### Normal singular carriers: an index-compatible construction

There is also a conditional extension beyond the smooth-along-\(C\) setting.
Let \(S\subset\mathbf P^3\) be a **normal integral** hypersurface over an
algebraically closed field of characteristic zero, and assume the fixed smooth
curve \(C\) is \(\mathbf Q\)-Cartier on \(S\). Choose \(h>0\) with \(hC\)
Cartier. It is effective Cartier: on a normal surface a Cartier divisor with
nonnegative Weil coefficients has regular local defining functions. Choose
\(\delta\) large enough that \(\delta H-hC\) is globally generated, as permitted
by Serre's theorem.

For any \(1\le u<v\) and \(b\ge\delta v+1\), the line bundles
\[
bH-rhC=r(\delta H-hC)+(b-\delta r)H,\qquad r=u,v,
\]
are very ample. Their general divisors are smooth integral and avoid the
finite singular locus of the normal surface. Let \(s_{hC}\) be the canonical
section of \(\mathcal O_S(hC)\); the same family
\[
s_{hC}^{\,v}\tau_v+t\,s_{hC}^{\,u}\tau_u
\]
therefore gives actual homogeneous pairs with exact multiplicity \(hu\)
for \(t\ne0\) and \(hv\) at zero. The proof of lifting, properness and
flatness is unchanged, and the fixed-lower residual specializes to
\[
(hv-hu)C+D_{hv}.
\]
Smooth residuals are asserted for general parameters only.

This is a construction in index-compatible increments on an **already
specified** \(\mathbf Q\)-Cartier normal carrier. It neither supplies such a
carrier for every proposed index nor gives a uniform \(\delta\) across carriers.
The characteristic-zero fixed-carrier mate problem still needs a positive
divisor/class relation and descent, such as the exact hypotheses of
[R-0003](../results/fixed_carrier_conductor_criterion.md). The uniform
one-third residual floor of §4 does not extend to arbitrary singular-along-\(C\)
carriers by this argument.

### Arbitrary normal carriers: partial cycle transfer needs no Cartier index

A weaker construction works on **any** normal integral hypersurface \(S\)
containing a prime curve \(C\), even if \(C\) is not \(\mathbf Q\)-Cartier.
This is a standard consequence of Serre global generation for coherent
divisorial sheaves. Fix \(1\le m<n\), and put
\[
\mathcal J_r=\mathcal O_S(-rC)\subset\mathcal O_S,\qquad r=m,n.
\]
These are coherent rank-one reflexive ideal sheaves. For sufficiently large
\(b\), both \(\mathcal J_m(bH)\) and \(\mathcal J_n(bH)\) are globally generated.
At the generic point \(\eta_C\), the normal surface has a DVR and
\((\mathcal J_r)_{\eta_C}\) is its \(r\)-th maximal-ideal power. Global
generation therefore supplies a section \(\sigma_r\) whose order on \(C\)
is exactly \(r\). Regard both as sections of \(\mathcal O_S(bH)\).

Their differing orders give a nonzero section
\[
\sigma_n+t\sigma_m
\]
for every finite \(t\), of exact order \(m\) when \(t\ne0\) and exact order
\(n\) at zero. The same hypersurface restriction sequence lifts the sections
to actual degree-\(b\) homogeneous equations. Every fiber intersects \(S\)
properly, and the resulting CI family is flat by the fiberwise Cartier
argument. This last construction uses no Bertini theorem and works in any
characteristic.

Thus partial **cycle** transfer alone does not require \(C\) to be
\(\mathbf Q\)-Cartier. Here there is no explicit uniform bound on \(b\), no
smooth-residual assertion, and no claim that the residual after primary
extraction forms a flat family or commutes with specialization. In particular
the product-ideal Cartier gluing of the preceding corollary has not been
extended to a non-Cartier \(mC\).

The pure-support endpoint has a stronger necessary condition. If a nonzero
section of \(\mathcal O_S(bH)\) has zero support exactly \(C\), its Cartier
divisor is \(nC\). Hence \(nC\sim bH\), and \(C\) is \(\mathbf Q\)-Cartier.
The weak partial construction supplies no such class relation. On a
specified non-\(\mathbf Q\)-Cartier normal carrier it can raise finite contact
orders, while it cannot reach a pure-support endpoint.

### Effective-cone interpretation and construction limits

There is an effective-cone interpretation with no degree enumeration. On a
fixed carrier write
\[
\tau_{\mathrm{eff}}(S,C)=
\sup\{t\ge0:[H-tC]\text{ is pseudo-effective}\}.
\]
For the general-curve hypotheses of (4), global generation of
\(\delta H-C\) gives \(\tau_{\mathrm{eff}}\ge1/\delta\).
When \(e(a+\delta-4)-(2g-2)>0\), intersecting a pseudo-effective class
with the nef \(\delta H-C\) gives
\[
\frac1\delta\le\tau_{\mathrm{eff}}(S,C)
\le\frac{\delta a-e}{e(a+\delta-4)-(2g-2)}.
\]
The construction works safely inside a uniformly very ample range;
the upper bound is a supporting nef inequality for the effective cone.
The actual threshold need not equal that upper bound, and computing it
carrier by carrier is not proposed as the main research task.

Partial absorption is available in characteristic zero in arbitrary finite
amounts, with actual global equations, a fixed carrier, and explicit
scheme-theoretic gluing. Thus an attempted universal rule forbidding all
such transfer would be false. The difficulty is more specific than the
possibility of any transfer.

The same Cartier-carrier setting has a degree-independent residual floor.
To move more than two thirds of the CI cycle degree onto \(C\), no integral
carrier in the pair can stay smooth at every point of \(C\). For equal
degree pairs the statement applies to every integral member of their
pencil: existence of even one member smooth along all \(C\) enforces (3).
This locates a geometric change any further construction must address;
it is not an exclusion of singular carriers or a proof of characteristic-zero
STCI nonexistence.

Smoothness along \(C\), rather than global smoothness, is the exact
hypothesis used for the residual floor. For the positive construction we
first kept global smoothness to ensure smooth residuals by ordinary Bertini,
then gave the separate normal \(\mathbf Q\)-Cartier extension above.
The weaker coherent-divisorial-sheaf construction permits arbitrary normal
carriers, with no smooth residual or scheme-gluing conclusion. No construction
on arbitrary nonnormal carriers is asserted. The new contribution is this general constructive/boundary
pair, not the classical linear-system machinery itself.

## 6. Literature, independent audit and limits

Primary sources freshly inspected for the standard mechanisms:

- [Stacks, Bertini smoothness](https://stacks.math.columbia.edu/tag/0FD4)
  and [Bertini irreducibility](https://stacks.math.columbia.edu/tag/0G4C).
- [Stacks, cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS)
  for hypersurface section lifting.
- [Stacks, relative effective Cartier divisors](https://stacks.math.columbia.edu/tag/062Y)
  and the surrounding section for fiberwise Cartier behavior and flat
  families. The proof above also states the needed local flatness argument.
- [Stacks, very ample sheaves](https://stacks.math.columbia.edu/tag/01VL);
  the tensor-with-generated-bundle step is independently explained by the
  graph and Segre construction.

The prior October 19 nef residual correction is explicitly retained as an
ingredient. The present floor uses the extra smooth-along-\(C\) hypothesis
and divisor subtraction on the carrier; it is not advertised as a new
unrestricted residual inequality. No inherited calculations were rerun and
no sampled cases were used to infer a general theorem.

Independent reconstruction is recorded in the
[deformation audit](2026-10-27-absorption-deformation-audit.md).
The unrestricted STCI question, singular-carrier absorption, and deformations
of non-Cartier marked structures remain open beyond the statements here.
