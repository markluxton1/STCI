#!/usr/bin/env python3
"""Construct generic rational corank-one data, for exact later specialization.

This is a fallback around expensive degree-15 field matrix reduction; no
accepted certificate verifier is called. The output still requires validation.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
D=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fresh',D/'general_localcoh_family2_degree15_corank_one_2026_10_14.py');G=importlib.util.module_from_spec(spec);spec.loader.exec_module(G)
T=G.T;a=G.a;t=a.tensor();seed=G.s['seed'];q=18;m=74
head=['P=QQ[k]; K=frac P; k=sub(k,K);']
head+=['z'+str(i)+'=sub(('+s.replace('**','^')+'),K);' for i,s in enumerate(seed)]
def entries(row,j):
 cs=[]
 for l in range(30):
  c=sum((T[row][r]*t[r][18*l+j]for r in range(m)),Q(0))
  if c:cs.append('('+str(c)+')*z'+str(l))
 return '+'.join(cs)or '0_K'
def matrows(rs):return 'matrix{'+','.join('{'+','.join(entries(i,j)for j in range(q))+'}'for i in rs)+'}'
head+=['A='+matrows(range(q))+';','B='+matrows(range(q,m))+';','v='+G.mat(G.U[:q])+';','w='+G.mat(G.U[q:])+';']
old=(D/'general-localcoh-family2-degree15-corank-one-2026-10-14.m2').read_text()
start=old.index('q=18; p=56;')
end=old.index('R=K[lambda];')
body=old[start:end]
base='general-localcoh-family2-symbolic-corank-one-2026-10-14'
body+='''
ff=openOut "research/computations/STEM-rational-data.txt";
for tag in {"h","a","c","Fh","Fa","pp"} do (VV=value tag; ff << tag << " " << numRows VV << " " << numColumns VV << endl; for i from 0 to numRows VV-1 do for j from 0 to numColumns VV-1 do ff << i << " " << j << " " << toString VV_(i,j) << endl);
for tag in {"gN0","gN1","gN2"} do (VV=value tag; ff << tag << " " << numRows VV << " " << numColumns VV << endl; for i from 0 to numRows VV-1 do for j from 0 to numColumns VV-1 do ff << i << " " << j << " " << toString VV_(i,j) << endl);
for ell from 0 to #linrows-1 do (
 ff << "linN0-" << ell << " " << numRows(linN0#ell) << " " << numColumns(linN0#ell) << endl; for i from 0 to 73 do ff << i << " 0 " << toString(linN0#ell)_(i,0) << endl;
 ff << "linN1-" << ell << " " << numRows(linN1#ell) << " " << numColumns(linN1#ell) << endl; for i from 0 to 73 do ff << i << " 0 " << toString(linN1#ell)_(i,0) << endl
 );
close ff;
print("PASS generic rational corank-one dual data saved");
exit 0;
'''.replace('STEM',base)
(D/(base+'.m2')).write_text('\n'.join(head)+'\n'+body)
print('SYMBOLIC GENERATED',len('\n'.join(head)+body),flush=True)
