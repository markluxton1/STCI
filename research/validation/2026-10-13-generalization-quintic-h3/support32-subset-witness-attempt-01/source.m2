-- NEW lower-degree extraction, verified against original SIX generators.
-- Accepted support alternatives are not replayed.
h3swR=QQ[xx,dl,ll]; delta=dl;lambda=ll;
h3swC=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3swU=dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*h3swC#5;
h3swM=value get "research/validation/2026-10-13-generalization-quintic-h3/support32-input.txt";
assert(numColumns h3swM==6);
h3swSub=h3swM_{0..4};
h3swI=ideal h3swSub;
h3swN=1;
while h3swN<=15 and (h3swU^h3swN % h3swI)!=0 do h3swN=h3swN+1;
print("support32 witness exponent="|toString h3swN);
assert(h3swN<=15);
h3swSubW=(matrix{{h3swU^h3swN}})//h3swSub;
h3swW=h3swSubW || matrix{{0_h3swR}};
assert(h3swM*h3swW==matrix{{h3swU^h3swN}});
"research/validation/2026-10-13-generalization-quintic-h3/support32-subset-witness.txt" << toString h3swW << close;
"research/validation/2026-10-13-generalization-quintic-h3/support32-subset-witness-exponent.txt" << toString h3swN << close;
print "PASS literal support32 original-six-generator witness";
