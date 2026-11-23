# Translate coordinates and fixed-surface equation lifts

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed the seed/Hodge multiplicity monoids, symmetry lattice, ADE contact-capacity bound and sextic endpoint consequences. Inherited inputs are the established local power–socle theorem, Picard saturation, actual almost-Cartier criterion and stated marked ADE formulas.

**Review:** the coefficient, syzygy, descent and certificate statements and
their controls received independent proof review. The fixed-carrier
multiplicity comparison also received independent reconstruction.

This interface separates what two restricted equations retain from their
normal extensions. It applies to arbitrary proper pairs, without assuming
an invariant ideal or a carrier equation among the generators. The restriction,
syzygy and multiplicity comparisons are characteristic free. The descent
and sextic applications state their characteristic assumptions.

Work over an algebraically closed field \(k\), with
\(S=k[x_0,x_1,x_2,x_3]\).

## Translate coordinates constrain actual coefficients

For any homogeneous form \(F\in S_d\), without an eigenform assumption,
write
\[
 F(1,t,ut^3,vt^4)=\sum_w t^w F_w(u,v),\qquad
 F_w(u,v)=\sum_{\substack{|\alpha|=d\\
       \alpha_1+3\alpha_2+4\alpha_3=w}}
       c_\alpha u^{\alpha_2}v^{\alpha_3}.
\]
Then \(F\) contains \(C_{u_i,v_i}\) exactly when
\(F_w(u_i,v_i)=0\) for every \(w\): the powers of \(t\) are independent,
and the torus is dense in the curve. For a prescribed finite support
\(\Xi=\{(u_i,v_i)\}\), the permitted degree-\(d\) equations are therefore
the kernel of an explicit linear evaluation map. Moving the points changes
this map, its kernel and possibly its rank. This extends the coefficient
description in the [reduced-cycle realization criterion](../equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle)
to containment by arbitrary forms; it does not extend that theorem's
eigenform-generator conclusion to repeated cycles.

For example, \(q=x_0x_3-x_1x_2\),
\(A=x_2^4-x_0x_3^3\), and \(c=x_1^3-x_0^2x_2\) give respectively
\[
 q=t^4(v-u),\qquad A=t^{12}(u^4-v^3),\qquad c=t^3(1-u)
\]
on this torus. Thus translates on the quadric have \(u=v\), while
translates on the named quartic have \(u^4=v^3\). These are literal
constraints from surface equations.

Repeated entries in \(\Xi\) add no new containment conditions. For a
proper pair, its multiplicity along \(C_{u_i,v_i}\) is instead
\[
 \dim_{k(t)}\frac{k(t)[[\xi,\eta]]}
 {\bigl(F(1,t,(u_i+\xi)t^3,(v_i+\eta)t^4),
        G(1,t,(u_i+\xi)t^3,(v_i+\eta)t^4)\bigr)}.
\]
This is the completed local intersection length at the generic point of
that curve. It is a joint condition on the two equations, not an order
of vanishing imposed separately on each. For distinct translated curves,
if these actual lengths are \(n_i\)
and \(ab=4\sum_i n_i\), they exhaust the degree of a proper pair;
purity then excludes every additional component, including boundary
components. Evaluating coefficients, determining these local algebras,
and checking properness retains the connection from parameters to actual
equations without assuming that the ideal is invariant.

## Restricted equations and their lifts

Put \(A=x_2^4-x_0x_3^3\), \(X=V(A)\), and \(B=S/(A)\).
Knowing the labeled restrictions \(f=F_a\bmod A\), \(g=G_b\bmod A\)
determines precisely the affine spaces
\[
 F=F_0+A U,\qquad G=G_0+A V,
 \quad U\in S_{a-4},\quad V\in S_{b-4},
\]
where \(S_d=0\) for \(d<0\). This follows from the kernel \((A)\)
of the graded restriction map. Thus the full restricted equations contain
more information than their common support, but still leave normal
corrections. Fixed degrees bound this ambiguity; they do not eliminate it
in arbitrary degrees. Properness and ambient residual support must be
tested for the same chosen lifts.
Full labeled restrictions modulo \(A^r\) recover the forms once
\(4r>\max(a,b)\), since no nonzero form of either degree is divisible
by \(A^r\); there is no uniform depth assertion in unbounded degree.

