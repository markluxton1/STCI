# Prescribing normal jets and every attachment divisor

Date: 2026-10-28. Status: **provisional contribution, independently reviewed
in the [separate audit](2026-10-28-prescribed-attachment-audit.md); no
canonical promotion**. Curve throughout:
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\). The cohomology lemma
works over any field; the smooth construction uses an algebraically closed
field of characteristic zero. Write \(I=\mathcal I_C\), the **ideal sheaf**,
and \(Q=V(q)\), where \(q=x_0x_3-x_1x_2\).

This continues the question of what actual intersections containing \(C\)
look like. It strengthens the October 27 **generic** attachment-dominance
statement to an existence theorem for **every** finite attachment divisor,
in a uniform range of arbitrary degrees. It also gives an explicit twist
threshold for lifting compatible finite normal jets. Neither conclusion
assumes or resolves the characteristic-zero STCI answer.

## 1. Inputs and the distinction from previous work

Retrieval followed [INDEX](../INDEX.md), [MAP](../MAP.md),
[R-0020](../results/quartic_conormal_characteristic_jump.md), the
[all-degree general-pair note](2026-10-27-global-containing-intersections.md),
and the [moving-thickening lifting interface](2026-10-27-absorption-formal-lifting-interface.md).
Use as inherited premises: \(C\) has type \((1,3)\) on the smooth \(Q\);
\(I(3)\) is globally generated; and in characteristic zero
\(E=I/I^2=\mathcal O_{\mathbf P^1}(-7)^2\). These premises are not
reproved or recertified here.

The earlier note already gives the general residual degree, genus, Rao
module, boundary degree, and dominance of the attachment map for
\(a,b\ge4\). It explicitly leaves special effective divisors outside its
existence assertion. The formal note distinguishes actual section lifting
from abstract jet data and from generation of a primary ideal. Those
distinctions remain in force.

## 2. An all-order sheaf-power calculation

For every \(r\ge1\) there is an exact sequence

\[
0\longrightarrow I^{r-1}(d-2)
 \xrightarrow{\ q\ } I^r(d)
 \longrightarrow \mathcal O_Q(d-r,d-3r)\longrightarrow0. \tag{1}
\]

This is an assertion about sheaf powers, not about an unsaturated ordinary
homogeneous ideal power. Locally \(I=(q,f)\) is a regular sequence. Reducing
\(I^r\) modulo \(q\) gives \((f^r)\), with kernel
\((q)\cap I^r=qI^{r-1}\). On \(Q\), the ideal of \(rC\) is
\(\mathcal O_Q(-r,-3r)\), which proves (1).

Induction on \(r\), with Künneth on \(Q\), gives

\[
\boxed{H^1(\mathbf P^3,I^r(d))=0\quad(d\ge3r-1).} \tag{2}
\]

Indeed the left term of (1) has vanishing \(H^1\) by induction and the
right term has both bidegrees at least \(-1\). The base \(r=0\) uses
\(H^1(\mathbf P^3,\mathcal O(d))=0\). The same induction gives
\(H^2(I^r(d))=0\) for \(d\ge2r-2\): the first bidegree of the
right term is then at least \(-1\), so its \(H^2\) vanishes.

The \(H^1\) threshold is sharp. For \(d=3r-2\), the right term of (1)
is \(\mathcal O_Q(2r-2,-2)\); the adjacent \(H^1,H^2\) of the left
term vanish by the preceding bounds. Thus

\[
h^1(I^r(3r-2))=2r-1. \tag{3}
\]

Consequently every compatible section on the finite neighborhood
\(V(I^N)\) in twist \(d\ge3N-1\) lifts to an actual homogeneous form.
In particular the map

\[
H^0(I^r(d))\longrightarrow H^0(\operatorname{Sym}^r E(d))
\quad\text{is onto for }d\ge3r+2. \tag{4}
\]

For characteristic zero its target is
\(H^0(\mathcal O_{\mathbf P^1}(4d-7r))^{r+1}\).
At \(d=3r+1\) the cokernel has dimension \(2r+1\), by (3) applied to
\(r+1\) and \(H^1(I^r(d))=0\). In particular **every first-normal
section is the symbol of an actual degree-\(d\) equation for \(d\ge5\)**.
At degree four the cokernel has dimension three, agreeing with the inherited
quartic calculation without rerunning that certificate.

