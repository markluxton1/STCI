# Which cover parameters can detect a smooth carrier?

Work in characteristic zero. Fix an integral smaller carrier \(F_a\)
through \(C_0\), with proposed mate degree \(b\ge a\ge5\) and
\(n=ab/4\) integral. At any point where \(F\) is smooth, let \(t\)
be a parameter along \(C_0\) lifted to the surface and \(Y\) a local
equation of \(C_0\) on it. If a mate exists, its equation on the smooth
completed carrier is a unit times \(Y^n\), by factoriality, sole
support and generic multiplicity. Thus \(A=k[[t]][Y]/Y^n\) is the
required local model. All its source restrictions can be computed
from \(F,n\) before a mate is supplied.

## A cyclic length independent of higher normal coefficients

Take a root value \(w\) of order \(e>0\) and write
\(R-w^2=\sum_{j\ge1} c_jY^j\) on the smooth carrier. If
\(s=\operatorname{ord}_t c_1<e\), the exact conductor length is
\[
 d(e,s)=(2e-s)\lfloor n^2/4\rfloor-e\lfloor n/2\rfloor.           \tag{5}
\]
The coefficients \(c_j\), \(j>1\), may be arbitrary integral series.
To prove this, expand \(z=\sqrt{w^2+(R-w^2)}\) in powers of \(Y\).
In the coefficient of \(Y^j\), the binomial term of index \(k<j\)
has valuation at least \(e-2ek+s\max(0,2k-j)\). This exceeds
\(e-(2e-s)j\) by at least \(2(e-s)(j-k)>0\). Hence the leading
coefficient comes entirely from the \(k=j\) term, with scalar
\(\binom{1/2}{j}\operatorname{lc}(w)^{1-2j}\operatorname{lc}(c_1)^j\).
In the triangular multiplication matrix an \(r\)-minor has pole order
at most \((2e-s)r(n-r)-er\) by summing the row and column indices.
This is largest at \(r=\lfloor n/2\rfloor\). The bottom-left minor
of that size attains the bound. After removing row and column units
its leading coefficient is the nonzero
[binomial determinant \(D_r(n-r)\)](endpoint_lattice_capacity.md#all-minors-capacity-and-a-cyclic-control).
Smith form gives (5). At \(s=e\), \(R-w^2=2wY+Y^2\) has integral
root \(w+Y\), so higher coefficients matter at this boundary.

## The two fixed endpoints leave at most one common parameter

Use the [smooth cover pencil](quadratic_cover_choice.md)
\(R_\lambda=2BC-AD+\lambda(AD-BC)\), \(\lambda\ne1,2\).
Assume \(F\) is smooth at both endpoints. At the first take
\(t=B/A,\ y=C/A-t^3,\ q=D/A-tC/A\); at the second reverse the four
coordinates. In each frame there is the exact identity
\[
             R_\lambda-t^4=t\,y+(\lambda-1)q                       \tag{6}
\]
after trivializing the quadric. If the image of \(q\) in the normal
line of \(C_0\) on \(F\) is a unit times \(Y\) to first order at an
endpoint, (6) gives \(s=0\) for every allowed \(\lambda\).
Otherwise \(F\) and the smooth quadric \(Q\) have the same tangent
plane there. Then \(y\) is a normal parameter and
\(q=\gamma_i(t)y\bmod y^2\), with \(\gamma_i(0)=0\), \(i=0,\infty\).
The coefficient \(t+(\lambda-1)\gamma_i(t)\) has order one unless
\[
                   1+(\lambda-1)\gamma_i'(0)=0.                   \tag{7}
\]
Only a nonzero slope can supply such a parameter. These slopes use
the indicated mutually reversed ambient frames.

Let \(B_{a,b}\) be the [nonsplit scalar lower bound](../../results/moving_quadratic_conductors.md#proof).
For any allowed nonsplit member, a strict scalar contradiction
\(\ell\Delta_\lambda<B_{a,b}\) requires tangency to \(Q\) at **both**
endpoints. For \(a\ge6\), both slopes must be equal and nonzero, and
the **only** candidate is \(\lambda=1-1/\gamma_0'(0)\). For \(a=5\),
at least one endpoint must satisfy (7), giving at most two candidates.
A candidate must still be an allowed nonsplit parameter, and its actual
higher coefficients must give a strict deficit.
Whenever \(s<2\), nonsplitting on \(F\) also follows locally.
A rational square root would be integral in the regular local ring.
Its restriction to the curve is \(\pm t^2\), so the linear normal
coefficient of its square would be divisible by \(t^2\).

Indeed \(d(2,0)=n(n-1)>B_{a,b}\) for \(a\ge5\), and
\(d(2,1)>B_{a,b}\) already for \(a\ge6\). For the second inequality
use \(d(2,1)\ge 3n^2/4-n-3/4\) and
\(B_{a,b}\le a(b^2/4-2b+27/4)-1\) from the linked proof.
The difference is bounded below by
\(ab^2(3a/64-1/4)+a(7b/4-27/4)+1/4>0\).
For the first inequality the corresponding lower bound is
\(ab^2(a/16-1/4)+a(7b/4-27/4)+1>0\).
Finally \(2d(2,1)=3\binom n2-\lfloor n/2\rfloor>B_{a,b}\) for
every \(a\ge5\): the proof of the scalar comparison bounds
\(3S_\Lambda-B_{a,b}\) below by
\(a(b^2/32+13b/8-27/4)+1>n/2\), here with \(\Lambda=(n)\).
The two endpoint lengths add since the supports are disjoint.

These conditions constrain the **whole actual degree-\(a\) source**.
Write the linear normal part of \(F\) as \(f_i(t)y+g_i(t)q\).
Tangency is \(f_i(0)=0,\ g_i(0)\ne0\), and then
\(\gamma_i'(0)=-f_i'(0)/g_i(0)\). Both tangencies have codimension
two on the open smooth at both points. Requiring an equal nonzero
slope has codimension three there. Indeed \(I_{C_0}(3)\) is globally
generated, and ambient forms of degree \(a-3\ge2\) restrict onto
the complete binary series of degree \(4(a-3)\). More explicitly,
\(A^m,A^{m-1}B,D^m,D^{m-1}C\), \(m=a-3\), interpolate the four
independent values and first derivatives in the two endpoint frames.
Multiplying the cubic generators by these forms surjects onto the two
jets of the rank-two conormal at both points, by local generation and
that interpolation. The conditions therefore have their displayed
codimensions in the ordinary homogeneous equation space. Integral
carriers in its dense open exist by Bertini: off \(C_0\) the system
has no basepoints and contains a nonzero cubic times all degree-\((a-3)\)
forms, so its image has dimension at least two. The generic member
already defeats this scalar comparison for **every** allowed nonsplit
choice and **every** allowed mate degree. This is a statement about
the local model a mate would require. Actual existence remains a
separate test. [Cubic generation](../../results/connected_normal_directions.md#connectedness-and-residual-attachment).

## Exact length at the moving osculating point

Now \(F\) need only be regular at the generic point of \(C_0\). Take
the [osculating cone](moving_quadratic_covers.md#a-general-osculating-cone-is-nonsplit-on-any-prescribed-carrier)
at a general \(p\). On \(A=1\) use \(x=B,\ y=C-x^3,\ q=D-xC\).
The two linear normal coefficients of \(R_p-(x-p)^8\) in this frame are
\[
\begin{split}
B_p(x)&=-56p^5+70xp^4-56x^2p^3+56x^3p^2-16x^4p+2x^5,\\
E_p(x)&=62p^4-56xp^3-8x^3p+2x^4.
\end{split}
\]
Both vanish at \(x=p\), with derivatives \(72p^4,-72p^3\).
Thus their combination on \(F\) has order \(s=1\) at general \(p\)
unless \(q-xy\) vanishes identically in the conormal line on \(F\)
over the generic point. This argument allows either \(y\) or \(q\)
to generate that line. The exceptional equality says exactly that
the tangent plane of \(F\) is the osculating plane along the general
point of \(C_0\). Indeed the plane with coefficients
\((-p^4,2p^3,-2p,1)\) has differential \(dq-p\,dy\) there.
In that case use \(Y=y\); the first coefficient is \(B_p+xE_p\),
whose Taylor series begins with \(-48p^3(x-p)^2\). Thus \(s=2\).
[Intrinsic osculating conormal line](../curve/special_plane_and_line_sections.md#1-the-intrinsic-line-defined-by-osculation).

The complete moving length on the required carrier model is \(d(4,1)\)
or \(d(4,2)\), respectively. Even the smaller value
\(d(4,2)=2d(2,1)>B_{a,b}\). This settles the scalar test on **all**
generically regular smaller carriers for this moving cover. The
[one-point homogeneous kernel](moving_quadratic_covers.md#the-homogeneous-jet-test)
continues to depend on the embedding of \(nC_0\) in \(F\). Both lengths
come from the full local algebra, including every higher normal term.

For the cyclic Hilbert function \(H=(1,\ldots,1)\), put
\(S=\binom n2\), \(M=\lfloor n/2\rfloor\), and
\(D=\lfloor n^2/4\rfloor\). The identity \(S+M=2D\) gives
\(U_H=3S+D-M=4S-D=d(4,1)\), whereas \(d(4,2)=4S-2D\).
Thus the general upper bound is sharp on the required nonosculating
regular local model. Concentrating four simple roots saves \(D\), or
\(2D\) in the osculating case, but neither saving reaches the scalar
contradiction. No actual supported CI is constructed by this equality.

Every integral quintic through \(C_0\) is generically regular along it.
Its nonzero restriction to \(Q\) has type \((5,5)\). Normal order at
least two would make that restriction divisible by \(s_{C_0}^2\), leaving
type \((3,-1)\), which has no sections. Hence the moving scalar test
fails for every integral quintic carrier; singularities at the fixed
endpoints and the homogeneous-kernel test remain separate questions.

The osculating exception has a global
[ribbon obstruction](../normal-geometry/osculating_ribbon_obstruction.md):
the fixed direction does not extend to a primitive triple. For a
generically regular carrier its first symbol vanishes at a divisor of
degree \(4a-8\). Those zeros and higher-thickening defects cannot be
discarded when using the generic cyclic calculation.
