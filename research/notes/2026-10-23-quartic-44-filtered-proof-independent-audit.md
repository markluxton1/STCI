# Independent mathematical audit of the proposed short (4,4) exclusion

Date: 2026-10-23. Scope: the fixed C0=[s^4:s^3t:st^3:t^4] over an algebraically closed field of characteristic zero. This audits `research/notes/2026-10-23-quartic-44-filtered-proof-proposal.md`, with the NEW e=0 computation in `research/computations/verify_44_filtered_contact_2026_10_23.py`. It does not audit or reopen the accepted all-mate-degree integral-quartic theorem STCI-R-0001.

**Verdict: the proposed narrow (4,4) proof passes independent mathematical review, under its explicitly listed inherited conormal, saturated quasiprimitive/Gorenstein, and e=1 classification inputs.** It is a provisional proof contribution and is not a separately promoted canonical result. It gives a useful shorter derivation of a known consequence, not a replacement proof for arbitrary quartic mate degree.

## 1. Scope and inherited authority

Read research/INDEX.md first. Checked research/results/quartic_carrier_exclusion.md, research/results/order_one.md, and the underlying saturated pairing audit research/notes/2026-10-05-mf6-pairing-audit.md for hypotheses. The accepted full quartic-carrier exclusion is not used as an input to this argument.

The e=1 completeness statements are inherited from research/notes/2026-10-07-session-mf6-e1-independent-audit.md, sections 2 and 4. That file is independently audited accepted proof evidence, rather than a separately ID-bearing promoted result. The proposal says this explicitly. Its fixed-C0, characteristic-zero, primitive-triple hypotheses agree exactly with the current e=1 branch. I did not rerun this inherited classification.

## 2. Numerical and thick-branch reductions

A pair with sole reduced support C0 has no common surface factor, so is a proper complete intersection of degree16. Its generic transverse length is4 and adjunction gives omega_Z=O_Z(4). Thus the last saturated piece is E3=omega_C tensor omega_Z|C^-1=O_P1(-18).

The conormal quotient E1=L=O(e-7) has e>=0 because N_C^*=O(-7)^2 surjects onto it. With E3=L^3(D3), deg D3=3-3e. The audited perfect multiplication E1 tensor E2 -> E3 gives equality of actual divisors D2=D3, not merely numerical equivalence. Effectivity therefore leaves exactly e=0 with d2=d3=3, and e=1 with both zero. No positive-defect e=0 branch has been discarded.

The order-one hypothesis is justified without the full quartic exclusion. On the unique smooth Q, C has class(1,3), up to ruling order. A quartic with generic normal order at least2 restricts to a section in H0(Q,O(2,-2))=0, so it is q times a quadric; that quadric must vanish on C and is proportional to q. Such a quartic is a scalar multiple of q^2. A mate restricted to Q has class(4,4), which cannot be supported solely on C, while a mate divisible by q gives a common surface. Hence a hypothetical pair has order-one equations. The argument also shows why an entirely-thick branch has not been silently omitted.

## 3. e=0: exhaustiveness and correction freedoms

The quotient to O(-7) is constant in the fixed balanced conormal frame. The ambient torus of weights(0,1,3,4), which preserves C0, acts transitively on the finite nonzero quotient parameters. The endpoints are separate. This justifies three orbits; no arbitrary GL2 normal-frame transformation or PGL2 support transformation is being used.

For a degree3 defect divisor D, multiplication by its section delta pushes the actual double-to-triple extension class from H1(O(-7)) into H1(O(-4)). In fixed ambient coordinates the only remaining quadratic correction is a section of Hom(M,L^2(D)), M=O(-7), whose global section space H0(O(-4)) is zero. Thus a fixed annihilator determines at most one embedded candidate. The moving support coordinate is already included in the exact ambient transition used to obtain the cocycle; no global retraction or splitting of the filtered algebra is assumed.

In the nonzero orbit the killing matrix has one-dimensional kernel (0,2,1,0), yielding the full homogeneous degree3 divisor with affine section delta=z(z+2), including infinity. The gluing identity delta*h=-3/8+6/z^4 gives gamma=3/8 in the convention delta*m-gamma*ell^2=0. Consequently the containment equation is delta*k+gamma*h_H=0. The positive sign is essential and agrees with m=(gamma/delta)*ell^2. The current clean note and script have this convention consistently.

