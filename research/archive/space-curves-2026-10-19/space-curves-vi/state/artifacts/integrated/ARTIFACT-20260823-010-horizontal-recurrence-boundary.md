# Tenth intervention: boundary of a horizontal thick recurrence

Date: 2026-08-23

Operation: direct lead transfer attempt and negative-result integration.

## Question and reason for the pivot

The vertical order-one branch now has an exact recursive normal-bundle budget. The
natural anti-lock-in test was whether the same state variables could control a surviving
horizontal branch of an order-minimal thick pair. If so, the unbounded horizontal depth
on \(C_{1,n}\) might be confronted by a parallel upper recurrence.

Some divisor recurrences transfer, but the proposed state is insufficient. The next
horizontal multiplicity depends on higher normal jets that are invisible in the leading
tangent divisor. A resultant-only or tangent-root-only iteration would therefore repeat
the earlier error of treating admissible first-level data as a realizable contact tree.

## 1. Data that do transfer

Let \(X_i\) be a smooth threefold, \(C_i\subset X_i\) a distinguished smooth
section, and \(N_i=N_{C_i/X_i}\). Choose a line \(K_i\subset N_i\) corresponding
to a horizontal tangent direction, with quotient \(L_i=N_i/K_i\). After blowing up
\(C_i\), the next section has

\[
 0\longrightarrow K_i^*L_i\longrightarrow N_{i+1}
 \longrightarrow K_i\longrightarrow0.                 \tag{1}
\]

If a strict hypersurface \(F_i\) has generic normal multiplicity \(m_i\) along
\(C_i\), and \(M_i^F=\mathcal O_{X_i}(F_i)|_{C_i}\), then

\[
 F_{i+1}\sim\pi_i^*F_i-m_iE_i,
\qquad
 M_{i+1}^F=M_i^F K_i^{-m_i}.                            \tag{2}
\]

Thus, once a multiplicity sequence and path are known,

\[
 \deg M_h^F
 =\deg M_0^F-\sum_{i=0}^{h-1}m_i\deg K_i,               \tag{3}
\]

while

\[
 \deg N_h
 =\deg N_0-\sum_{i=0}^{h-1}\deg K_i.                    \tag{4}
\]

These are exact global bookkeeping identities and remain candidates for a future
proximity-plus-line-bundle obstruction.

## 2. Why the leading tangent form is insufficient

At the generic point of \(C_i\), use plane normal coordinates \(x,y\). Consider

\[
 f_r=y^p+x^{p+r},\qquad r\ge1.                           \tag{5}
\]

Every \(f_r\) has:

- the same multiplicity \(p\);
- the same leading tangent form \(y^p\); and
- the same tangent direction \(y=0\) with root multiplicity \(p\).

Blow up that direction by writing \(y=xv\) and dividing by \(x^p\). The strict
transform is

\[
 v^p+x^r.                                               \tag{6}
\]

Its multiplicity at the next infinitely-near point is

\[
 \min(p,r),                                             \tag{7}
\]

which can take every value from \(1\) to \(p\) while all leading tangent data in
(5) stay fixed.

The coefficient responsible for (7) lies in a higher normal graded piece, not in the
degree-\(p\) tangent form. Globalizing only the root line \(K_i\), its multiplicity in
the binary initial form, and the line bundles (1)--(2) therefore does not determine the
next state.

## 3. Contrast with the vertical order-one recurrence

For a surface generically smooth along \(C_i\), the first normal derivative is a
generically nonzero map \(N_i\to M_i\). Its closed-point zero divisor defines a
saturated kernel line, and that line gives an upper bound on the next Jaffe type even
though it does not determine it. This is what made the ninth intervention possible.

For a thick horizontal branch of order \(p>1\), the first derivative vanishes
identically. The leading section lies in

\[
 H^0\!\left(C_i,\operatorname{Sym}^pN_i^*\otimes M_i\right),
\]

but (5)--(7) show that this section alone cannot bound the next multiplicity sharply:
the relevant information is distributed through the higher normal jets

\[
 \mathcal I_{C_i}^{p+j}/\mathcal I_{C_i}^{p+j+1}.
\]

## 4. Correct next state and current lock

A valid horizontal recurrence must carry, in addition to (1)--(4), enough of one of the
following equivalent structures:

- the filtered normal jet of each equation along the chosen infinitely-near path;
- the corresponding Rees-algebra or valuation data;
- a cluster/proximity state recording which higher terms attain the next multiplicity;
  or
- a finite Newton polygon together with its global coefficient line bundles.

The tangent-cone degree budgets remain necessary, but they are only the first row of
this state. The multisection resultant controls a terminal transverse stage; it cannot
be iterated through an unresolved thick point without the missing jets.

## Research delta

- **Positive transfer:** the normal-bundle extension and hypersurface line-bundle
  recurrences (1)--(4) are exact along any chosen horizontal section.
- **Negative result:** multiplicity at the next point is not a function of the leading
  tangent form, its root multiplicity, or those line bundles. The family (5) is the
  minimal counterexample.
- **Prevented drift:** further resultant formulas using only successive tangent roots
  would not improve understanding; they would omit the state variable that determines
  whether contact actually persists.
- **Reframed thick target:** construct the smallest global higher-jet/proximity state
  compatible with (1)--(4), then ask whether a surface-effective threshold forces that
  state outside its degree budgets.
- **Reason to pause this branch:** no canonical finite truncation of the required
  higher-jet state has yet been justified. Computation at a fixed arbitrary truncation
  would test the truncation rather than the STCI problem.

## Evidence boundary

- The local example proves insufficiency of the proposed state; it is not evidence
  against existence of deep homogeneous pairs.
- Equations (1)--(4) assume one chosen section. Branched multisections require norm and
  ramification terms already recorded in the fourth intervention.
- A Rees/jet formulation is a direction, not an established obstruction in this
  research state.
