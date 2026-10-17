-- Root's bounded support for the proposed Jbar=0 conductor theorem.
-- Polynomial identities only; the written proofs establish length, finiteness,
-- conductor-prime accounting, full unit-jet descent and all-mate scope.
jzCheck=(label,condition)->(assert(condition);print("PASS "|label));
jzRing=QQ[jzDelta,jzLiftB,jzLiftG,jzLiftA,jzAlp,jzBet,jzChi,jzW,jzR,jzT,jzX,jzU,jzC0,jzC1,jzC2,jzC3,jzC4,jzC5];
jzH=jzBet+jzChi;
jzDZ=jzAlp*jzBet-jzChi^2;
jzEZ=jzBet^2-jzAlp*jzBet*jzChi+jzChi^3;
jzX0=1-jzAlp+jzLiftA*jzH;
jzX1=1-jzAlp+jzDelta*jzAlp+(jzLiftA+jzLiftB)*jzH;
jzX2=1-jzAlp+3*jzDelta*jzAlp+3*jzDelta^2*jzChi-jzDelta^3*jzDZ+(jzLiftA+3*jzLiftB+jzLiftG)*jzH;
jzX3=1-jzAlp+4*jzDelta*jzAlp+6*jzDelta^2*jzChi-4*jzDelta^3*jzDZ+jzDelta^4*jzEZ+(jzLiftA+4*jzLiftB+2*jzLiftG)*jzH;
jzCheck("first-actual-target-generator",jzX1-jzX0==jzDelta*jzAlp+jzLiftB*jzH);
jzCheck("second-actual-target-generator",jzX2-3*jzX1+2*jzX0==jzLiftG*jzH+3*jzDelta^2*jzChi-jzDelta^3*jzDZ);
jzCheck("third-actual-target-generator",jzX3-2*jzX2+2*jzX1-jzX0==jzDelta^4*jzEZ-2*jzDelta^3*jzDZ);
jzCheck("linear-elimination-determinant",det matrix{{jzDelta,0},{0,3*jzDelta^2}}==3*jzDelta^3);
-- Substitute the linear solution with the denominator 3delta^2 cleared.
-- The remaining source equation's degree-two coefficient is G(G+3delta^2).
jzSurface=jzBet*(jzAlp^2-jzChi)-jzAlp*jzChi^2;
jzSubSurface=sub(jzSurface,{jzAlp=>-3*jzLiftB*jzDelta*jzW,jzBet=>(3*jzDelta^2+jzLiftG)*jzW,jzChi=>-jzLiftG*jzW});
jzCheck("actual-source-quadratic-coefficient",jzSubSurface%ideal(jzW^3)==jzLiftG*(jzLiftG+3*jzDelta^2)*jzW^2);
jzV=(jzT-jzR^2)^2-jzR^3;
jzLow=jzC0*jzV+jzC1*jzR*(jzT-jzR^2)+jzC2*jzR^2+jzC3*(jzT-jzR^2)+jzC4*jzR+jzC5;
jzCheck("complete-low-pole-restriction",sub(jzLow,{jzT=>0})==jzC0*jzR^4-(jzC0+jzC1)*jzR^3+(jzC2-jzC3)*jzR^2+jzC4*jzR+jzC5);
jzBoundaryB=1+jzX*jzU;
jzBoundaryH=jzX*jzBoundaryB*(1+jzX+jzX^2*jzU);
jzBoundaryNumer=3*jzDelta^2*jzX*jzBoundaryB-jzDelta^3*jzX^3*jzBoundaryB^2+jzLiftG*jzBoundaryH;
jzBoundaryX0=jzU-jzBoundaryB+jzLiftA*jzBoundaryH;
jzCheck("generic-line-transverse-uniformizer",sub(diff(jzX,jzBoundaryNumer),{jzX=>0})==jzLiftG+3*jzDelta^2 and sub(jzBoundaryX0,{jzX=>0})==jzU-1);
jzRam2=jzLiftG+3*jzDelta^2;
jzRam3=2*jzLiftG+6*jzDelta^2;
jzCheck("retained-ramified-line-specialization",jzRam3==2*jzRam2);
print "PASS all eight bounded conductor-local identity groups";
