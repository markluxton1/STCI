-- NEW bounded global finite-field prospect of the shared logarithmic ODE.
-- Exact accepted Q6 coefficients are read; no accepted construction replay.
-- A finite-field result is NOT a characteristic-zero certificate.
outDir="research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-07-low-degree-ode-name-repair";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
R=(ZZ/32003)[h2DLog,h2ULog,deltaPar,vPar,wPar];
save("stage","loading-inputs");
qDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient";
nDir="research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01";
q=apply(toList(0..6),i->value get(qDir|"/Q-coefficient-"|toString i|".txt"));
qi=i->if i<0 or i>6 then 0_R else q#i;
jNum=value get(nDir|"/Jbar-numerator.txt");
cofactorNum=value get(nDir|"/cofactor-determinant-numerator.txt");
delta1Num=value get(nDir|"/Delta1-numerator.txt");
normProduct=value get(nDir|"/primitive-norm.txt");
odeEquations=apply(toList(0..7),i->wPar*(i+1)*qi(i+1)+(vPar*i-h2ULog)*qi(i)+(i-1-h2DLog)*qi(i-1));
inputGenerators=join(odeEquations,{(h2DLog-5)*(h2DLog-6),jNum*(h2DLog-6),normProduct});
I=ideal inputGenerators;
U=deltaPar*(vPar^2-4*wPar)*(vPar^2+6*vPar*wPar+6*wPar^2+2*wPar)*cofactorNum*delta1Num;
save("input-degrees",apply(inputGenerators,f->first degree f));
save("stage","starting-single-actual-domain-saturation");
J=saturate(I,ideal U);
save("final-saturated-ideal",gens J);
save("stage","complete");
print("COMPLETE shared low-degree ODE modular prospect, unit="|toString(J==ideal(1_R))|", dimension="|toString dim(R/J));
exit 0;
