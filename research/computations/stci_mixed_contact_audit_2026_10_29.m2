-- Independent reconstruction of the normalized mixed-weight sextic certificate.
-- Parameter a=c0, so x2=t^3-a and x3=q+t*x2. This differs in sign from
-- the proposer implementation with v=-c0. No finite parameter sample in k.
R=QQ[k];
exps=flatten for a from 0 to 6 list flatten for b from 0 to 6-a list for c from 0 to 6-a-b list {a,b,c,6-a-b-c};
weights=apply(exps,e->(e#1+3*e#2+4*e#3)%6);
sampleMatrices={};
for ss in {1,8} do (
 P=R[t]; A=P/ideal(t^18-ss); B=A[q]; T=B/ideal(q^6);
 a=-2*t^5*(t^12-t^6+1)/(ss+1)*q;
 for n from 2 to 4 do (
  x2=t^3-a; x3=q+t*x2;
  f=k*q^3+(x2^3-t*x3^2)^2-a^2;
  a=a-sub(coefficient(q^(n+1),lift(f,B)),T)*t^13/(4*ss)*q^n;
 );
 x2=t^3-a; x3=q+t*x2;
 f=k*q^3+(x2^3-t*x3^2)^2-a^2;
 assert(f==0);
 polys=apply(exps,e->lift(t^(e#1)*x2^(e#2)*x3^(e#3),B));
 rows={};
 for j from 0 to 4 do (
  rowPolys=apply(polys,f->lift(sub(coefficient(q^j,f),A),P));
  rows=join(rows,for i from 0 to 17 list apply(rowPolys,f->sub(coefficient(t^i,f),R)));
 );
 M=matrix rows;
 assert(all(toList(0..89),i->all(toList(0..83),j->(((i%18)+4*(i//18))%6==weights#j) or M_(i,j)==0)));
 sampleMatrices=append(sampleMatrices,M);
 print("AUDIT_SAMPLE="|toString ss|" SHAPE="|toString(numRows M,numColumns M));
);
Fitting0={};
for w from 0 to 5 do (
 cs=positions(weights,i->i==w);
 rs=select(toList(0..89),i->((i%18)+4*(i//18))%6==w);
 Mw=submatrix(sampleMatrices#0,rs,cs);
 D=presentation prune coker transpose Mw;
 print("AUDIT_BLOCK="|toString w|" SHAPE="|toString(numRows Mw,numColumns Mw));
 print("AUDIT_PRESENTATION="|toString D);
 if w==0 then (
  Fitting0=append(Fitting0,minors(numRows D-1,D));
  D2=presentation prune coker transpose submatrix(sampleMatrices#1,rs,cs);
  print("AUDIT_SECOND_WEIGHT0_PRESENTATION="|toString D2);
  Fitting0=append(Fitting0,minors(numRows D2-1,D2));
  assert(saturate(sum Fitting0,ideal k)==ideal 1_R);
 ) else assert(saturate(minors(numRows D,D),ideal k)==ideal 1_R);
);
print("AUDIT_ALL_NONZERO_PARAMETERS_PASS");
