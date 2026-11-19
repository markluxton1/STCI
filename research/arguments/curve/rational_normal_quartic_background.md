# Background example: the rational normal quartic in P4

This set-theoretic calculation is valid over an algebraically closed field
of arbitrary characteristic. It concerns the P4 curve, not the fixed C0.
For the standard coordinates [s4:s3t:s2t2:st3:t4] in P4 use

    F2=x0*x2-x1²,
    F3=x0*x3²-2*x1*x2*x3+x2³,
    F4=x0*x4³-3*x1*x3*x4²+3*x2*x3²*x4-x3⁴.

On x0=1 put t=x1. F2 forces x2=t², then F3=(x3-t³)² forces
x3=t³, and F4=(x4-t⁴)³ forces x4=t⁴. On x0=0 the equations
successively force x1=x2=x3=0. The remaining point is the endpoint of
the rational normal quartic. This works over every algebraically closed
field, including characteristics two and three: powers still have only
zero as a root. It proves equality of reduced supports, not of schemes.
The degree-two ideal has dimension six: multiplication from Sym² of the
five-dimensional H0(O(4)) onto H0(O(8)) is surjective, so its kernel has
dimension 15-9=6. The standard six Hankel minors form its basis. The
three displayed equations do not eliminate this need for
six minimal quadratic scheme generators. No implication for the projected
P3 quartic follows.
