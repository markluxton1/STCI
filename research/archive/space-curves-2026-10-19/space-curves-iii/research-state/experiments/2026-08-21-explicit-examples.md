# Initial explicit checks

Date: 2026-08-21  
Move: `MOVE-20260821-003`  
Script: `explicit_examples.py`

## Environment

No computer-algebra system was installed in the workspace. SymPy was installed into a temporary directory, and the durable script was then run with that temporary package on `PYTHONPATH`. The experiment is limited to polynomial substitution and factorization; claims about radicals are completed by the short hand arguments recorded below.

## Output

```text
rational quartic substitutions: [0, 0, 0, 0]
q,g on residual line x=y=0: [0, 0]
q,h on residual line z=w=0: [0, 0]
ruled cubic partials: [z**2, -2*w*y, 2*x*z, -y**2]
ruled cubic singular-line check y=z=0: [0, 0, 0, 0]
cuspidal normalization Cartier identity: (U - V**4)**3
cuspidal conductor restriction modulo x=y=tau^2=0: 3*tau*z**2 - z**4
twisted cubic substitutions: [0, 0]
twisted cubic x=1 patch after q1: -(u**3 - v)**2
```

## Interpretation

For the twisted cubic, take

\[
q_1=xz-y^2,
\qquad
F=z(yw-z^2)-w(xw-yz).
\]

On the affine patch \(x=1\), the equation \(q_1=0\) gives \(z=y^2\), and then
\(F=-(w-y^3)^2\). Hence the reduced common zero locus on this patch is the twisted cubic. On \(x=0\), the two equations force \(y=z=0\), giving only the endpoint \([0:0:0:1]\). This verifies the two-equation set-theoretic certificate.

For the rational quartic, the natural pair

\[
q=xw-yz,
\qquad
g=y^3-x^2z
\]

also contains the line \(x=y=0\). On the smooth quadric \(Q\), the quartic has bidegree \((1,3)\), while a cubic section has class \((3,3)\); the residual class is \((2,0)\), so this line occurs with multiplicity two. The symmetric pair \((q,h)\) leaves the opposite ruling. This is a structural failed construction, not an artifact of the chosen coefficients.

## Cuspidal cubic cone: normalization succeeds, conductor fails

On the affine chart \(w=1\), the cuspidal cubic \(g=y^3-x^2z=0\) has

\[
A=k[z,za^2,za^3]
  =k[z,y,x]/(y^3-x^2z).
\]

Its normalization is

\[
B=k[z,za,za^2,za^3].
\]

Equivalently, using a cyclic index-three cover, set

\[
z=V^3,\qquad \tau=UV^2,\qquad y=U^2V,\qquad x=U^3.
\]

The lifted rational quartic is the image of \(U=V^4\). The semi-invariant
\(U-V^4\) has weight one, so its cube descends to \(B\):

\[
F=(U-V^4)^3=x-3yz+3\tau z^2-z^4.
\]

Thus \(3\widetilde C\) is Cartier on the normalization. In divisor-class
notation, if \(R\) is a ruling then \(H=3R\) and
\(\widetilde C=4R\), hence \(3\widetilde C=4H\).

The conductor preimage is the double line

\[
\Gamma=(x,y,\tau^2).
\]

On \(\Gamma\),

\[
F=-z^4+3\tau z^2=-z^4(1-3\tau/z^2).
\]

After removing the pullback divisor \(-z^4\) from the reduced conductor
line, the remaining nilpotent unit represents the polar part
\(-3z^{-2}\) in the additive conductor quotient
\(W=z^{-1}k[z^{-1}]\). It is nonzero, and \(W\) is torsion-free in
characteristic zero. Consequently no positive multiple of
\(3C-4H\) vanishes in \(\operatorname{APic}(X)\): the normalization
proportionality does not descend through the conductor.

This calculation is made with the coordinate orientation of
\(y^3-x^2z\). It is the coordinate-permuted version of the cuspidal-cone
normalization and double-line conductor in Hartshorne--Polini, Example 6.9.

## Ruled cubic: local torsion succeeds, normalization fails

The other generator

\[
p=xz^2-y^2w
\]

defines a ruled cubic whose singular locus is the line \(y=z=0\), as the
displayed partial derivatives verify. The rational quartic meets this line
at its two endpoints. On the normalization \(S\simeq
\operatorname{Bl}_P\mathbf P^2\), write divisor classes as
\((a,b)=a\ell-be\). Then

\[
H=(2,1),\qquad \Gamma=(1,0),\qquad \widetilde C=(2,0).
\]

The two intersection points are pinch points, whose local almost-Cartier
groups are \(\mathbf Z/2\); the local torsion test therefore passes. But
\(r(2,0)=m(2,1)\) has no positive solution, so the global pullback class on
the normalization already forbids \(rC=mH\) in \(\operatorname{APic}(X)\).

These two cubics therefore fail for complementary reasons: the cuspidal
cone has the right global class after normalization but a non-torsion
conductor defect, while the ruled cubic has torsion-compatible local
singularities but the wrong global normalization class.

## Limitations

- No primary decomposition was computed.
- The script does not search over arbitrary equations or degree pairs.
- The residual-divisor conclusion uses the standard identification \(Q\simeq\mathbf P^1\times\mathbf P^1\), not only the substitution output.
- The conductor computation uses the exact sequence and identification of
  the additive group \(W\) in Hartshorne--Polini, not only symbolic expansion.
- The ruled-cubic class notation and pinch-point description use the
  normalization analysis in Hartshorne--Polini.
