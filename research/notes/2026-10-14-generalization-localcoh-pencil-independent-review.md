# Independent review of the observable corank-one pencil theorem

Date: 2026-10-14. Reviewer: root. Status: **PROVED under the stated exact
rank hypotheses**. This reviews the new abstract theorem in
[the polynomial-dual note](generalization-localcoh-dual-lemma.md), not
any previously accepted tensor computation.

For a field `K`, consider `L(lambda)=(lambda I_q+A; B)` with
`rank B=q-1` and `rank(B;BA)=q`. These hypotheses give a generator
`h` of `ker B` with `h,Ah` independent. If the lower target is outside
`im B`, a constant normalized left dual excludes it. Otherwise choose
`Bc=w`. Every prospective solution has the form `c+t h`. After a
constant basis change making `h=e1,Ah=e2`, and choosing `c1=0`, its
top equation is exactly

```
t(lambda e1+e2)=p-lambda c,  p=v-Ac.
```

Eliminating `t` gives the `q-2` linear equations
`p_j-lambda c_j=0` for `j>=3`, and the single quadratic
`p1-lambda p2+lambda^2 c2=0`. The direction `lambda e1+e2` never
vanishes, so these equations are sufficient as well as necessary,
including every finite geometric parameter value.

For a matrix `D` with `DB=diag(0,1,...,1)` and `Dw=c`, each row
`t` annihilating `lambda h+Ah` defines the left dual

```
(t, -t(lambda I_q+A)D).
```

Direct multiplication gives zero on `L`, and evaluation on the target
gives `t(p-lambda c)`. Rows `e_j` give the linear residuals with dual
degree at most one; `e1-lambda e2` gives the quadratic with dual
degree at most two. If the linear residual ideal is the unit ideal,
constant coefficients already produce one. If it has a common
linear factor, division of the quadratic by that factor gives the
stated Bezout identity with coefficient degree at most one. If all
linear residuals vanish identically, exclusion requires the quadratic
to be a nonzero constant. Thus full geometric exclusion is equivalent
to a normalized polynomial dual of degree at most two. The bound is
complete on this locus, not a guess about a syzygy search.

I also checked the note's rank-drop counterexample and determinantal
fallback. At an unobservable point the specialized left kernel can
grow, and normalized global polynomial duals need not detect an
exclusion there. The rank-stratified minor ideals retain this
exception. Over a parameter ring, the field rank hypotheses and any
pivots must be certified throughout the stratum; a generic matrix
calculation is insufficient.

This review accepts the abstract algebra and its finite-dimensional
reduction. It does not certify any particular family-two exceptional
field computation, any unrecorded rank stratum, the projective lift
at infinity, or the full ancestor incidence. Those applications have
separate evidence records.
