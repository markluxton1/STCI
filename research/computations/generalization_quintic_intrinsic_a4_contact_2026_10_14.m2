-- NEW intrinsic A4 contact bound: only the first two needed octic
-- coefficients are extracted from the accepted actual primitive section.
-- This is not a replay of any accepted verifier.
base=QQ[delta,a,B,G,J]; R=base[p];
inPath="research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
outDir="research/validation/2026-10-14-quintic-intrinsic-a4-contact/attempt-01";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
F=value get inPath;
F0=sub(F,{sub(J,R)=>0_R});
c0=lift(coefficient(p^0,F0),base);
c1=lift(coefficient(p^1,F0),base);
assert(c0==0_base);
assert(c1==-2*G*(delta^2+2*B+G)*(3*delta^2+G)^2);
specialF=sub(F0,{sub(G,R)=>-3*(sub(delta,R))^2});
c2special=lift(coefficient(p^2,specialF),base);
assert(c2special==-108*delta^5*(delta^2-B));
save("jzero-first-coefficient",c1);
save("jzero-Gminus3delta2-second-coefficient",c2special);
print "PASS jzero A4 value, literal first coefficient, and literal second coefficient on its only surviving first-drop locus";
print "COMPLETE new intrinsic A4 contact identities; no accepted verifier replay";
exit 0;
