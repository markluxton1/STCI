# Independent review: the actual transverse first layer and global socle

Date: 2026-10-14. Reviewer: root. Status: **PROVED under the owner's
explicit hypotheses, in every characteristic**. The reviewed source is
[the transverse-differential theorem](2026-10-14-generalization-transverse-differential-socle-bound.md).
The accepted socle-duality theorem and C0 normal splitting are inputs;
neither was recomputed.

The carrier must be regular at the generic point of the smooth support.
Its full normalization inverse support must be a singleton degree-one
smooth curve c that is Cartier upstairs. These hypotheses give a global
normal differential from `O_c(c)` to `N_C/P3`; the source surface is
regular along c. Saturating its generically nonzero image gives
`B=O_c(c)(A)` for its actual common-zero divisor A.

I independently reconstructed the first-layer identification. The
quotient of `I_C/I_C^2` by the actual first symbols of both equations
is `J/J^2`. Generic carrier regularity makes its generic quotient the
single normal direction inside the carrier. Removing torsion saturates
its kernel, and a saturated kernel is determined by its generic
subspace. This kernel is exactly the annihilator of B, hence
`(J/J^2)_tf=B^*=O_c(-c)(-A)`. This is an identification of the full
actual first layer, not a replacement by the derivative at one point.

Generic curvilinearity of length `n=ab/deg C` gives `J^n=0` everywhere
by Cohen--Macaulay purity. The top ideal `J^(n-1)` has no point torsion
and lies in the actual socle. Multiplication through the first layer
kills its torsion in every input and gives a generically nonzero map
of line bundles

```
O_c(-(n-1)c)(-(n-1)A) -> J^(n-1) -> omega_C(4-a-b).
```

Its degree inequality, using `c^2=deg(C)^2/a` and `n c^2=b deg(C)`,
is exactly

```
(n-1)deg A >= deg(C)(a-4)+deg(C)^2/a-(2g(C)-2).
```

The proof keeps the entire top-socle inclusion; its finite-point defect
can only strengthen the inequality. For C0 the image line cannot
exceed degree seven in `O(7)^2`, so the three Cartier-lift targets
have precisely the owner's bounds: degree8 requires
`1<=deg A<=5`, `(2b-1)deg A>=20`; degree16 requires
`1<=deg A<=6`, `(4b-1)deg A>=51`. The mate lower bounds for A of
degrees one and two follow by integer rounding and are correct.

This accepts the written theorem and those necessary consequences.
It neither bounds mate degree above nor proves a surviving projection
exists. The generic regularity, Cartier-lift and singleton assumptions
are essential; rank-two first layers in entirely thick cases and
non-Cartier lifts remain outside the argument. The optional conductor
intersection interpretation needs its additional duality hypothesis
and is not used to prove the inequality.
