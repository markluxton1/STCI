# Independent exclusion of the entire contact partition [4]

Date: 2026-10-09. Author: root. Status: **PROVED HERE under the accepted
genus-one ribbon-net and actual-coordinate projection reductions**.
This proof handles both endpoints and every direction chart. It does
not exclude [3,1] or prove complete coverage of [2,2].

Use the six actual RNC quadrics E0,...,E5 and the net condition

    M(c) eta=0,
    M(c)=[[c0,c1,c2],[c1,c2+c3,c4],[c2,c4,c5]],
    eta=(a,b,c),     b^2-ac != 0.

Normalize the surface pencil so Q2 has coefficient c3=0 and Q1 has
c3 nonzero. The latter is required because the deleted-middle center
misses the normalization. The hidden derivative of Q2 on the curve is

    L_C=c0 U^4-c1 U^3V-c4 UV^3+c5 V^4.

It is nonzero. If its divisor is [4], write it as a nonzero scalar
multiple of (alpha U+beta V)^4. Its missing middle coefficient gives
6 alpha^2 beta^2=0 in characteristic zero. Thus its only root is one
of the two parameter endpoints. Reversal of the five RNC coordinates
preserves the deleted-middle center and exchanges the endpoints, so
it suffices to treat L_C=U^4 after scaling Q2.

Then Q2=E0+h E2. Its net matrix is

    [[1,0,h],[0,h,0],[h,0,0]],

of determinant -h^3. Existence of the nonzero kernel eta forces h=0.
Hence Q2=E0, a=0, and the off-conic condition forces b nonzero.

Full singleton support at the endpoint U=0 requires the other hidden
derivative also to vanish there. For Q1 this says c5=0. The three net
equations, with a=0 and b nonzero, then give

    c4=0,     c2=-c3,     c1=c c3/b.

Modulo Q2 the first quadric is therefore a combination of E1 and
E3-E2. Every quadric in this surface pencil vanishes on the line

    Y0=Y1=Y2=0

with free coordinates Y3,Y4. On the entire line the gradient of
Q2=Y0Y2-Y1^2 is zero. The two-quadric complete intersection consequently
has Jacobian rank at most one at every point of this line and is
singular along a curve. This contradicts normality of the surface:
a normal surface is regular in codimension one.

The reverse endpoint follows by the center-preserving coordinate
reversal. Thus the entire partition [4] is excluded. The proof uses
singularity along an actual line, not an isolated ramification point.
No numerical sample, valuation parity assumption, or transformation
moving the projection center occurs. The two elementary matrix and
gradient identities are explicit above; an independent worker's
complete remaining-partition reconstruction is still in progress.
