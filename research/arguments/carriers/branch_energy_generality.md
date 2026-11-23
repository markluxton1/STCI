# Branch energy, genus, and the location of index corrections

**Status.** These deductions were independently reconstructed from the
marked-ideal/Hodge-gap and actual Cartier-relation proofs during the
algebraic-geometry review. A distinct generalizations reviewer independently
reconstructed this written proof, including BG1–BG2 and BI1–BI2, on
November 23, 2026. The inputs and their characteristic restrictions remain those of
[numerical surface pullback](numerical_surface_pullback.md).

## A degree-and-genus criterion for positive branch energy

Work over an algebraically closed field of characteristic zero. Let \(C\subset\mathbf P^3\) be a smooth integral curve of degree \(d>0\)
and genus \(g\), and let \(X=V(F_a)\) be an integral carrier with generic
normal order \(p>0\) along \(C\). Use the normalization, smooth
principalizing model, branch vectors \(\mathbf e,\mathbf n\), normalized
Hodge matrix \(Q\), and exceptional principalization correction \(V\) of
[N4–N5](numerical_surface_pullback.md#exact-decomposition-of-the-first-graph-gap).
In particular, for an actual sole-support mate, \(\mathbf n\in\ker Q\).
Put
\[
 \lambda=4d+2g-2,\qquad
 \kappa=\frac{d^2p^2}{a}+ad-p\lambda.
\]

The elementary inequality
\[
 \boxed{\kappa\ \ge\
 p\bigl(2d\sqrt d-(4d+2g-2)\bigr)}
 \tag{BG1}
\]
follows from AM–GM applied to \(d^2p^2/a+ad\). Therefore
\[
 4d+2g-2<2d\sqrt d
 \tag{BG2}
\]
implies \(\kappa>0\) for every positive carrier degree \(a\) and order \(p\).
No splitting hypothesis on \(N_{C/\mathbf P^3}\) is used.

**No-vertical consequence.** Under (BG2), an integral carrier whose first
strict transform \(X'\to X\) has no vertical fibers cannot have an actual
sole-support mate with \(\mathbf n\) proportional to \(\mathbf e\).
In particular, it cannot have a mate if its normalization has only one
divisorial inverse branch above \(C\), regardless of that branch's
residue degree.

Indeed, absence of vertical fibers makes the proper birational map
\(X'\to X\) finite. The normalization then factors through \(X'\), so
the marked ideal becomes Cartier on the normalization and \(V=0\).
The actual mate gives \(Q\mathbf n=0\); proportionality gives
\(\mathbf e^tQ\mathbf e=0\). The exact identity
\[
 \kappa=-\mathbf e^tQ\mathbf e-V^2
\]
would then force \(\kappa=0\), contradicting (BG1)–(BG2). A singleton
branch makes the two positive one-entry vectors proportional automatically.
For several branches proportionality is an additional hypothesis.

Every smooth rational curve of degree \(d\ge3\) satisfies (BG2), since
\(4d-2<2d\sqrt d\). Thus the quartic no-vertical singleton exclusion is
part of a degree-and-genus phenomenon, rather than a consequence of its
balanced normal bundle.

**The strict inequality is essential.** For an elliptic quartic,
\(\lambda=16=2d\sqrt d\), and
\[
 \kappa=\frac{4(a-2p)^2}{a}.
\]
A smooth elliptic \((2,2)\) complete intersection on a smooth quadric
has \(a=2,p=1\), a singleton inverse branch and no vertical fibers, but
does have its other quadric as a sole-support mate. Here \(\kappa=0\).
Equality in (BG1)'s AM–GM step requires \(a=p\sqrt d\); no positivity
conclusion is asserted at that equality.

The argument has the same characteristic scope as the supplied
principalizing-model and intersection identities: in characteristic zero
these models are available; in other characteristics the statement is
conditional on the same model hypotheses recorded in the input owner.
This is an exclusion on a specified geometric carrier locus, not a
non-STCI theorem for every curve satisfying (BG2).

## Which index denominators must occur at shared branch points?

The following local statement is useful independently of the quartic.
Let \(S\) be a normal projective surface, let \(\Gamma_1,\Gamma_2\) be
distinct integral Q-Cartier curves, and suppose that the actual divisor
\[
 E=e_1\Gamma_1+e_2\Gamma_2,\qquad e_i>0,
 \tag{BI1}
\]
is Cartier. Write \(r_{i,P}\) for the local Cartier index of \(\Gamma_i\),
and put
\[
 R_i^{\mathrm{sh}}
 =\operatorname{lcm}_{P\in\Gamma_1\cap\Gamma_2} r_{i,P},
\]
with the empty lcm equal to one. Only singular points contribute
nontrivial indices. If \(s_i\) and \(t\) are the positive denominators
in lowest terms of \(\Gamma_i^2\) and \(\Gamma_1\cdot\Gamma_2\), then
\[
 \boxed{\quad
 s_i\mid\operatorname{lcm}(e_i,R_i^{\mathrm{sh}}),\qquad
 t\mid R_1^{\mathrm{sh}},\quad t\mid R_2^{\mathrm{sh}}.
 \quad}
 \tag{BI2}
\]

**Proof.** At a point of \(\Gamma_i\) outside the other curve, (BI1)
makes \(e_i\Gamma_i\) Cartier. Thus every local index away from the
shared support divides \(e_i\). The global Cartier index \(R_i\)
therefore divides \(\operatorname{lcm}(e_i,R_i^{\mathrm{sh}})\).
Since \((R_i\Gamma_i)\cdot\Gamma_i\) is the integral degree of a line
bundle on the integral projective curve, \(s_i\mid R_i\). This proves
the first assertion.

For the second assertion, \(R_i^{\mathrm{sh}}\Gamma_i\) is Cartier
on an open neighborhood of the opposite curve \(\Gamma_j\). At shared
points this is its definition; away from \(\Gamma_i\) the divisor is
zero. Its restriction to \(\Gamma_j\) has integral degree, equal by
numerical pullback and the projection formula to
\(R_i^{\mathrm{sh}}(\Gamma_i\cdot\Gamma_j)\). Hence
\(t\mid R_i^{\mathrm{sh}}\), for both \(i\). \(\square\)

Consequently, a prime power in a self-intersection denominator that
exceeds its exponent in \(e_i\) must occur in full in the index of that
branch at some shared point. Every prime power in the mixed-intersection
denominator must occur at shared points for each branch. Different prime
powers, or the two branches, need not attain them at the same point.
If \(e_i=1\), all non-Cartierness of \(\Gamma_i\) is confined to the
shared support; for \(e_i>1\), denominator factors already allowed by
\(e_i\) need not be shared.

In the [two-branch no-vertical quartic locus](numerical_surface_pullback.md#cartier-test-divisors-and-the-degree-three-per-order-boundary),
the marked ideal supplies (BI1), and the independent actual mate
relation makes both branches Q-Cartier. Thus (BI2) localizes the
denominator requirements of N11 and the all-order split table. It does
not rule out the required singularities or establish their global
realization. These are indices on the normalization, not the downstairs
almost-Cartier indices, conductor section classes, or full-CI Rees
valuations.
