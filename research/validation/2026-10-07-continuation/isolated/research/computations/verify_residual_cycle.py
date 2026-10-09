"""Exact lattice checks for the local residual-cycle determinant.

These checks cover t^a x-y^r,x^s and q=t^beta y+x. The accompanying
filtered-module argument, not this finite family, proves the theorem.
"""
import sympy as sp

t = sp.symbols('t')
count = 0
for r in range(2, 5):
    for s in range(2, 5):
        m = r*s
        for a in range(1, 4):
            defects = [(i//r)*a for i in range(m)]
            assert defects[0] == defects[1] == 0
            for beta in range(3):
                # e_i=t^{-D_i} y^i, x=t^{-a}y^r.
                mat = sp.zeros(m)
                for i in range(m):
                    if i+1 < m:
                        mat[i+1, i] += t**(beta+defects[i+1]-defects[i])
                    if i+r < m:
                        mat[i+r, i] += t**(defects[i+r]-defects[i]-a)
                assert all(mat[0,j] == 0 for j in range(m))
                assert all(mat[i,m-1] == 0 for i in range(m))
                block = mat[1:m, 0:m-1]
                det = sp.prod(block[i,i] for i in range(m-1))
                assert sp.expand(det - t**((m-1)*beta+defects[-1])) == 0
                # First-normal content of (t^a*x-y^r,x^s) is t^a.
                assert a <= defects[-1]
                count += 1
print(f'PASS: {count} exact residual-cycle lattice determinants; A<=Dtop')
