-- NEW exact remaining support pattern: a triple root and a double root,
-- both lying on the complete homogeneous common conormal cubic H.
h3patR=QQ[xx,dl,ll,MonomialOrder=>GRevLex];delta=dl;lambda=ll;
h3patC=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3patHC=value get "research/validation/2026-10-13-evening-h3-proportional/main-H-coefficients.txt";
h3patS=sum apply(toList(0..5),i->h3patC#i*xx^i);
h3patH=sum apply(toList(0..3),i->h3patHC#i*xx^i);
h3patD1=diff(xx,h3patS);h3patD2=diff(xx,h3patD1);
h3patDisc=h3patC#4^2-4*h3patC#3*h3patC#5-6*xx*h3patC#4*h3patC#5-15*xx^2*h3patC#5^2;
h3patYn=-h3patC#4-3*xx*h3patC#5;h3patYd=2*h3patC#5;
h3patHy=sum apply(toList(0..3),i->h3patHC#i*h3patYn^i*h3patYd^(3-i));
h3patI=ideal(h3patS,h3patD1,h3patD2,h3patDisc,h3patH,h3patHy);
"research/validation/2026-10-13-generalization-quintic-h3/support32-input.txt" << toString gens h3patI << close;
h3patU=dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*h3patC#5;
print "PHASE remaining complete triple/double support incidence";
h3patSat=saturate(h3patI,ideal h3patU);
print("triple/double support saturated ideal="|toString gens gb h3patSat);
"research/validation/2026-10-13-generalization-quintic-h3/support32-ideal.txt" << toString gens gb h3patSat << close;
print "DONE remaining triple/double support incidence";
