# Explicit triple-quartic residual example: exact finite checks

Date: 2026-10-26. Status: coordinate evidence for a new residual-cycle calculation; no canonical promotion.

Run from the repository root, using Python's standard library only:

```sh
python3 research/computations/verify_44_triple_residual_example_2026_10_26.py
```

The script writes [checks.json](checks.json), including its own SHA-256. It uses exact rational arithmetic in `Q[r]/(12*r^2+4*r+3)`. Expected terminal output starts with `PASS: 15 exact finite checks`.

The displayed quartics are inherited from the accepted [primitive-triple pencil audit, section 4](../../notes/2026-10-07-session-mf6-e1-independent-audit.md):

\[
R_0=x_0^3x_3-(r+3/2)x_0^2x_1x_2+(r+1/2)x_1^4,
\]
\[
R_1=x_0x_3^3+(r-7/6)x_1x_2x_3^2+(1/6-r)x_2^4.
\]

The new calculation puts `p=x2/z^3`, `q=x3/z^4` on `x0=1`, `z=x1!=0`, eliminates `q=(r+3/2)p-(r+1/2)`, and checks

\[
R_1/z^{12}=(p-1)^3\bigl((1/6-r)p+(r+1/2)^3\bigr).
\]

The residual root is

\[
\kappa=(2r-3)/(18r-3),\qquad \eta=-\kappa/3,
\qquad 27\kappa^2-14\kappa+3=0.
\]

Thus the candidate residual component is the smooth diagonal image
\(C_\kappa=[s^4:s^3t:\kappa st^3:\eta t^4]\), on the different quadric \(3x_0x_3+x_1x_2=0\). The script checks both parametrizations, their nonzero and distinct coefficients, and their endpoint intersection ideals. At either endpoint the latter have generators of orders three and four, so the scheme intersection length is three. It also expands the explicit first normal coefficients, checks the global gradient identity \(\nabla R_0|_C=s^8v\), \(\nabla R_1|_C=(2r+2/3)t^8v\) for a nowhere-zero vector v, and checks that a representative general pencil member has eight simple first-symbol roots. The general nonzero-coefficient case follows by the same elementary derivative argument.

The script does not reconstruct the inherited classification of primitive triples or prove the previous sole-support exclusion. It does not claim to classify all multiplicity-three pairs.

The global proof is separate from the finite identities: `R0` is primitive linear in `x3`, with coefficient `x0^3` coprime to the constant coefficient because `r+1/2!=0`; hence it is irreducible. `R1` is not proportional to it, so the pair is proper. On the dense chart it has triple `C` and simple `C_kappa`. Their degrees already total sixteen. Complete-intersection purity and degree therefore give the full cycle `3[C]+[C_kappa]`, without extra endpoint-supported curve components. Smoothness of `C_kappa` follows from its nonzero diagonal coordinate scaling. First-symbol roots detect carrier singularities by the differential criterion; the script does not certify an analytic `A2` normal form.
