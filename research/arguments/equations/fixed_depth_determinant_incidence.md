# Fixed-depth equation incidence and actual residual controls

**Scoped independent reconstruction (2026-11-23):** FD1–FD3 were checked as
scheme statements over every field, including universal factorization over
nonreduced coefficient rings. FD4–FD7 were independently reconstructed in
characteristic zero, including both Laurent windows, the explicit correction,
all bounded fixed homogeneous tests, and the residual-support conclusion.
The center-jet surjectivity and universal source-depth theorem remain inherited
inputs. No unrestricted exclusion or full translated-cycle realization is claimed.
The normal-carrier and reduced-intersection extension in Section 5 received
independent correctness and geometric reconstruction, including both degree
bounds and the affine-coset Bertini argument.

This note separates two facts. In sufficiently large degrees, imposing
containment of the quartic changes a fixed determinant incidence only by an
affine-space factor. In characteristic zero there are explicit proper pairs
through that quartic, with residual curves, on which every bounded collection
of characteristic tests from fixed containing surfaces vanishes. Neither fact
decides the full growing-degree incidence.

The inputs are the characteristic-free
[center-jet calculation](../torus/chow_matched_equation_layers.md#sharpness-and-the-last-missing-center-layer)
and [universal finite source-depth theorem](../torus/fixed_surface_and_endpoint_algebras.md#the-whole-characteristic-tower-has-finite-source-depth).
The original set-image statement is
[HJ8–HJ9](global_equation_jets.md#fixed-determinant-truncations-forget-containment-of-the-quartic-in-large-degrees).
The proofs below strengthen that statement and supply actual residual controls;
the norm, characteristic-polynomial and Newton identities are classical inputs.

## 1. The common finite-jet source

Let
\[
 S=k[x_0,x_1,x_2,x_3],\qquad
 C=[s^4:s^3t:st^3:t^4],\qquad P=(x_0,x_3),\qquad M=V_+(P).
\]
For degrees \(a,b\), write \(V=S_a\times S_b\),
\(V_C=(I_C)_a\times(I_C)_b\). The open \(\mathcal U\subset V\)
where the restrictions to \(M\) have nonzero binary resultant consists of
proper pairs whose intersection is finite flat over the pencil
\([x_0:x_3]\). Put \(\mathcal U_C=\mathcal U\cap V_C\).

For \(N\ge1\), let
\[
 Q_N=(S/P^N)_a\times(S/P^N)_b,
 \qquad Q_N^\circ=(Q_N)_{\operatorname{Res}\ne0}.
\]
If \(a,b\ge N+2\), both linear projections \(V\to Q_N\) and
\(V_C\to Q_N\) are onto. The sharp semigroup proof identifies
\(S/I_C=k[s^4,s^3t,st^3,t^4]\): in degree \(d\ge N+2\),
the image of \(P^N\) covers every exponent \(0,\ldots,4d\).
Equivalently, \((I_C)_d\to(S/P^N)_d\) is onto. This holds over every
field, without a general-point argument.

Choose a linear splitting of \(V_C\to Q_N\), and a complement
\(W\) to \(\ker(V_C\to Q_N)\) inside \(\ker(V\to Q_N)\).
Then addition gives a noncanonical isomorphism
\[
 \tag{FD1}
 V_C\times W\xrightarrow{\sim}V
 \quad\text{over }Q_N,
 \qquad
 \mathcal U_C\times\mathbf A^e\xrightarrow{\sim}\mathcal U,
 \qquad e=4(a+b)+2.
\]
Indeed the quotient dimension is
\(h^0(C,O_C(a))+h^0(C,O_C(b))=(4a+1)+(4b+1)\)
in this degree range. Every element of \(W\) vanishes modulo \(P^N\),
so the resultant and all retained jets are unchanged. These are scheme
isomorphisms over \(k\), and persist after any base change, including to
nonreduced coefficient rings.

## 2. Scheme-theoretic determinant incidence

For a homogeneous test form \(H\) of degree \(d\), let
\(\eta_j(H)\in H^0(\mathbf P^1,O(dj))\) denote the \(j\)-th
characteristic coefficient of multiplication by \(H\) on the finite-flat
pencil algebra. The source-depth theorem says that \(\eta_j(H)\) depends
only on the source modulo \(P^{dj+1}\). This is a universal regular
factorization on the resultant open, not merely equality of values at
field-valued points: scaling base coordinates by \(\epsilon\) gives
the identity \(\eta_j(H_\epsilon)=\epsilon^{dj}\eta_j(H)\) over the
universal coefficient ring, and reduction modulo \(\epsilon^{dj+1}\)
removes every deeper source coefficient. Only the binary resultant needs
to be inverted. No Newton division is used.

Consequently, for any finite tuple of such coefficients with \(dj\le L\),
and \(a,b\ge L+3\), let \(\Phi\) be its regular map to the corresponding
affine coefficient space \(\mathcal T\). Taking \(N=L+1\) in (FD1) gives
\[
 \tag{FD2}
 (\mathcal U,\Phi)\simeq
 (\mathcal U_C\times\mathbf A^{4(a+b)+2},\Phi_C\circ\mathrm{pr}_1).
\]
For every subscheme \(Z\subset\mathcal T\), therefore,
\[
 \tag{FD3}
 \Phi^{-1}(Z)\simeq\Phi_C^{-1}(Z)\times\mathbf A^{4(a+b)+2}.
\]
The two source maps have the same scheme-theoretic image. Their incidences
have the same nonemptiness, reducedness, smoothness and geometric
irreducibility properties, with the displayed affine dimension difference.
These claims also follow directly after a field extension from (FD3).
They do not assert that any prescribed target is attained.

For the [paired quartic determinant](../torus/chow_arrangement_moments.md#a-two-operator-determinant-recovers-the-full-transverse-chow-polynomial),
put
\[
 D_4=x_0^3x_3,\qquad
 P_4=x_0^2(x_0x_3-x_1x_2),\qquad
 R_4=x_1^4-x_0^3x_3.
\]
The regular target uses the homogeneous coefficients
\(\eta_j(TP_4+ZR_4)=D_4^j\Delta_j(T,Z)\), as sections of
\(O(4j)\) with coefficients homogeneous of degree \(j\) in \(T,Z\).
An arbitrary-source \(\Delta_j\) can vary over the pencil base; it is
not assumed to be a constant scalar. For \(j\le r\), (FD2) applies at
\(a,b\ge4r+3\). For the separate quadric and cubic characteristic
towers through order \(r\), it applies at \(a,b\ge3r+3\).

The center-jet threshold is sharp for the linear source map: its final
cokernel has dimension \(L+2\) in degree \(L+2\). The determinant map
may forget some missing directions, so no sharpness claim for (FD2)'s
degree threshold follows.

## 3. Explicit finite Laurent trace matching

The following construction is in characteristic zero. Fix \(L\ge1\),
\(b\ge L+3\), and \(p\ge1\). Set
\[
 q=x_0x_3-x_1x_2,\qquad a=2p,\qquad
 J=\lfloor L/4\rfloor,\qquad
 c_j=(-1)^j\binom{b/2}{j},\qquad A_J=\sum_{j=0}^Jc_j.
\]
The binomial coefficients are generalized rational binomial coefficients;
\(b\) need not be even. Define
\[
 \tag{FD4}
 G_0=\sum_{j=0}^J c_j
 \left(x_0^{3j}x_3^j x_1^{b-4j}
       +x_0^j x_3^{3j}x_2^{b-4j}\right).
\]
All exponents are nonnegative. The binary restrictions of \(q^p,G_0\)
are \((-x_1x_2)^p\) and \(x_1^b+x_2^b\), so their resultant is nonzero.

Over the generic pencil field \(K=k(t)\), use \(x_0=1,x_3=t\).
On \(q=0\), put \(z=x_1\), so \(x_2=t/z\). The algebra of
\(q,G_0\) is
\[
 K[z,z^{-1}]/(P_b(z)),\qquad
 P_b(z)=z^bG_0(1,z,t/z,t)
       =\sum_{j=0}^Jc_j
          \left(t^jz^{2b-4j}+t^{b-j}z^{4j}\right).
\]
It has dimension \(2b\): the polynomial is monic of degree \(2b\)
and has constant coefficient \(t^b\ne0\). Since \(b\ge L+3\), its
top and bottom coefficient windows through order \(L\) do not meet.
At infinity these coefficients agree with the formal expansion
\((1-tz^{-4})^{b/2}\); at zero, after division by \(t^b\), they agree
with \((1-z^4/t)^{b/2}\). Newton identities, or the logarithmic
derivatives of these two expansions, give
\[
 \tag{FD5}
 \operatorname{Tr}(z^\ell)=
 \begin{cases}
  2b\,t^{\ell/4},&4\mid\ell,\\
  0,&4\nmid\ell,
 \end{cases}
 \qquad -L\le\ell\le L.
\]
The \(\ell=0\) value is the dimension \(2b\). Negative exponents use
the reciprocal polynomial and are part of the assertion.

Thus, on every Laurent polynomial with exponent support in \([-L,L]\),
this trace equals \(b/2\) times the trace on the quartic's generic fiber
\(K[z,z^{-1}]/(z^4-t)\). For \((q^p,G_0)\), the trace is multiplied
by \(p\). Indeed the \(q\)-adic filtration has \(p\) successive
quotients isomorphic to the algebra for \((q,G_0)\): the coprime
binary restrictions ensure properness, and \(q\) is a nonzerodivisor
modulo \(G_0\). Additivity of trace gives the assertion, including
multiple roots of \(P_b\).

## 4. An explicit containing mate and all bounded fixed tests

The restriction of (FD4) to \(C\) is
\[
 G_0|_C=A_J(s^{3b}t^b+s^bt^{3b}).
\]
The following correction makes the mate contain \(C\) while changing
none of its source layers through degree \(L\). Write \(b=4h+\epsilon\),
\(0\le\epsilon\le3\), and set
\[
 (R_0,R_1,R_2,R_3)=(1,x_1,x_1^2,x_2),\qquad e_\epsilon=\deg R_\epsilon,
 \qquad U=x_0^{b-h-e_\epsilon}x_3^h R_\epsilon.
\]
Let \(V\) be obtained from \(U\) by exchanging
\(x_0\leftrightarrow x_3\), \(x_1\leftrightarrow x_2\). Then
\(U|_C=s^{3b}t^b\), \(V|_C=s^bt^{3b}\), and both belong to
\(P^{b-e_\epsilon}\subset P^{L+1}\), since \(e_\epsilon\le2\).
Define the actual homogeneous pair
\[
 \tag{FD6}
 \boxed{F=q^p,\qquad G=G_0-A_J(U+V).}
\]
Both forms contain \(C\), have degrees \((2p,b)\), and retain the
nonzero binary resultant. Hence they form a proper CI avoiding \(M\),
finite flat over the same pencil.

For every homogeneous \(H\in I_C\) of degree \(d\ge1\), and every
\(j\ge1\) satisfying \(dj\le L\), one has
\[
 \tag{FD7}
 \boxed{\eta_j(H;F,G)=0.}
\]
To see this first for \((q^p,G_0)\), the restriction of \(H^i\) to
\(q=0,x_0=1,x_3=t\) is a Laurent polynomial with exponents between
\(-di\) and \(di\). It vanishes modulo \(z^4-t\), because \(H\)
contains \(C\). Formula (FD5) makes its trace zero for \(i\le j\).
Newton identities make its characteristic coefficients through order
\(j\) zero. The source-depth theorem then transports those coefficients
to (FD6), since \(G-G_0\in P^{L+1}\). Vanishing over the generic
pencil field is vanishing of the corresponding global section on the
integral base. The same proof works with auxiliary coefficients in \(H\),
so it includes all mixed characteristic coefficients of a fixed
equal-degree family with total degree at most \(L\).

Every pair (FD6) has a residual curve. Its reduced support lies on the
smooth quadric \(Q=V(q)\); the nonzero restriction of \(G\) to \(Q\)
cuts a divisor of class \((b,b)\). The curve \(C\) has class \((1,3)\),
so this divisor cannot be supported only on \(C\). Multiplying the
quadric equation to \(q^p\) changes multiplicities, not that support.

In particular, taking \(L=4r\) gives actual residual pairs with
\(\Delta_1=\cdots=\Delta_r=0\). Taking \(L=3r\) gives actual
residual pairs for which the quadric and cubic characteristic towers both
vanish through order \(r\). The first defining degree can be any positive
even integer; only the mate requires \(b\ge L+3\). Equal large even
degrees are available by choosing \(2p=b\).

## 5. The controls also admit normal integral carriers

Assume now that \(k\) is algebraically closed of characteristic zero,
\(a=2p\ge L+4\), and \(b\ge L+4\). There are pairs retaining every
vanishing in (FD7)
for which both carrier surfaces are normal and integral, each is smooth
along \(C\), and the two surfaces meet transversely at the generic point
of \(C\). The whole intersection can also be chosen reduced. Its generic
multiplicity along \(C\) is one and its residual degree is \(ab-4>0\).

Put \(N=L+1\) and
\[
 \tag{FD8}
 K_d=(I_C)_d\cap(P^N)_d.
\]
Start from the pair \((F,G)\) in (FD6) and vary it independently in
\((F+K_a)\times(G+K_b)\). The binary resultant and all source layers
through order \(L\) stay fixed, hence so do the asserted characteristic
coefficients. It remains to verify the geometric assertions for a general
pair in these affine spaces.

The sheaf \(I_C(3)\) is globally generated: \(I_C\) has its quadric
and three cubic generators, and the four linear multiples of the quadric
put all generators in degree three. For \(d\ge N+3\), the space
\[
 (I_C)_3\cdot(P^N)_N\cdot S_{d-N-3}\subset K_d
\]
has no base points outside \(C\cup M\). At every point of \(C\) it
surjects onto the two-dimensional conormal fiber, because \(C\cap M\)
is empty. These statements use global generation and multiplication by
a section nonzero at the selected point, not surjectivity onto all global
conormal sections.

For either affine coset, at a fixed point of \(C\) the condition that
the member be singular is two independent affine-linear conditions on
its conormal fiber. The incidence of singular members with points of
\(C\) has dimension at most \(\dim K_d-1\). Since \(C\) is proper,
its projection is closed and proper; a general member is smooth along
all of \(C\). The fixed form has nonzero binary restriction, so does not
belong to \(K_d\); its affine coset is the coefficient-one chart in their
projective span. That projective linear system is base-point-free off
\(C\cup M\), so characteristic-zero Bertini gives
smoothness there for a general member of the affine chart as well.
The precise standard input is the base-point-free linear-series form of
Bertini, for example [Vakil, *The Rising Sea*, Exercise 25.3.D and
Theorem 25.3.3](https://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf#page=683).

On \(M\), every member has its fixed nonzero binary restriction.
Consequently only finitely many points of \(M\) belong to that surface.
The general surface is therefore regular in codimension one; as a
hypersurface it is Cohen–Macaulay, hence satisfies \(S_2\), and Serre's
criterion makes it normal. A positive-degree projective hypersurface in
\(\mathbf P^3\) is connected (also directly from its structure-sheaf
sequence). A connected normal scheme has one irreducible component here,
so the surface is integral. This argument needs no separate irreducibility
form of Bertini.

Finally choose one fixed point of \(C\). The two independent affine
conormal evaluations are both surjective, so the condition that their
values be linearly independent is a nonempty open in the product of
the two cosets. It meets the dense opens just obtained. Such a pair is
transverse at this point and therefore generically along \(C\). Its
unchanged binary resultant ensures properness; Bézout gives residual
degree \(ab-4\). This proves the strengthening.

For reducedness of the whole intersection, first fix such a general \(F\).
Its surface is smooth outside its finite intersection with \(M\).
The mate's restricted system is base-point-free on
\(V(F)\setminus(C\cup M)\), so another application of Bertini makes
the intersection smooth there for a general \(G\) in its coset. Every
residual component meets this open, and generic transversality gives
generic reducedness on \(C\). The pair avoids \(M\) and is a complete
intersection, so it has no embedded associated primes. Generic reducedness
therefore makes the whole curve reduced.

The geometric perturbation proof itself applies to any nonempty containing
coset with nonzero binary restriction and \(d\ge N+3\); it does not use
evenness of \(d\). The even first degree belongs to the explicit source
construction (FD6).

## 6. Meaning and limits

The cycle-level roots-of-unity controls showed that moment cancellation
does not characterize sole support among abstract translated cycles.
Equations (FD4)–(FD7) now exhibit cancellation on actual proper global
pairs through \(C\). Thus a fixed finite family of homogeneous test
surfaces, tested to bounded characteristic order, cannot characterize
sole support uniformly in degree, even after imposing actual containment
and properness. This covers the paired determinant and the two fixed
quadric/cubic towers by one mechanism.

The explicit control starts with the carrier \(q^p\), but Section 5 shows
that the same bounded tests also vanish on reduced intersections of normal
integral carriers, smooth and generically transverse along \(C\), in its
larger degree range. Thus reducedness, normality or integrality alone does not repair this
bounded detector. These are not candidate minimal defining pairs, full
translated-cycle realizations, or thickenings of the large generic
multiplicity required for sole support. The scheme comparison (FD2)
does not impose those additional strata. No uniform bound on the order
needed for every actual candidate follows.

There is also a direct geometric explanation of the translated-cycle
boundary. The reduced controls of Section 5 are planar at both endpoints
because either carrier is smooth along \(C\). If all their components
were translates, their number would be \(m=ab/4\); it is either not an
integer or at least five in this degree range. The [endpoint-planarity
threshold](../torus/arrangement_strata_and_orders.md#2-intrinsic-endpoint-planarity-and-the-four-component-threshold)
excludes such a reduced CI arrangement. Thus these controls necessarily
retain nontranslated residual geometry, rather than resolving the full
translated-cycle incidence.

The exact support criteria remain exact when their full data is retained.
In particular, growing-degree Jacobian/cofactor membership, the complete
characteristic tower, and joint normal or carrier geometry are additional
conditions. This result redirects a bounded test toward such a condition;
it supplies no all-degree nonexistence theorem and leaves unrestricted
characteristic-zero STCI open.
