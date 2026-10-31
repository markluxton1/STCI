-- Characteristic-zero certificate for every alpha*beta != 0 in
-- F=q^3+alpha*c0^2+beta*c2^2, against every actual global degree-six G.
-- Torus normalization gives F_k=k*q^3+c2^2-c0^2, k!=0.
-- Two exact finite sample orbits retain every nonzero parameter k.
-- This is a degree-(6,6) exclusion; no all-mate-degree assertion.
R=QQ[k]; P=R[t]; A=P/ideal(t^18-1); B=A[q]; T=B/ideal(q^6);
exps=flatten for a from 0 to 6 list flatten for b from 0 to 6-a list for c from 0 to 6-a-b list {a,b,c,6-a-b-c};
v=t^5*(t^12-t^6+1)*q;
for n from 2 to 4 do (
 x2=t^3+v; x3=t^4+q+t*v;
 f=k*q^3+(x2^3-t*x3^2)^2-v^2;
 correction=sub(coefficient(q^(n+1),lift(f,B)),T)*t^13/4;
 v=v+correction*q^n;
);
x2=t^3+v; x3=t^4+q+t*v;
f=k*q^3+(x2^3-t*x3^2)^2-v^2;
assert(f==0);
polys=apply(exps,e->lift(t^(e#1)*x2^(e#2)*x3^(e#3),B));
rows={};
for j from 0 to 4 do (
 rowPolys=apply(polys,f->lift(sub(coefficient(q^j,f),A),P));
 rows=join(rows,for i from 0 to 17 list apply(rowPolys,f->sub(coefficient(t^i,f),R)));
 stdio << "ROW_ORDER=" << j << endl; flush stdio;
);
M=matrix rows;
print("SHAPE="|toString(numRows M,numColumns M));
S=R[X0,X1,X2,X3];
qAmbient=X0*X3-X1*X2; c0Ambient=X1^3-X0^2*X2; c2Ambient=X2^3-X1*X3^2;
fAmbient=k*qAmbient^3+c2Ambient^2-c0Ambient^2;
carrierVector=transpose matrix {apply(exps,e->sub(coefficient(X0^(e#0)*X1^(e#1)*X2^(e#2)*X3^(e#3),fAmbient),R))};
assert(M*carrierVector==0);
assert(sub(carrierVector_(position(exps,e->e=={0,0,6,0}),0),R)==1_R);
print("GLOBAL_CARRIER_ANNIHILATED_AND_PRIMITIVE");
print("BLOCK_START"); flush stdio;
for residue from 0 to 5 do (
 colIds=select(toList(0..83),ii->(exps#ii#1+3*exps#ii#2+4*exps#ii#3)%6==residue);
 rowIds=select(toList(0..89),ii->(ii%18+4*(ii//18))%6==residue);
 blockM=submatrix(M,rowIds,colIds);
 otherRows=select(toList(0..89),ii->not member(ii,rowIds));
 assert(submatrix(M,otherRows,colIds)==0);
 if residue==0 then weightZeroBlock=blockM;
 blockCoker=prune coker transpose blockM;
 if residue!=0 then (
  assert(rank blockCoker==0);
  assert(saturate(ann Ext^1(blockCoker,R),ideal k)==ideal 1_R);
 );
 stdio << "BLOCK=" << residue << " SHAPE=" << (numRows blockM,numColumns blockM) << endl;
 stdio << "PRESENTATION=" << presentation blockCoker << endl; flush stdio;
);
-- A second exact sample orbit resolves every exceptional root in weight zero.
P2=R[t]; A2=P2/ideal(t^18-8); B2=A2[q]; T2=B2/ideal(q^6);
v=2/9*t^5*(t^12-t^6+1)*q;
for n from 2 to 4 do (
 x2=t^3+v; x3=t^4+q+t*v;
 f=k*q^3+(x2^3-t*x3^2)^2-v^2;
 correction=sub(coefficient(q^(n+1),lift(f,B2)),T2)*t^13/32;
 v=v+correction*q^n;
);
x2=t^3+v; x3=t^4+q+t*v;
f=k*q^3+(x2^3-t*x3^2)^2-v^2;
assert(f==0);
zeroExps=select(exps,e->(e#1+3*e#2+4*e#3)%6==0);
polys=apply(zeroExps,e->lift(t^(e#1)*x2^(e#2)*x3^(e#3),B2));
extraRows={};
for j from 0 to 4 do (
 rowPolys=apply(polys,f->lift(sub(coefficient(q^j,f),A2),P2));
 iList=select(toList(0..17),i->(i+4*j)%6==0);
 extraRows=join(extraRows,apply(iList,i->apply(rowPolys,f->sub(coefficient(t^i,f),R))));
);
combinedZero=weightZeroBlock||matrix extraRows;
combinedCoker=prune coker transpose combinedZero;
assert(rank combinedCoker==1);
assert(saturate(ann Ext^1(combinedCoker,R),ideal k)==ideal 1_R);
zeroIds=select(toList(0..83),ii->(exps#ii#1+3*exps#ii#2+4*exps#ii#3)%6==0);
assert(combinedZero*submatrix(carrierVector,zeroIds,{0})==0);
stdio << "COMBINED_ZERO_SHAPE=" << (numRows combinedZero,numColumns combinedZero) << endl;
stdio << "COMBINED_ZERO_PRESENTATION=" << presentation combinedCoker << endl; flush stdio;
print("PASS_ALL_NONZERO_PARAMETERS_BRANCH_ORDER5_KERNEL_IS_SCALAR_CARRIER");