This is a concrete application of standard ideal-power cohomology.
[Shang, Theorem 1.1 and Theorem A](https://arxiv.org/html/2205.06289v1)
recalls Bertram–Ein–Lazarsfeld's general vanishing and studies its regularity
boundary. Our proof uses the specific smooth quadric to get (2) directly,
over any field. No literature novelty is asserted. Separate graded layers
chosen arbitrarily need not form a compatible finite-neighborhood section;
the full-jet assertion only concerns sections that already glue on that
neighborhood. Its bound grows with \(N\), so it supplies no fixed-twist
all-order lift or supported complete intersection.

## 3. Every attachment divisor can be constructed

**Proposition (sufficient range, not claimed sharp).** Let \(a,b\ge7\)
and let \(A\) be **any** effective divisor of degree
\(N=4(a+b)-14\) on the fixed marked \(C\), including nonreduced divisors.
There are actual degree-\(a,b\) homogeneous forms \(F,G\) such that:

1. \(S=V(F)\) and \(V(G)\) are smooth integral surfaces;
2. \(Y=V(F,G)=C\cup D\) scheme-theoretically, with \(D\) smooth and
   geometrically integral and with no common surface factor;
3. \(C\cap D=A\) as a scheme on \(C\), and the generic multiplicity
   along \(C\) is exactly one;
4. \(\deg D=ab-4\) and
   \(g(D)=(a+b-4)(ab-8)/2\).

The range seven is a convenient uniform bound ensuring first-jet separation
off \(C\) for the fixed-symbol variations. It is not a preferred degree
or a proposed reduction of arbitrary intersections.

**Proof.** Exchange \(a,b\) if needed to make \(a\le b\), and put
\(e=4a-7\), \(f=4b-7\). Choose a basepoint-free pair of binary forms
\(u=(u_1,u_2)\) of degree \(e\), for example \((s^e,t^e)\).
For a binary equation \(\delta\) of \(A\), the exact sequence

\[
0\to\mathcal O(f-e)\xrightarrow{u}
\mathcal O(f)^2\xrightarrow{v\mapsto\det(u,v)}
\mathcal O(e+f)\to0 \tag{5}
\]

shows that there is a pair \(v\) of degree \(f\) with
\(\det(u,v)=\delta\), since \(f-e\ge0\).
We can also choose \(v\) basepoint-free. It can vanish only at a point
of \(A\); adding \(h u\) for \(h\in H^0(\mathcal O(f-e))\)
avoids vanishing at every point of the finite support, because that line
bundle is globally generated and the field is infinite. This is a finite
union of proper affine hyperplanes to avoid, not an assertion about a
general divisor \(A\).

By (4), choose actual equations with first symbols \(u,v\). For a fixed
symbol, all lifts form an affine space under \(H^0(I^2(d))\). The sheaf
\(I^2(6)\) is globally generated, because it is a quotient of the square
of the globally generated \(I(3)\). Multiplication by linear forms makes
\(H^0(I^2(d))\) separate first jets on \(\mathbf P^3\setminus C\)
for every \(d\ge7\): at a point off \(C\), take a degree-six section
nonzero there and multiply it by ambient forms of degree \(d-6\).
[Bertini smoothness](https://stacks.math.columbia.edu/tag/0FD4) therefore
makes a general lift of \(u\) smooth off \(C\); its nowhere-zero first
symbol makes it smooth along \(C\). Such a projective hypersurface is
connected, hence smooth integral. Fix such an \(S\).

On \(S\), divide \(G|_S\) by the Cartier equation of \(C\). The
remaining section \(h\) defines an effective divisor
\(D\sim bH-C\) and restricts to \(\delta\) on \(C\), up to the
natural invertible factors. Thus \(D\) has no \(C\)-component and
\(D\cap C=A\). The local ideal is \((x,yh)\), with
\(S=(x)\), \(C=(x,y)\); since \(h\notin(y)\),
\((x,yh)=(x,y)\cap(x,h)\). This proves the scheme union and properness.

General fixed-symbol variations of \(G\) make \(D\) smooth away from
\(C\) by the same first-jet argument. At a simple zero of \(\delta\),
\(\partial h/\partial t\ne0\), so \(D\) is already smooth. At a
multiple zero \(p\), it suffices to make
\(\partial h/\partial y(p)\ne0\). Varying by \(I^2(b)\) changes
this value nontrivially: its stalk surjects onto the square of the ideal of
\(C\) on \(S\), and global generation of \(I^2(b)\) realizes a
nonzero value in its one-dimensional fiber. Avoid the corresponding
finitely many hyperplanes. Also choose the lift of \(v\) generally so
\(V(G)\) is smooth; \(v\) is nowhere zero on \(C\). All these are
nonempty open conditions on the same irreducible affine space of lifts.

Finally \(3H-C\) is globally generated on \(S\), as a quotient of
\(I(3)\). Hence \(bH-C\) is ample for \(b\ge4\). A smooth ample
effective divisor on a smooth projective surface is connected (for example
by the Hodge index theorem: two disjoint nonempty parts would both have
positive square and intersection zero). It is therefore integral. Adjunction
gives the stated degree and genus, as in the earlier general-pair note. □

## 4. A useful falsification control: all contact at one point

Set \(a=b=d\ge7\), \(e=4d-7\), and choose

\[
u=(s^e,t^e),\qquad v=(s^e,t^e+s^e).
\]

Both pairs are basepoint-free and \(\det(u,v)=s^{2e}\). The proposition
constructs smooth \(D\) with **all** \(8d-14\) attachments concentrated
at the single point \(s=0\), while the generic thickness is still one.
For \(d=7\), the residual has degree 45 and genus 205, and meets \(C\)
in the length-42 scheme at that point. The full CI has arithmetic genus
246, agreeing with \(0+205+42-1\).

This is an existence construction with prescribed actual equation symbols;
no full coefficient list or computed rational smooth pair is asserted.
It shows that extreme attachment concentration can coexist with a smooth
integral residual of the full residual degree. The distinction between
contact concentration and absorption is not merely a generic observation.

## 5. Evidence and next constructive use

The [new exact verifier](../computations/verify_normal_jet_freedom_2026_10_28.py)
checks the normal-layer ranks for \(1\le r\le5\), in the three degrees
\(3r+1,3r+2,3r+3\), over \(\mathbf Q\). Its
[saved output](../computations/normal_jet_freedom_2026_10_28.json) distinguishes
the nonzero cokernel just below the threshold from surjectivity at/above it.
These 15 finite cases corroborate the new formula, not its universal proof.

The resulting construction protocol is: choose compatible finite normal
data and a desired attachment pattern, lift in the stated twist range, then
use the remaining homogeneous equation freedom to control geometry away
from \(C\). To increase generic multiplicity one must instead make the
determinant vanish **identically** and retain higher symbols; the finite
effective divisor construction does not cross that boundary. With fixed
degrees, growing normal order eventually leaves the surjective range, so
the higher-order/global presentation question remains substantive.

The next general test is which prescribed higher-order local models admit
globally glued finite jets whose general lifts have a specified full
\(C\)-primary component and a controlled residual. This requires primary
extraction and actual equations, not just a chosen binary normal form.
