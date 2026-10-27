# Independent audit: partial absorption and the smooth-carrier residual floor

Date: 2026-10-27. Reviewer: independent smooth-absorption audit agent.
Source: [Partial residual absorption on a Cartier carrier](2026-10-27-absorption-deformation-interface.md).
Outcome: **PASS under the source's literal hypotheses**. A small justification of the sharpness example was requested and incorporated: divisor classes alone do not prove a residual ruling is doubled; the explicit Segre factorization supplies it. No substantive correction to either general proposition is required. All new results remain provisional and unpromoted.

## 1. Retrieval and independence

The review followed [INDEX](../INDEX.md), [MAP](../MAP.md), and the
[contribution protocol](../CONTRIBUTING_AGENT.md). It read the relevant
October 19 [exceptional-cycle proof, §2](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md)
and its [independent reconstruction, §3](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md).
Those already establish global generation of \(I_C(3)\), and the earlier nef residual correction. They were treated as inherited reviewed evidence, not rediscovered or promoted. No historical certificate was rerun.

The reviewer reconstructed the arbitrary-\((m,n)\) construction and the uniform fraction directly. No sampled degree pairs or extrapolation from computations enter the argument.

## 2. The actual global section construction

Let \(k\) be algebraically closed of characteristic zero, let
\(C=[s^4:s^3t:st^3:t^4]\), and let \(S\subset\mathbf P^3\) be a globally smooth integral surface containing it. Then \(C\) is Cartier on \(S\). The restriction of the globally generated ideal sheaf \(I_C(3)\) has a surjection onto
\(\mathcal O_S(3H-C)\), so \(L=3H-C\) is globally generated.

Fix \(1\le m<n\) and \(b\ge3n+1\). For \(r=m,n\),

\[
bH-rC=rL+(b-3r)H
\]

is very ample. Indeed \((b-3r)H\) is very ample and \(rL\) is globally generated. A closed immersion furnished by the first, together with the morphism furnished by the second, gives a graph closed immersion into a product; the Segre embedding gives the asserted tensor-product polarization. This is valid for the actual finite-dimensional global section spaces.

Bertini therefore permits sections \(\tau_r\) cutting smooth integral divisors \(D_r\) and not vanishing identically on \(C\). Avoiding \(C\) as a component is a nonempty open condition in a globally generated system: there is a section nonzero at any chosen point of \(C\). This can be combined with the Bertini open.

The sections \(\sigma_r=s_C^r\tau_r\) of the same bundle \(\mathcal O_S(bH)\) have exact \(C\)-orders \(r\), hence are linearly independent. Therefore every finite member

\[
\sigma_n+t\sigma_m
=s_C^m\bigl(s_C^{n-m}\tau_n+t\tau_m\bigr)
\]

is nonzero. Its generic order along \(C\) is exactly \(m\) for **every** \(t\ne0\), because the residual bracket restricts to \(t\tau_m|_C\); the zero fiber has exact order \(n\). There is no cancellation of its nonzero \(C\)-restriction when \(t\ne0\).

The hypersurface restriction sequence and
\(H^1(\mathbf P^3,\mathcal O(b-a))=0\) for every integer \(b-a\) lift the two sections to actual degree-\(b\) forms \(G_m,G_n\) over \(k\). Their linear combination lifts the whole family, without introducing \(k(C)\)-valued coefficients. Since every restriction to integral \(S\) is nonzero, \(F_a\) divides no \(G_n+tG_m\). Thus every finite fiber is a proper complete intersection. No hypothesis \(b\ge a\) is needed.

## 3. Flatness and the special residual scheme

The ambient product \(S\times\mathbf A^1\) is flat, and each nonzero fiber section cuts an effective Cartier divisor on integral \(S\). The total zero scheme is locally principal. The fiberwise effective-Cartier criterion therefore makes it a relative effective Cartier divisor and proves flatness. The same argument applies after removing the fixed factor \(s_C^m\), because its two residual-pencil sections are independent.

