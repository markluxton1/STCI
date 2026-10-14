infRing=QQ[delta,a,B,G,J,p];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
Finf=sub(F,{a=>0,B=>0});
print("F infinity="|toString Finf);
scan(0..8,n->print("f"|toString n|"="|toString factor(sub(diff(p,n,Finf),{p=>0})/(n!))));
