-- Independent exact identities for the Jbar-zero phase audit.
-- These checks support the actual geometry; they do not prove the
-- finite-module, field-period, purity or global STCI arguments by sampling.
PhaseAuditRing=QQ[phDel,phA,phB,phG,phAlpha,phBeta,phChi,phH,phX,phU,phR,phT,phC0,phC1,phC2,phC3,phC4,phC5];
phaseAuditChecks=0;
phaseCheck=(label,condition)->(
  if not condition then error("FAIL "|label);
  phaseAuditChecks=phaseAuditChecks+1;
  print("PASS "|label);
);
phaseD=2*phG-2*phB+phA;
phaseE=phG-3*phB+2*phA;
phaseH=phBeta+phChi;
phaseDZ=phAlpha*phBeta-phChi^2;
phaseEZ=phBeta^2-phAlpha*phBeta*phChi+phChi^3;
phaseX0=1-phAlpha+phA*phaseH;
phaseX1=1+(phDel-1)*phAlpha+phB*phaseH;
phaseX2=1+(3*phDel-1)*phAlpha+3*phDel^2*phChi-phDel^3*phaseDZ+phG*phaseH;
phaseX3=1+(4*phDel-1)*phAlpha+6*phDel^2*phChi-4*phDel^3*phaseDZ+phDel^4*phaseEZ+phaseD*phaseH;
phaseCheck("actual first target generator",phaseX1-phaseX0==phDel*phAlpha+(phB-phA)*phaseH);
phaseCheck("actual second target generator",phaseX2-3*phaseX1+2*phaseX0==phaseE*phaseH+3*phDel^2*phChi-phDel^3*phaseDZ);
phaseCheck("actual third target generator",phaseX3-2*phaseX2+2*phaseX1-phaseX0==phDel^4*phaseEZ-2*phDel^3*phaseDZ);
phaseScaledAlpha=-3*phDel*(phB-phA)*phH;
phaseScaledChi=-phaseE*phH;
phaseScaledBeta=(3*phDel^2+phaseE)*phH;
phaseCheck("cleared linear elimination",phDel*phaseScaledAlpha+(phB-phA)*(phaseScaledBeta+phaseScaledChi)==0 and phaseE*(phaseScaledBeta+phaseScaledChi)+3*phDel^2*phaseScaledChi==0);
phaseCheck("cleared fiber quadratic coefficient",-phaseScaledBeta*phaseScaledChi==phaseE*(phaseE+3*phDel^2)*phH^2);
phaseCheck("third generator has no linear term",sub(phDel^4*phaseEZ-2*phDel^3*phaseDZ,{phAlpha=>phT*phAlpha,phBeta=>phT*phBeta,phChi=>phT*phChi})%phT^2==0);
phaseChartA=1+phX*phU;
phaseChartU4=phU-phaseChartA;
phaseChartU3=-phaseChartA;
phaseChartU2=phX*phaseChartA;
phaseChartU1=phX^3*phaseChartA^2;
phaseChartU0=phX^5*phaseChartA^3;
phaseChartH=phX*phaseChartA+phX^2*phaseChartA^2;
phaseChartX0=phaseChartU4+phA*phaseChartH;
phaseChartX1=phaseChartU4-phDel*phaseChartU3+phB*phaseChartH;
phaseChartX2=phaseChartU4-3*phDel*phaseChartU3+3*phDel^2*phaseChartU2-phDel^3*phaseChartU1+phG*phaseChartH;
phaseChartX3=phaseChartU4-4*phDel*phaseChartU3+6*phDel^2*phaseChartU2-4*phDel^3*phaseChartU1+phDel^4*phaseChartU0+phaseD*phaseChartH;
phaseCheck("actual ell restriction",apply({phaseChartX0,phaseChartX1,phaseChartX2,phaseChartX3},item->sub(item,{phX=>0}))=={phU-1,phU-1+phDel,phU-1+3*phDel,phU-1+4*phDel});
phaseEllNumerator=3*phDel^2*phaseChartU2-phDel^3*phaseChartU1+phaseE*phaseChartH;
phaseCheck("actual image-line equation",phaseChartX2-3*phaseChartX1+2*phaseChartX0==phaseEllNumerator);
phaseCheck("generic ell valuation one numerator",(phaseEllNumerator-phX*(phaseE+3*phDel^2))%phX^2==0 and sub(phaseChartX0,{phX=>0})==phU-1);
phaseCheck("ramified-line exception on Jbar zero",phaseD+6*phDel^2+3*phA-4*phB==2*(phaseE+3*phDel^2));
phaseLow=phC0*(phT^2-phR^3)+phC1*phR*phT+phC2*phR^2+phC3*phT+phC4*phR+phC5;
phaseCheck("complete low-pole restriction polynomial",sub(phaseLow,{phT=>-phR^2})==phC0*phR^4+(-phC0-phC1)*phR^3+(phC2-phC3)*phR^2+phC4*phR+phC5);
phaseCheck("conormal leading coefficients coincide",2*phaseD-3*phG+phB==phaseE);
print("PASS ALL "|toString phaseAuditChecks|" exact identities");