Equivalently, locally over \(k[t]\), reduction at any \(t=c\) makes the defining section a nonzerodivisor. If \((t-c)q=\sigma h\), reduction modulo \(t-c\) forces \(h\) divisible by \(t-c\), so \(q\) is a multiple of \(\sigma\). The quotient has no \(k[t]\)-torsion and is flat. This also verifies that the flat residual family is the closure of its generic fiber, rather than a closure with an unrecorded vertical component.

The residual pencil extends to \(\mathbf P^1\). Its member at infinity is the chosen smooth integral \(D_m\). Smoothness and geometric integrality are open near that point in the proper flat pencil, so a general finite nonzero member is smooth integral. The argument does **not** assert this for every nonzero parameter; the source correctly retains that distinction.

At zero the residual section is exactly \(s_C^{n-m}\tau_n\). Consequently its scheme is the Cartier sum

\[
\mathscr D_0=(n-m)C+D_n,
\]

with the product ideal that specifies the gluing. This is stronger than a cycle statement. Its degree agrees with the generic residual:

\[
4(n-m)+(ab-4n)=ab-4m.
\]

The full primary component is \(mC\) away from zero and \(nC\) at zero. Its degree changes, so it cannot be a flat family of fixed Hilbert polynomial. The source's distinction between its fiberwise extraction and the flat fixed-lower residual family is essential and correct.

## 4. The residual bound needs smoothness along C only

For the second proposition, global smoothness may be dropped. Let \(S\) be an integral hypersurface smooth at every point of \(C\). Then \(C\) is Cartier near its support, and off \(C\) its ideal is the unit ideal. Hence it is a global Cartier divisor on \(S\), even if \(S\) is singular elsewhere.

For a proper mate \(G_b\), divide the corresponding divisor by its exact generic multiplicity \(mC\). Near \(C\) this division is regular because the local surface is regular and the prime \(C\)-ideal is principal. Away from \(C\) its local equation is a unit times \(G_b\). Thus

\[
D=\operatorname{div}_S(G_b)-mC
\]

is an effective Cartier divisor with no \(C\)-component. The line bundle \(3H-C\) is still globally generated, so its degree on each integral residual component is nonnegative. Nonreduced multiplicities of components contribute with positive integer coefficients; hence \((3H-C)\cdot D\ge0\).

The normal sequence is exact along the smooth \(C\):

\[
0\to N_{C/S}\to N_{C/\mathbf P^3}\to\mathcal O_C(a)\to0.
\]

The tangent/Euler degree calculation gives
\(\deg N_{C/\mathbf P^3}=4\deg C+2g-2=14\), in every characteristic. Consequently \(C^2=14-4a\). Using \(H^2=a\) and \(H\cdot C=4\) yields

\[
0\le(3H-C)\cdot(bH-mC)
=b(3a-4)-m(4a-2).
\]

Thus

\[
\frac{4m}{ab}\le\frac{4(3a-4)}{a(4a-2)}.
\]

Since \(C\) is nonplanar, the integer \(a\) is at least two. The remaining numerical comparison is exact:

\[
\frac23-\frac{4(3a-4)}{a(4a-2)}
=\frac{8(a-2)(a-3)}{3a(4a-2)}\ge0.
\]

The weighted residual degree is therefore at least \(ab/3\). This argument uses neither balanced normal splitting nor an STCI exclusion. In positive characteristic the same conclusion holds under these carrier and ideal-generation hypotheses.

For equal-degree pairs, replacing the pair by any other basis of its pencil preserves its intersection. Thus the bound applies whenever an **integral** pencil member is smooth along all of \(C\). No statement about arbitrary reducible pencil members is inferred.

## 5. Sharpness and the requested proof clarification

The bound is uniformly sharp on the smooth quadric. In Segre coordinates

\[
(x_0,x_1,x_2,x_3)=(su,sv,tu,tv),
\]

the cubic \(A=x_0^2x_2-x_1^3\) restricts to

\[
s^2(tu^3-sv^3).
\]

The second factor cuts the fixed \((1,3)\) quartic; \(s=0\) cuts the ruling line \(\ell=(x_0,x_1)\). Thus \(\operatorname{div}_Q A=C+2\ell\), and \((q,A^n)\) has cycle \(n[C]+2n[\ell]\) with degrees \((2,3n)\). Its residual degree is \(2n=ab/3\).

