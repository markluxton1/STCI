# Normal flatness and actual homogeneous generators

The first theorem propagates a full generic binary-CI Hilbert function through every point of an actual lci thickening. The second part uses actual global homogeneous equations to impose additional arithmetic restrictions. These conclusions have separate hypotheses: normal flatness alone does not supply an actual pair or exclude every STCI.

The canonical records are [R-0010](../results/saturated_first_relation_normal_flatness.md) and [R-0013–R-0015](../results/saturated_actual_generator_movement.md). This consolidation retains their inherited scope. The source-level local variant below also treats r=s with an exact-special-order hypothesis; that broader variant is not silently promoted through R-0010.

<a id="2026-10-19-filtered-generic-ci-normal-flatness"></a>
<a id="2026-10-19-filtered-local-normal-flatness-independent-audit"></a>
<a id="2026-10-19-normal-flatness-adversarial-audit"></a>

## Local normal-flatness theorem

Let `k` be algebraically closed of any characteristic. Let `C` be a smooth
integral curve in a smooth threefold `X`, and let `Y` be an ACTUAL locally
complete-intersection thickening with `Y_red=C`. Put

    I=I_C,       J=I O_Y,       E=I/I^2,
    K_j=ker(Sym^j E -> J^j/J^(j+1)).

Suppose that the FULL generic ordinary initial algebra is the coprime binary
complete intersection of degrees `2<=r<=s`:

    gr_(J_eta)(O_(Y,eta)) = k(C)[x,y]/(f_r,g_s),
    gcd(f_r,g_s)=1.                                         (1)

Assume also that at EVERY point `P` of `C`, after choosing a local curve
parameter `t`, the planar ideal defining the transverse special fiber
`O_(Y,P)^hat/(t)` has exact initial order `r`.                   (2)

Then:

1. Every ordinary power `J^i` is saturated in `O_Y`; equivalently,
   `O_Y/J^i` has no finite-support torsion.
2. Every ordinary normal layer `J^i/J^(i+1)` is locally free on `C`.
3. Formation of these layers commutes with the transverse special fiber.
   At every `P`, its Hilbert function is exactly the generic CI Hilbert
   function of degrees `(r,s)`.
4. Every fiber of `gr_J(O_Y)` is an Artinian graded Gorenstein algebra,
   and hence a binary graded complete intersection of degrees `(r,s)`.

The hypothesis concerns the FULL generic initial ideal, not merely two
selected initial symbols. No balanced conormal, pure-power first relation,
projectivity, or rationality hypothesis is used.

Here is a convenient sufficient condition for (2). If `r<s`, the actual
first relation sheaf `K_r` has generic rank one; it suffices that `K_r` be
a line subbundle of `Sym^r E` (the actual first relation is saturated).
If `r=s`, the corresponding rank-two first kernel being a subbundle is
sufficient. More generally it is enough that the actual degree-`r` kernel
contain locally a relation whose image in `Sym^r E` is nonzero at `P`.
The proof of this sufficient condition is included below; saturation is
not silently substituted for an actual relation.

## The codimension-two Hilbert-function input

The accepted codimension-two Gorenstein Hilbert-function drop theorem is
used as an input. It states that if a planar Artinian local Gorenstein
algebra has first ideal order `r`, then its Hilbert function begins
`1,2,...,r` and subsequently drops by at most one at each step.