At theta=0 the kernel is delta=z^2(a+bz), gamma=(3/8)(a+bz), hence the rational correction is independent of the extra linear factor. At the missing endpoint gamma_U=0 and delta=a+bz. The proposal allows these supersets even when a common zero prevents the putative triple from being pure. Enlarging the candidate space is safe for an exclusion. Their complete quartic spaces are respectively D_cubic*S1 and A_cubic*S1, so any pair has a common cubic surface. There is no omitted endpoint, repeated divisor, infinity divisor, or extra regular correction parameter.

## 4. The cubic determinant is the correct obstruction

For H=h*m+k*ell^2+e*m*ell+c*ell^3+O(normal degree4), substitute m=f2*ell^2+m_new. The common triple condition k+h*f2=0 leaves cubic coefficient tau=c+e*f2. Terms involving m^2 only start at order4 after this substitution. If the first derivative h is nonzero, formal elimination of m_new shows that the residual other equation begins with (h0*tau1-h1*tau0)/h0 times ell^3. A nonzero determinant gives transverse length exactly3.

Every proper pair in a two-dimensional complete quartic source must be an independent basis. Its determinant differs by a nonzero constant from that of the displayed basis. Therefore checking the determinant once excludes every independent pair in the pencil. Scalar-dependent pairs already have a common surface.

For the new e=0 open-orbit pencil the exact determinant is 32*z*(z-2)*(z+2), which is nonzero in k(C0). Its vanishing at some individual closed points does not invalidate the generic length argument and need not be divided out or classified. Every nonzero pencil member has a nonzero first symbol, so elimination is available.

## 5. e=1 and the rejected fixed-line shortcut

The inherited primitive-triple classification is exhaustive over exactly four actual torus orbits. The quadric orbit has entire quartic space q*S2 and cannot provide a proper pair.

Using the h,T expressions in the accepted audit, I independently expanded the principal-orbit determinant and obtained

    h_P0*T_P1-h_P1*T_P0
      =(2z-1)^3*(2z+1)*(4z^2+2z+1)/256.

It is nonzero. In those conventions T=-tau, so this is the same obstruction up to sign. For either algebraic boundary root 12r^2+4r+3=0, the inherited formulas give h_R0=1,T_R0=0,h_R1=(2r+2/3)z^8,T_R1=(8r/9)z^3, and determinant (8r/9)z^3 is nonzero because r!=0. Constant rescalings of a displayed basis or simultaneous trivialization change alter these determinant formulas by a nonzero scalar; only nonvanishing is needed.

The proposal correctly rejects the older assertion that every nonquadric e=1 pencil has fixed ruling lines on Q. The later exact algebraic boundary pencil restricts to Q with gcd only C; that old shortcut must not be cited as evidence. The present cubic argument does not need it.

## 6. New independent computational check and limits

The structural certificate reconstructs every e=0 quartic source in all35 homogeneous degree4 monomials, checks the kernel dimensions and displayed bases, and verifies the cubic determinants. Its new e=1 arithmetic is only a consequence of inherited h,T expressions; it does not independently establish e=1 classification completeness.

A separate audit script `research/computations/audit_44_filtered_contact_2026_10_23.py` constructs direct Taylor substitutions along x2=z^3+ell, x3=z^4+(3z/2-1)ell+3ell^2/(8z(z+2)). It does not import the proposal's code or data. It checks the full rational Taylor identities for both displayed forms and the generic cubic determinant. Its rank lower bound uses exact rational evaluations followed by Gaussian elimination modulo1009; rank33 modulo the prime proves rank at least33 in characteristic zero. Two independent forms satisfying the full rational identities prove rank at most33. Thus finite evaluation is used only for a rigorous rank lower bound, not to infer a polynomial identity from sampling.

The first attempted independent rank computation with direct generic SymPy rational elimination was interrupted because it was unnecessarily slow. It produced no mathematical conclusion and is not evidence. The replacement modular rank calculation is the meaningful independent check.

This proof explains a failure of actual embedded quartic relations through the fourth transverse layer. Sym(N_C^*) alone records first-order bundle data; it does not encode the ambient nonlinear extension cocycle or the global quartic source. The characteristic-two prescribed pair has a primitive O(-6) first quotient and fourth transverse power by Frobenius. The characteristic-zero e=1 analogue is numerically allowed, but its actual quartic source cannot have simultaneous fourth contact. No conclusion about pairs of higher degrees follows.

The independent script completed with exit0 on 2026-10-23 and printed:

    independent necessary evaluation rank modulo1009 33
    full rational-function contact identities: PASS
    cubic determinant 32*z*(z-2)*(z+2)
    Generic contact for any independent pair is exactly three: PASS
    e1 principal cubic determinant: PASS
