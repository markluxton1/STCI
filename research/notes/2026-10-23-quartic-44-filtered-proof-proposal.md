# A shorter normal-algebra proof for characteristic-zero (4,4)

Date: 2026-10-23. **Independently reviewed proof proposal; not canonically promoted.**
This does not replace STCI-R-0001, and it does not assert a new general STCI
exclusion. The contribution is a shorter proof of its much narrower (4,4)
consequence, using the multiple-curve algebra and actual quartic contact.

## Exact proposed claim

Let k be algebraically closed of characteristic zero and
C=[s^4:s^3t:st^3:t^4] in P3. There are no homogeneous quartics F,G with
V(F,G)_red=C. Reducible or nonreduced quartics are included. The proof assumes
the accepted balanced conormal and quasiprimitive/Gorenstein filtration
lemmas described below; it does not invoke the complete quartic-carrier
exclusion itself.

## Inherited premises and scope

1. N_C^*=O(-7)^2, and C is contained in its unique smooth quadric
   q=x0*x3-x1*x2. O_C(1)=O_P1(4).
2. H0(I_C^2(4))=k*q^2. This follows by restricting to the quadric:
   I_(C/Q)^2(4,4)=O_Q(2,-2), up to interchanging the rulings; hence a
   quartic vanishing twice on C is divisible by q, and the remaining
   quadric must be proportional to q.
3. A complete-intersection curve supported on C with at least one generic
   normal order one has a saturated quasiprimitive filtration
   E_i=L^i(D_i), L=O(e-7), e>=0, with effective D_i, D_0=D_1=0.
   Its Gorenstein duality gives D_i+D_(m-1-i)=D_(m-1) and
   E_(m-1)=omega_C tensor (omega_Z|C)^-1.
   See research/results/order_one.md and its stated proof dependency
   research/notes/2026-10-05-mf6-pairing-audit.md. The general statement is
   finite-flat/quasiprimitive and not a hypothesis of global primitiveness.
4. The accepted e=1 primitive-triple classification and complete quartic
   pencils in research/notes/2026-10-07-session-mf6-e1-independent-audit.md,
   sections 2 and 4. These are preserved accepted evidence rather than a
   separately promoted canonical result record. Only the stated fixed-C,
   characteristic-zero scope is used.

Premises 1 and 3 are accepted mathematics, not verification tasks here.
Premise 2 is also checked by another workstream. The NEW e=0 calculation
is reconstructed in all 35 quartic monomials. The e=1 calculation only
extracts a simpler simultaneous-pair consequence of existing contact
identities; it does not re-run their accepted classification.

## Reduction to two numerical types

If F,G had a common factor, their zero set would contain a surface. Hence
they form a regular sequence and Z=V(F,G) is a pure degree-16
complete-intersection curve with generic length m=4 along C and
omega_Z=O_Z(4).

A quartic of generic normal order at least two is in H0(I_C^2(4)) because
Sym^j N_C^* is torsion-free: the lower normal symbol vanishes everywhere
when it vanishes generically. Thus it is a multiple of q^2. If one equation
is q^2, the other cuts a divisor of class (4,4) on Q, which cannot have
sole support C of class (1,3). If both are q^2, the pair has a common
surface. Therefore any hypothetical pair has generic normal order one,
and the quasiprimitive filtration applies.

Adjunction gives E_3=O(-18). Since E_3=L^3(D_3),

    deg D_3 = 3-3e.

The duality relation at i=1 is D_2=D_3. Effectivity and e>=0 leave
exactly:

- e=0, L=O(-7), deg D_2=deg D_3=3;
- e=1, L=O(-6), D_2=D_3=0.

The second type is globally primitive. The first permits the two quartics
to be singular at common points on C; it is not omitted.

## A common pencil criterion

Over K=k(C), choose ambient normal parameters m,ell so a common triple
has m=f2*ell^2 modulo ell^3. Write a quartic H as

    H=h_H*m+k_H*ell^2+e_H*m*ell+c_H*ell^3+O(normal order4).

Containing the triple means k_H+h_H*f2=0. After the local change
m=f2*ell^2+m_new, its cubic contact is

    tau_H=c_H+e_H*f2.

Two independent quartics H0,H1 can have generic intersection length at
least four only if

    h_H0*tau_H1-h_H1*tau_H0=0 in K.

Otherwise eliminate m_new with one equation: the other equation is a
unit times ell^3 plus higher terms, so the quotient has length exactly
three. Replacing the basis of a two-dimensional quartic pencil scales
this determinant by a nonzero constant. This is an obstruction for every
pair in the pencil, not a test of one special pair.