On the [normalization of \(X\)](../arithmetic/positive_characteristic_constructions.md#normalization-and-its-fibers),
write \(h=s^3t\) and \(\phi=z-h\). If both restrictions are nonzero and
the ambient pair has sole support \(C=C_0\), then
\[
 \nu^*f=\phi^r f_0,\qquad \nu^*g=\phi^s g_0,
 \qquad r,s\ge1,
\]
with \(\phi\nmid f_0g_0\). Their common zero set off \(V(\phi)\)
is empty. In particular the residual factors cannot share a divisor,
and all their common projective points must lie on \(V(\phi)\).
These facts follow from unique factorization and finite surjectivity of
\(\nu\). They do not force either residual factor to be constant.

## A control on this very quartic

Take
\[
 q=x_0x_3-x_1x_2,\qquad c=x_1^3-x_0^2x_2.
\]
Their normalized restrictions are
\[
 \nu^*q=-s t^3\phi,\qquad
 \nu^*c=\phi(z^2+zh+h^2).
\]
Their common projective zero support is exactly \(V(\phi)\) in every
characteristic. Indeed a common zero off that divisor would have
\(s t^3=0\), hence \(h=0\), and then \(z^2=0\), contradicting
\(\phi\ne0\). Nevertheless the ambient proper pair has cycle
\[
 [V(q,c)]=[C]+2[L],\qquad L=V(x_0,x_1).
\]
In Segre coordinates \([x_0:x_1:x_2:x_3]=[a u:a v:b u:b v]\),
\(c|_Q=a^2(av^3-bu^3)\), proving the cycle identity.
The residual line meets \(X\) only at \(p_\infty\in C\).
Thus even this fixed quartic can hide an actual residual curve from a
support-only restriction test. This example does not claim that the full
restricted scheme is reduced, or that the same restricted data admit an
STCI lift. The [stronger simultaneous-surface control](fixed_surface_and_endpoint_algebras.md#3-full-fixed-d-restrictions-do-not-determine-generic-thickness)
already gives pairs with identical full restrictions and different generic
thicknesses on the quadric and both endpoint planes.

## Relations recover the first annihilator

Let \(I=(F,G)\) be any proper homogeneous pair, and \(E=S/I\).
Write \(\operatorname{Syz}_B(f,g)\) for pairs \((u,v)\) with
\(uf+vg=0\). As ungraded modules there is a natural isomorphism, for
these actual lifts,
\[
 \frac{\operatorname{Syz}_B(f,g)}{B(g,-f)}
 \ \simeq\ \operatorname{Ann}_E(A)
 =\frac{I:A}{I}. \tag{1}
\]
With the usual degree-labeled Koszul modules, the right side is shifted
by \(-4\). The restriction pair therefore determines the abstract module
on the right. Its embedding in \(E\), and multiplication through further
normal layers, require the lifts.

**Proof.** Lift a relation to \(U,V\in S\). There is a unique \(H\in S\)
with \(UF+VG=AH\); send the relation to \(H\bmod I\).
Changing the lifts of \(U,V\) adds an element of \(I\) to \(H\).
Every element of \(I:A\) occurs. If \(H=PF+QG\), then
\((U-AP)F+(V-AQ)G=0\). Since \(F,G\) form a regular sequence,
this relation is a multiple of \((G,-F)\). Reduction modulo \(A\)
identifies the kernel in (1). Conversely those Koszul relations map to
zero. This proves (1), including when a restriction is zero.
The standard [regular-sequence Koszul exactness](https://stacks.math.columbia.edu/tag/062F)
is the general algebraic input; no novelty is claimed for that input.

For nonzero normalized restrictions with sole common support \(V(\phi)\),
their gcd is \(\phi^\ell\), up to scalar. Put \(T=k[s,t,z]\) and
identify \(B\) with \(k[s^4,st^3,t^4,z]\). Unique factorization gives
the more explicit description
\[
 M=\{w\in T:w\nu^*g/\phi^\ell\in B,
                 \ w\nu^*f/\phi^\ell\in B\},\qquad
 \operatorname{Syz}_B(f,g)/B(g,-f)\simeq M/(\phi^\ell B).
\]
Indeed every syzygy upstairs is a multiple of the coprime pair
\((\nu^*g/\phi^\ell,-\nu^*f/\phi^\ell)\); both entries must descend.
This is a simultaneous module descent problem, broader than asking that
one scalar power \(\phi^N\) descend. The relation's quotient by \(A\)
still uses the actual ambient lifts in (1).

For a supported pair, \(A\in\sqrt I\), so some
\[
 A^N=PF+QG \tag{2}
\]
already follows. A proper homogeneous CI ideal is saturated, so there
is no distinction here between projective sole support and the required
homogeneous radical membership. The least such \(N\) is the nilpotence
index of multiplication by \(A\) on \(E\). Equivalently the chain
\(I\subseteq I:A\subseteq I:A^2\subseteq\cdots\) reaches \(S\).
Equation (1) identifies its first quotient, not the entire chain.
Conversely, if the restricted pair already has sole common support \(C\)
on \(X\), nilpotence of \(A\) on \(E\) is equivalent to sole ambient
support \(C\): it forces all of \(V(F,G)\) into \(X\).

For a homogeneous control, choose any quartic \(D\) coprime to \(A\).
The proper pairs
\[
 I=(D^2,D^2+A^2),\qquad J=(D^2,D^2+A^2+AD)
\]
have the same type \((8,8)\), the identical labeled restrictions
\((\bar D^2,\bar D^2)\), and the same reduced support \(V(A,D)\).
But the least powers of \(A\) in them are two and three. For \(J\),
\(A^3=AD^2+(A-D)(A^2+AD)\), while \(A^2\notin J\): in degree eight,
membership would express \(A^2\) as a scalar combination of
\(D^2,A^2+AD\), contrary to their independence for coprime \(A,D\).
This control works in every characteristic; it is not a construction
supported on \(C_0\).

## Where a characteristic-sensitive obstruction could occur

For a single mate on \(X\), sole support forces its normalized equation
to be a scalar multiple of \(\phi^N\). Descent to
\(k[s^4,st^3,t^4,z]\) fails in characteristic zero because the
coefficient \(-N s^3t\) is missing from the semigroup ring.
Frobenius can remove that coefficient in positive characteristic.
The [exact criterion](../arithmetic/positive_characteristic_constructions.md#exact-semigroup-and-characteristic-criteria)
is \(p^{v_p(N)}\in\langle3,4\rangle\).
For two unrestricted equations, each may have residual factors; this
rank-one descent argument does not automatically constrain their full
relation module and its normal extensions.
The control above displays the arithmetic directly: in characteristic
three, \(z^2+zh+h^2=(z-h)^2\), so \(\nu^*c=\phi^3\), and
\((A,c)\) is the known supported presentation.

Identity (2) also gives a matrix with determinant \(A^N\),
\(\left(\begin{smallmatrix}F&-Q\\G&P\end{smallmatrix}\right)\).
Its adjugate gives a matrix factorization. This is the same construction
already used for the [multiple quadric](../carriers/finite_pullback_and_matrix_obstructions.md#double-quadric-matrices-and-punctual-defects),
where a control disproves automatic splitting into determinant-\(q\)
factors. Producing (2) or its matrix alone is an exact reformulation,
not an obstruction.

There is a concrete degree target: in characteristic zero a hypothetical
sole-support pair with \(a\le b\) must have \(4N>b\) for every certificate
(2), taking its coefficients homogeneous. Neither equation can have
\(A\) as a factor, since the resulting
subpair on \(X\) would have sole support \(C\), which is excluded.
If \(4N<b\), homogeneity in (2) forces \(Q=0\), hence \(F\mid A^N\),
impossible since \(A\) is irreducible and \(A\nmid F\).
If \(4N=b\), \(Q\) is a nonzero constant and
\((F,G)=(F,A^N)\), again giving the excluded mate on \(X\).
Thus a sufficiently low-degree reconstructed power would be decisive;
no universal upper bound of this strength is proved.

The open target is to determine which restricted pairs, their relation
modules and homogeneous normal corrections can give a proper CI with
nilpotent \(A\) and no residual support. A useful characteristic-zero
theorem would show that every such lift forces a descent or extension
condition that fails, while identifying precisely why Frobenius avoids it.
Neither the ordinary restriction nor the first annihilator currently
supplies that theorem. This connects fixed-carrier semigroup descent to
the [actual-source lifting problem](../equations/global_lifting_interfaces.md#a-fixed-symbol-lifting-lemma)
without identifying their obstruction spaces or asserting universal
coverage for a chosen finite-degree source.

## Comparing multiplicities on one fixed carrier

Let \(T=V(F_a)\) be integral and regular at the generic points of
distinct curves \(C_i\). Take actual proper mates \(G_j\) of degrees
\(b_j\) with all intersection cycles supported on the \(C_i\), and let
their multiplicity vectors be \(v_j=(n_{ij})_i\), allowing zero entries.
Every nonzero nonnegative vector in the integer span of the \(v_j\)
is realized by another mate on the same carrier. In fact, for
\(v=\sum z_jv_j\ge0\), the rational section
\[
S_v=\prod_j (G_j|_T)^{z_j}
\]
has degree \(\sum_j z_j b_j>0\) by the cycle degree identity. At the
generic point of \(C_i\), its order is \(v_i\) in a discrete valuation
ring. At every other codimension-one point each \(G_j\) is a unit upon
trivializing its line bundle. Thus \(S_v\) is regular in codimension one,
extends on the \(S_2\) surface, and lifts to an ambient form by the
hypersurface restriction sequence. The lifted pair is proper and pure
with exactly the prescribed cycle. If \(v=0\), the ratio has degree
zero and both it and its inverse extend, so it is constant.
This argument permits nonnormality away from the supported generic
points. The extension across codimension two is the standard
\(S_2\) generalized-divisor/reflexive-sheaf mechanism; see Hartshorne,
[*Generalized Divisors and Biliaison*](https://arxiv.org/abs/math/0301162).
The project-specific content is that actual mate equations supply the
seed rational sections and the hypersurface restriction sequence lifts
the resulting regular section back to an ambient homogeneous form.

In particular, define \(M_T\subset\mathbf Z_{\ge0}^r\)
to be the multiplicity vectors of **actual
homogeneous mates** whose entire intersection
cycle is supported on the indicated curves,
together with zero. The rational-product argument
establishes the saturated-monoid identity
\[
 \boxed{\quad M_T=
 \operatorname{gp}(M_T)\cap\mathbf Z_{\ge0}^r.\quad} \tag{MON}
\]
Indeed a nonzero vector in this intersection
is a nonnegative integer combination of
actual mate vectors, allowing negative
exponents. The resulting rational section has
nonnegative valuations at every codimension-one
point, extends by \(S_2\), and lifts through the
hypersurface restriction sequence; its degree
is positive by the cycle-degree identity.
This is **saturation in the lattice generated by
existing actual mates**, not saturation in all
\(\mathbf Z^r\) and not realizability of every
abstract Weil-divisor relation. The latter
would still need descent of a seed section
through the normalization conductor and a
global equation lift, as emphasized by the
[carrier-normalization framework](../../frameworks/carrier-normalization/index.md).
Once actual seed equations exist, the
conductor-descent obstruction has already
been passed for their rational products.
For a retained exceptional quartic carrier,
the all-mate theorem gives precisely
\(M_T=2\mathbf Z_{\ge0}(1,1)\);
hence \(\operatorname{gp}(M_T)=2\mathbf Z(1,1)\),
rather than the full diagonal lattice.
The nodal even-eight class supplies a
different explanation for that parity
**only on the normal nodal members**.

With just two curves, two nonproportional multiplicity vectors give
positive multiples of both coordinate vectors by integer subtraction.
Thus they yield actual sole-support mates for the two curves on the
same carrier. If an ambient symmetry preserves \(T\) and exchanges the
two curves, a single mate with unequal multiplicities suffices.

The [retained exceptional quartic](quartic_exceptional_carrier_geometry.md#all-mate-degrees-on-a-retained-exceptional-carrier)
exhibits the opposite outcome. Unequal multiplicities would contradict
the all-mate quartic-carrier exclusion, and the absence of a common
quadric rules out an odd common multiplicity.

### Normal carriers: a complete geometric description of the arrangement monoid

The seed theorem above does not need normality. On a normal integral
degree-\(a\) hypersurface \(T\), however, the entire monoid can be
described **without finding seed mates first**. This is a direct
application of the classical Hodge index theorem, Mumford's
intersection theory on normal surfaces (see [Kollár, *Minimal models
and their singularities*, §11.57](https://web.math.princeton.edu/~kollar/FromMyHomePage/modbook-final.pdf)),
and the [complete-intersection Picard saturation theorem](../carriers/normal_carrier_divisor_geometry.md#3-exact-exponent-and-minimal-mate-once-the-boundary-is-reached).

Let \(C_1,\ldots,C_s\) be distinct integral curves of degrees \(e_i\)
on \(T\). In arbitrary characteristic define \(C_i\cdot C_j\) via
Mumford's numerical pullback to a resolution, even if individual
curves are not Q-Cartier. Set
\[
 Q_{ij}=C_i\cdot C_j-\frac{e_i e_j}{a},\qquad
 D(n)=\sum_i n_i C_i.
\]
Then \(Q\) is a rational negative-semidefinite matrix. Indeed it is
the Gram matrix of the numerical pullbacks projected perpendicular
to the positive-square hyperplane class. Hodge index identifies
\(\ker Q\) with the vectors whose numerical pullback is numerically
proportional to the pulled-back hyperplane class.

The exact multiplicity monoid is
\[
 \boxed{\quad M_T=\{n\in\mathbf Z_{\ge0}^s:\ Qn=0,\
                D(n)\text{ Cartier on }T\}.\quad} \tag{HM}
\]
Necessity follows from the actual divisor of a mate. Conversely, if
\(n\ne0\) satisfies the two conditions, the numerical class of
\(D(n)\) is \((\sum_i e_i n_i/a)H\). Clearing the denominator gives
a numerically trivial Cartier difference, hence a trivial line
bundle by Cotner–Zavyalov, Theorem 1.1.8. Česnavičius–Scholze,
Corollary 7.2.3, then gives that \(D(n)\) itself is linearly
equivalent to an integral hyperplane multiple. Its canonical
section lifts by the hypersurface restriction sequence. This
realizes \(n\), including the exact mate degree
\[
 b=\frac{\sum_i e_i n_i}{a}.
\]
Normality ensures the effective Cartier section has no additional
components invisible to its divisor. No separate degree integrality
or global torsion test is needed.

The Cartier condition in (HM) is imposed on the **total** divisor;
individual curve classes may cancel at common singular points.
Numerical pullback alone does not imply Q-Cartierness. If every
\(C_i\) is Q-Cartier, the monoid's rational cone is exactly
\(\ker Q\cap\mathbf R_{\ge0}^s\): every rational vector in this cone
has a positive integer multiple realizing a mate. Even without
individual Q-Cartierness, (HM) remains exact at integral vectors
whose total divisor is Cartier. Thus the two tests are genuinely
different: Hodge geometry determines possible multiplicity
directions and the local class-group conditions determine the
integral lattice.

For two curves with positive individual Hodge gaps
\(\Gamma_i=e_i^2/a-C_i^2\), a positive ray in \(\ker Q\) forces
\(Q_{12}=\sqrt{\Gamma_1\Gamma_2}>0\) and
\(n_1/n_2=\sqrt{\Gamma_2/\Gamma_1}\).
In particular unequal multiplicities require unequal gaps.
If an automorphism exchanges two such curves, the gaps agree and
the only possible positive ray is diagonal, independently of the
normal-carrier exclusion theorem. This is the numerical mechanism
behind the seed-monoid argument, not a sufficient test of
realizability until Cartierness is checked. The [exceptional nodal
quartic](quartic_exceptional_carrier_geometry.md#the-hodge-matrix-of-the-exceptional-carrier)
is an explicit worked example.

The same Gram formalism explains what happens for residual
absorption on a **fixed normal** carrier. For an actual divisor
\(mC+D\sim bH\), assume C is Q-Cartier, put
\(d=\deg D\) and \(\Gamma=e^2/a-C^2\). Then
\[
 C\cdot D=ed/a+m\Gamma,\qquad D^2=d^2/a-m^2\Gamma .
\]
These follow by projecting the divisor relation perpendicular to
\(H\). A positive gap must be compensated by residual contact.
This is an identity, not a new lower bound on residual degree
without an independent upper bound on contact. It gives a precise
comparison target for the residual-capacity framework.

**Review status:** the exact monoid characterization and its
consequences are new deductions from the cited classical inputs;
independent reconstruction is recorded in the scoped review above. The original seed theorem on
generically regular integral, possibly nonnormal carriers is
preserved above.

**Nonnormal extension with no seed mates.** The [normalized Hodge matrix and downstairs almost-Cartier theorem AC1](../carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) drops normality from the exact monoid characterization whenever the carrier is regular at the marked generic points: replace the intersection matrix by that of the strict transforms on the normalization, and impose actual local almost-Cartier relations downstairs. This is stronger than the seed monoid but retains exactly the local conductor obstruction; it cannot be applied to reduced branches supported generically in the singular locus. This extension is included in the scoped correctness review above.

### Symmetry and the multiplicity lattice

The preceding argument has a useful finite-group form. Suppose a
finite group \(\mathcal G\) preserves an integral \(S_2\) carrier \(T\),
permutes the supported curves \(C_1,\ldots,C_r\), and \(T\) is regular
at their generic points. An actual mate with multiplicity vector
\(v\in\mathbf Z_{\ge0}^r\) produces mates with all vectors in the
\(\mathcal G\)-orbit of \(v\). By taking rational products and
extending across codimension two as above, **every nonzero,
nonnegative vector in the integer lattice generated by this orbit**
is an actual mate vector. In particular, if the lattice contains
a positive multiple of a coordinate vector, that curve is a
set-theoretic complete intersection with a mate on \(T\).
This is a consequence of the existing rational-section argument,
not a general statement about arbitrary surface cycles.

For two curves interchanged by an involution, let a degree-\(b\)
mate have multiplicity vector \((m,n)\) with \(m>n>0\), and put
\(g=\gcd(m,n)\). The orbit lattice is generated by
\((m,n)\) and \((n,m)\). Its first intersection with the positive
first-coordinate ray is
\[
 \frac{m}{g}(m,n)-\frac{n}{g}(n,m)
   =\left(\frac{m^2-n^2}{g},0\right). \tag{L}
\]
Indeed every integral relation \(An+Bm=0\) has
\((A,B)=t(m/g,-n/g)\). Hence the **smallest positive mate degree
obtained from this two-vector orbit lattice** is
\[
 \boxed{\ b_{\mathrm{orbit}}=\frac{b(m-n)}{g}.\ } \tag{L1}
\]
This is not asserted to be the smallest possible mate degree from
unrelated constructions. The older determinant
\(m^2-n^2\) is the unnormalized version of the same lattice argument.

More generally, if a cyclic group of prime order \(p\) permutes
\(p\) supported curves transitively and a mate has a nonconstant
multiplicity vector \(v=(n_0,\ldots,n_{p-1})\), then the cyclic
translates of \(v\) span \(\mathbf Q^p\). To see this, put
\(f(t)=\sum_{i=0}^{p-1}n_it^i\). The circulant eigenvalues are
\(f(1)\) and \(f(\zeta^j)\), \(1\le j<p\). Here \(f(1)>0\);
if \(f(\zeta^j)=0\), irreducibility of
\(\Phi_p=1+t+\cdots+t^{p-1}\) over \(\mathbf Q\) forces
all \(n_i\) to be equal, contrary to hypothesis. Thus the integral
orbit lattice has finite index in \(\mathbf Z^p\) and contains a
positive multiple of every coordinate vector. Under the same
\(S_2\), generic-regularity and ambient lifting hypotheses, every
supported component therefore has a sole-support mate. This is only
a lattice corollary; it does not assert that such cyclic arrangements
exist.

On a normal surface the underlying divisor relation is
\(bH\sim\sum_i n_i C_i\) in \(\operatorname{Cl}(T)\);
the \(S_2\) extension argument is stronger because it does **not**
require normality at every other codimension-one point.

### Reverse application: single-curve exclusions constrain multi-curve Chow cycles

The fixed-carrier monoid theorem above is commonly used
**forwards**, to construct new mate vectors from known ones.
For the degree-exclusion program it should also be
used **backwards**: a proved impossibility of a sole-support
mate constrains every *multi-support* mate on the
**same carrier**.

Let \(T=V(F_a)\) be an integral hypersurface,
regular at the generic points of distinct curves
\(C_1,C_2\). Suppose an all-mate theorem excludes
the singleton \(C_1\) on \(T\).
Then the actual supported-mate vectors in
\(\mathbf Z_{\ge0}^2\) lie on a **single rational ray**.
Indeed, two nonproportional vectors would generate,
by integer subtraction and the \(S_2\) extension
argument, a nonzero positive multiple of \((1,0)\)
and hence a forbidden actual sole-support mate
on \(C_1\). This is independent of the
mate degrees.

**Complete quartic-carrier application.**
For every integral **quartic** \(T\) containing
distinct projective translates \(C_i\) of the
fixed \(C_0\), the unique-quadric restriction
shows that \(T\) has generic normal order
one along *each* \(C_i\): order two would
force \((4,4)-2(1,3)=(2,-2)\) effective
on that translate's unique quadric.
Thus the generic-regularity hypothesis
of the monoid theorem is automatic. The
accepted [all-degree-mate quartic
exclusion](../../results/quartic_carrier_exclusion.md)
applies to every projective translate.
Consequently:

* For **two translates**, every supported
  actual mate multiplicity vector is
  proportional to a single ray; in
  particular the cycle-realization
  monoid has rank at most one.
* If an involution of the quartic carrier
  exchanges the two translates, all such
  vectors are **diagonal** \((m,m)\).
  The retained exceptional \((2,2)\)
  cycle is an example, not the theorem's
  only possible numerical configuration.
* If a prime cyclic group of order \(p\)
  preserves \(T\) and permutes \(p\)
  distinct translates transitively,
  **every** actual supported mate has
  equal multiplicities \(m\) on all
  \(p\) components. Otherwise the
  prime-orbit lattice proved above
  would supply a forbidden singleton.
  Degree comparison then forces
  \[
    4b=\deg(T)\,b=4pm,
    \qquad \boxed{b=pm}.                    \tag{OR1}
  \]
  This is **conditional on existence of
  such a symmetric carrier and supported
  mate**; it does not assert that
  such arrangements exist.

**All-degree normal-carrier variant.**
Replace quartic \(T\) by any normal integral
degree-\(a\) carrier with a supported set
of projective translates. If one component
has actual on-curve Cartier indices at
most four, the
[all-degree normal-index theorem](../carriers/normal_carrier_symbolic_torsion.md#5-closing-the-entire-actual-index-at-most-four-class)
excludes its sole-support mate. For two
components the supported-mate monoid
again has rank at most one; under a prime
cyclic symmetry, all translates have
the same index conditions and every
mate vector is uniform. This is a
**new consequence of existing theorems**,
not a fresh normal-index classification.

This is the direct connection to the
[Chow-polytope realization work](../../results/quartic_chow_pencil_classification.md):
the single-orbit STCI exclusion, a
multi-support lattice theorem, and
the exceptional \((4,4)\) orbit are
different views of the same actual
equation-realization constraint.
The general multiplicity-lattice theorem
controls the **fiber of actual equations
over a fixed carrier**. It does **not**
classify the carriers or Chow cycles
themselves, and for a composite
group a nonconstant orbit vector may
span a proper rational subrepresentation,
so the prime-order conclusion
must not be asserted without its
irreducibility hypothesis.

### A two-translate sextic construction criterion

In characteristic zero let \(\sigma\) be \(x_3\mapsto -x_3\), which
exchanges \(C_{1,\pm1}\). If a proper \((6,6)\) pair with one
\(\sigma\)-preserved carrier has cycle supported on these two
translates, then \(C_0\) is an STCI. Any such carrier is integral
and regular at the generic points that occur, as verified below.
If only one translate occurs, the pair itself gives the conclusion
after diagonal transport. If both occur, their multiplicities sum to
nine, so they are unequal. With \(n_+>n_->0\), put
\(g=\gcd(n_+,n_-)\). The primitive orbit-lattice ratio
\[
 \frac{G^{n_+/g}}{(\sigma G)^{n_-/g}}
\]
extends to a sole-support mate of degree
\[
 6\frac{n_+-n_-}{g},
\]
with cycle
\[
 \frac{n_+^2-n_-^2}{g}[C_{1,1}].
\]
Exchanging signs gives the corresponding mate on the other curve.
Thus the three surviving positive partitions would imply
\[
\begin{array}{c|c|c}
(n_+,n_-)&\text{sole-support multiplicity}&\text{mate degree}\\ \hline
(6,3)&9&6\\
(7,2)&45&30\\
(8,1)&63&42
\end{array}
\]
and reversals give the same degrees. In particular, a hypothetical
\((6,6)\) pair with partition \((6,3)\) would produce an actual
\((6,6)\) STCI of the rational quartic, not merely a higher-degree
mate. The degree here is minimal only inside the integer lattice
generated by the mate and its involution translate.

A necessary involution bound below excludes the partition
\((5,4)\), so no conclusion is drawn from that partition.
The permitted positive two-support partitions are narrowed to
\((6,3),(7,2),(8,1)\) and their reversals. Existence of these
remaining pairs is open.

Every irreducible factor of either sextic has even degree, since its
intersection with the mate has degree six times that factor degree
and consists of quartic curves. A reducible sextic or a proper power
would have a quadratic factor. This would be the unique smooth quadric
of a translate, and a sum of translated curves on it cannot have
ruling class \((6,6)\). This proves integrality, also for arbitrary
translated support in \((6,6)\).

If the \(\sigma\)-preserved carrier were singular along one translate,
it would be singular along both. The degree-six forms vanishing to
order at least two along both are precisely the span of \(A^2,AB,B^2\)
with the cubics \(A,B\) from the
[exceptional quartic pencil](quartic_chow_pencils.md#classification).
The description follows from the first-normal map and the
Hilbert--Burch presentation of the reduced union. Put \(Y=C_+\cup C_-\) and
\(L=V(x_1,x_2)\). Its
[Hilbert--Burch resolution](quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
gives
\[
 I_Y=(A,B,D),\quad I_Y(3)=kA\oplus kB,\quad
 I_Y(4)=AS_1\oplus BS_1\oplus kD.
\]
In particular, the image of \(I_Y(4)\) on the coordinate
line \(L\), which meets \(Y\) only at the two endpoints, is
the **one-dimensional** space
\(k\,x_0^2x_3^2\), since \(A|_L=B|_L=0\) and
\(D|_L=-x_0^2x_3^2\). The two degree-five
Hilbert--Burch syzygies are
\[
 x_1D=x_2^2A+x_0^2B,\qquad
 x_2D=x_3^2A+x_1^2B. \tag{A}
\]

Let \(H\in S_6\) vanish to order at least two at the generic
points of **both** components of \(Y\). Since it vanishes
on \(Y\), write
\[
 H=A U+B V+D W,\qquad U,V\in S_3,\quad W\in S_2.
\]
At either generic point, \(A,B\) are regular transverse
parameters. The vanishing of the first normal class of \(H\),
combined with (A), forces all four quartics
\[
 x_1U+x_2^2W,\quad x_1V+x_0^2W,\quad
 x_2U+x_3^2W,\quad x_2V+x_1^2W
\]
to lie in \(I_Y(4)\): each is the coefficient of a
regular transverse parameter after multiplication of
the first normal class by \(x_1\) or \(x_2\).
Restrict the **second** and **third** of these quartics
to \(L\). The one-dimensional restriction image gives
\[
 x_0^2 W|_L\in k\,x_0^2x_3^2,\qquad
 x_3^2 W|_L\in k\,x_0^2x_3^2.
\]
Therefore \(W|_L\) is at once a multiple of \(x_3^2\)
and of \(x_0^2\), so \(W|_L=0\).
Thus \(W\in(x_1,x_2)_2\), and (A) eliminates the \(DW\)
term, writing \(H=AU'+BV'\) with
\(U',V'\in S_3\). The vanishing of its first normal class
and the generic independence of \(A,B\) imply
\(U',V'\in I_Y(3)=kA+kB\). Consequently
\[
 \boxed{\
 \{H\in S_6:\operatorname{ord}_{C_\pm}H\ge2\}
        =\operatorname{Sym}^2(kA\oplus kB)
        =\langle A^2,AB,B^2\rangle .\ } \tag{B}
\]
The first-normal equations and restriction to \(L\)
therefore determine the entire sextic space.
Every nonzero member of (B) factors as a quadratic in
the two cubics \(A,B\) over an algebraically closed field,
and hence cannot define an integral sextic. This establishes the regularity required by the ratio argument.

### Involution--Bezout bound and the remaining sextic locus

The symmetry provides a useful degree-independent necessary
inequality **under generic regularity**. Work in characteristic
different from two. Suppose \(T=V(F_a)\) is integral,
\(\sigma\)-preserved, **and regular at the generic points of
both \(C_+\) and \(C_-\)**; assume that \((T,G_b)\) is proper,
with full cycle \(n_+C_++n_-C_-\), \(n_+\ne n_-\).
An irreducible
\(\sigma\)-eigen equation for \(T\) must be **even** in \(x_3\):
an anti-invariant polynomial would have \(x_3\) as a factor.
Set \(q=\min(n_+,n_-)\). Then
\[
 G_b-\sigma G_b=x_3H_{b-1}.
\]
Since the multiplicities differ, \(H_{b-1}\ne0\).
At the generic point of each curve, the local ring
\(\mathcal O_{T,\eta_{C_\pm}}\) is a **DVR by the generic
regularity hypothesis**. The coordinate \(x_3\) is a unit
there, and \(G_b|_T\) and \((\sigma G_b)|_T\)
have valuations \(n_+,n_-\) in opposite order.
Because these valuations differ, the DVR valuation of
their difference is exactly \(q\). Hence
\(H_{b-1}|_T\) has order \(q\) on **both** curves.

Moreover \(H_{b-1}|_T\ne0\): if it vanished, the two
sections would agree on \(T\), contradicting their
unequal generic valuations. Since \(T\) is an integral
hypersurface, it is not a component of \(V(H_{b-1})\).
The proper divisor intersection has degree \(a(b-1)\),
and its curve multiplicities are at least \(q\)
at \(C_+\) and \(C_-\). Bézout therefore gives
\[
 a(b-1)=\deg(T\cap H_{b-1})\ge8q.
\]
As \(n_++n_-=ab/4\), this is equivalent to
\[
 \boxed{\,4|n_+-n_-|\ge a.\,} \tag{6}
\]
For \((a,b)=(6,6)\), the sum is nine; among positive
two-support partitions (6) removes \((5,4)\), leaving
\((6,3),(7,2),(8,1)\) and the reversals.
A one-support pair would already solve STCI and is not
claimed to be excluded by this inequality.

**Scope of the inequality.** The condition that \(T\) be
integral does **not** imply that its codimension-one local
rings are DVRs. If \(T\) is singular at the generic point of
a supported curve, the local intersection length is not
a discrete valuation; in particular, the length of the
difference of two sections need not equal the minimum of
their lengths. Thus the degree-independent inequality is
**not proved without generic regularity**. In the
\((6,6)\) application, however, integrality was established
above and the Hilbert--Burch/first-normal argument (B)
shows that an integral \(\sigma\)-invariant sextic **cannot**
be singular generically along either \(C_+\) or \(C_-\)
(the involution exchanges the curves). Hence the DVR
hypothesis is satisfied for the sextic sector, and its
\((5,4)\) exclusion is unaffected.

The singularities of a surviving carrier cannot be ignored.
If a \(\sigma\)-preserved sextic were smooth along both curves,
the rational function \(G_b/\sigma G_b\) would make their
classes numerically equivalent, whereas adjunction gives
\(C_\pm^2=-2-(6-4)\deg C_\pm=-10\),
contradicting the nonnegative intersection of distinct curves
on a smooth surface along their support. Thus a viable
two-support sextic must be singular somewhere on these curves
(while remaining generically regular as proved above).

### Nodal sextic obstruction

**Proposition (nodal-carrier exclusion).** There is no
\(\sigma\)-preserved integral sextic with only ordinary
nodes supporting a proper \((6,6)\) intersection of
unequal multiplicities on \(C_+\) and \(C_-\).

To prove the proposition, suppose \(T\) is normal and
its singularities are all ordinary double points (\(A_1\)). The difference
\(\Delta=n_+-n_-\in\{3,5,7,-3,-5,-7\}\)
is odd, and
\[
  \operatorname{div}_T(G_b/\sigma G_b)
       =\Delta(C_+-C_-).
\]
At a node the local class group is \(\mathbf Z/2\).
A smooth branch through that singularity is non-Cartier:
if it were locally \((f)\), its local ring \(R/(f)\) would
be regular of dimension one, impossible for the singular
surface local ring of embedding dimension three.
Thus a node lying on just one of \(C_+,C_-\) violates the
odd principal relation. Their only common points are
\(p_0,p_\infty\); at a common node the fractional
exceptional corrections \(E/2\) to their pullbacks agree.
On the minimal resolution \(\pi:X\to T\), therefore,
\(\Delta(\Gamma_+-\Gamma_-)\sim0\).
Because the resolution is crepant,
\(K_X=2h\) with \(h=\pi^*H\), and the strict transforms
are smooth rational quartics, so
\[
 \Gamma_\pm^2=-2-K_X\cdot\Gamma_\pm=-10.
\]
Numerical equivalence would give
\(\Gamma_+\cdot\Gamma_-=-10\), impossible for distinct
effective curves on smooth \(X\).
**No \(\sigma\)-preserved integral \((6,6)\) carrier
with only \(A_1\) singularities realizes an unequal
two-support partition.**
This says nothing about higher ADE or non-Du-Val
singularities.

### Local index lattice and contact capacity of symmetric arrangements

**Status: new deductions, covered by the scoped correctness review above.** The
localization of the actual mate lattice gives more than the global
singleton construction. At a point \(P\) on a generically regular
integral carrier, each actual mate vector \(v\) yields
\(\sum_i v_i[C_i]_P=0\) in the local almost-Cartier group. Project the
lattice of these vectors onto the coordinates of curves through \(P\);
the homomorphism from the free coordinate lattice to the local
almost-Cartier group factors through its quotient by the projected
mate lattice. In particular, at a point on just \(C_i\), its actual
local class order divides the **gcd of all the available \(i\)-th mate
multiplicities**. This uses both effective mates, not only their
difference. The assertion includes nonnormal carriers regular at all
marked generic points by the [almost-Cartier theorem AC1](../carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices).

For an involution exchanging two curves, with an unequal positive
mate vector \((p,q)\), put
\[
 g=\gcd(p,q),\qquad N=p+q,\quad \Delta=|p-q|,\qquad J=N\Delta/g .
\]
The Smith invariants of the orbit lattice are \(g,J\): the gcd of
its entries is \(g\) and its determinant has absolute value \(N\Delta\).
Thus every local index of either curve divides \(J\), and at points
off the common support it divides \(g\). If \(g=1\), the carrier
is smooth along both smooth curves away from their intersections.
Indeed an index-one reduced curve Cartier divisor is pure and
generically reduced, hence reduced, and a regular quotient by one
equation forces the local surface to be regular.

Now assume characteristic zero, both curves are smooth and projectively
equivalent of degree \(e\) and genus \(g_C\), and every common point is
fixed by the involution. Assume \(N\) odd, and that at the common points
the carrier is smooth or Du Val. No ADE assumption is made elsewhere.
Write \(L_P=\ell_k(\mathcal O_{\mathbf P^3,P}/(I_{C_+,P}+I_{C_-,P}))\)
for the actual scheme intersection length and \(L=\sum L_P\).

**Local contact bound.** Write \(A_{\pm,P}\) for the first-normal
vanishing orders of the carrier along the two smooth curves.
They are equal at a common fixed point, since the restricted Jacobian
ideal of a hypersurface is intrinsic and the involution exchanges the
curves. Denote their common value by \(A_P\). We claim \(A_P\le L_P\).

Every local class order is odd because \(J\) is odd. At a singular
common point the class of a smooth curve is nonzero, so by the
standard ADE class groups only \(A_j\) and \(E_6\) are possible.
For \(A_{M-1}\) use completed coordinates \(xy=z^M\). The first-normal
order is the minimum of the restrictions of \(x,y,z^{M-1}\).
If \(A_P=1\) the bound is immediate; if \(A_P\ge2\), then \(z\)
is a uniformizer on both curves by smoothness and \(\operatorname{ord}x,
\operatorname{ord}y\ge A_P\) on both. Write each curve as its graph
over \(z\); both differences in the graph coordinates vanish to order
at least \(A_P\), giving \(L_P\ge A_P\). For \(E_6\),
\(x^2+y^3+z^4=0\), a smooth branch must have \(z\) a uniformizer,
\(y\) of order at least two, and \(x\) of order exactly two
(compare lowest orders in the equation). The restricted gradient
has order two, and any two such graph branches have intersection
length at least two. Smooth carrier points have \(A_P=0\).
This is a joint-branch use of the standard analytic ADE forms;
for the single-branch first-symbol and exceptional correction
formulas see [Ellia, Definitions 6 and 8, Lemmas 9--10](https://arxiv.org/abs/1409.3801).

**All-degree capacity inequality.** The orbit lattice gives an
actual singleton mate on this same carrier for each curve. Let
\(a=\deg T\), let \(\ell\) be the degree of the dual of its saturated
first free conormal line along \(C_+\), and let \(\eta\) bound the
degrees of line subbundles of its ambient normal bundle. Put
\(\nu_C=4e+2g_C-2=\deg N_{C/\mathbf P^3}\). By the
[exact almost-Cartier local budget](../carriers/normal_index_socle_and_torsion.md#intrinsic-divisor-on-a-possibly-nonnormal-generically-regular-carrier)
(using the reviewed normal theorem if \(T\) is normal),
\[
 \deg A=ea-\nu_C+\ell,\qquad
 \ell-e^2/a=\sum_P\frac{A_P+D_{r_P,P}}{r_P}.
\]
Here \(r_P\) is the true downstairs almost-Cartier index,
\(D_{r_P,P}\ge0\), and \(\ell\le\eta\). Off the common points
\(r_P\le g\), at common points \(r_P\le J\), and the sum of their
first-symbol coefficients is at most \(L\). Since \(J\ge g\),
\[
 g(\ell-e^2/a)\ge ea-\nu_C+\ell-(1-g/J)L .
\]
Consequently every such symmetric arrangement satisfies
\[
 \boxed{\quad ea-\nu_C+g e^2/a
       \ \le\ (g-1)\eta+(1-g/J)L. \quad} \tag{SC}
\]
This is a degree-independent, contact-sensitive obstruction,
not a bound on ADE rank. The local class lattice identifies where
a low-index budget must be paid; actual shared curve contact limits
how much first-symbol vanishing can concentrate there.
It extends to possibly nonnormal generically regular carriers using
the almost-Cartier power theorem. No conclusion is asserted when a
common point is not smooth or Du Val, nor without the actual orbit
mates or the stated oddness and fixed-point conditions.

For \(C_\pm=C_{1,\pm1}\), the common endpoints have contact length
four each: on either reversed affine chart the cubic graph
coordinates agree and the quartic graph coordinates differ in
order four. Thus \(L=8\), \(e=4,\ \nu_C=14,\ \eta=7\), and (SC) gives
\[
 4a-7+16g/a-7g\le (1-g/J)8.                 \tag{SC4}
\]
In particular **every coprime unequal positive multiplicity
partition of odd total on a degree-\(a\ge5\) symmetric carrier
requires a non-Du-Val singularity at a common endpoint** (a
nonnormal endpoint also lies outside the ADE regime).
For \(g=1\) the left side is \(4a-14+16/a>8\).
The criterion depends on actual multiplicity relations and
contact, not on the mate degree or a classification of carriers.

### The sextic symmetric arrangement must escape ADE at an endpoint

The entire \((6,6)\) symmetric two-translate problem, not just
the ordinary nodal sector, is outside the regime where both
endpoints are smooth or Du Val. This follows from (SC4) together
with one additional **mixed** Hodge-matrix comparison.

The existing Hilbert--Burch argument proves integrality and generic
regularity along both curves. Of the three surviving partitions,
\((7,2),(8,1)\) have \(g=1\), already excluded by (SC4).
For \((6,3)\) one has \(g=3,J=9\); the orbit ratio gives an actual
sextic mate cutting \(9C_+\). Suppose both endpoints are smooth or
Du Val. The refined inequality before substituting \(\ell\le7\)
gives
\[
 2\ell\ge 10+8-(1-3/9)8=38/3,
\]
so \(\ell=7\). Thus \(\deg A=17\) and the exact local budget is
\(E=13/3\). Let \(U\) denote the sum of first-normal coefficients
at the common points with index nine. All other indices are at
most three, and
\[
 13/3\ \ge\ (17-U)/3+U/9,\qquad U\ge6.       \tag{8}
\]
Since each endpoint contributes at most four, **both** endpoints
have actual index nine, and each has an \(A_{M-1}\) singularity
with \(M\ge9\).

At an index-nine endpoint the involution lifts to the minimal
resolution of the \(A_{M-1}\) germ and acts on its exceptional chain
either trivially or by reversal. The latter inverts the local class,
whereas \(3([C_+]-[C_-])=0\) from the two actual mates. Inversion
would give \(6[C_+]=0\), impossible for index nine. Hence the
two curves meet the **same marked component** of the chain,
and their rational exceptional corrections \(Z_{+,P},Z_{-,P}\)
are equal. Let \(k=\min(j,M-j)\) for the marked component \(E_j\).
Ellia Lemmas 9--10 give \(k=A_P\le4\) and
\[
 -Z_{+,P}\cdot Z_{-,P}=k(M-k)/M
                 \ge (5/9) A_P .
\]

On the normalization of the carrier the full inverse of each
curve is its singleton degree-one strict transform, by the actual
singleton mates. Those strict transforms are numerically \(2H/3\),
so their numerical mutual intersection is \(8/3\). Resolve the
normalization. The strict transforms of distinct effective curves
have nonnegative intersection, and their exceptional correction
vectors have overlap only over the two common endpoints. At these
points the original carrier is normal by assumption, so the
preceding ADE calculation is valid there. The numerical intersection
is therefore at least
\[
 \sum_{P=p_0,p_\infty}-Z_{+,P}\cdot Z_{-,P}
       \ge(5/9)U\ge10/3>8/3,
\]
a contradiction.

We conclude, **with the stated extensions independently reconstructed in the scoped review above**,
that an actual symmetric sextic two-translate arrangement would have
a common endpoint that is neither smooth nor Du Val. For a normal
carrier the proof uses the previously reviewed normal socle theorem
and the classical ADE marked formulas, so the new nonnormal extension
is not a premise of that sector's exclusion. Off the common endpoints
the proof does not require an ADE or even a normal surface.
In particular this closes all globally ADE symmetric sextic
carriers, while not excluding arbitrary asymmetric arrangements
or a symmetric carrier with a genuinely worse endpoint. It is
not a proof or disproof of STCI itself.

### ADE local classes and the global sextic correction budget

Work over an algebraically closed field of characteristic zero. Let
\(\sigma:x_3\mapsto-x_3\), let \(C_\pm=C_{1,\pm1}\), and let
\(T\subset\mathbf P^3\) be a \(\sigma\)-preserved **normal sextic with only
Du Val singularities**. Suppose \((T,G_6)\) is proper with cycle
\[
 n_+[C_+]+n_-[C_-],\qquad n_++n_-=9,\qquad n_+\ne n_-,
\]
and put
\[
 \Delta=n_+-n_-\in\{\pm3,\pm5,\pm7\}.
\]
Normality makes \(T\) regular at the generic points of \(C_\pm\), so the
generic-regularity hypothesis used in the involution--Bézout argument is
satisfied. The conclusions below are necessary conditions for this
normal/Du-Val sextic sector only.

The stronger [local lattice and contact argument above](#local-index-lattice-and-contact-capacity-of-symmetric-arrangements) now bounds the off-endpoint index by \(\gcd(n_+,n_-)\), not just the difference, and excludes the full ADE symmetric sextic sector (included in the scoped correctness review above). The earlier weaker difference calculation and its independent endpoint numerator argument follow for comparison.

At any singular point \(q\in C_+\setminus C_-\)
(or vice versa), the local class of the smooth branch
is nonzero and has order dividing \(|\Delta|\).
By the classical local class groups
\[
\begin{array}{c|c}
 A_n&\mathbf Z/(n+1)\\
 D_{2m}&(\mathbf Z/2)^2\\
 D_{2m+1}&\mathbf Z/4\\
 E_6&\mathbf Z/3\\
 E_7&\mathbf Z/2\\
 E_8&0
\end{array}
\]
only \(A_{3m-1}\) or \(E_6\) can occur off-endpoint for
\(\Delta=\pm3\); only \(A_{5m-1}\) for \(\Delta=\pm5\);
and only \(A_{7m-1}\) for \(\Delta=\pm7\).
These are **necessary local possibilities if such an off-endpoint
singularity occurs**, not existence assertions. At the common
endpoints the relevant local class is the anti-invariant
\([C_+]-[C_-]\), rather than either curve's class.
See [Lipman, *Rational singularities, with applications to
algebraic surfaces and unique factorization*](https://www.numdam.org/item/PMIHES_1969__36__195_0/),
for the established class-group theory.

The global divisor-class relations provide an additional sieve.
On the carrier
\[
 bH\sim n_+C_++n_-C_-,
 \qquad\Delta(C_+-C_-)\sim0.
\]
Tensoring with \(\mathbf Q\), and using \(n_++n_-=ab/4\),
gives \([C_+]=[C_-]=(4/a)[H]\).
For the sextic this reads \([C_\pm]=\tfrac23[H]\).
Let \(\pi:X\to T\) be the crepant minimal resolution,
\(h=\pi^*H\), and let
\(\pi^*C_\pm=\Gamma_\pm+Z_\pm\)
be the rational Cartier pullbacks, where each \(Z_\pm\)
is an exceptional \(\mathbf Q\)-cycle. The resolution pairing
satisfies \((\Gamma_\pm+Z_\pm)\cdot E_j=0\).
Because \(h^2=6\), \(K_X=2h\),
\(h\cdot\Gamma_\pm=4\), and
\(\Gamma_\pm^2=-10\), it follows that
\[
 (\pi^*C_\pm)^2=\frac83
     =\Gamma_\pm^2-Z_\pm^2,
 \qquad\boxed{\ -Z_+^2=-Z_-^2=\frac{38}{3}.\ } \tag{7}
\]

**Proposition (3-primary endpoint condition).**
Under the normal Du Val sextic hypotheses above,
if \(|\Delta|=5\) or \(7\), corresponding to
the partitions \((7,2)\) or \((8,1)\)
and their reversals, then **at least one**
of the common endpoints \(p_0,p_\infty\)
has a nontrivial 3-primary class of both
\(C_+\) and \(C_-\) in its local class group.
In particular, that endpoint singularity
must be of type \(A_{3m-1}\) or \(E_6\).
At **each** endpoint the 3-primary parts of
\([C_+]\) and \([C_-]\) agree.

For the proof, decompose \(Z_\pm\) over the
singular points. At an ADE point \(q\), the
exceptional root lattice \(R_q\) is integral
and negative definite, and the correction
\(Z_{\pm,q}\) lies in its dual \(R_q^\vee\).
If the corresponding local class has order
\(m_q\) in \(R_q^\vee/R_q\simeq
\operatorname{Cl}(\mathcal O_{T,q})\), then
\(m_q Z_{\pm,q}\in R_q\) and
\[
 m_q Z_{\pm,q}^2
  =(m_q Z_{\pm,q})\cdot Z_{\pm,q}
  \in\mathbf Z.
\]
Thus the denominator of the local
self-intersection divides \(m_q\).
At a singularity on exactly one of the
two curves, \(m_q\mid|\Delta|\)
by the principal relation
\(\Delta(C_+-C_-)\sim0\).
For \(|\Delta|=5,7\), all these off-endpoint
contributions have denominator prime to
three; singularities on neither curve
contribute zero. Since (7) has denominator
three, an endpoint contribution must have
denominator divisible by three, and its
local class has nontrivial 3-primary part.
Only \(A_{3m-1}\) and \(E_6\) have
3-torsion among Du Val class groups.
Finally, at either common endpoint
\(\Delta([C_+]-[C_-])=0\), and multiplication
by \(\Delta\) is an automorphism of any
3-primary group because \(3\nmid\Delta\).
The 3-primary classes therefore agree.

This is a **necessary endpoint restriction**,
not an exclusion or an existence theorem.
For \(|\Delta|=3\), off-endpoint
\(A_{3m-1}\) or \(E_6\) singularities
can already contribute denominator three,
so the same endpoint conclusion does not
follow.

The local inverse ADE intersection matrices determine the
contributions to these two budgets. They must be checked
**simultaneously** with the local anti-invariant class at the
endpoints and any off-endpoint odd-torsion singularities.
Equation (7) is a **necessary condition**, not an exclusion of
all Du Val sextic carriers or a new STCI theorem. Outside
the Du Val/Q-Cartier crepant setting, these numerical
identities have not been asserted.

