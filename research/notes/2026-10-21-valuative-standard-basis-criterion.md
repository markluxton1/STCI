# Valuative standard-basis test — audited local criterion

**Status:** Local algebra criterion checked on 2026-10-23; working research note, not independently promoted to a canonical result. The standard-basis and valuation program remains exploratory.

## Setup and definitions

Let \(p\) be a closed point of a smooth curve \(C\), and work in completed local coordinates

$$
B=k[[t]],\qquad R=B[[x,y]],\qquad J=(F,G)\subset(x,y),
$$

where \(F,G\) form an \(R\)-regular sequence and \(C=V(x,y)\). Write \(A=R/J\). Define the **generic transverse length along \(C\)** by

$$
m_C=\operatorname{length}_{K[[x,y]]}
\bigl(K[[x,y]]/(F,G)\bigr),\qquad K=k((t)),
$$

where the coefficients are extended to \(K[[x,y]]\) via the generic formal neighborhood of \(C\). Define the **special transverse length** by

$$
\lambda_p=\operatorname{length}_{k[[x,y]]}
\bigl(k[[x,y]]/(F(0,x,y),G(0,x,y))\bigr),
$$

allowing \(\lambda_p=\infty\).

**Important distinction:** Define \(\rho_p=\dim_K(A\otimes_BK)\) when \(A\) is finite over \(B\). The number \(m_C\) measures only the component \(C\) at its generic point, whereas \(\rho_p\) measures the entire generic fiber and can include residual components through \(p\). The rings \(R[1/t]\) and \(K[[x,y]]\) are different: the latter is the completion of the former at its \((x,y)\)-adic maximal ideal. Thus \(m_C\) is the length of the completed local factor at \(C\), not automatically the total generic-fiber dimension.

## Criterion

Under the setup above,

$$
\boxed{\lambda_p=m_C<\infty
\quad\Longleftrightarrow\quad
V(J)\text{ has no residual reduced curve component through }p.}
$$

More precisely, if \(\lambda_p<\infty\), then

$$
\boxed{
\lambda_p=\rho_p=m_C+
\sum_{D\ne C}\operatorname{length}(\mathcal O_{V(J),\eta_D})\,
\deg(D\longrightarrow\operatorname{Spec}B),
}
$$

where the sum is over the other one-dimensional components of the formal local scheme through \(p\), and the degree is the finite generic-fiber degree over \(K\). The formula counts components after passing to the generic fiber; it does not assume they are geometrically irreducible. If \(\lambda_p=\infty\), the finite-length comparison is unavailable, and in this complete-intersection setup a residual component lies in the special fiber.

### Proof

Assume \(\lambda_p<\infty\). Since \(A/tA\) is Artinian, the formal finiteness/Weierstrass theorem (equivalently, topological Nakayama plus completeness) makes \(A\) a finite \(B\)-module. The ring \(A\) is one-dimensional Cohen–Macaulay because \(F,G\) form a regular sequence in the three-dimensional regular local ring \(R\). Since \(A/tA\) is zero-dimensional, \(t\) is a parameter and therefore a nonzerodivisor on \(A\). Thus \(A\) is finite torsion-free, hence finite free, over the DVR \(B\). It follows that

$$
\lambda_p=\dim_k(A/tA)
=\operatorname{rank}_B(A)
=\rho_p=\dim_K(A\otimes_BK).
$$

The finite generic fiber \(A\otimes_BK\) is Artinian. Its localization at the maximal ideal corresponding to \(C\), followed by completion, identifies with \(K[[x,y]]/(F,G)\); its \(K\)-dimension is \(m_C\). The other Artinian local factors correspond to residual components through \(p\) and have positive \(K\)-dimensions, incorporating residue-field degrees. This localization/completion step is essential: one must not identify \(R[1/t]\) with \(K[[x,y]]\). This gives the formula and shows that \(\lambda_p=m_C\) exactly when there is no other curve component.

If \(\lambda_p=\infty\), then \(A/tA\) has positive dimension. Since \(A\) is one-dimensional Cohen–Macaulay and has no embedded associated primes, some one-dimensional component lies in \(t=0\). It cannot be \(C\), on which \(t\) is a parameter, so it is residual. Conversely, absence of residual components means \(\sqrt J=(x,y)\) locally; then \(A\) is finite over \(B\) and the preceding argument yields \(\lambda_p=m_C\).

This is a **local** statement; it does not claim that arbitrary initial factors lift to global algebraic components without further work.

## Exact example: special-length jump

Take

$$
F=x^2,\qquad G=x^2+ty^3+y^4.
$$

Then

$$
J=(x^2,y^3(t+y)).
$$

At the generic point of \(C\), \(t+y\) is a unit in \(K[[x,y]]\), giving

$$
m_C=\operatorname{length}K[[x,y]]/(x^2,y^3)=6.
$$

At \(t=0\),

$$
\lambda_p=\operatorname{length}k[[x,y]]/(x^2,y^4)=8.
$$

The additional curve \(D=V(x,t+y)\) has generic multiplicity two (the \(x^2\) direction), so its contribution is exactly \(8-6=2\).

## Standard bases, valuations, and limitations

Compute a local standard basis of \(J\) in the generic formal neighborhood of \(C\) to obtain \(m_C\), and separately compute one in the special fiber to obtain \(\lambda_p\). The colength of each certified monomial initial ideal equals the corresponding finite length. **Do not specialize a generic standard basis naively:** leading coefficients may vanish at \(t=0\), changing the initial ideal and its colength.

Weighted initial forms and cancellation relations, such as \(G-F=y^3(t+y)\) in the example, help expose the jump. Ordinary tropicalization of a zero-dimensional scheme supported at the origin in the torus is empty and does not retain this length information. Use local standard bases, multiplicity-sensitive weighted initial ideals, or tropical schemes instead.

For the fixed rational quartic, a global STCI pair has no residual components, hence satisfies \(\lambda_p=m_C\) at every smooth point \(p\) after passing to appropriate completed local coordinates. This is a **necessary local test**, not a new global numerical exclusion.

**Open direction:** Relate the local jumps and their valuation data to global conormal sections, poles of cancellation coefficients, and degree constraints without assuming that a factor of an initial polynomial lifts to a separate component.