## e=0: three orbits, one nonzero cubic-contact determinant

Use the balanced ambient coordinates on x0=1:

    z=x1,
    V=x2-z^3,
    U=x3-z^4-(3/2)*z*V.

A quotient N_C^* -> O(-7) is constant in this frame. Its finite chart is
U=-theta*ell,V=ell; the other endpoint is U=ell,V=0. The actual ambient
torus (x0,x1,x2,x3)->(x0,lambda*x1,lambda^3*x2,lambda^4*x3)
changes (z,U,V) to (lambda*z,lambda^4*U,lambda^3*V), so theta changes
to lambda*theta. Thus exactly three orbits suffice: theta=0, infinity,
and theta=1. This uses an actual projective automorphism preserving C,
not an arbitrary change of the embedded conormal frame.

Put m=U+theta*V in the finite chart. The double-to-triple obstruction is
h_theta in H1(O(-7)). A defect section delta of O(3) must annihilate it
in H1(O(-4)). Once delta is fixed, all regular quadratic corrections
form a torsor under

    H0(Hom(O(-7),O(-14)(D))) = H0(O(-4)) = 0.

Therefore there are no omitted free correction parameters. This is the
pushout of the standard double-to-triple extension by L^2 -> L^2(D).
The condition that the resulting structure be pure can only shrink this
parameter space; we allow all annihilators in the exclusion.

On the opposite ambient chart put

    W=x2/x3,
    a=x1/x3-W^3,
    b=x0/x3-W^4,
    U'=a/2,
    V'=-3*W*a+2*b.

Expanding this exact coordinate change through degree two produces:

    h_1=3/z^5-3/(2z^4)+3/(4z^3)-3/(8z^2),
    h_0=-3/(8z^2),
    h_infinity=3/z^5.

For theta=1 the multiplication matrix from delta=sum_(j=0)^3 d_j*z^j
to the Laurent coefficients z^-1,z^-2,z^-3 of delta*h_1 is

    [    0   -3/8    3/4   -3/2 ]
    [ -3/8    3/4   -3/2     3  ]
    [  3/4   -3/2     3      0  ].

Its kernel is k*(0,2,1,0), so delta=z(z+2), understood as a section
of O(3); its full divisor includes infinity. Moreover

    delta*h_1 = -3/8 + 6/z^4.

With the sign convention m=gamma/delta*ell^2, gamma=3/8. Thus a quartic
H, expanded at U=-ell,V=ell, contains the triple exactly when

    H|C=0,
    [ell]H=0,
    delta*[ell^2]H + gamma*[U]H=0.

These are polynomial coefficient equations in the 35 ambient quartic
monomials. Their matrix has rank 33. A compact basis of its full kernel
is the following. Put

    q=x0*x3-x1*x2,
    A=x0^2*x2-x1^3,
    B=x0*x2^2-x1^2*x3,
    D=x2^3-x1*x3^2.

Then

    F0=-(x2+x3)*(16*A+(16*x0+8*x1)*q)
          +(4*x2+x3)*B-x2^2*q,

    F1=x2*D-256*x1*A
          -4*q*(64*x0*x1+16*x0*x2+4*x0*x3+32*x1^2
                +4*x1*x2+4*x1*x3+2*x2^2+x2*x3).

In coordinates U=m-ell,V=ell, set f2=3/(8z(z+2)). The exact first
and cubic contacts are

    h0=-2*z^3*(z+2)^3,
    h1=-2*z*(z+2)*(z^2+4)*(z^4+16),
    tau0=-(z+4)/8,
    tau1=-(z^5+2*z^4+16*z^2-16*z+96)/(8*z*(z+2)).

Their determinant is

    h0*tau1-h1*tau0 = 32*z*(z-2)*(z+2) != 0.

Hence every independent pair in the full quartic pencil has generic
intersection length three, not four. This excludes the open quotient
orbit.

At theta=0 every annihilator is delta=z^2*(a+b*z). The regular correction
is gamma=(3/8)*(a+b*z), so the common factor cancels from the quartic
containment equations. Those equations have complete solution space
D*H0(O_P3(1)), of dimension four. At infinity every annihilator is a+b*z;
its common factor likewise cancels, and the complete quartic space is
A*H0(O_P3(1)). Both cases force a common cubic surface in any pair.
This excludes both endpoint orbits without asserting that each annihilator
actually defines a pure triple.

## e=1: existing pencils fail the same cubic-contact test

The existing accepted classification gives four torus orbits of primitive
triple directions. One is the quadric direction and every quartic through
it is q times a quadric. It cannot provide a proper (4,4) pair.

