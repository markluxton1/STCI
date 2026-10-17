-- NEW original-generator power witnesses; no inherited check replayed.
h3mwR=QQ[xx,dl,ll]; delta=dl;lambda=ll;
h3mwC=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3mwU=dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*h3mwC#5;
h3mwM=value get "research/validation/2026-10-13-generalization-quintic-h3/multiplicity4-input.txt";
h3mwI=ideal h3mwM;
h3mwN=1;
while h3mwN<=15 and (h3mwU^h3mwN % h3mwI)!=0 do h3mwN=h3mwN+1;
print("multiplicity4 witness exponent="|toString h3mwN);
assert(h3mwN<=15);
h3mwW=(matrix{{h3mwU^h3mwN}})//h3mwM;
assert(h3mwM*h3mwW==matrix{{h3mwU^h3mwN}});
"research/validation/2026-10-13-generalization-quintic-h3/multiplicity4-witness.txt" << toString h3mwW << close;
"research/validation/2026-10-13-generalization-quintic-h3/multiplicity4-witness-exponent.txt" << toString h3mwN << close;
print "PASS literal multiplicity4 original-generator witness";
