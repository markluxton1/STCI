# Entirely-thick boundary: Segre coordinate audit of the ruling-root argument

Date: 2026-10-07
Status: AUDITED / EXISTING DISTINCT-ROOT BOUND SURVIVES

For C=[s^4:s^3t:st^3:t^4] on the quadric x0*x3=x1*x2, the parametrization is, up to swapping the two middle Segre coordinates,
[s:t] x [s^3:t^3].
Thus the two ruling projections restricted to C have degrees 1 and 3.

With C=(1,3), the fibers occurring in R_F of class (2p,0) are trisecant ruling lines. A generic root selects L with C cap L=P1+P2+P3.

The first normal form of F on the quadric-direction section S_Q vanishes at all three points. This accounts for deg(D|S_Q)=6p=3*(2p).

However a point lies in D cap D' cap S_Q only if the first normal form of G also vanishes there. Although G|Q contains h^q, after dividing by the generic C-order q the first normal form on S_Q is controlled by the residual factor R_G. On L, R_G|L is a nonzero section of O_L(q), whose zeros are supported on C cap L. It has at least one zero but may concentrate all q zeros at one of the three points.

Therefore each distinct root of R_F guarantees at least one common point on S_Q, not three.

At the boundary W=sum c_j T_j and each distinct T_j meets S_Q once. Distinct trisecant fibers give disjoint degree-three divisors on C, so their guaranteed common points are distinct. Hence the existing bound survives:
#roots(R_F) <= #horizontal sections <= min(p,q).

Divisor interpretation: D|S_Q contains the pullback under the degree-three ruling projection C=S_Q -> P1_ruling of the degree-2p root divisor of R_F. By contrast W|S_Q=sum c_j P_j records only points where the mate first normal form also vanishes, with multiplicities from the full pair intersection. Thus c_j and root multiplicities M_j are not directly comparable.

The surviving discrete datum for each root L_i is an exponent allocation
(e_i1,e_i2,e_i3), e_i1+e_i2+e_i3=q,
with positive entries indicating which of the three preimages are common first-normal zeros. Any stronger obstruction must constrain these incidence assignments or their exceptional clusters; degree counting alone does not.
