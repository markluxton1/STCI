# Endpoint septic: independent two-common-root contact audit

Status: **PROVED conditional univariate support exclusion, characteristic zero.**
The proof below verifies the target-septic contact calculation directly. Its
geometric application requires the parent's separately audited assertion that
full inverse support forces all roots of this target septic to be common roots
of `U,V`. This note does not assert that global reduction independently.

## 1. Data and precisely stated conclusion

Work over an algebraically closed field of characteristic zero. Put

\[
\begin{aligned}
U&=2az^3-3bz^2-z+g,&V&=3az^4-4bz^3-2z^2-z+d,\\
A&=az-b,&H&=az^3+z-g-1,\\
J&=AV-(Az-1)U,&E&=J^2-(3zA-1)HJ+AUH^2,\\
C_b&=a^2g-ab-b^3.
\end{aligned}
\]

Assume `a C_b != 0`. Exact expansion gives degree seven in `z`, with leading
coefficient `a C_b`. Suppose additionally that the endpoint projection has no
point off the lifted curve mapping into the affine target curve. Then:

* At every common root of `U,V`, the multiplicity as a root of `E` is at most
  four.
* A common root with multiplicity four as a root of `E` is the only common
  root of `U,V`; moreover `U/(z-rho),V/(z-rho)` have no common root, even at
  `rho` itself.
* Consequently, if `U,V` have exactly two distinct common roots, every one of
  them has `E`-multiplicity at most three. Their total multiplicity is at most
  six, so the degree-seven `E` cannot have all its roots supported there.

No squarefreeness assumption is used. In particular, a repeated common root
does not evade the conclusion.

## 2. Common-root parameters and the exceptional H=0 fiber

At a common root `rho` set `w=a rho-b` and `q=w rho`. Solving the two
common-root equations gives

\[
b=a\rho-w,\quad g=a\rho^3-3w\rho^2+\rho,\quad
d=a\rho^4-4w\rho^3+2\rho^2+\rho.
\]

The exact carrier identity is

\[
C_b=w\bigl(a(1-3q)+w^2\bigr).
\]

Thus `w != 0`; this covers, and excludes on the present locus, the possible
exception `k=b-a rho=0` in the opposite sign convention.

Writing `c_j` for the coefficient of `(z-rho)^j` in `E`, exact expansion gives

\[
H(\rho)=3w\rho^2-1,\qquad
c_1=-H(\rho)\bigl(6q^2-6q+1+3wq\bigr).
\]

The factor `H(rho)` must not simply be divided away. At the fixed target
parameter `z=rho`, the two residual affine fiber equations are

\[
\begin{aligned}
F&=wT(-1+3q+w^2T),\\
G&=T\{6q^2-4q-w+1+(4\rho w^3-2w^2)T+w^4T^2\}.
\end{aligned}
\]

If `q != 1/3`, put `T_0=(1-3q)/w^2`. It is nonzero and

\[
F(T_0)=0,\qquad G(T_0)=T_0 wH(\rho),\qquad
1+aT_0=C_b/w^3\ne0.
\]

Thus `H(rho)=0` with `q != 1/3` yields an actual off-curve point in the affine
chart, contrary to the stated no-extra-support hypothesis. This does not
confuse a vanishing affine denominator with an actual fiber.

The remaining exceptional case `H(rho)=0,q=1/3` forces
`rho=1,w=1/3`. Exact expansion then gives `c_2=1/9`, independently of `a`.
Since `c_1=0`, its `E`-multiplicity is exactly two.

## 3. Parameterization of contact order at least two

It remains to consider `H(rho) != 0`. If `c_1 != 0`, the multiplicity is one.
Otherwise put `D=6q^2-6q+1`; the equation `c_1=0` gives

\[
w=-D/(3q),\qquad \rho=q/w.
\]

Both `q` and `D` are nonzero: `q=0` would leave the defining equation equal to
one, while `D=0` would force `w=0`. Further,

\[
H(\rho)=-\frac{(3q-1)(3q^2+3q-1)}D.
\]

Therefore `q != 1/3` and `3q^2+3q-1 != 0` on this branch. The exceptional
zeros of these factors have already been handled in Section 2.

Here `c_2` is affine linear in `a`, with slope

\[
-\frac{3q(3q-1)^2(3q^2+3q-1)}{D^2},
\]

which is nonzero on the branch. Consequently `c_2=0` forces exactly

\[
a=-\frac{D^2(54q^4-72q^3+15q^2-3q+1)}{27q^3(3q-1)^2}.
\]

There is no unexamined zero of the coefficient of `a` in this step.

## 4. Exact coprimality checks and maximum contact order

After substituting this value of `a`, let

\[
\begin{aligned}
N_9={}&8748q^9-20412q^8+18954q^7-8262q^6+1458q^5\\
&-252q^4+180q^3-66q^2+12q-1,\\
N_{11}={}&17496q^{11}-46656q^{10}+39366q^9-16848q^8\\
&+12123q^7-12231q^6+8316q^5-2934q^4+612q^3\\
&-129q^2+25q-2.
\end{aligned}
\]

The actual next coefficients are

\[
c_3=-\frac{(3q^2+3q-1)DN_9}{81q^4(3q-1)^3},\qquad
c_4=-\frac{D^2N_{11}}{81q^4(3q-1)^3}.
\]

The exact gcd of their numerators is a nonzero rational multiple of `D`.
Since `D != 0`, these coefficients cannot both vanish. Every common root
therefore has multiplicity at most four in `E`.

Let

\[
R_{\mathrm{other}}=\operatorname{Res}_z
\bigl(U/(z-\rho),V/(z-\rho)\bigr)
\]

after the same substitutions. A separate exact Sylvester determinant gives
the gcd of the numerator of `R_other` with the numerator of `c_3` as again a
nonzero rational multiple of `D`. All denominators in this calculation are
products of nonzero rational numbers, powers of `q` and powers of `3q-1`.
Thus `c_3=0` forces `R_other != 0`. This includes the possibility that the
quotients both vanish at `rho`: such a repeated common root would also force
the resultant to vanish.

Multiplicity four requires `c_1=c_2=c_3=0`. It therefore forces no second
common root. If there are two distinct common roots, both multiplicities are
at most three, and their sum is less than the degree seven of `E`.

## 5. Scope and captured evidence

The proof is a conditional local-contact and univariate-support exclusion.
The parent's global audit must still justify the target residual equations
and the necessary support condition for `E` across all affine and projective
boundary cases. This note supplies no bound from first-normal degree alone;
the bound follows from the actual higher coefficients `c_1` through `c_4`.

The independent source is
[two-root-contact-target.m2](../validation/2026-10-11-endpoint-support-global-audit/two-root-contact-target.m2).
The final captured execution passed **14 exact assertions**, checking the
septic leading coefficient, common-root substitution, first coefficient,
exceptional fiber, order-two exceptional case, second-coefficient slope,
solved value of `a`, and both polynomial gcd conclusions. See
[the final execution record](../validation/2026-10-11-endpoint-support-global-audit/two-root-contact-attempts/20261012T000753990549Z/execution-record.json)
and its adjacent source snapshot, stdout and stderr.

The same directory preserves an earlier 12-assertion PASS and an intermediate
failed assertion caused by using total polynomial degree in all coefficient
variables instead of degree in `z`. The final source checks the eighth
`z`-derivative and the seventh `z`-coefficient directly. These are development
executions of one audit source, not independent geometric cases.
