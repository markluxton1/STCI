-- Exact identities for the finite/infinite common-quadratic cover.
CoverAuditRing=QQ[cvV,cvW,cvDel,cvT,cvRho,cvA,cvB];
coverAuditChecks=0;
coverAuditCheck=(label,condition)->(
  if not condition then error("FAIL "|label);
  coverAuditChecks=coverAuditChecks+1;
  print("PASS "|label);
);
coverM=matrix{{cvW,cvV+3*cvW,0,-3*cvW},{cvV,1-3*cvW,0,6*cvW},{0,0,cvW,cvV+3*cvW},{-3,-3*cvW,cvV,1+6*cvW}};
coverRhs=matrix{{2*cvDel},{cvDel^2-3*cvDel},{cvDel-cvDel^2},{5*cvDel^2-3*cvDel}};
coverK=cvV^2+2*cvW+6*cvV*cvW+6*cvW^2;
coverAuditCheck("finite H determinant",det coverM==(cvV^2-4*cvW)*coverK);
coverDen=cvT^2+6*cvT+6;
coverExceptionalScaled=matrix{{-2,-2*cvT-6,0,6},{-2*cvT,coverDen+6,0,-12},{0,0,-2,-2*cvT-6},{-3*coverDen,6,-2*cvT,coverDen-12}};
coverExceptionalAug=coverExceptionalScaled_{0,2,3}|(coverDen*coverRhs);
coverAuditCheck("exceptional K augmented minor",det coverExceptionalAug==-24*cvDel*(cvT+2)*coverDen^2);
coverRepeated=sub(coverM,{cvV=>-2*cvRho,cvW=>cvRho^2});
coverLeft=matrix{{-(2*cvRho+1),-cvRho*(cvRho+2),2*cvRho,cvRho^2}};
coverAuditCheck("repeated H left kernel",coverLeft*coverRepeated==0);
coverAuditCheck("repeated H compatibility",(coverLeft*coverRhs)_(0,0)==2*cvDel*(2*cvDel*cvRho*(cvRho-1)+2*cvRho-1));
coverRepeatedMinor=submatrix(coverRepeated,{0,1,2},{0,1,2});
coverAuditCheck("repeated H rank-three minor",det coverRepeatedMinor==-3*cvRho^4*(cvRho-1)^2);
coverInfinityM=matrix{{-6*cvRho^2+6*cvRho-2,6*cvRho^2-3*cvRho},{-6*cvRho^2,6*cvRho^2+3*cvRho-1}};
coverInfinityRhs=matrix{{-cvDel*((cvDel-3)*cvRho^2+2*cvRho)},{-cvDel*((5*cvDel-3)*cvRho^2+(1-cvDel)*cvRho)}};
coverAuditCheck("infinity plus finite root determinant",det coverInfinityM==2*(6*cvRho^2-6*cvRho+1));
coverInfinitySolution=matrix{{cvDel*cvRho*(2*cvDel*cvRho+1)},{cvDel*cvRho*(2*cvDel*cvRho-cvDel+1)}};
coverAuditCheck("universal infinity particular solution",coverInfinityM*coverInfinitySolution==coverInfinityRhs);
print("PASS ALL "|toString coverAuditChecks|" exact identities");
