-- NEW exact h2 conductor quotient and shared reduced Hamiltonian incidence.
-- Inputs are corrected-coordinate coefficients captured by attempt05.
-- No inherited verification or accepted rational coefficient map is rerun.
par=QQ[deltaPar,vPar,wPar];
inDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-05-correct-coordinate";
outDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
cf=apply(toList(0..8),ii->value get(inDir|"/F-source-coefficient-"|toString ii|".txt"));
R=par[x];
F=sum(toList(0..8),ii->sub(cf#ii,R)*x^ii);
H=x^2+sub(vPar,R)*x+sub(wPar,R);
Q=F//H;
assert(F==H*Q);
qf=apply(toList(0..6),ii->lift(coefficient(x^ii,Q),par));
qi=ii->if ii<0 or ii>6 then 0_par else qf#ii;
quadraticImage=apply(toList(0..6),jj->(6-2*jj)*vPar*qi(jj)+(14-2*jj)*qi(jj-1)-2*(jj+1)*wPar*qi(jj+1));
a4Image=apply(toList(0..7),jj->(6-3*jj)*vPar*qi(jj)+(15-3*jj)*qi(jj-1)-3*(jj+1)*wPar*qi(jj+1));
assert(sum(toList(0..6),ii->sub(quadraticImage#ii,R)*x^ii)==6*diff(x,H)*Q-2*H*diff(x,Q));
assert(sum(toList(0..7),ii->sub(a4Image#ii,R)*x^ii)==6*diff(x,H)*Q-3*H*diff(x,Q));
-- Factorization of the homogeneous Hamiltonian action. On this affine
-- chart the source-infinity linear form has dehomogenization 1.
assert(8*diff(x,H)*F-2*H*diff(x,F)==H*(6*diff(x,H)*Q-2*H*diff(x,Q)));
assert(8*diff(x,H)*F-3*H*diff(x,F)==H*((6*diff(x,H)*Q-3*H*diff(x,Q))-diff(x,H)*Q));
scan(toList(0..6),ii->save("Q-coefficient-"|toString ii,qf#ii));
save("Q-sextic",Q);
save("quadratic-Hamiltonian-matrix",transpose matrix{qf,quadraticImage});
save("A4-Hamiltonian-image",matrix{a4Image});
print "PASS literal F=H*Q6; both reduced Hamiltonian coefficient identities; both product-action identities";
print "COMPLETE sextic support incidence capture on accepted finite inverse-map open";
exit 0;
