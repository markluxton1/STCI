# Generic normal forms and saturation of relations

[Formal normal Framework](index.md) · [Original section addresses](from_symbols_to_equations.md)

## 3.1 Generic normal forms versus global relations

At the generic point of \(C\), first normal forms may share a factor even
when the original equations meet properly. In \(k(C)[[u,v]]\), the pair
\((u^2,u^2+v^3)\) has displayed orders \((2,2)\). The ideal equals
\((u^2,v^3)\), so its full normal initial ideal has minimal generator degrees
\((2,3)\).

[Chapter 2](../residual-construction/two_surfaces.md#21-generic-length-and-common-normal-directions)
relates the displayed orders to generic length. For a hypothetical
sole-support pair on \(C_0\), [P-006](../../arguments/normal-geometry/formal-normal-intersection.md#p-006)
forces a generic common normal factor. The [actual-CI bridge](actual_equation_module_and_ci_bridge.md#35-the-actual-complete-intersection-bridge)
additionally requires equal original orders, an everywhere jointly generated
saturated line relation, the full coprime binary initial ideal with gap at
least two, and a smooth full root.

The [unequal-order comparison](#unequal-orders-and-the-quotient-relation)
asks when the horizontal common divisor gives the saturated first relation of
the full initial ideal. The [normal-filtration account](normal_filtration_boundaries.md)
covers the separate comparison of initial equations with the filtered actual
equation module.

For the source comparison and its limits, see the [common-factor source audit](https://github.com/markluxton1/STCI/blob/af116e79e7dfee77d92e00d429faa304f411fad9/research/synthesis/COMMON_FACTOR_SOURCE_AUDIT.md).

### Horizontal common divisors and special-fiber defects

Let \(C\) be a smooth integral projective curve and \(\pi:E=\mathbf P_C(N)\to C\)
a ruled surface. Take nonzero sections \(a,b\) of invertible sheaves on \(E\).
For an actual pair, these can be the leading normal forms, obtained by
restricting the individually divided strict-transform equations to \(E\).
Write \(D=D_{\mathrm{hor}}+D_{\mathrm{vert}}\) for the divisorial gcd of
their zero divisors. The coefficient of each prime divisor in \(D\) is the
minimum of its coefficients in the two zero divisors. The horizontal
components dominate \(C\), and the vertical components are fibers.

If \(D_{\mathrm{hor}}\ne 0\), it is finite flat over \(C\), of degree equal
to the degree of the gcd of the two generic binary forms. Indeed,
\(D_{\mathrm{hor}}\) is an effective Cartier divisor on the smooth surface.
No fiber contains a curve of this divisor, as such a curve would be the
entire irreducible fiber. Thus the projective map to \(C\) is quasifinite and
hence finite. The Cartier divisor is Cohen–Macaulay and pure of dimension
one. With no vertical associated prime, a uniformizer of the base DVR is
a nonzerodivisor, so the finite module is flat. This gives the flat closure
of the full generic common divisor, with its multiplicities.

Divide out the canonical equation of \(D\). The resulting sections
\(a',b'\) have no common prime divisor, so \(T=V(a',b')\) is either empty
or zero-dimensional. Locally, the common ideal before division is
\(h(a',b')\) for an equation \(h\) of \(D\). The generic gcd therefore
misses both \(D_{\mathrm{vert}}\) and \(T\).

For example, on a ruled chart with base parameter \(t\) and fiber coordinate
\(z\), the pair \(a=tz, b=t(z+t)\) has common vertical divisor \(t=0\)
and a residual point at \(t=z=0\). Its generic gcd is trivial. In
characteristic different from two, \(a=z(z-t), b=z(z+t)\) gives the flat
horizontal section \(z=0\) and a residual point at \(t=z=0\).
These examples concern the first symbols on \(E\). They give no
decomposition of the intersection of the two strict transforms in the
blown-up threefold.

Under the [equal-order bridge](actual_equation_module_and_ci_bridge.md#35-the-actual-complete-intersection-bridge),
the two symbols are multiples of one global root form with coefficients
that jointly generate everywhere. Their common subscheme on \(E\) is
then exactly the root divisor. Smoothness of this divisor and the
full-initial-ideal hypotheses still require separate verification.

### Unequal orders and the quotient relation

When the full initial ideal has a saturated first line relation, determine
when its root divisor equals \(D_{\mathrm{hor}}\). An open first test is a
pair with unequal original normal orders and a proper common factor. Use
higher normal terms to control the second quotient relation, its
special-fiber evaluation divisor, and how \(D_{\mathrm{vert}}\) and \(T\)
affect the intersection of the individually divided strict transforms.
For sole support the strict transform of the original intersection scheme
is empty, since that scheme is supported on the blowup center.

[Historical source](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/synthesis/COMMON_DIRECTION_DEFECT.md).


## 3.2 Saturating the first relation

A generic first normal relation need not extend as a saturated, everywhere-generated line subbundle of \(\operatorname{Sym}^rN_C^*\). Its special fibers can acquire base points or quotient torsion. A **saturated** degree-\(r\) relation instead defines a full relative Cartier root divisor \(\mathcal R\to C\) in the exceptional ruled surface, retaining multiplicities and nonreduced fibers. In the balanced split case \(N_C^*=H^{-1}\otimes V\), this surface is \(C\times\mathbf P(V^*)\) and the root direction bundle is \(\mathcal O_{\mathcal R}(1)\). This root divisor is not automatically the common-direction scheme of arbitrary displayed equations. The [Picard criterion](../../results/spectral_root_picard_criterion.md) and [actual-CI bridge](../../results/actual_ci_smooth_root_bridge.md) impose their additional, different hypotheses.

## 3.3 The second relation lives in a quotient

A second independent graded relation is naturally defined **modulo multiples of the first**. It may fail to lift to a global polynomial line, even when it exists perfectly well as a line in the quotient. This is not merely a technicality: requiring such a global lift would exclude legitimate abstract graded configurations.

The established [spectral Picard criterion, STCI-R-0008](../../results/spectral_root_picard_criterion.md) applies when the conormal is balanced split, the first relation is saturated, and the second relation is required to be coprime to it in **every** fiber. For degree \(s>r\), it asserts that a second quotient relation exists exactly when
\[
\mathcal O_{\mathcal R}(s)\cong\pi^*M
\]
for some line bundle \(M\) on \(C\). Equivalently, the class of \(\mathcal O_{\mathcal R}(1)\) in \(\operatorname{Pic}(\mathcal R)/\pi^*\operatorname{Pic}(C)\) is killed by \(s\).

The criterion uses the Picard group of the **full** finite flat scheme, including nonreduced fibers. It constructs an abstract graded regular-sequence family, **not** a lift to the embedded formal neighborhood of \(C\), and not a pair of projective defining equations.

