R=QQ[aa,bb,zz];
for nn in {1,2,3} do (
 pp=6-nn;
 hh=(zz-1)*(zz-aa)^nn*(zz-bb)^pp;
 c2=coefficient(zz^2,hh);
 c5=coefficient(zz^5,hh);
 print("PROFILE "|toString(nn)|","|toString(pp));
 print(c2); print(c5);
 print factor resultant(c2,c5,bb);
 print gb ideal(c2,c5)
);
hh=(zz-1)*(zz-aa)^6;
print "DOUBLE SIX";
print coefficient(zz^2,hh);
print coefficient(zz^5,hh);
print gb ideal(coefficient(zz^2,hh),coefficient(zz^5,hh));