Its characteristic-free proof is preserved in
[Reflection, higher moments, and sharp codimension-two Loewy bounds,
section 2](SOCLE_AND_LOEWY_BOUNDS.md#source-2026-10-13-generalization-higher-moment-and-loewy-boundsmd).
The delicate separate restriction calculations and Jordan-block argument
were independently checked in
[the independent socle audit](SOCLE_AND_LOEWY_BOUNDS.md#source-2026-10-13-generalization-socle-independent-auditmd),
section 6. These inherited proofs are inputs and were not rerun here.

A current primary research statement was directly checked during this
investigation: J. Jelisiejew, S. K. Masuti, M. E. Rossi,
*On the Hilbert function of Artinian local complete intersections of
codimension three*, arXiv:2202.04021v3 (1 August 2023), printed page 7,
equation (3.2):

    |h_i-h_(i-1)| <= 1.

The statement concerns codimension-two local Artinian Gorenstein/complete
intersection Hilbert functions. It credits Macaulay, Briancon, and
Iarrobino, and refers to Bertella's Theorem 2.6 for realizations.
Verified primary PDF: <https://arxiv.org/pdf/2202.04021>.

The proof below passes from this numerical theorem to uniformity of all ordinary normal powers in an actual thickening.
The proof is independent of the global spectral/apolar bridge in
[the moving pure-power proposal](SATURATED_DUALITY_AND_MOVING_POWERS.md#2026-10-19-filtered-saturated-duality-moving-purepower-bridge).

## 3. Purity, the local finite free algebra, and exact special order

Set

    n=rs,                 d=r+s-2.

These are respectively the generic length and generic last nonzero normal
degree in (1). The actual sheaf `O_Y` is Cohen--Macaulay of dimension one,
and is pure with unique reduced support `C`.

The ideal `J^(d+1)` is zero generically along `C`. It would therefore be a
finite-support submodule of the pure sheaf `O_Y`; hence

    J^(d+1)=0 EVERYWHERE.                                  (3)

Fix a closed point `P`. Complete and choose regular coordinates `(t,x,y)`
on `X` with `I=(x,y)` and `t` a parameter on `C`. Then

    A = O_(Y,P)^hat = k[[t,x,y]]/(F,G),
    R = k[[t]].                                           (4)

The normal variables are nilpotent because `Y_red=C`, so `A` is finite over
`R`. Purity makes `t` a nonzerodivisor. Thus `A` is finite free over the DVR
`R`, of rank `n`. The special fiber

    B=A/tA = k[[x,y]]/(F(0,x,y),G(0,x,y))                  (5)

has length `n`. It is a planar Artinian complete intersection: quotienting
the regular sequence `(F,G)` by the nonzerodivisor `t` preserves the
Cohen--Macaulay codimension count. In particular `B` is Gorenstein.
Writing `m=(x,y)B`, equation (3) gives `m^(d+1)=0`.

For clarity, the sufficient saturated-first condition really gives exact
order `r` in (5). First the ideal of `Y` satisfies

    I_Y subset I_C^r.                                     (6)

Indeed this containment holds at the generic point by (1). The sheaf
`O_X/I_C^r` has a filtration with vector-bundle layers `Sym^j E` on the
smooth curve, so it is pure of dimension one. The image in this sheaf of
any local section of `I_Y` is generically zero, and consequently zero.
This proves (6), and every element of the special planar ideal has order
at least `r`.

Because of (6), the actual kernel `K_r` is the image of actual equations
in `I_Y` modulo `I_C^(r+1)`. A local section of `K_r` whose value at `P` is
nonzero can therefore be lifted locally to an actual equation `Q` of `Y`
whose degree-`r` normal symbol is nonzero at `P`. Reducing `Q` modulo `t`
gives a special-fiber equation of exact order `r`. Hence the special ideal
has exact order `r`, as required by (2). A line subbundle `K_r` for `r<s`
provides such a section at every point; a rank-two subbundle does so when
`r=s`.

This argument uses actual relation sections. A nonzero generic relation
with a coefficient vanishing at `P` does not meet this condition.

## 4. The sharp Hilbert envelope forces equality in every degree

Let `h_i=dim_k(m^i/m^(i+1))` for the special fiber (5). Its exact first
ideal order `r` gives

    h_i=i+1                  for 0<=i<r.

A nonzero degree-`r` initial form belongs to its initial ideal. Multiplying
this form by binary forms gives independent relations, and therefore

    h_i<=r                   for all i>=r-1.               (7)

Let `e<=d` be the actual special socle degree. Gorensteinness gives
`h_e=1`. By the accepted drop theorem in section 2, consecutive decreases
are at most one, so

    h_i<=e+1-i<=d+1-i        for 0<=i<=e.

Together with `h_i=0` for `i>e`, this yields the termwise upper bound

    h_i <= u_i := min(i+1,r,d+1-i),  0<=i<=d.             (8)

Because `d=r+s-2` and `r<=s`, the right hand side is precisely the Hilbert
function of the homogeneous binary CI of degrees `(r,s)`:

    1,2,...,r-1, r,...,r, r-1,...,2,1.

Its sum is

    sum_(i=0)^d u_i = r(d-r+2) = rs = n.                  (9)

But `sum h_i=length(B)=n`. Every term in (8) is an upper bound and the
total sums agree. Therefore equality holds termwise:

    h_i=u_i  for every i.                                 (10)

In particular the special socle degree is `d`, and its entire Hilbert
function is the generic CI Hilbert function. This establishes an exact
special-fiber conclusion, not merely a bound on generic ranks.

## 5. Constant special Hilbert functions remove every saturation defect

For each `i`, the finite `R`-module

    M_i=A/J^i

has generic rank

    rank_R(M_i)=sum_(j<i) u_j.

Its reduction modulo `t` is exactly the quotient by the ordinary special
maximal-ideal power:

    M_i/tM_i = A/(J^i,t) = B/m^i.

The equality here needs no a priori flatness of `J^i`: the image of the
ordinary ideal power `J^i` under the surjection `A->B` is `m^i` by the
definition of ideal multiplication. Equation (10) gives

    dim_k(M_i/tM_i)=sum_(j<i)u_j=rank_R(M_i).              (11)

By the structure theorem for finite modules over the DVR `R`, a nonzero
torsion summand would increase the left side beyond the rank. Thus every
`M_i` is torsion-free and hence free. Equivalently, every ordinary `J^i`
is saturated in `A`.

The kernel in

    0 -> J^i/J^(i+1) -> A/J^(i+1) -> A/J^i -> 0

is consequently free over `R`. Since the right hand quotient is free,
this sequence also stays exact after tensoring with `k=R/(t)`. Thus the
ordinary normal layer specializes to `m^i/m^(i+1)`. The argument holds
at every closed point of `C`, proving assertions 1--3 of section 1.

## 6. Every graded fiber is a complete intersection

For completeness, the symmetry in (10) gives more than flat graded
vector-space dimensions. In the Gorenstein algebra `B`, one always has

    m^(d+1-i) subset Ann_B(m^i).

The symmetric Hilbert function makes the dimensions equal, so these
ideals coincide. Actual multiplication therefore induces perfect
pairings

    (m^i/m^(i+1)) tensor (m^(d-i)/m^(d-i+1)) -> m^d.

Thus `gr_m(B)` is Gorenstein. A zero-dimensional graded Gorenstein quotient
of a polynomial ring in two variables is a complete intersection (the
height-two Gorenstein ideal has two generators). Its Hilbert series is

    ((1-z^r)(1-z^s))/(1-z)^2,

so the generator degrees are exactly `(r,s)`. Section 5 identifies this
algebra with the fiber of `gr_J(O_Y)`. This proves assertion 4.

## 7. Necessary failure shield: nonsaturated first relation

Consider

    A=k[[t,x,y]]/(x^2-t*y, y^2).

It is finite free of rank four over `k[[t]]`, with basis `1,x,y,xy`, is an
actual lci, and has reduced support the smooth `t`-axis. Over `k((t))`,
eliminating `y=x^2/t` gives `k((t))[x]/(x^4)`: the generic transverse
algebra has first ideal order one and socle degree three. At `t=0`, the
fiber is `k[[x,y]]/(x^2,y^2)`, of first ideal order two and socle degree
two.

The actual degree-one relation is `t*y`, so the first relation sheaf is
not saturated at `t=0`. This is precisely the hypothesis that fails.
Consequently smooth support, actual lci Gorensteinness, and a generic
tangent CI ALONE do not exclude special-fiber degeneration.

The argument also does not apply to the whole intersection when only
`C subset Y_red` is known and other reduced components are present. The
unique-support purity argument yielding (3) is then unavailable for that
whole intersection. No vertical exceptional degeneration is identified
here with an additional component downstairs.

## 8. Optional comparison with ordinary torsion before applying the theorem

Without assuming the exact-order condition, let `P_i` be the saturation
of `J^i` and write

    L_i=J^i/J^(i+1),       T_i=torsion(L_i),
    D_i=P_i/J^i,           C_i=P_i/(J^i+P_(i+1)),
    B_i=P_i/P_(i+1).

The kernel of the canonical map `L_i->B_i` is exactly `T_i`; its image is
`F_i=L_i/T_i`. There are canonical exact sequences

    0 -> F_i -> B_i -> C_i -> 0,
    0 -> T_i -> D_(i+1) -> D_i -> C_i -> 0.                (12)

The second sequence follows by mapping `P_(i+1)/J^(i+1)` to `P_i/J^i`;
its kernel is `(P_(i+1) intersect J^i)/J^(i+1)`, exactly the torsion of
`L_i`. Pointwise lengths therefore satisfy

    length(T_i)=length(D_(i+1))-length(D_i)+length(C_i).

Since `D_0=D_(d+1)=0`, this telescopes to

    sum_i length(T_i)=sum_i length(C_i).                  (13)

These identities compare the two filtrations without equating them in
advance. The theorem above proves that ALL of these finite-support
defects vanish under its exact hypotheses.


## Actual homogeneous generators and arithmetic

<a id="2026-10-19-global-ci-filtration-investigation"></a>
<a id="2026-10-19-global-ci-filtration-independent-audit"></a>

## 1. Exact scope and proposed conclusions

Let the ground field be algebraically closed of characteristic different from two, and let

\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
Suppose an actual homogeneous complete intersection

\[
Y=V(F_a,G_b),\qquad Y_{\rm red}=C,
\]
exists. The equations have no common surface component. Put
\(I=I_C\), \(Q=I_Y\), and \(J=I\mathcal O_Y\). Assume the **full** generic
ordinary initial ideal is a coprime binary complete intersection of degrees
\(2\le r<s\), and the actual first degree-r relation kernel

\[
R=\ker(\operatorname{Sym}^r N_C^*\longrightarrow J^r/J^{r+1})
\]
is a line subbundle. These are exactly the substantive additional hypotheses
of promoted STCI-R-0010. Write

\[
N_C^*=\mathcal O_{\mathbf P^1}(-7)^{\oplus2},\qquad
R=\mathcal O_{\mathbf P^1}(-7r-\epsilon),\quad\epsilon\ge0.
\]
Thus the full first root has class \((\epsilon,r)\) in
\(\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm dir}\).

The following conclusions are canonically recorded in characteristic zero (R-0013–R-0015). The proof below also gives their source-level extension to characteristic different from two, independently reconstructed during consolidation. No canonical metadata is enlarged here.

The conclusions are:

1. The original homogeneous equations necessarily **both** have exact
   generic normal order r, and their first symbols jointly generate R at
   every point. Their two coefficient sections have positive degrees and
   no common zero. This requires the actual homogeneous two-generator
   presentation, rather than merely an abstract graded CI family.
2. Movement one, \(\epsilon=1\), is impossible, in every normal order and
   every homogeneous degree pair under these hypotheses.
3. For movement two, \(\epsilon=2\), the only possible unordered numerical
   data are

   | r | s | a | b | s-r |
   |---:|---:|---:|---:|---:|
   | 2 | 8 | 8 | 8 | 6 |
   | 2 | 12 | 6 | 16 | 10 |
   | 6 | 21 | 18 | 28 | 15 |
   | 14 | 42 | 48 | 49 | 28 |
   | 15 | 45 | 50 | 54 | 30 |
   | 20 | 60 | 64 | 75 | 40 |

   This is an exhaustive **necessary numerical list**, not an existence
   result or a completed exclusion of the six cases.
4. For each fixed integer \(1\le\epsilon\le8\), only finitely many
   numerical quadruples \((r,s;a,b)\) can satisfy these hypotheses.
   A finite divisor procedure is supplied below. No corresponding claim
   is made here for \(\epsilon\ge9\).

Neither nonsaturated first relations, non-CI full generic initial ideals,
nor intersections with residual curve components are covered.

## 2. Inputs, evidence paths, and authority boundary

- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md)
  supplies normal flatness of the entire ordinary J-adic algebra under
  the stated hypotheses. Its preserved proof computes the second minimal
  quotient relation T and its degree in
  [the saturated first-relation bridge](SATURATED_DUALITY_AND_MOVING_POWERS.md#projective-normal-flatness-by-duality-and-resultants),
  sections 3--6. In the present splitting,

  \[
  \deg T=-7s+\frac{s\epsilon}{r}.
  \tag{1}
  \]

  The second relation is a **quotient relation**. No global second
  polynomial line is assumed.
- The general generator-filtration lemma is proved independently in
  [the generator-filtration audit](RELATION_LIFTING_AND_GAP_COSTS.md#source-2026-10-13-generalization-thick-generator-filtration-auditmd),
  sections 1--4. It is a reviewed supporting source, not a separate
  promoted result record. Its general statement applies to a full
  locally CI initial ideal; the application below is enabled by R0010.
  The minimal argument needed here is recorded in section 3, so that
  this additional interface can be independently assessed.
- The no-quadric-factor assertion is characteristic free and does not require the quartic-carrier exclusion. If q divides F, then V(q,G) must have support C. If q also divides G the pair is improper. Otherwise G|Q is a nonzero divisor of class (b,b) supported only on C of class (1,3), so (b,b)=n(1,3) for some n>0, impossible. This applies even to reducible/nonreduced F or G. It yields a,b>=3r after the actual-order conclusion. The characteristic-zero R-0001 is compatible with this elementary argument but is not its necessary premise.

The new claims in this note remain unpromoted proposals. Independent
reconstruction passed in [the core audit](NORMAL_FLATNESS_AND_FILTERED_CI.md#abstract-bundle-realizations-of-the-six-rows)
and [the fixed-movement audit](#2026-10-19-global-ci-filtration-independent-audit).

## 3. The actual generator sequence and why it cannot split

Since the full ordinary initial ideal K is locally generated by a
regular sequence of degrees r,s, put

\[
M=Q/IQ,\qquad
\mathcal F^jM=\operatorname{image}(Q\cap I^j\longrightarrow Q/IQ).
\]
The generator-filtration lemma gives

\[
\operatorname{gr}_{\mathcal F}M=K/(S_+K),
\quad S=\operatorname{Sym}(N_C^*).
\]
Its two graded pieces are R in degree r and T in degree s. Consequently

\[
0\longrightarrow T\longrightarrow
\mathcal O(-4a)\oplus\mathcal O(-4b)
\longrightarrow R\longrightarrow0.
\tag{2}
\]

Here \(M=\mathcal O_C(-a)\oplus\mathcal O_C(-b)\) comes from the
**actual** homogeneous CI ideal. To recall why cancellation does not
invalidate this identification, local lifts f,g of the regular initial
sequence generate Q by finite initial-term elimination followed by Krull
intersection. Any cancellation of leading terms is a Koszul syzygy of
the two regular initial forms. Removing it gives

\[
Q\cap I^j=I^{\max(j-r,0)}f+I^{\max(j-s,0)}g,
\qquad \operatorname{in}_I(IQ)=S_+K.
\]
This proves the stated filtered quotient without assuming a global
change of homogeneous generators or a formal retraction.

The generic length of Y along C is rs. Degree of the complete
intersection gives

\[
ab=4rs.
\tag{3}
\]

Set

\[
P=7r+\epsilon,\qquad Q_0=7s-\frac{s\epsilon}{r}.
\]
Equation (1) says \(R=\mathcal O(-P)\),
\(T=\mathcal O(-Q_0)\), with both P and Q_0 integers. Taking
determinants in (2) gives

\[
4(a+b)=7(r+s)-\frac{\epsilon(s-r)}r.
\tag{4}
\]

If (2) split, uniqueness of the splitting type on \(\mathbf P^1\)
would give \(\{4a,4b\}=\{P,Q_0\}\). Therefore

\[
16ab=P Q_0
=rs\left(49-\frac{\epsilon^2}{r^2}\right)
\le49rs,
\]
contradicting \(16ab=64rs\) from (3). Thus (2) never splits, including
when \(\epsilon=0\).

The quotient map in (2) is given by sections

\[
\alpha\in H^0\mathcal O(4a-P),\qquad
\beta\in H^0\mathcal O(4b-P)
\]
with no common zero. If one were zero, the other would be nowhere zero
and would split the sequence. If either had degree zero, its nonzero
constant value would also split the sequence. Hence both sections are
nonzero and have positive degrees. They are exactly the degree-r first
symbols of the original F and G, expressed in the first relation line.
Thus both original equations have exact generic order r and jointly
generate R everywhere.

The kernel is locally generated by \((-\beta,\alpha)\). Its two
components are also nonzero positive-degree sections. We obtain the
strict interval and movement bound

\[
7r+\epsilon<4a,4b<7s-\frac{s\epsilon}{r},
\qquad 0\le\epsilon<7r.
\tag{5}
\]

The last inequality follows since the right endpoint is positive.
This rigidity is specific to genuine homogeneous C0 complete
intersections; it is not a restriction on arbitrary abstract graded
families admitted by R0008.

## 4. The quadric bound and normalized arithmetic

Neither F nor G has the unique quadric q as a factor, by the characteristic-free divisor-class argument just given. Restrict F to the smooth quadric
\(Q\simeq\mathbf P^1\times\mathbf P^1\), where C has class (1,3).
Its exact ambient normal order r implies that the nonzero restriction
vanishes along C to order at least r. Its remaining effective divisor
has class \((a-r,a-3r)\), possibly after subtracting further copies of C.
Therefore \(a\ge3r\); the same reasoning gives \(b\ge3r\).
This argument needs no integrality of F or G.

Put \(t=s/r>1\) and \(k=\epsilon/r\). From (3)--(4) and AM--GM,

\[
7(1+t)-k(t-1)=\frac{4(a+b)}r\ge16\sqrt t.
\]
Since \(k\ge0\), necessarily

\[
t\ge\rho:=\frac{79+16\sqrt{15}}{49}>\frac{23}{8}.
\tag{6}
\]
The inequality \(\rho>23/8\) can be checked exactly by substituting
\(23/8\) into \(49t^2-158t+49\), obtaining \(-15/64<0\).
For \(\epsilon>0\), the first inequality in (6) is strict.

If \(a\le b\), then \(3r\le a\le\sqrt{ab}\). The function
\(x+ab/x\) decreases on that interval. Thus

\[
a+b\le3r+\frac{4s}{3}.
\]
Combining with (4) gives

\[
(5r-3\epsilon)t\le15r-3\epsilon.
\tag{7}
\]
For \(r>3\epsilon/5\), this is the useful upper bound

\[
t\le\frac{15r-3\epsilon}{5r-3\epsilon}
=3+\frac{6\epsilon}{5r-3\epsilon}.
\tag{8}
\]
Finally, (1) gives

\[
r\mid\epsilon s,
\quad\text{equivalently}\quad \epsilon t\in\mathbf Z.
\tag{9}
\]
These inequalities retain all first-root components and impose no
smoothness, irreducibility, or reducedness on the root.

## 5. Uniform exclusion of movement one

Let \(\epsilon=1\). Equation (9) makes t an integer. Equation (6)
forces \(t\ge3\). For every \(r\ge2\), (8) gives

\[
t\le\frac{15r-3}{5r-3}<4.
\]
Thus t=3. But (4) now gives

\[
4(a+b)=28r-2,
\]
which is impossible for integers a,b. This excludes movement one in
the full stated saturated-first-relation, full-generic-CI class, with
no bound on the defining degrees or normal orders.

## 6. Exhaustive movement-two list

Let \(\epsilon=2\). Equation (9) makes t an integer if r is odd and
a half-integer if r is even. Equations (6) and (8) force \(t\ge3\).
For \(r\ge7\), the upper bound is less than 7/2, so t=3. For
\(2\le r\le6\), the possibilities before the final integer-degree
check are exactly

| r | possible s |
|---:|:---|
| 2 | 8, 9, 10, 11, 12 |
| 3 | 9, 12 |
| 4 | 12, 14 |
| 5 | 15 |
| 6 | 18, 21 |

For r=2 the lower bound t>=4 follows directly from
\(8+6t\ge16\sqrt t\), rather than the weaker (6).
For each pair, compute the integer

\[
A=\frac{7(r+s)-2(s-r)/r}{4}.
\]
It must be an integer, and \(A^2-16rs\) must be a nonnegative square
with the correct parity. The roots of \(X^2-AX+4rs\) must be at least
3r. The only survivors from this small table are
\((r,s;a,b)=(2,8;8,8),(2,12;6,16),(6,21;18,28)\).

On t=3, equation (4) gives \(a+b=7r-1\), and the discriminant is

\[
D=(7r-1)^2-48r^2=(r-7)^2-48.
\]
For r>=7 a nonnegative square D=d^2 is equivalent to

\[
(r-7-d)(r-7+d)=48.
\]
Both factors are positive integers of the same parity. Their ordered
factor pairs are (2,24), (4,12), and (6,8), yielding respectively
\(r=20,15,14\). Substitution yields the three remaining rows in the
statement. This factorization proves exhaustion for arbitrarily large r;
a bounded search is not the proof.

## 7. Finiteness for each fixed movement at most eight

Fix \(1\le\epsilon\le8\). Since \(\epsilon t\) is an integer and
\(t>\rho>23/8\), we have \(t\ge3\): the largest possible grid point
below 3 is \(3-1/\epsilon\le23/8\).

If

\[
r>\frac{3\epsilon(2\epsilon+1)}5,
\tag{10}
\]
then (8) gives \(t<3+1/\epsilon\), so t=3. In this range

\[
a+b=7r-\epsilon/2.
\]
Odd epsilon is impossible. For even epsilon=2h the discriminant is

\[
D=(r-7h)^2-48h^2.
\]
A nonnegative square D=d^2 gives

\[
(r-7h-d)(r-7h+d)=48h^2.
\tag{11}
\]
There are finitely many signed integer factor pairs of the nonzero
fixed integer on the right, hence finitely many r and a,b. More explicitly,
the factors in (11) have the same parity and even product, so both are
even. Writing them as 2u,2v gives uv=12h^2 and
r=7h+u+v<=7h+12h^2+1. This bound also covers negative factor pairs.
Together with the small-r cutoff, the following normal-order bounds hold:

| epsilon | bound on r |
|---:|---:|
| 1 | no cases |
| 2 | 20 |
| 3 | 12 |
| 4 | 63 |
| 5 | 33 |
| 6 | 130 |
| 7 | 63 |
| 8 | 221 |

There remain finitely many r satisfying the reverse of (10), but (8)
need not bound s when its denominator is nonpositive. The following
exact factorization handles that stratum and prevents a hidden gap.
For fixed r and epsilon set \(c=7r-\epsilon>0\), as proved in (5).
Eliminate s from (3)--(4) to obtain

\[
\boxed{(ca-16r^2)(cb-16r^2)=4r^2(15r^2+\epsilon^2).}
\tag{12}
\]
The right side is a fixed positive nonzero integer. Its finitely many
signed divisor pairs determine a,b uniquely, after which
\(s=ab/(4r)\) is determined. Keeping only positive integer a,b,s with
all original conditions yields a finite exact enumeration. Thus (11)
and (12) establish finiteness without dropping small-r strata.

For epsilon>=9, the grid may contain t<3 but t>rho (for example
26/9). The argument above no longer proves finiteness; no extension
beyond the literal small-movement scope is asserted.

## 8. Smooth-root consequence and remaining work

Equation (6) with r>=2 forces s-r>=4, hence in particular the gap is
at least two. Conclusion 1 supplies automatically the two-original-
equation order and joint-generation hypotheses in
[STCI-R-0006](../results/actual_ci_smooth_root_bridge.md). Thus for a
**smooth full root**, R0010 plus an actual global homogeneous C0 CI
satisfies the ancillary equation hypotheses of that bridge. The bridge
then supplies its stated finite primitive thickness on the root.

For epsilon=2, promoted R0011 restricts the total root to be reduced;
its possibilities remain an integral (2,r) divisor or, for even r,
two distinct (1,r/2) components. Smoothness is an additional restriction.
The six numerical rows include possible singular and reducible roots
and are not discarded by the present argument. Existing smooth-root
formal nonexistence is an all-orders statement with a nonexplicit
finite empty stage; the finite gaps in the table cannot be compared
with that stage without additional work.

The frontier advances here by excluding movement one under exact
saturated/full-generic-CI hypotheses and reducing movement two to six
numerical rows. It does not classify the remaining root divisors, prove
that one of the six rows lifts, exclude every one of those rows, or
settle unrestricted STCI for C0.


## Exact arithmetic support and boundary checks

The proof above, rather than a bounded search, establishes exhaustion. The independent arithmetic reconstruction confirms that the small-order factorization retains both positive and negative divisor pairs. The cutoff is strict: at epsilon=7, (r,s;a,b)=(63,198;189,264) has r=3*epsilon*(2*epsilon+1)/5 and t=22/7, so it belongs to the small-order factorization, not the strict large-order stratum. The exact arithmetic script [global_ci_small_movement_divisor_audit.py](../computations/global_ci_small_movement_divisor_audit.py) gives counts 0,6,4,11,9,19,9,19 for movements 1 through 8 and maximal r respectively none,20,3,63,10,130,63,221. Those counts do not test Picard descent or embedded realization.

The local Hilbert-envelope/DVR proof and the homogeneous-generator arithmetic received independent reconstruction in the inherited source state. The alternative projective proof by saturated Gorenstein duality and a degree-zero resultant is retained in [Saturated duality](SATURATED_DUALITY_AND_MOVING_POWERS.md#projective-normal-flatness-by-duality-and-resultants). The two proofs use different hypotheses: the local proof allows r=s and needs exact transverse special order; the resultant proof uses projectivity, r<s and a saturated actual first-relation line. They should not be merged into a statement omitting those alternatives.

## Abstract bundle realizations of the six rows

The six numerical rows pass the abstract generator-bundle test. Put P=7r+epsilon and Q0=7s−s*epsilon/r. For any row choose u=4a−P>0 and v=4b−P>0. The quotient entries x^u,y^v on P1 have no common zero, giving

    0 -> O(-Q0) -> O(-4a)⊕O(-4b) -> O(-P) -> 0,

because its kernel degree is P−4a−4b=−Q0. These are actual abstract bundle sequences, with no assertion of ambient formal or homogeneous equation realization. Thus this sequence alone cannot eliminate the six rows. As an exact arithmetic guardrail, the discarded r=2,s=10,epsilon=2 case has a+b=19,ab=80 and discriminant41, so it supplies no integral carrier degrees.

## Characteristic scope

The local Hilbert-envelope/DVR theorem above is valid over an algebraically closed field in every characteristic. The [codimension-two drop proof](SOCLE_AND_LOEWY_BOUNDS.md#source-2026-10-13-generalization-higher-moment-and-loewy-boundsmd) uses one y-Jordan block in Ann(x), restriction to a general linear form and Gorenstein duality; it requires no characteristic-dependent division. The proof then uses only purity and DVR module structure, including r=s. The separate projective resultant proof likewise uses integral identities and arbitrary conormal. These are explicit source-level extensions; canonical R-0010 keeps its recorded scope.

For C0, the actual-generator and arithmetic proofs need balanced conormal O(-7)^2, which holds in characteristic different from2, together with the characteristic-free no-quadric-factor argument above. The generator filtration, determinant equations, nonsplitting inequality and all integer arithmetic are characteristic independent. Therefore movement-one exclusion, the six movement-two necessary rows and fixed-movement1–8 finiteness extend under the **same** r>=2, saturated actual first-relation/full generic-CI/actual homogeneous sole-support hypotheses to every p≠2. This does not extend the separate characteristic-zero repeated-root theorem or section8's reduced-root consequences. In characteristic2 the balanced model changes.

The [every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) is consistent with these restrictions: its displayed quartic has generic normal order one, outside r>=2. The extension constrains a specified class of entirely thick presentations, not all positive-characteristic STCI presentations.
