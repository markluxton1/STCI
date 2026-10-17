-- NEW one bounded shared spectral/ODE prospect, no root or factor cases.
-- Finite-field output is NOT a characteristic-zero emptiness certificate.
outDir="research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-08-spectral-ode-prospect";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
R=(ZZ/32003)[h2DLog,h2EtaLog,deltaPar,vPar,wPar];
save("stage","loading-accepted-coefficients");
qDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient";
nDir="research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01";
q=apply(toList(0..6),i->value get(qDir|"/Q-coefficient-"|toString i|".txt"));
qi=i->if i<0 or i>6 then 0_R else q#i;
jNum=value get(nDir|"/Jbar-numerator.txt");
cofactorNum=value get(nDir|"/cofactor-determinant-numerator.txt");
delta1Num=value get(nDir|"/Delta1-numerator.txt");
normProduct=value get(nDir|"/primitive-norm.txt");
disc=vPar^2-4*wPar;
coverK=vPar^2+6*vPar*wPar+6*wPar^2+2*wPar;
-- eta=d*v-2*u is an invertible affine change in the two witness variables.
odeEquations=apply(toList(0..7),i->2*wPar*(i+1)*qi(i+1)+((2*i-h2DLog)*vPar+h2EtaLog)*qi(i)+2*(i-1-h2DLog)*qi(i-1));
degreePolynomial=(h2DLog-5)*(h2DLog-6);
charSix=h2EtaLog*(h2EtaLog^2-4*disc)*(h2EtaLog^2-16*disc)*(h2EtaLog^2-36*disc);
charFive=(h2EtaLog^2-disc)*(h2EtaLog^2-9*disc)*(h2EtaLog^2-25*disc);
spectralPolynomial=(h2DLog-5)*charSix+(6-h2DLog)*charFive;
inputGenerators=join(odeEquations,{degreePolynomial,jNum*(h2DLog-6),spectralPolynomial,normProduct});
I=ideal inputGenerators;
U=deltaPar*disc*coverK*cofactorNum*delta1Num;
save("input-degrees",apply(inputGenerators,f->first degree f));
save("spectral-polynomial",spectralPolynomial);
save("stage","starting-single-actual-domain-saturation");
J=saturate(I,ideal U);
save("final-saturated-ideal",gens J);
save("stage","complete");
print("COMPLETE unified spectral ODE modular prospect, unit="|toString(J==ideal(1_R))|", dimension="|toString dim(R/J));
exit 0;
