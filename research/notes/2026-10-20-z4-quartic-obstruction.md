# Integral obstruction for the prescribed Z4: independent calculation

Status: new exact calculation, independently reviewed on 2026-10-21; not
promoted. See [independent audit](2026-10-20-z4-lift-independent-audit.md) and
[full report](2026-10-20-z4-characteristic-zero-lifting-report.md).  This note does not rely on the
previous integral quartic-carrier exclusion or on previously recorded primitive
triple formulas.

Scope: the fixed curve `[s^4:s^3t:st^3:t^4]` over R=Z_(2) or R=Z_2.  Assume an embedded primitive
triple over the fixed curve has conormal line `O(-6)` and reduces to the
prescribed characteristic-two ribbon (raw direction `X=0, Y=epsilon`).  The
calculation proves this triple cannot exist.  A separate argument must show
that every admissible full Z4 lift supplies such a triple.

## Raw integral normal coordinates

Write `u=x1/x0`, `X=x3/x0-u^4`, `Y=x2/x0-u^3` and on the other chart
`c=x2/x3`, `A=x0/x3-c^4`, `B=x1/x3-c^3`.  Expansion of the exact rational
coordinate change gives

```
c = u^-1 + (u^-4 Y-u^-5 X) + (u^-9 X^2-u^-8 XY) + O((X,Y)^3),
A = 3u^-8 X-4u^-7 Y-9u^-12 X^2+16u^-11 XY-6u^-10 Y^2 + O(3),
B = 2u^-7 X-3u^-6 Y-5u^-11 X^2+9u^-10 XY-3u^-9 Y^2 + O(3).
```

The linear transition has determinant `-u^-14`.  At characteristic two it is
diagonal of degrees `-8,-6`; this integral frame avoids division by two in a
characteristic-zero balanced frame.

Trivialize the quotient line `L=O(-6)` by `epsilon` on U and `eta` on V,
with `eta=u^-6 epsilon` to first order.  Put `X=p(u)epsilon`,
`Y=q(u)epsilon`.  The opposite direction is

```
P(u^-1)=3u^-2 p-4u^-1 q,
Q(u^-1)=2u^-1 p-3q.
```

Requiring all four expressions to be regular on their charts gives exactly

```
p=a+b u+3h u^2,       q=d+2h u,
P=3a c^2+(3b-4d)c+h, Q=2a c+(2b-3d).
```

To see exhaustiveness, the equations on positive Laurent powers first imply
`2p_(j+1)-3q_j=0` and `3p_(j+2)-4q_(j+1)=0` for `j>0`.
Their coefficient determinant is a unit (`9-8=1`), eliminating all higher
terms.  The remaining relation `2p_2=3q_1` has exactly the parameterization
`p_2=3h,q_1=2h`, since three is a unit.  Thus all quotient variations are
included, before imposing the basepoint-free open condition.  The prescribed
special ribbon requires `a,b,h in 2R` and `d in R^times` with `d=1 mod 2`
after scalar trivialization.  The impossibility below holds on this entire
parameter space, so imposing basepoint-freeness adds no loophole.

## Exact triple cocycle and all quadratic corrections

Set `m_U=qX-pY`, `m_V=Q(c)A-P(c)B`.  Its linear transition is
`m_V=-u^-8 m_U`.  For a general local primitive triple write

```
X=p epsilon+r epsilon^2, Y=q epsilon+s epsilon^2,
eta=u^-6 epsilon+t epsilon^2, epsilon^3=0.
```

Here `r,s,t` are arbitrary local functions.  Equivalently the two local
equations for the line kernel are `m_U=gamma_U epsilon^2` and
`m_V=gamma_V eta^2`.  The exact ambient transition gives

```
m_V = -u^-8 m_U + Kfull epsilon^2,
u^8 Kfull = gamma_U(u)+u^-4 gamma_V(u^-1).
```

The quadratic remainder `m_V+u^-8 m_U`, denoted `Kfull epsilon^2`,
is independent of `r,s`; the quadratic parameter
change `t` disappears because it is multiplied by an additional epsilon.
The functions `gamma_U,gamma_V` range over the whole local correction
space.  Consequently the actual obstruction is the class of `K=u^8 Kfull`
in

```
R[u,u^-1] / (R[u]+u^-4 R[u^-1]) = H^1(P1_R,O(-4)),
```

with free basis `u^-1,u^-2,u^-3`.  It is the extension class for the kernel
line `M=O(-8)` against `L^2=O(-12)`; the sheaf is derived here from the
explicit embedded transition rather than postulated.

The complete Laurent expression is

```
K = 3a^3/u^5 + (9a^2b-12a^2d)/u^4
    + C3/u^3+C2/u^2+C1/u+3bh^2+3h^3u,
C1 = h(ah+3b^2-5bd+3d^2),
C2 = (b-d)(4ah+3b^2-8bd+6d^2),
C3 = a(ah+9b^2-23bd+15d^2).
```

For `a,b,h` even and `d` odd, `C2` is congruent to `2` modulo four: its
second factor is `2` modulo four and its first factor is odd.  Thus this
free cohomology class cannot vanish over `Z_(2)` or `Z_2`, over either of these specified bases. Ramified DVRs with a different
uniformizer are outside the stated parity argument.  Even the
necessary equations over `Z/4` are inconsistent.  This is one finite
integral identity, not a sequence of inconclusive lifts.

Changing the generator of `L` scales the cocycle by a unit and may change
its representative by the displayed coboundaries.  Every local quadratic
coordinate change is already covered by `r,s,t,gamma_U,gamma_V`.  Therefore
these freedoms cannot remove the obstruction.  Generator changes of the
full ideal have no effect on this intrinsic quotient and its extension.

## Reproduction and verification boundary

```
python3 -m venv /tmp/stci-z4-env
/tmp/stci-z4-env/bin/pip install -r research/computations/requirements-z4-2026-10-20.txt
/tmp/stci-z4-env/bin/python research/computations/verify_z4_quartic_obstruction_2026_10_20.py
```

The script reconstructs the rational coordinate changes with arbitrary
quadratic corrections, verifies their cancellation, checks every Laurent
coefficient and the uniform polynomial congruence modulo four.  The
global-family-to-triple reduction, existence of relative line bundles and
primitive filtrations, and the exhaustiveness proof above are mathematical
arguments, not claims certified by symbolic expansion alone.

The initial development run extracted an epsilon coefficient before expanding
a product and failed its correction-cancellation assertion. The code now
expands the entire expression before coefficient extraction; its final run and
the independent integer Macaulay2 reconstruction both pass. No failed run is
used as evidence for an algebraic assertion.
