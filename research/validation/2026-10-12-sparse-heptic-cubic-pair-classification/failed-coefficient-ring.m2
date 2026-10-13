R=QQ[aa,bb,zz];
for nn in {1,2,3} do (
 pp=6-nn;
 spH=(zz-1)*(zz-aa)^nn*(zz-bb)^pp;
 c2=coefficient(zz^2,spH);
 c5=coefficient(zz^5,spH);
 print("PROFILE "|toString(nn)|","|toString(pp));
 print(c2); print(c5);
 print factor resultant(c2,c5,bb);
 print gb ideal(c2,c5)
);
spH=(zz-1)*(zz-aa)^6;
print "DOUBLE SIX";
print coefficient(zz^2,spH);
print coefficient(zz^5,spH);
print gb ideal(coefficient(zz^2,spH),coefficient(zz^5,spH));
