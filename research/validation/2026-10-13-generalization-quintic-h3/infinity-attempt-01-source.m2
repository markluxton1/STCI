-- NEW complete infinity-leading-drop locus from the actual fixed-degree forms.
h3infR=QQ[ll];h3infRing=h3infR[pp];delta=1-2*ll;lambda=ll;
h3infHC=value get "research/validation/2026-10-13-evening-h3-proportional/main-H-coefficients.txt";
h3infSC=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3infH=sum apply(toList(0..3),i->h3infHC#i*pp^i);
h3infS=sum apply(toList(0..5),i->h3infSC#i*pp^i);
print("infinity S leading factor="|toString factor h3infSC#5);
print("infinity H degree2 leading="|toString factor h3infHC#2);
print("infinity S degree4 leading="|toString factor h3infSC#4);
"research/validation/2026-10-13-generalization-quintic-h3/infinity-H.txt" << toString h3infH << close;
"research/validation/2026-10-13-generalization-quintic-h3/infinity-S.txt" << toString h3infS << close;
h3infConstraint=ideal h3infSC#5;
h3infUnits=(1-2*ll)*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*(1-2*ll)+ll-1);
h3infIdeal=saturate(h3infConstraint,ideal h3infUnits);
print("infinity finite candidate ideal="|toString gens gb h3infIdeal);
"research/validation/2026-10-13-generalization-quintic-h3/infinity-candidates.txt" << toString gens gb h3infIdeal << close;
-- Quotient by the complete finite candidate ideal preserves all branches.
h3infQ=h3infR/h3infIdeal; h3infQP=h3infQ[qq];
h3infMap=map(h3infQP,h3infRing,{qq,sub(ll,h3infQ)});
h3infHv=h3infMap h3infH;h3infSv=h3infMap h3infS;
print("candidate H degree="|toString degree h3infHv);
print("candidate S degree="|toString degree h3infSv);
-- Test leading coefficients invertible in this reduced complete finite algebra.
assert(ideal(h3infIdeal,lift(h3infSC#4,h3infR))==ideal(1_h3infR));
assert(ideal(h3infIdeal,lift(h3infHC#2,h3infR))==ideal(1_h3infR));
h3infF=frac h3infQ;
-- Use the polynomial quotient ring with explicit inverse of S4 instead of a fraction field.
h3infBez=(matrix{{1_h3infR}})//gens ideal(h3infSC#4,gens h3infIdeal);
h3infInverse=sub(h3infBez_(0,0),h3infQ);
h3infMonic=h3infInverse*h3infSv;
h3infRem=h3infHv^4 % h3infMonic;
h3infRemCs=apply(toList(0..3),i->coefficient(qq^i,h3infRem));
assert(ideal h3infRemCs==ideal(1_h3infQ));
print "PASS every leading-drop candidate has forbidden finite support";
"research/validation/2026-10-13-generalization-quintic-h3/infinity-support-remainders.txt" << toString h3infRemCs << close;
print "DONE complete infinity support chart";
