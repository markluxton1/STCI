-- NEW all-root-multiplicity cover for an affine quintic with <=2 roots.
h3multR=QQ[xx,dl,ll,MonomialOrder=>GRevLex]; delta=dl;lambda=ll;
h3multC=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3multS=sum apply(toList(0..5),i->h3multC#i*xx^i);
h3multD1=diff(xx,h3multS); h3multD2=diff(xx,h3multD1); h3multD3=diff(xx,h3multD2);
h3multU=dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*h3multC#5;
h3multI4=ideal(h3multS,h3multD1,h3multD2,h3multD3);
"research/validation/2026-10-13-generalization-quintic-h3/multiplicity4-input.txt" << toString gens h3multI4 << close;
h3multI4sat=saturate(h3multI4,ideal h3multU);
print("multiplicity4 saturated ideal="|toString gens gb h3multI4sat);
"research/validation/2026-10-13-generalization-quintic-h3/multiplicity4-ideal.txt" << toString gens gb h3multI4sat << close;
h3multDisc=h3multC#4^2-4*h3multC#3*h3multC#5-6*xx*h3multC#4*h3multC#5-15*xx^2*h3multC#5^2;
h3multI32=ideal(h3multS,h3multD1,h3multD2,h3multDisc);
"research/validation/2026-10-13-generalization-quintic-h3/multiplicity32-input.txt" << toString gens h3multI32 << close;
h3multI32sat=saturate(h3multI32,ideal h3multU);
print("multiplicity3+2 saturated ideal="|toString gens gb h3multI32sat);
"research/validation/2026-10-13-generalization-quintic-h3/multiplicity32-ideal.txt" << toString gens gb h3multI32sat << close;
print "DONE complete at-most-two-affine-root multiplicity cover";
