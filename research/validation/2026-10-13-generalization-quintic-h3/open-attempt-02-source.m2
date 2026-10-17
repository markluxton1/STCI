-- NEW all-parameter support incidence on the proportional h=3 main chart.
-- Accepted h3 coefficient artifacts are premises; no inherited checks replayed.
R3=QQ[dl,ll,MonomialOrder=>GRevLex]; K3=frac R3; P3=K3[p3];
delta=dl; lambda=ll;
Hs=value get "research/validation/2026-10-13-evening-h3-proportional/main-H-coefficients.txt";
Ss=value get "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt";
h3pol=sum apply(toList(0..3),i->Hs#i*p3^i);
s3pol=sum apply(toList(0..5),i->Ss#i*p3^i);
print "PHASE actual homogeneous support condition on finite leading chart";
rr=h3pol^5 % s3pol;
rrn=apply(toList(0..4),i->lift(numerator coefficient(p3^i,rr),R3));
rrd=apply(toList(0..4),i->lift(denominator coefficient(p3^i,rr),R3));
print("NUMERATOR DEGREES="|toString apply(rrn,degree));
scan(toList(0..4),i->("research/validation/2026-10-13-generalization-quintic-h3/remainder-"|toString i|".txt" << toString rrn#i << close));
"research/validation/2026-10-13-generalization-quintic-h3/denominators.txt" << toString rrd << close;
print "PHASE primitive coefficient ideal";
cmn=first rrn;scan(drop(rrn,1),g->cmn=gcd(cmn,g));
print("COMMON FACTOR="|toString factor cmn);
rrn=apply(rrn,g->g//cmn);
h3ideal=ideal rrn;
print("SUPPORT GROEBNER="|toString gens gb h3ideal);
open3=dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*Ss#5;
print "PHASE saturation by explicitly regular main chart";
h3sat=saturate(h3ideal,ideal open3);
print("SATURATED SUPPORT IDEAL="|toString gens gb h3sat);
print("SATURATED DIMENSION="|toString dim h3sat);
print "DONE new h3 regular-chart support incidence";
