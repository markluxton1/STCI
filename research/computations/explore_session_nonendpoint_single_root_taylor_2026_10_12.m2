-- Bounded exploration of highest Taylor coefficients, with delta retained.
singleRing=QQ[delta,a,B,G,J,p,q,tt];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
Gs=-(6*B+delta^2-3*delta)*q-(3*a-3*B+2*delta)*q^2+2*a*q^3;
Js=(-Gs*(1+3*q)-(6*B+5*delta^2-3*delta)*q-(3*a+3*B+delta-delta^2)*q^2+(a+B)*q^3)/2;
Fshift=sub(F,{G=>Gs,J=>Js,p=>q+tt});
assert(sub(Fshift,{tt=>0})==0);
print "PASS automatic common-root factor";
scan(reverse toList(1..8),n->(
  cn=(sum select(terms Fshift,mm->((exponents mm)#0)#7==n))//tt^n;
  print("Taylor coefficient "|toString n|" terms="|toString(#terms cn));
  print(factor cn);
  ("/private/tmp/nonendpoint_single_root_taylor_coefficient_"|toString n|".txt") << toString cn << close;
));
"/private/tmp/nonendpoint_single_root_taylor_shifted.txt" << toString Fshift << close;
"/private/tmp/nonendpoint_single_root_taylor_GJ.txt" << toString Gs << endl << toString Js << close;
print "PASS COMPLETE bounded coefficient extraction";
