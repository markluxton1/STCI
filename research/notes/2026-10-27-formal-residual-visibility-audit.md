# Independent audit: formal residual visibility and section extension

Date: 2026-10-27. Reviewer: the positive-characteristic research agent,
independent of the proposing formal-neighborhood agent. Source under review:
[What the formal neighborhood sees](2026-10-27-formal-neighborhood-residual-visibility.md),
especially sections 5–7. **Outcome:** the stated deductions pass independent
reconstruction under their displayed hypotheses. They remain provisional
and unpromoted; this review does not decide existence of the required formal
sections or the unrestricted STCI question.

## 1. Scope and primary-source check

The ambient space is P3 over an algebraically closed field, the marked C
is the smooth positive-dimensional connected fixed rational quartic, and
the formal completion is the **embedded ambient completion along the whole
C**, with its specified completed twists O(d). This is stronger than a
generic transverse algebra, an abstract ribbon, or local choices of formal
equations.

I independently opened [Hartshorne, Cohomology of non-complete algebraic
varieties (1971), original NUMDAM PDF](https://www.numdam.org/article/CM_1971__23_3_257_0.pdf).
Printed p. 258 states the Hironaka–Matsumura G3 theorem for connected
positive-dimensional subvarieties of projective space. Proposition 1.2 on
the same page gives the equivalence of G3 with G2 plus the Lefschetz
condition, for a complete nonsingular ambient variety. The hypotheses fit
this P3 and C in arbitrary characteristic. This verifies the external
input through an accessible primary account; I did not re-prove the
classical G3 theorem or recover the original HM proof.

## 2. Section extension: independent proof using Lefschetz

G3 immediately implies G2 and, by the cited proposition, Lef(P3,C).
Apply the Lefschetz condition to the locally free sheaf O(d). Every global
formal section therefore extends to an actual section over some Zariski
open neighborhood V of C. Each irreducible component of the closed
complement P3 minus V has codimension at least two: a component of
codimension one would be a projective hypersurface disjoint from C, whereas
an ample hypersurface meets every positive-dimensional projective curve.
Since P3 is normal, a section of the invertible sheaf O(d) over an open
set with codimension-at-least-two complement extends uniquely over P3.

This reconstructs, for every integer d,

    H0(P3,O(d)) = H0(P3 completed along C, completed O(d)).

It independently confirms the proposing note's rational-section argument.
That argument contracts regularity from faithful local completion and
then excludes a polar divisor avoiding C. One can use either proof. The
Lefschetz proof makes the standard extension step explicit without any
choice of rational frame.

The conclusion does not assert extension of arbitrary local sections,
formal vector bundles, or formal ideals. The actual completed ambient line
bundle and its **global** section are essential data.

## 3. Full twisted formal pairs and actual STCI

Let a,b>0 and suppose globally glued formal sections of completed O(a),
completed O(b) generate a formal ideal Jhat with

    I_C^N contained in Jhat contained in I_C

for one finite integer N. Section extension yields actual homogeneous
F,G. The right inclusion implies F,G vanish on C, by contraction at its
stalks.

I checked properness separately. If F,G shared an irreducible hypersurface
H, projectivity and positivity force H to meet C. At p in their
intersection the left inclusion, faithful flatness of the local I-adic
completion, and contraction give I_C,p^N contained in (H)_p. Taking radicals
forces the local surface into the local curve, impossible by dimension.
This also rules out a zero generator or the zero pair. Hence F,G form a
regular sequence and Y=V(F,G) is a proper complete-intersection curve.

The same power containment excludes any other curve component whose
support meets C. If any residual components remain, their union is
disjoint from C. The complete intersection is connected: its Koszul
resolution and the vanishing of intermediate line-bundle cohomology on
P3 give H0(O_Y)=k. A union of C and a nonempty closed residual union
disjoint from C would disconnect Y. Thus no residual component remains.
Purity of the complete intersection excludes stray zero-dimensional
components. Therefore Y_red=C.

Conversely an actual pair with Y_red=C gives a uniform finite power
containment by Noetherianity, and then gives the required completed global
sections. This confirms the equivalence in section 6. There is no
additional algebraization requirement after **these complete data** have
been supplied. Constructing those data is still the unresolved task.

I specifically checked that connectedness is applied only after properness
has been proved, and that it concerns the whole residual union, not an
assertion that every residual component meets C directly.

## 4. Consecutive neighborhood obstruction and injectivity indices

Use the source's convention C_n=V(I_C^{n+1}). Since the smooth C is a
regular codimension-two embedding in P3,

    I_C^{n+1}/I_C^{n+2} = Sym^{n+1}(E),  E=I_C/I_C^2.

Tensoring the exact sequence of consecutive neighborhoods with O(d)
gives the connecting obstruction in

    H1(C, Sym^{n+1}(E) tensor O_C(d)).

Its vanishing is necessary and sufficient for lifting a given section
across that **one** step. It does not establish a coherent infinite tower
without carrying out subsequent steps. Ambiguity of one lift is the H0 of
the same kernel bundle.

For characteristic different from two, the canonical premise R-0020 gives
E=O_P1(-7)^2. A first nonzero normal symbol of order r for a degree-d
section lies in O(4d-7r)^{r+1}. If r>4d/7 there are no such global symbols.
If every symbol vanishes, I-adic separatedness gives the zero section.
Consequently vanishing on C_n with n=floor(4d/7) forces a global or global
formal section to vanish. The index is correct: vanishing on C_n means
order at least n+1, not order n.

In characteristic two, E=O(-8) plus O(-6), so every summand of Sym^r(E)
tensor O_C(d) has degree at most 4d-6r. The same proof gives the sufficient
injectivity index floor(2d/3). No balanced-bundle argument has been
transferred across the characteristic-two splitting jump.

These indices assert uniqueness when a lift exists. A concrete control is
d=1: restriction to C itself is injective, but H0(C,O_C(1)) is the
five-dimensional space H0(P1,O(4)), while the image of the four ambient
linear forms is span{s^4,s^3t,st^3,t^4}. Its missing section s^2t^2 cannot
lift through all neighborhoods, since full formal section extension would
make it an ambient linear form. Thus injectivity certainly does not imply
surjectivity or all-order liftability.

## 5. Counterchecks and exact limits

- Replacing C by a point destroys the section-extension conclusion:
  formal functions at a point contain arbitrary power series, whereas
  H0(P3,O)=k. Positive dimension and the divisor-intersection argument
  cannot be dropped.
- Replacing global sections of specified twists by unglued local
  generators destroys the proposed algebraization argument. Its stated
  hypotheses do not make this substitution.
- Keeping only formal topological support cannot replace power
  containment. A completion along C already has underlying space C even
  when completed local equations retain an attached residual branch.
- Generic transverse completion loses the residual factor t-y in the
  source's example (x,y^m(t-y)), while the closed-point completion retains
  it. The proposed full-formal detector does not conflate these data.
- A single colon J:I removes one generic layer and can retain C when
  m>1; saturation J:I^infinity removes the full C-primary component. The
  source distinguishes these operations correctly.

No source correction is required by this audit. The author was sent the
independent Lefschetz proof and the explicit missing-linear-section
control as optional explanatory additions. The inherited accepted
multiplicity detector and R-0020 were treated as premises and were not
re-run. No canonical result record or accepted mathematics was edited.
