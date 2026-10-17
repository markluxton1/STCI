infRing=QQ[delta,a,B,G,J,p];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
Finf=sub(F,{a=>0,B=>0});
print("F infinity="|toString Finf);
fc=apply(0..8,n->(sum select(terms Finf,mm->((exponents mm)#0)#5==n))//p^n);
scan(0..8,n->print("f"|toString n|"="|toString factor(fc#n)));
infJ0=sub(Finf,{J=>0});