The principal orbit has normalized quotient A=1+z,B=-2-8z and a complete
two-dimensional quartic pencil H=alpha*P0+beta*P1. In the accepted audit's
coordinates m=B*U-A*V, ell=(4/3)*U+(1/6)*V, the triple is
m=-gamma*ell^2, gamma=192*z+96. Its audit defines T=gamma*e-c,
so T=-tau in the common criterion above. The explicit h,T formulas in
section 4 of that audit give the new simultaneous-pair identity

    h_P0*T_P1-h_P1*T_P0
      =(2*z-1)^3*(2*z+1)*(4*z^2+2*z+1)/256 != 0.

Thus its two independent quartics have generic intersection length three.

The other two orbits are the conjugate directions A=r*z,B=1 with
12*r^2+4*r+3=0. Their complete pencil has basis

    R0=x0^3*x3-(r+3/2)*x0^2*x1*x2+(r+1/2)*x1^4,
    R1=x0*x3^3+(r-7/6)*x1*x2*x3^2+(1/6-r)*x2^4.

The accepted exact contact formulas are

    h_R0=1, T_R0=0,
    h_R1=(2*r+2/3)*z^8, T_R1=(8*r/9)*z^3.

Their determinant (8*r/9)*z^3 is nonzero for both roots. Again generic
intersection length is three. This exhausts e=1 and proves the proposed
(4,4) exclusion from the inherited premises.

## Characteristic comparison and exact interpretation

This gives a coherent algebraic explanation of the characteristic-zero
failure: adjunction and Gorenstein duality leave only two types, and the
actual quartic relations cannot agree through the fourth layer. The
associated symmetric algebra alone does not contain the nonlinear
quadratic cocycle or the cubic contact determinants. The calculation
uses the filtered embedded algebra together with the global quartic
source.

The characteristic-two pair x1^4-x0^3*x3, x2^4-x0*x3^3 has local algebra
k[z,Y]/(Y^4), first quotient O(-6), and graded pieces O(-6i). Its
characteristic-zero numerical analogue is the e=1 primitive type above.
Frobenius permits exactly the fourth transverse power; in characteristic
zero the permitted triple directions and their global quartic pencils
have the nonzero cubic determinants above. This is a sharper comparison
than asserting that every O(-6) triple is obstructed: some exist even in
characteristic zero, including the thickening inside Q.

This does not establish a uniform obstruction to pairs of arbitrary
higher degree, and it does not replace the stronger all-mate-degree
quartic-carrier theorem.

## Evidence, independent-review requirements, and failed shortcuts

Certificate: research/computations/verify_44_filtered_contact_2026_10_23.py. Run with
/tmp/stci-z4-env/bin/python. It reconstructs the new e=0 cocycles,
all three degree-three annihilator spaces, full 35-column quartic contact
spaces, and the exact cubic determinant. It separately checks the new
e=1 determinants from inherited accepted h,T expressions. Expected final
output includes PASS for e=0 and e=1 determinants; it explicitly retains
the inherited status of e=1 completeness.

The [independent audit](2026-10-23-quartic-44-filtered-proof-independent-audit.md) checks the degree3 defect pushout and correction
uniqueness; the signs in m=gamma/delta*ell^2; the ambient torus action;
the exhaustiveness of quartic source matrices; and the passage from a
nonzero cubic determinant to generic intersection length three. It also checks that the inherited BF and e=1 classification hypotheses match
this application.

Two rejected shortcuts are preserved here:

- Global primitiveness cannot be assumed from generic order one. The
  e=0, D2=D3 degree3 type is essential and is covered explicitly.
- The early e1 jet-rebuild note claims fixed ruling lines in all nonquadric
  pencils, but that assertion conflicts with the later exact R0,R1
  pencil above: restricting those to Q gives common factor only C. This
  proposed proof uses the later independently audited complete pencils
  and flags the older line assertion as an unreconciled legacy passage.

The first exploratory e=0 script used the wrong sign in its quadratic
contact constraint and produced a false zero-dimensional quartic source.
Correcting the sign to delta*k+gamma*h=0 yields the two-dimensional source
and agrees with the exact gluing equation. The clean certificate states
this convention explicitly. No failed exploratory result is used.

Independent review outcome: PASS under the listed inherited inputs, with
finite-defect and global-realization hypotheses explicitly checked. The new
independent direct-Taylor certificate is
`research/computations/audit_44_filtered_contact_2026_10_23.py`. See the
[execution record](../validation/44-conormal-2026-10-23/README.md) for logs.
