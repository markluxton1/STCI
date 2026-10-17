-- One bounded modular prospect of the complete shared coefficient ideal.
-- Finite-field output is not a characteristic-zero emptiness certificate.
outDir="research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-05-modular-global-prospect";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
R=(ZZ/32003)[deltaPar,vPar,wPar];
genDir="research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-04-flint-preparation";
qDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient";
nDir="research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01";
gens=apply(toList(0..11),i->value get(genDir|"/normalized-generator-"|toString i|".txt"));
normProduct=value get(nDir|"/primitive-norm.txt");
q5=value get(qDir|"/Q-coefficient-5.txt");q6=value get(qDir|"/Q-coefficient-6.txt");
cofactorNum=value get(nDir|"/cofactor-determinant-numerator.txt");
U=deltaPar*(vPar^2-4*wPar)*(vPar^2+6*vPar*wPar+6*wPar^2+2*wPar)*cofactorNum;
I=ideal append(gens,normProduct);
save("stage","starting-actual-domain-saturation");
J=saturate(I,ideal U);
save("after-domain-saturation",gens J);
save("stage","starting-qhigh-ideal-saturation");
J=saturate(J,ideal(q5,q6));
save("final-saturated-ideal",gens J);
save("stage","complete");
print("COMPLETE unified modular global prospect, unit="|toString(J==ideal(1_R))|", dimension="|toString dim(R/J));
exit 0;
