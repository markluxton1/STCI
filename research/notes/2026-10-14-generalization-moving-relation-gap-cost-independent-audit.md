# Independent audit: movement and saturation of the first normal relation

Date: 2026-10-14. Reviewer: root. Status: **PROVED** under the stated
balanced-normal and generic relation-rank hypotheses. This reviews new
Section 7 of [the thick extension](2026-10-13-generalization-thick-equality-extension.md).
It does not replay a previously accepted statement or computation.

Let `N_C=H tensor k^2` on a smooth integral projective curve, and let
the unique first generic initial relation have degree r. Write its
saturated line bundle and actual relation line as

```
W=H^-r tensor A^-1,    K_r=W(-D).
```

Here A is the pullback of `O(1)` by the projective binary-relation
direction map, so it is globally generated. Put `epsilon=deg A>=0`
and `delta=deg D>=0`. Let s>r be the next independent generic
relation degree. For every r<=j<s, the generic relation space is
the first relation times all normal forms of degree j-r.

Multiplication by a nonzero binary form on every fiber is injective.
Consequently

```
A_j=W tensor Sym^(j-r)N_C^*
```

injects into `Sym^j N_C^*` with constant fiber rank and locally free
cokernel. Its image is saturated. Since its generic span equals
that of K_j, it is exactly the saturation of K_j. Products of actual
degree-r relations give the other inclusion, hence

```
A_j(-D) subset K_j subset A_j.
```

Set `t_j=length(A_j/K_j)`. On a curve the inclusions give

```
0<=t_j<=(j-r+1)delta,   t_r=delta.
```

Since `rank A_j=j-r+1` and its degree is
`-(j-r+1)(j deg H+epsilon)`, the exact kernel/quotient degree formula
gives

```
Delta_j=(j-r+1)epsilon+t_j.
```

This retains the torsion of the actual normal-layer quotient. Summing
these identities, and using nonnegativity of the other layer defects,
proves

```
Delta >= epsilon(s-r)(s-r+1)/2 + delta.
```

For C0 the accepted exact socle budget therefore gives

```
n mu >= 7 Asym+epsilon(s-r)(s-r+1)+2delta.
```

No generic Gorenstein associated graded hypothesis is needed for this
inequality. A moving direction has epsilon>=1; a constant direction
has epsilon=0. On the constant branch, the separately accepted pole
constraints apply when s>=r+2. If s=r+1, the next independent relation
can absorb the quadratic obstruction; no such pole lower bound is
claimed there. This qualification was requested during review.

Thus movement pays a quadratic cost in the gap before the next
independent relation, while saturation pays its effective-divisor
cost. These are necessary global compatibility constraints and do not
bound all carrier degrees or all possible Loewy indices. The separate
moving-base differential operator in the owner note is a new exact
reduction with its own evidence; it is not used in this proof.
