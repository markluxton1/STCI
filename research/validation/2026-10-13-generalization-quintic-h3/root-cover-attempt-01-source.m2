-- NEW exact root-count structural cover; no old checks replayed.
h3coverBase=QQ[dl,ll,MonomialOrder=>GRevLex]; h3coverRing=h3coverBase[pp];
delta=dl;lambda=ll;
h3Hc=value get "research/validation/2026-10-13-evening-h3-proportional/main-H-coefficients.txt";
h3Sc=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3H=sum apply(toList(0..3),i->h3Hc#i*pp^i);
h3S=sum apply(toList(0..5),i->h3Sc#i*pp^i);
h3Prem=(ff,gg,nn)->(
    vv:=ff;lk:=coefficient(pp^nn,gg);
    for ii from (max apply(exponents ff,e->e#0)) to nn by -1 do vv=lk*vv-coefficient(pp^ii,vv)*pp^(ii-nn)*gg;
    vv
);
h3lcH=h3Hc#3;h3lcS=h3Sc#5;
h3smallrem=h3Prem(h3S,h3H,3);
h3smallCs=apply(toList(0..2),i->lift(coefficient(pp^i,h3smallrem),h3coverBase));
"research/validation/2026-10-13-generalization-quintic-h3/h-divides-s-remainder.txt" << toString h3smallCs << close;
h3common=first h3smallCs;scan(drop(h3smallCs,1),cc->h3common=gcd(h3common,cc));
print("H divides S common factor="|toString factor h3common);
h3smallCs=apply(h3smallCs,cc->cc//h3common);
h3smallideal=ideal h3smallCs;
print("H divides S raw ideal="|toString gens gb h3smallideal);
h3units=dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1);
h3smallsat=saturate(h3smallideal,ideal(h3units*h3lcH*h3lcS));
print("H divides S saturated ideal="|toString gens gb h3smallsat);
"research/validation/2026-10-13-generalization-quintic-h3/h-divides-s-ideal.txt" << toString gens gb h3smallsat << close;
print "PHASE Newton distinct-root rank";
-- e_i=(-1)^i*c_(5-i)/c5, scaled power sums P_k=c5^k sum roots^k.
h3nums=apply(toList(0..5),i->(-1)^i*h3Sc#(5-i));
h3powers={5_h3coverBase};
for kk from 1 to 8 do (
    vv=0_h3coverBase;
    for ii from 1 to min(kk-1,5) do vv=vv+(-1)^(ii-1)*h3nums#ii*h3lcS^(ii-1)*h3powers#(kk-ii);
    if kk<=5 then vv=vv+(-1)^(kk-1)*kk*h3nums#kk*h3lcS^(kk-1);
    if kk>5 then vv=vv+(-1)^4*h3nums#5*h3lcS^4*h3powers#(kk-5);
    h3powers=append(h3powers,vv)
);
h3Hermite=matrix apply(toList(0..4),i->apply(toList(0..4),j->h3powers#(i+j)));
-- This congruence rescales entry (i,j) by c5^(i+j), so ranks agree if c5!=0.
h3rank2ideal=minors(3,h3Hermite);
print "PHASE rank-two Groebner";
h3rank2sat=saturate(h3rank2ideal,ideal(h3units*h3lcS));
print("at-most-two-root saturated ideal="|toString gens gb h3rank2sat);
"research/validation/2026-10-13-generalization-quintic-h3/rank2-ideal.txt" << toString gens gb h3rank2sat << close;
print "DONE new h3 root-support cover";
