-- Correct source-coordinate binding for the NEW h2 Hamiltonian incidence.
-- Prior saved c_i describe B(t)=Fdet(1-t,1) at the accepted h2 map.
-- Accepted h2 x=r/delta has target p=delta/r=1/x, so the actual
-- source binary octic is G(x)=x^8*B(1-1/x).
-- Only a constant invertible binary-coordinate transformation is done here.
par=QQ[deltaPar,vPar,wPar];
inDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-02";
outDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-05-correct-coordinate";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
oldCf=apply(toList(0..8),ii->value get(inDir|"/F-coefficient-"|toString ii|".txt"));
cf=apply(toList(0..8),jj->(-1)^(8-jj)*sum(toList((8-jj)..8),ii->binomial(ii,8-jj)*oldCf#ii));
R=par[x];
oldF=sum(toList(0..8),ii->sub(oldCf#ii,R)*x^ii);
newF=sum(toList(0..8),ii->sub(cf#ii,R)*x^ii);
literalTransform=sum(toList(0..8),ii->sub(oldCf#ii,R)*(x-1)^ii*x^(8-ii));
assert(newF==literalTransform);
-- Inverse transformation recovers every saved old coefficient, including
-- fixed-degree leading drops: B(t)=(1-t)^8*G(1/(1-t)).
inverseTransform=sum(toList(0..8),ii->sub(cf#ii,R)*(1-x)^(8-ii));
assert(oldF==inverseTransform);
ci=ii->if ii<0 or ii>8 then 0_par else cf#ii;
eigenCf=apply(toList(0..8),jj->(8-2*jj)*vPar*ci(jj)+(18-2*jj)*ci(jj-1)-2*(jj+1)*wPar*ci(jj+1));
a4Cf=apply(toList(0..9),jj->(8-3*jj)*vPar*ci(jj)+(19-3*jj)*ci(jj-1)-3*(jj+1)*wPar*ci(jj+1));
H=x^2+sub(vPar,R)*x+sub(wPar,R);
assert(sum(toList(0..8),ii->sub(eigenCf#ii,R)*x^ii)==8*diff(x,H)*newF-2*H*diff(x,newF));
assert(sum(toList(0..9),ii->sub(a4Cf#ii,R)*x^ii)==8*diff(x,H)*newF-3*H*diff(x,newF));
scan(toList(0..8),ii->save("F-source-coefficient-"|toString ii,cf#ii));
save("support-eigenvector-matrix",transpose matrix{cf,eigenCf});
save("A4-Hamiltonian-image",matrix{a4Cf});
save("source-conductor",newF);
print "PASS exact coordinate transform and inverse; quadratic and A4 cubic Hamiltonian identities";
print "COMPLETE corrected source-coordinate actual h2 incidence; no accepted verifier replay";
exit 0;
