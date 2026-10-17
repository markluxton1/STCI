-- New support incidence on the one remaining Jbar=0 proportional branch.
-- Input: previously accepted conormal and actual octic identities.
h3lBase=QQ[delta,lambda];
h3lHcs=value get "research/validation/2026-10-13-evening-h3-proportional/main-H-coefficients.txt";
h3lScs=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3lParam=QQ[dl]; h3lField=frac h3lParam; h3lRing=h3lField[q];
h3lMap=map(h3lField,h3lBase,{dl,1_h3lField});
h3lH=sum apply(toList(0..3),i->h3lMap(h3lHcs#i)*q^i);
h3lS=sum apply(toList(0..5),i->h3lMap(h3lScs#i)*q^i);
print("LAMBDA1 H="|toString factor h3lH);
print("LAMBDA1 S="|toString factor h3lS);
h3lPorder=0;
while sub(h3lS,{q=>0})==0 do (h3lPorder=h3lPorder+1;h3lS=h3lS//q);
print("LAMBDA1 generic order at p=0="|toString h3lPorder);
print("LAMBDA1 S reduced leading="|toString factor numerator coefficient(q^4,h3lS));
-- For the complete projective support incidence, H*q contains every allowed
-- root, including A4 q=0 and target infinity if the homogeneous H drops.
-- Work first on the displayed nonzero leading-coefficient chart.
h3lRem=(h3lH*q)^5 % h3lS;
h3lRemCs=apply(toList(0..3),i->lift(numerator coefficient(q^i,h3lRem),h3lParam));
h3lG=first h3lRemCs;scan(drop(h3lRemCs,1),c->h3lG=gcd(h3lG,c));
print("LAMBDA1 support coefficient gcd="|toString factor h3lG);
print("LAMBDA1 remainder coefficients="|toString h3lRemCs);
"research/validation/2026-10-13-evening-h3-proportional/lambda1-remainder-coefficients.txt" << toString h3lRemCs << close;
print "DONE lambda1 probe";
