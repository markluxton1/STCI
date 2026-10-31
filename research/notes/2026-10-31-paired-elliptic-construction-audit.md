# Independent audit: paired elliptic construction and failed nodal gluing

October 31, 2026. Reviewer: `paired_cover_selection_review`, an independent
agent with no nested delegation. Outcome: the explicit construction and
component polarization pass mathematical review; the one evaluated
quadratic-residue gluing gate fails. The fixed candidate is stopped.
This is reviewed provisional evidence, not canonical promotion.

## Scope and evidence

The object reviewed is the fixed construction in
[the paired-cover note](2026-10-31-paired-elliptic-construction.md), over an
algebraically closed field of characteristic zero, with
\(C_0=[s^4:s^3t:st^3:t^4]\) as the fixed target quartic. The reviewer first
read `research/INDEX.md` and `research/MAP.md`, the
[failed palindromic spin test](2026-10-31-palindromic-polarization-spin.md),
and the [canonical-extension criterion](2026-10-31-elliptic-canonical-extension.md),
especially its Section 3 residue criterion. The parent supplied the
proposed rational functions and subsequently its proposed residue
calculation. The reviewer independently reconstructed their derivatives,
normalization, divisors, local expansions, marking transformation, and
the polynomial contradiction below.

The construction is explicit over a number field; no analytic descent or
general-curve assertion is needed. The original RET proposal is replaced
by these algebraic functions. The review consulted
[Moschetti--Pirola, *Hyperelliptic odd coverings*, Section 3](https://arxiv.org/html/2011.12159)
for the involution/monodromy distinction. That source works over the
complex numbers. Its general lifting assertion is not an input to this
algebraic proof. The initial proposed permutations were checked to have
product one and generate a group of order twelve, but those finite checks
were not treated as evidence for the required fixed-fiber action.

After the main proof note was written, the reviewer read its actual
preserved statement, including equations (1)--(10) and its stopping and
scope language. These match the construction and residue argument
covered below. Its explicit formula for A is equivalent to B^3/f, and
its coefficient 5R_0/3 in the quartic model equals K(2s-3) below.
No material transcription or scope defect was found in that check.
This covered-state check did not rerun the proof or open a later gate.

## Construction, boundary, and component polarization

Put
\[
a=-7+4\sqrt3,\quad u=(a-1)/4,\quad s^2=8/3,
\quad r(x)=\frac{(x-1)^3(x-a)}{x^2},\quad R_0=r(u).
\]
Here \(u^2=-a\), \(u^2+4u+1=0\), and
\[
r'(x)=\frac{2(x-1)^2(x-u)^2}{x^3}.
\]
Thus the three branch fibers of \(r\) are \((3,1)\), \((3,1)\),
and \((2,2)\), over \(0,R_0,\infty\), respectively. None of the
displayed critical points or values collapses. Let \(q\) be the unique
Möbius postcomposition taking these three values to
\(-3,3,-2s\). These values and \(2s\) are distinct. Consequently
\(q^{-1}(2s)\) has four simple points, and the four poles of \(q\)
are simple as well.

The normalization of
\[
h+s^2/h=q(x)
\]
is a connected smooth genus-one curve \(E\). The degree-two map \(x\)
branches exactly at the four points of \(q^{-1}(2s)\): even orders over
\(-2s\) and poles of \(q\) give no additional branches. Its involution
\(j(h)=s^2/h\) fixes exactly the four points of \(h^{-1}(s)\).
The degree-four map \(h\) has four triple ramification points, two over
\(q=-3\), and two over \(q=3\), with no other ramification.

For \(P(v)=(3v^5-10v^3+15v)/15\), put
\[
g(v)=\frac{P(v)-8/15}{P(v)+8/15},\quad f=g(h),
\quad B=\frac{h-1}{h+1}\frac{x-1}{x-u},\quad A=B^3/f.
\]
The factorization
\(15(P(v)-8/15)=(v-1)^3(3v^2+9v+8)\), and its sign counterpart,
give the asserted degree-twenty passport. The zero and pole divisors of
\(B\) have degree six, with exactly the prescribed supports; the factors
introduce no common boundary points. The remaining simple points over
\(q=-3,3\) occur at \(x=a,v_0\), respectively, where
\(v_0=a+3-3u=u+4\). Hence
\[
\operatorname{div}(A)=x^*(v_0)-x^*(a),\qquad
A=C\frac{x-v_0}{x-a},\quad C\ne0.
\]
In particular \(A\) is the degree-two quotient by \(j\). It recovers
\(x\), and then \(B/((x-1)/(x-u))\) recovers \(h\). Thus \((A,B)\)
is birational onto its image without an additional monodromy assumption.

Write \(H_x\) for an \(x\)-fiber class and \(Z=h^{-1}(\infty)\).
The fixed-point divisor of \(j\) has class \(2H_x\), so the \(h\)-fiber
class is \(2H_x\). The half-ramification divisor of \(h\) also consists
of two \(x\)-fibers. Therefore its induced theta characteristic is
trivial. The composition with \(g\) preserves this spin class, since
the unique theta characteristic on its rational intermediate curve is
\(\mathcal O(-1)\). More concretely, the actual bundles satisfy
\[
L=\mathcal O_E(H_x),\qquad \mathcal O_E(Z)=L^2,\qquad M=L^3.
\]
This is a genuine successful component-polarization construction.

The four points of \(Z\) have distinct finite \(x\)-coordinates, and
their marks are
\(T(x)=(x-1)/(x-u)\). They are finite, nonzero and distinct, and obey
\(A=T^3\). These facts identify the marked target incidence; they do
not assert nodal gluing or the later source determinant condition.

## Normalized quartic and the section representing the target coordinate

Set
\[
F=(x-1)^3(x-a),\quad K=R_0(2s+3),\quad
D=-6F+Kx^2,\quad N=12sF-3Kx^2.
\]
Then \(q=N/D\), with coprime numerator and denominator. The exact
factorization
\[
\frac{N^2-4s^2D^2}{x^2}
=K(2s-3)\bigl(24sF-R_0(2s+3)^2x^2\bigr)
\]
has degree four and nonzero constant and leading coefficients. Its four
roots are simple because they are precisely \(q^{-1}(2s)\).
Thus
\[
Y^2=(N^2-4s^2D^2)/x^2,\qquad Y=(2h-q)D/x
\]
is the smooth quartic double-cover model. In particular both \(x=0\)
and \(x=\infty\) have two unramified normalized branches; neither
contributes a missing ramification point or mark. With \(H_\infty=x^*(\infty)\),
\(\omega=dx/Y\) is a nonzero holomorphic differential and
\[
\operatorname{div}(Y)=\operatorname{Ram}_x-2H_\infty,\qquad
\operatorname{div}(h-s)=\operatorname{Ram}_x-Z.
\]
The pullback of the target coordinate section \(x_0\) has zero divisor
\[
\mathcal D_{x_0}=x^*(a)+x^*(u)+h^*(-1).
\]
Indeed these are the pole divisors of \(A\) and \(B\). Direct divisor
addition, including the two points over \(x=\infty\), gives
\[
\tau_E=\frac{(x-a)(x-u)(h+1)(h-s)}{Y}\,\omega^2
=\frac{(x-a)(x-u)(h+1)(h-s)}{Y^3}\,dx^2,
\]
\[
\operatorname{div}(\tau_E)=\mathcal D_{x_0}-2Z.
\]
Thus \(\tau_E\), up to one common nonzero scalar, is precisely the
quadratic differential representing \(h_E^*x_0\) in the criterion's
\(\omega_E^2(2Z)\). Matching degrees alone was not used to identify it.

## Local residues and failure of the actual gluing gate

Let \(x_i\) be the four distinct roots of \(D\), and let \(P_i\in Z\)
be the corresponding \(h=\infty\) points. They avoid \(0,a,u\).
On this branch, and specifically with the displayed choice of \(Y\),
\[
Y_i=N_i/x_i,\qquad
h\sim\frac{N_i}{D'_i(x-x_i)},\qquad
N_i=\frac53R_0x_i^2.
\]
The opposite sign of \(Y_i\) selects the \(h=0\) point and is not a
mark. The coefficient of \((d(x-x_i)/(x-x_i))^2\) in \(\tau_E\) is
therefore
\[
\rho_i=\frac{x_i^3(x_i-a)(x_i-u)}{N_i(D'_i)^2}.
\]
Write \(\mathcal R(T)=\prod_i(T-T_i)\), with
\(T_i=T(x_i)\). Since \(T\) is Möbius and its pole is not a mark,
\[
\mathcal R(T(x))=c\frac{D(x)}{(x-u)^4},\quad c\ne0,\qquad
T'(x)=\frac{1-u}{(x-u)^2}.
\]
Differentiating at each \(x_i\) gives exactly
\[
\mathcal R'(T_i)=\frac{cD'_i}{(1-u)(x_i-u)^2}.
\]
Thus the four gluing values \(\rho_i\mathcal R'(T_i)^2\) are one
common nonzero scalar times
\[
J(x_i)=\frac{x_i(x_i-a)}{(x_i-u)^3}.
\]
If they were equal, some \(\lambda\) would make
\(x(x-a)-\lambda(x-u)^3\) vanish at four distinct points. Its degree
is at most three, so it would be identically zero, which its coefficients
make impossible. The quadratic residues consequently do not match in
the criterion's required trivializations:
\[
\boxed{\kappa\ne1.}
\]
The quadratic nature removes the node-generator sign; changing the
elliptic component trivialization only multiplies all four values by a
common nonzero scalar. Neither freedom repairs this failure.

## Disposition, geometric meaning, and limits

The construction controls a genuine elliptic double cover and actual
ruling functions, and proves that odd spin and the required component
line bundles can occur for this passport. It therefore answers a real
missing-input question left by the previous even-spin failure. However,
the target polarization and the square of the nodal dualizing bundle
do not glue to the same line bundle on the union of this elliptic curve
and the marked rational component. The obstruction is in the
three-dimensional gluing torus, after the component Picard gate.

No determinant/first-normal test, source-section construction, carrier
construction, conductor calculation or mate descent was performed.
The fixed incidence is stopped at the first failed remaining gate.
No numerical approximation, candidate enumeration, or new computation
was needed for the residue proof; the evidence is the exact divisor and
local calculation above. No failed or unperformed check is recorded as
passing. No material mathematical defect remains in the reviewed
construction or this failed-gate conclusion.

This excludes extension of this fixed marked incidence through the
reviewed canonical-extension criterion. It does not exclude every odd-spin
target, every degree-eight carrier, or arbitrary defining pairs. There
is no exhaustive reduction from unrestricted STCI to this construction.
The unrestricted characteristic-zero STCI question for \(C_0\) remains
open, and this failure does not justify another target enumeration.
