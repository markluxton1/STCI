load "research/computations/stci_projection_elliptic_target_2026_10_30.m2";
rdisc=sub(resultant(quartic,diff(tt,quartic),tt),R);
svars={ss0,ss1,ss2,ss3};
for kk from 0 to 3 do (
 local sq; local residual; local eq; local targetDegree; local jj;
 sq=xx^kk+sum(toList(0..kk-1),i->svars#i*xx^i);
 targetDegree=4+2*kk;
 residual=sum(toList(0..targetDegree),i->coefficient(xx^i,disc)*xx^i);
 eq=apply(toList(targetDegree+1..12),i->sub(coefficient(xx^i,disc),R));
 if kk>0 then (
  for jj in reverse toList(2*kk..targetDegree) do (
   residual=residual-coefficient(xx^jj,residual)*xx^(jj-2*kk)*sq^2;
  );
  eq=join(eq,apply(toList(0..2*kk-1),i->sub(coefficient(xx^i,residual),R)));
 );
 stdio << "SQUARE_FACTOR_AFFINE_DEGREE=" << kk << endl; flush stdio;
 J=saturate(ideal eq,ideal rdisc);
 stdio << "SATURATED_IS_UNIT=" << (J==ideal 1_R) << endl;
 stdio << "SATURATED_DIMENSION=" << dim(R/J) << endl;
 stdio << "SATURATED_GROEBNER=" << gens gb J << endl; flush stdio;
);
print "LOWER_SQUARE_FACTOR_CHARTS_COMPLETED";
