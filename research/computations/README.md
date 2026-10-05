# Exact computation checks

The fourteen scripts in this directory, together with the preserved mixed-degree
script under `../scratch/degree6`, use exact symbolic arithmetic in SymPy;
they do not use floating point calculations.

- `verify_c0.py` checks the parametrization ideal, the characteristic 2 and 3
  radical pairs, the uniform positive-characteristic family in characteristics
  2, 3, 5, and 7, coordinate saturations, and wrong-characteristic controls.
- `verify_normal_bundle.py` checks the two-chart conormal transition, its
  extension class, an independent Jacobian-syzygy determinant, and the local
  characteristic-3 primitive triple.
- `verify_primitive_obstruction.py` checks the quadratic transition jet used
  in the Banica--Forster obstruction calculation.
- `verify_all_quartic_primitive_obstruction.py` checks the marked
  degree-three-map normal form, the six homogeneous obstruction coordinates,
  and the non-incidence identities that eliminate primitive triples for every
  characteristic-zero smooth rational quartic.
- `verify_positive_quartic_descent.py` checks the cusp semigroup lemma,
  representative Frobenius-descent supports, and the exceptional
  characteristic-3 normalization identities used in P-012.
- `verify_degree6.py` checks the degree-six symbolic square, its five
  residual classes on the quadric, the cubic symbolic-power boundary, an
  integral sextic singular exactly along the curve, and the first-normal
  discriminant/resultant calculations.
- `verify_chow_form.py` checks a compact 10-term Pluecker-coordinate formula
  for the Chow form of \(C_0\) against the exact 64-term binary resultant of
  two hyperplane pullbacks. It also verifies Pluecker degree four and
  coefficient bidegree \((4,4)\).
- `verify_typeb45_endpoint_certificate.py` checks the terminal rational
  identity at the proposed dense type-B survivor and the exact Bezout
  certificate excluding the proposed boundary survivor.  Its scope is
  intentionally narrower than the mathematical proof: it does not derive the
  transition recursion, justify Cech reductions, or prove chart exhaustion.
- `verify_chow_pencil_45.py` checks the exact dimensions and bases of the
  restricted carrier spaces excluded by one Schubert-line pencil, including
  the stronger 13-dimensional quartic and 28-dimensional quintic spaces.  It
  also checks the Chow restriction, coefficientwise resultant orders, and an
  explicit irreducible-quartic pair that passes this pencil but fails the
  reversed pencil.  It does not certify the full Grassmannian identity.
- `verify_typeb45_boundary.py` independently reproduces the full moving-frame
  obstruction on the \(b_0=0\) type-B boundary, including all six Cech
  coordinates and the characteristic-zero unit certificate.  It takes the
  lower Bănică--Forster delta/gamma chart data as input and does not cover the
  distinct rank-zero corner \(a_0=b_1=0\).
- `verify_typeb45_corner.py` checks the full moving-coordinate
  second-order coefficient, the three rank-zero parameters, and a bounded
  gamma-gluing calculation at the formerly missed corner.  Its final
  length-four statement counts a displayed monomial basis rather than
  deriving a Gröbner basis; the exhaustive proof uses
  \(H^0(O_{\mathbf P^1}(-3))=0\) and the elementary quotient
  \(k[m,\ell]/(m^2,m\ell,\ell^3)\).
- `verify_localcoh_degree4_counterexample.py` checks membership in
  \(I_{C_0}\), the nonconstant proportional first-symbol rows, the two exact
  polynomial identities, and generic coprimality over \(\mathbb Q(\lambda)\).
  It does not construct or assert a common local-cohomology ancestor.
- `verify_localcoh_degree4_allstage_certificate.py` checks P-043's two sparse
  coefficient functionals for stages \(N=2,\ldots,8\): annihilation of all
  correction and boundary spaces, target value \(-1\), and exact compatibility
  with multiplication by \(qB\).  The written proof is uniform in \(N\); this
  finite exact check does not classify other degree-four pairs.
- `verify_split22_boundary_survivor.py` checks the content-free
  \(d=1,[2,2]\) two-ramified-root first-normal survivor, including both factor
  evaluations and all eleven sextic normal-image equations.  It does not
  construct an ambient integral sextic or a mate.
- `../scratch/degree6/verify_mixed45_reduction.py` checks the quartic and
  quintic first-normal maps for the \((4,5)\) problem, the two allowed gcd
  strata, and, after assuming the regular-ratio missing-section normalization,
  exact augmented-minor exclusions for three carrier families. It does not
  prove that the ratio is regular or cover the newly separated pole strata.
  Its SHA-256 at handoff is
  `862ec150664459fc94187164bcaa1d25e87c5f815e589fff1608a28efc6a89d5`.

Run them with a Python environment containing SymPy:

```sh
python3 research/computations/verify_c0.py
python3 research/computations/verify_normal_bundle.py
python3 research/computations/verify_primitive_obstruction.py
python3 research/computations/verify_all_quartic_primitive_obstruction.py
python3 research/computations/verify_positive_quartic_descent.py
python3 research/computations/verify_degree6.py
python3 research/computations/verify_chow_form.py
python3 research/computations/verify_typeb45_endpoint_certificate.py
python3 research/computations/verify_chow_pencil_45.py
python3 research/computations/verify_typeb45_boundary.py
python3 research/computations/verify_typeb45_corner.py
python3 research/computations/verify_localcoh_degree4_counterexample.py
python3 research/computations/verify_localcoh_degree4_allstage_certificate.py
python3 research/computations/verify_split22_boundary_survivor.py
python3 research/scratch/degree6/verify_mixed45_reduction.py
```

On 2026-09-30 all 15 script executions passed sequentially under the temporary environment
`/private/tmp/stci-cas-venv/bin/python`.  Both the system Python and the bundled
workspace Python failed before running any assertion because SymPy was not
installed.  The proofs recorded in `../RESEARCH_RECORD.md` do not rely on the
continued existence of that temporary environment.
