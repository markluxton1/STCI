# Four complete pure-top charts for the remaining degree-two quartic incidence

Date: 2026-10-06. Status: **EXACT SPECIFICATION; FULL LOCUS UNRESOLVED**.
The companion `localcoh-e2-incidence-2026-10-06.py` exports actual
two-target equations from the verified tensor. This reduces the 30 free
ancestor coordinates while retaining all allowed degeneration of the cyclic
inverse system at its top-symbol zero.

Use the 32-by-30 top map \(M\), of rank 29, and its three-row annihilator
\(L\). For a primitive homogeneous quadratic normal-dual direction
\(\nu=(p,r)\), the pure cubic top is

\[
c_i(t)=h(t)p(t)^i r(t)^{3-i},\qquad i=0,1,2,3,
\]

in the residue divided-power coordinates, where \(h=h_0+h_1t\) is
nonzero. The three equations \(Lc=0\) express precisely that this top lifts
to the 30-dimensional \(H^0(T_4(-7))\) space. They do not assert that its
annihilator quadruple is primitive at the zero of \(h\).

Select 29 independent columns of \(M\) and 29 independent rows of that
column submatrix. Inverting their rational square matrix gives a fixed
rational right inverse \(R\) on \(\operatorname{im}M\). Thus, on the
three-equation top-image locus, every ancestor is uniquely

\[
\alpha=Rc+\lambda k,
\]

where \(k\) spans the one-dimensional \(T_3(-7)\) kernel. The exporter
retains \(\lambda\) and contracts the entire actual quartic multiplication
tensor with these ancestor coordinates.

Primitivity forces at least one of \(p(0),r(0)\) nonzero. Normalize that
coordinate to one. Scaling the ancestor normalizes either \(h_0=1\) when
\(h_0\ne0\), or \(h=t\) when \(h_0=0\). Hence four charts cover every
primitive degree-two ancestor candidate:

| Direction normalization | Top coefficient |
| --- | --- |
| \(p(0)=1\) | \(h=1+h_1t\) |
| \(r(0)=1\) | \(h=1+h_1t\) |
| \(p(0)=1\) | \(h=t\) |
| \(r(0)=1\) | \(h=t\) |

For each chart the exporter writes the three top-image equations and the
74 multiplication equations for each target. The full two-target systems
have 43 variables on the first two charts and 42 variables on the last two:
five free direction coefficients, one optional coefficient \(h_1\), the
one lower correction, and 36 multiplier coefficients. Depending on zero
equations the stored generator count is smaller than 151. A one-target
version is exported as well.

If a computation returns a nonempty closed locus, primitive degree two
requires the homogeneous resultant \(\operatorname{Res}(p,r)\ne0\).
The exported systems do not discard this open condition or pretend that
all their lower-degree boundary directions are primitive degree two. A
unit ideal for the larger chart would suffice for exclusion; a non-unit
ideal requires inspecting this open locus and retaining the rank conditions
in `2026-10-06-localcoh-incidence.md`.

Two direct Gröbner attempts on the \(p(0)=1\) charts were interrupted
after a bounded run on Oct6 without an ideal result. The equations remain
available for continuation. A second run with multiline input and live
terminal output reached the 145-generator ideal on the \(h=t\) chart;
no full-locus conclusion is obtained merely from its progress.

The separate uniform parity certificate excludes the full primitive family
\((p,r)=(a_0+a_2t^2,b_1t)\), whose top coefficient is necessarily the
constant line. It is a verified sublocus of these general charts, not a
classification of all quadratic directions. All other non-ruling direction
strata remain research obligations.
