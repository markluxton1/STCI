# Conditional (2,12;6,16;2): compact norm-symbol and cubic realization incidence

Date: 2026-10-20. Status: **new exact reduction, provisional pending independent review**. No canonical result is changed. Work is over an algebraically closed characteristic-zero field, with the fixed curve C0 and the full generic ordinary coprime binary-CI initial ideal and actual saturated first relation required in the parent task. A bounded CAS interruption is process evidence only.

The source symbol matrix, exact image minor, and cubic layer are the new reviewed proposal in [the earlier global-realization note](2026-10-20-conditional-2-12-global-realization-incidence.md). The first-incidence construction is the promoted [STCI-R-0007](../results/quadratic_root_obstruction_model.md), used within its actual-CI interface and the separately reviewed finite singular-root bridge. The source script does not rerun accepted proofs.

## 1. Eight symbol equations are a norm factorization

Put `l=u+z*v/2`, the exact first symbol of the quadric `q=x0*x3-x1*x2`, and put

    D(z)=z^2*a(z)-2*z*b(z)+4*c(z)=sum(d_i*z^i,i=0..4).

The restriction of `alpha*f` to `l=0`, after the harmless scalar factor four, is `alpha*D`. The eight of the eleven symbol equations whose indices are not 3,6,9 say exactly that

    alpha(z)*D(z) belongs to span(1,z^3,z^6,z^9,z^12).

This has a geometric explanation: on the smooth quadric Q the sextic restriction is the square of the (1,3) curve equation times a section of O_Q(4,0), whose restriction to C0 is a binary quartic in z^3.

For four distinct roots of D in four distinct free mu3-orbits, the elementary factorization alone makes alpha unique up to scalar:

    alpha_can(z)=D(omega*z)*D(omega^2*z).

The stronger claim that this multiplier is necessary on **every actual supported pair**, including shared orbits and endpoint multiplicities, uses the separate quadric-intersection norm argument developed in parallel. The present exporter does not substitute generic factorization for that missing hypothesis: it explicitly imposes alpha_can. Its integration into the all-root necessity statement must cite that separate argument and its audit.

The formula needs no root of unity in the coefficient ring. With

    U=d0+d3*z^3, V=d1*z+d4*z^4, W=d2*z^2,

one has identically

    alpha_can=U^2+V^2+W^2-U*V-U*W-V*W,
    D*alpha_can=U^3+V^3+W^3-3*U*V*W.

The exporter checks symbolically that substitution of alpha_can makes exactly eight annihilator rows zero and leaves only rows 3,6,9 (zero-based indexing in the earlier symbol artifact).

## 2. A finite cover of the nonzero-endpoint chart

The C0-preserving torus acts by diag(1,lambda,lambda^3,lambda^4). Together with projective scaling of f, it permits the normalization d0=d4=1 wherever d0*d4 is nonzero: the two coefficients have torus weights differing by four, and the field is algebraically closed. Thus this is a finite cover of that chart; it does not cover endpoint-zero roots.

Choose four remaining root coordinates y0=b0,y1=b1,y2=b2,y3=c2. Then

    a=d2+2*y1-4*y3+(d3+2*y2)*z+z^2,
    b=y0+y1*z+y2*z^2,
    c=1/4+(d1/4+y0/2)*z+y3*z^2.

Writing T=y1-4*y3, the three surviving symbol equations are a linear system in (y0,T,y2). After dividing its first and third rows by four and its second row by two, the matrix is

    J = [ d2-d1^2       -d1       1          ]
        [ -2*d1+d2*d3   d2^2-1   2*d3-d1*d2 ]
        [ -1            -d3      d3^2-d2    ].

The constant vector is

    ((d3-d1*d2-d1^3)/4,
     (-d2-d1^2+d3^2-d1*d2*d3+d2^3)/2,
     (-d1-3*d2*d3+d3^3)/4).

Its determinant is minus

    d1^2*d2^2*d3^2-d1^2*d2^3-d1^3*d2*d3-d2^3*d3^2
    -d1*d2*d3^3+d2^4+2*d1*d2^2*d3+3*d1^2*d3^2
    -2*d2^2-4*d1*d3+1.

