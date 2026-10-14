-- NEW literal witness for the H | S incidence exclusion.
h3certR=QQ[dl,ll];
h3certCs=value get "research/validation/2026-10-13-generalization-quintic-h3/h-divides-s-remainder.txt";
h3certCs=apply(h3certCs,g->g//ll^2);
h3certI=ideal h3certCs;
h3certU=dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*(dl+2*ll-1);
-- S leading need not be retained if this stronger power lies in the original ideal.
h3certN=1;
while h3certN<=12 and (h3certU^h3certN % h3certI)!=0 do h3certN=h3certN+1;
print("first candidate witness exponent="|toString h3certN);
assert(h3certN<=12);
h3certW=(matrix{{h3certU^h3certN}})//gens h3certI;
assert((gens h3certI)*h3certW==matrix{{h3certU^h3certN}});
"research/validation/2026-10-13-generalization-quintic-h3/h-divides-s-witness.txt" << toString h3certW << close;
"research/validation/2026-10-13-generalization-quintic-h3/h-divides-s-witness-exponent.txt" << toString h3certN << close;
print "PASS literal H-divides-S coefficient witness";
