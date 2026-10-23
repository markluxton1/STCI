# Residual-cycle criterion and wedge degeneracy — proof audit proposal

**Status:** Residual-cycle identity follows from standard intersection theory; the proposed global wedge obstruction remains open. This note has not received an independent audit.

**Scope:** Arbitrary characteristic. Let \(C\subset\mathbf P^3\) be an integral curve of degree \(c\), and let \(F,G\) be homogeneous forms of degrees \(d,e\) with no common surface component, both vanishing on \(C\).

## 1. Exact residual-cycle criterion

Put \(Z=V_+(F,G)\). Since \((F,G)\) is a regular sequence, \(Z\) is a pure one-dimensional Cohen–Macaulay complete intersection. Write

$$
[Z]=m_C[C]+R,\qquad
m_C=\operatorname{length}(\mathcal O_{Z,\eta_C}),
$$

where \(R\) is an effective cycle without \(C\) as a component. Bézout gives

$$
\boxed{de=c\,m_C+\deg R.}
$$

Consequently \(R=0\) if and only if \(Z_{\mathrm{red}}=C\): purity excludes isolated components. For the fixed rational quartic, \(c=4\), so

$$
\boxed{\deg R=de-4m_C.}
$$

For projective homogeneous ideals, the appropriate statement is \(\sqrt{(F,G)^{\mathrm{sat}}}=I_C\); do not silently replace this with an unsaturated radical equality.

If the full initial ideal of the generic local ideal \(J=(F,G)\) in \(k(C)[[x,y]]\) is known, its colength computes \(m_C\). Initial forms of the two generators alone need not generate this full initial ideal: cancellation and standard-basis completion can be essential.

## 2. What the wedge actually says

**Pointwise singularity.** At \(p\in C\), the differential of \(F\) is naturally a twisted conormal vector:

$$
dF(p)\in N_{C/\mathbf P^3,p}^{\vee}\otimes\mathcal O_C(d)_p.
$$

Because \(F|_C=0\), this is the entire ambient differential restricted to \(C\). The hypersurface Jacobian criterion therefore gives

$$
\boxed{dF(p)=0\quad\Longleftrightarrow\quad V(F)\text{ is singular at }p.}
$$

If \(dF|_C\equiv0\), then \(F\) vanishes to order at least two along \(C\), and \(V(F)\) is singular at every point of \(C\). The same applies to \(G\).

**Tangency of two smooth surfaces.** If both differentials are nonzero at \(p\), then

$$
\boxed{
dF(p)\wedge dG(p)=0
\quad\Longleftrightarrow\quad
T_pV(F)=T_pV(G).
}
$$

This is different from wedge vanishing because one differential is zero: that case is a singularity of at least one surface, not tangency between two smooth surfaces.

If the two first normal symbols are nonzero and proportional **at the generic point of \(C\)**, then the generic transverse intersection multiplicity satisfies \(m_C>1\). But this does **not** by itself force a residual component.

## 3. Two local models: thickness versus residual contact

Work over \(k[[t,x,y]]\) with \(C=V(x,y)\). The coordinate \(t\) runs along \(C\).

**Model A — only a thickened \(C\).**

$$
F=x,\qquad G=x+y^4,\qquad (F,G)=(x,y^4).
$$

Both differentials are the same nonzero vector along the whole curve:

$$
dF|_C=dG|_C=dx\ne0.
$$

Their wedge vanishes identically, yet the reduced support is only \(C\) and \(m_C=4\). There is no residual curve.

**Model B — a separate curve tangent at one point.**

$$
F=x,\qquad G=x+y(y-t^4),\qquad
(F,G)=(x,y(y-t^4)).
$$

Here the reduced intersection has two components,

$$
C=V(x,y),\qquad D=V(x,y-t^4).
$$

They meet at \(t=0\) with contact/intersection order four **inside the smooth surface** \(V(x)\). At \(t=0\), the two hypersurface differentials are both \(dx\), so their wedge vanishes there. But at the generic point of \(C\),

$$
dG|_C=dx-t^4dy,
$$

which is independent of \(dF|_C=dx\), and \(m_C=1\).

**Conclusion:** These models distinguish generic transverse thickness from residual-component contact at a special point. Wedge vanishing, even with both differentials nonzero, does not by itself tell us which phenomenon occurs. For the projective quartic the exact residual test is \(de>4m_C\).

## 4. Characteristic-zero versus characteristic-two benchmark

For

$$
F=x_1^4-x_0^3x_3,\qquad
G=x_2^4-x_0x_3^3,
$$

on the chart \(x_0=1\), put

$$
t=x_1,\qquad u=x_2-t^3,\qquad v=x_3-t^4.
$$

Then

$$
(F,G)=\bigl(v,(t^3+u)^4-t^{12}\bigr).
$$

In characteristic zero, \(m_C=1\), so the residual degree is \(16-4=12\). In characteristic two, \(m_C=4\), so the residual degree is zero. The two forms have no common surface factor: \(F\) is irreducible and does not divide \(G\). Thus the criterion establishes that the characteristic-two intersection has reduced support exactly \(C\), whereas the characteristic-zero intersection does not.

## 5. Open global question

When two integral surfaces containing \(C\) have **nonzero proportional first conormal symbols**, can global constraints on their degrees, on the divisor of the common normal direction, or on poles in higher cancellation relations force \(de>4m_C\)?

This is an investigation, not an established theorem. In particular, neither pointwise tangency nor generic proportionality alone implies a residual curve.