The exporter does **not** invert this determinant. All its rank-drop strata remain in the compact model. Changing y3 while keeping (d1,d2,d3,y0,T,y2) fixed adds `4*y3*l^2` to f; this explains why y3 is absent from the linear system.

## 3. Eight first-incidence correction variables disappear without denominators

On this chart a2=1,c0=1/4. The top four and bottom four equations of the accepted first incidence give the exact recurrences

    h3=-a0*h5-a1*h4,
    h2=-3-a0*h4-a1*h3,
    h1=-4*a1+3*b2-a0*h3-a1*h2,
    h0=-5*a0+3*b1-a0*h2-a1*h1,

    h8=-4*c1*h7-4*c2*h6,
    h9=-9/2-4*c1*h8-4*c2*h7,
    h10=-3*b0/2-16*c1-4*c1*h9-4*c2*h8,
    h11=-3*b1/2-14*c2-4*c1*h10-4*c2*h9.

Only h4,h5,h6,h7 remain. The exporter substitutes these expressions and verifies that precisely the original rows 0..3 and 12..15 become the zero polynomial. The other eight first equations are retained. Thus the base norm-symbol model on the smooth open has twelve variables and twelve equations: seven root coefficients, four h coefficients, one smooth inverse; eight first equations, three symbol equations, and the smooth-open equation. This is only an equation count, not a dimension computation.

## 4. An exact polynomial test for the actual sextic cubic lift

The fixed 22-by-22 image minor in the earlier symbol artifact defines a k-linear splitting rho. Every sextic with prescribed symbol alpha_can*f is

    rho(alpha_can*f)+eta*q^3.

Its cubic discrepancy from the canonical root correction is

    T=T0*u^3+T1*u^2*v+T2*u*v^2+T3*v^3
     =rho(alpha_can*f)_3+eta*l^3-alpha_can*G0.

The normal cubic is divisible by f in k[z,u,v] precisely when these four polynomial identities hold on the basepoint-free root locus:

    (b^2-a*c)*T0-a*b*T1+a^2*T2=0,
    b*c*T0-a*c*T1+a^2*T3=0,
    c^2*T0-a*c*T2+a*b*T3=0,
    c^2*T1-b*c*T2+(b^2-a*c)*T3=0.

To prove sufficiency, view multiplication by f as the rank-two bundle map O(7)^2 -> O(9)^4. The four displayed syzygies annihilate its image. Where a is nonzero, the first two syzygies are independent; where c is nonzero, the last two are independent; where a=c=0 and b is nonzero, the first and fourth are independent. They therefore span the entire rank-two annihilator at every point of a basepoint-free root. Vanishing of the four identities puts T in the image bundle. The corresponding quotient coefficients are global sections of O(7)^2. This retains zeros of alpha and does not divide by a,b,c or alpha in the final condition.

The compact exporter gives exactly 48 nonzero scalar coefficient equations from these four identities. It has thirteen variables including eta and the smooth inverse. The cubic equations are sufficient and necessary for the same cubic condition as the earlier 73-equation presentation on the specified open, provided the imposed norm multiplier is applicable. They do not replace the second obstruction, full spectral gluing/torsion, later sextic compatibility, or global degree-sixteen mate.

## 5. Reproduction and current computational boundary

Run

    python3 research/computations/conditional_2_12_elimination_2026_10_20.py
    /opt/homebrew/bin/M2 --script research/computations/conditional_2_12_elimination_2026_10_20.m2

The latter loads the hierarchical model and reports `COMPACT_BASE_MODEL_READY` and `COMPACT_CUBIC_EQUATIONS=48`. It launches no Groebner computation. The model is smooth-open only for the bounded CAS trial; singular-root strata remain in the parent structured incidence and are not excluded by this note.

The bounded QQ trials in `research/validation/2026-10-20-conditional-2-12-elimination/` preserve exact input files, return codes, and resource limits. Early expanded models and the first compact base model hit their 60-second CPU limits. These runs supplied **no ideal, dimension, unit, or emptiness certificate**. The final reduced cubic trial is recorded separately. No theorem may be inferred from a CPU-limited or killed process.

The precise unresolved computation is the intersection of these compact first/global-cubic equations with the inherited complete second test and full spectral torsion, together with the endpoint-zero charts. Even a nonempty answer would remain a low-order incidence rather than a global pair.
