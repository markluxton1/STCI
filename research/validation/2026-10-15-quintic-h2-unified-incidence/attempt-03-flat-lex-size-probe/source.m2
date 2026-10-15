-- NEW one shared 12-generator support incidence on D(q5,q6).
-- Accepted Q6, rational-map domain and old closures are inputs.
-- Flat lex order with v first makes Delta,K monic-leading divisors.
outDir="research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-03-flat-lex-size-probe";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
tower=QQ[vPar,deltaPar,wPar,MonomialOrder=>Lex];
save("stage","loading-inputs");
qDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient";
nDir="research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01";
q=apply(toList(0..6),i->value get(qDir|"/Q-coefficient-"|toString i|".txt"));
qi=i->if i<0 or i>6 then 0_tower else q#i;
r=apply(toList(0..6),i->(6-2*i)*vPar*qi(i)+(14-2*i)*qi(i-1)-2*(i+1)*wPar*qi(i+1));
ri=i->if i<0 or i>6 then 0_tower else r#i;
jNum=value get(nDir|"/Jbar-numerator.txt");
cofactorNum=value get(nDir|"/cofactor-determinant-numerator.txt");
normProduct=value get(nDir|"/primitive-norm.txt");
disc=vPar^2-4*wPar; coverK=vPar^2+6*vPar*wPar+6*wPar^2+2*wPar;
mat=transpose matrix{apply(toList(0..7),qi),apply(toList(0..7),i->qi(i-1)),apply(toList(0..7),ri)};
triples=unique join(apply({0,1,2,3,4,7},i->sort{i,5,6}),apply(toList(0..5),i->sort{i,6,7}));
assert(#triples==11);
M56=qi(5)*ri(6)-qi(6)*ri(5);
raw={jNum*M56};
scan(toList(0..10),i->(save("stage","constructing-cubic-"|toString i); raw=append(raw,det submatrix(mat,triples#i,{0,1,2})); save("raw-generator-"|toString(i+1),last raw)));
save("raw-12-generators",matrix{raw});
save("cubic-row-triples",triples);
save("nonzero-Q-ideal",matrix{{qi(5),qi(6)}});
save("domain-unit-product",deltaPar*disc*coverK*cofactorNum);
save("stage", "built-12-generators");
normalize=f->(
 nf:=f; mult:=1_tower; exps:={0,0};
 if nf!=0 then scan(toList(0..1),i->(
  u:={disc,coverK}#i;
  while nf%u==0 do (nf=nf//u; mult=mult*u; exps=apply(toList(0..1),j->exps#j+if i==j then 1 else 0));
 ));
 assert(f==mult*nf);
 {nf,mult,exps}
 );
normRows=apply(toList(0..11),i->(
 save("stage","normalizing-generator-"|toString i);
 normalize(raw#i)
 ));
flat=QQ[deltaPar,vPar,wPar];
toFlat=map(flat,tower,{vPar,deltaPar,wPar});
flatRaw=apply(raw,f->toFlat f);
flatNorm=apply(normRows,row->toFlat(row#0));
deltaExps=apply(toList(0..11),i->(
 f:=flatNorm#i; ee:=0;
 if f!=0 then while f%deltaPar==0 do(f=f//deltaPar;ee=ee+1);
 assert(flatRaw#i==deltaPar^ee*toFlat(normRows#i#1)*f);
 flatNorm#i=f;
 ee
 ));
save("normalized-12-generators",matrix{flatNorm});
save("removed-Delta-K-exponents",apply(normRows,row->row#2));
save("removed-delta-exponents",deltaExps);
save("norm-product",toFlat normProduct);
save("normalized-degrees",apply(flatNorm,f->if f==0 then -1 else first degree f));
save("normalized-term-counts",apply(flatNorm,f->#terms f));
save("stage","complete");
print "PASS exact product bindings for 12 generators; removed only delta/Delta/K units";
print("degrees "|toString apply(flatNorm,f->if f==0 then -1 else first degree f));
print("term counts "|toString apply(flatNorm,f->#terms f));
print "COMPLETE unified reduced incidence size probe; no elimination launched";
exit 0;
