-- New support restrictions from the accepted actual primitive octic.
-- No conductor/module theorem or old verifier is replayed.
h3eBase=QQ[delta,lambda]; h3eField=frac h3eBase; h3eRing=h3eField[p];
a=delta*(delta+2*lambda-1)/(6*lambda^2);
h3eB0=delta*(delta+2*lambda-1)/(3*lambda);
h3eG0=delta*((lambda-3)*delta+lambda+1)/3;
h3eD0=delta*((lambda^2-12)*delta+lambda^2-2*lambda+6)/6;
B=h3eB0-a; G=h3eG0-3*h3eB0+2*a; J=h3eD0-2*h3eG0+2*h3eB0-a;
h3eOctic=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
h3eH=G+(6*B+delta^2-3*delta)*p+(3*a-3*B+2*delta)*p^2-2*a*p^3;
h3eS=h3eOctic//h3eH;
h3eHC=-3*lambda^2/delta*h3eH;
h3eSC=432*lambda^4/delta^3*h3eS;
-- Save exact coefficient lists so no multivariate coefficient interface is used.
h3eHcs=apply(toList(0..3),i->lift(coefficient(p^i,h3eHC),h3eBase));
h3eScs=apply(toList(0..5),i->lift(coefficient(p^i,h3eSC),h3eBase));
"research/validation/2026-10-13-evening-h3-proportional/main-H-coefficients.txt" << toString h3eHcs << close;
"research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt" << toString h3eScs << close;
print("H LEADING="|toString factor(h3eHcs#3));
print("S LEADING="|toString factor(h3eScs#5));
print("Jbar="|toString factor numerator J);
print "PHASE resultant";
h3eRes=lift(numerator resultant(h3eHC,h3eSC,p),h3eBase);
print("H S RESULTANT="|toString factor h3eRes);
"research/validation/2026-10-13-evening-h3-proportional/main-resultant.txt" << toString factor h3eRes << close;
print "DONE resultant";