The source originally justified the doubled ruling just by the divisor classes. Classes alone would only specify a residual \((2,0)\) divisor and would not distinguish a double line from two distinct fibers. The explicit factorization above supplies the missing justification. The exact example is correct and is a sharpness control, not an additional case program.

## 6. Primary-source checks and outcome

The later general-curve remarks were also independently checked. For a smooth connected curve of degree \(e\), genus \(g\), and globally generated \(I_C(\delta)\), the construction uses \(\delta H-C\) and the sufficient range \(b\ge\delta n+1\). The normal-degree calculation is

\[
C^2=(4-a)e+2g-2.
\]

Hence the general nef inequality is

\[
0\le b(\delta a-e)-
m\bigl(e(a+\delta-4)-(2g-2)\bigr).
\]

The source correctly divides by the coefficient of \(m\) only when it is positive. Its quartic substitution gives precisely the earlier bound, without suggesting a universal fraction for arbitrary curves.

For the effective-cone paragraph, \(\delta H-C\) is globally generated and therefore pseudo-effective, so \(H-\delta^{-1}C\) is pseudo-effective. Intersection with the nef \(\delta H-C\) is nonnegative on the closure of the effective cone. With the same positive coefficient, this gives exactly the stated bounds on \(\tau_{\mathrm{eff}}\). This is a supporting-nef bound, not a proof of attainment or an assertion that every intervening rational slope is represented by a residual curve. The actual constructive family lies in the sufficient very ample region \(r/b<1/\delta\). These qualifications are correctly retained.

Freshly inspected standard sources:

- [Stacks, Lemma 33.47.3](https://stacks.math.columbia.edu/tag/0FD4): smooth members of a generated linear system inducing an immersion.
- [Stacks, Lemma 37.32.3 and Remark 37.32.4](https://stacks.math.columbia.edu/tag/0G4C): geometric irreducibility and smooth integral hyperplane sections.
- [Stacks, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS): intermediate cohomology vanishing on projective three-space.
- [Stacks, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/062Y): locally principal fiberwise Cartier schemes in a flat ambient family are relative effective Cartier divisors.
- [Stacks, very ample sheaves](https://stacks.math.columbia.edu/tag/01VL): the definition used in the graph/Segre verification.

**PASS.** The general operation proves partial absorption in characteristic zero for arbitrary prescribed finite multiplicity increases when the mate degree is sufficiently large. It does not show that every residual configuration is absorbable. The uniform residual floor applies while an integral carrier remains smooth along all of \(C\). It gives no obstruction for arbitrary singular or non-Cartier carriers and does not determine the unrestricted STCI answer. Standard linear-system ingredients are not claimed as literature novelties. The useful new research synthesis is the constructive mechanism paired with its precise degree-independent boundary.

## 7. Later normal Q-Cartier carrier corollary

The added §5 corollary was independently reconstructed and also **PASSES**. Its hypotheses are an already specified normal integral hypersurface \(S\) over an algebraically closed characteristic-zero field, and an actual Cartier multiple \(hC\) of the marked Weil curve, with \(h>0\).

Effectivity matters. A local Cartier equation for \(hC\) has nonnegative valuation at every codimension-one point. Since a normal noetherian domain is the intersection of its height-one valuation rings, the equation is regular locally. Thus \(hC\) is an effective Cartier divisor on \(S\), not just a numerical class.

For sufficiently large \(\delta\), ampleness of \(H\) makes \(\mathcal O_S(\delta H-hC)\) globally generated. This is the usual coherent-sheaf consequence of ampleness, freshly checked in [Stacks, ample invertible sheaves](https://stacks.math.columbia.edu/tag/01PR). The source claims neither an explicit \(\delta\) for every carrier nor a uniform bound across a carrier family.

With \(1\le u<v\) and \(b\ge\delta v+1\), the bundles
\[
bH-rhC=r(\delta H-hC)+(b-\delta r)H,\qquad r=u,v,
\]
are very ample by the same graph/Segre argument. A normal surface has no codimension-one singular locus, by [Serre's normality criterion](https://stacks.math.columbia.edu/tag/031O), so its projective singular locus is a finite set. General sections of these very ample bundles avoid that finite set, and Bertini on the regular locus gives smooth integral residual divisors.

The sections \(s_{hC}^r\tau_r\) have exact generic \(C\)-orders \(hr\), because normality makes the generic point of \(C\) a DVR and \(\tau_r\) does not contain \(C\). Their differing orders again prove independence. The interpolation, homogeneous lifting, properness and fiberwise Cartier flatness work without alteration. The fixed-lower residual special fiber is
\[
(hv-hu)C+D_{hv}
\]
as an effective Cartier divisor. Smooth residuals occur for general parameter; some exceptional parameter can pass through a singular point outside \(C\), which is why the source's generic qualification is necessary.

The supported Cartier multiples \(ruC\) in this argument are pure CM schemes: \(S\) is a hypersurface and quotient by the regular local equation of an effective Cartier divisor is CM. Their only generic support is \(C\). No additional component is inferred from exceptional or normal-cone geometry; no blowup construction is used. Conversely, having a Cartier multiple merely upstairs on a normalization of a nonnormal carrier would not establish this corollary's hypothesis on the actual carrier. The statement does not claim such a descent or replace full inverse-support/conductor conditions.

The construction supplies partial absorption in index-compatible increments \(h\) once that Cartier multiple and carrier exist. It supplies neither a class relation \(rhC\sim bH\) removing the residual nor a construction of carriers with arbitrary index. In particular the one-third floor proved for carriers smooth along \(C\) is not transferred to these singular-along-\(C\) carriers. These boundaries are correctly preserved in the source.

## 8. Weak divisorial-ideal construction on an arbitrary normal carrier

The final proposed weak extension also **PASSES**, with its stronger conclusions expressly omitted. Let \(S\) be any normal integral hypersurface and \(C\) the marked prime curve. The divisorial ideals
\[
\mathcal J_r=\mathcal O_S(-rC)\subset\mathcal O_S
\]
are coherent rank-one reflexive sheaves. For the two fixed integers \(1\le m<n\), Serre global generation gives a sufficiently large common \(b\) for \(\mathcal J_m(b)\) and \(\mathcal J_n(b)\). This does not require either sheaf to be invertible.

At \(\eta_C\), normality gives a DVR and \((\mathcal J_r)_{\eta_C}=(\pi^r)\). A globally generating set must contain a section of exact valuation \(r\); if all sections had larger valuation, they could not generate \((\pi^r)\). Choose such actual global sections \(\sigma_m,\sigma_n\), regarded through the sheaf inclusions as sections of \(\mathcal O_S(b)\).

They are linearly independent by their different valuations. For every \(t\ne0\), \(\sigma_n+t\sigma_m\) has exact valuation \(m\), and the zero member has valuation \(n\). Every section is nonzero. Hypersurface restriction lifts the two sections and their pencil to degree-\(b\) homogeneous equations, using the same intermediate-cohomology vanishing. Since \(S\) is integral, every fiber pairs properly with its equation \(F_a\). On \(S\times\mathbf A^1\) the resulting family is locally principal with nonzero Cartier fibers, hence flat.

The source's added paragraph was read after completion and matches these hypotheses. Its further observation that this weak construction works in every characteristic is correct: no Bertini, separability, or characteristic-zero duality enters the argument.

Thus arbitrary prescribed finite increases in generic \(C\)-multiplicity are available for sufficiently positive mate degree even if \(C\) is not \(\mathbf Q\)-Cartier on \(S\). This statement concerns the **total CI family and its cycle multiplicities**. It does not assert smooth integral residual curves, a uniform degree threshold, a flat family obtained by removing the whole \(C\)-primary component, or compatibility of residual colon ideals with base change. In particular the earlier Cartier residual factorization cannot simply be reused when \(\mathcal J_r\) is not invertible.

The endpoint boundary is exact: if a proper mate on this fixed normal surface had sole support \(C\), its effective Cartier divisor would have Weil divisor \(rC\) for some \(r>0\), linearly equivalent to \(bH\). Therefore \(rC\) would be Cartier, forcing \(C\) to be \(\mathbf Q\)-Cartier. Consequently the weak construction does not bypass the non-\(\mathbf Q\)-Cartier fixed-carrier endpoint obstruction. It demonstrates partial transfer while retaining residual support.
