-- All-length symbolic reconstruction of the two endpoint A-chain equations.
-- Inequalities and local geometric attachment are proved in the audit note;
-- this checks rational identities without a finite graph-length cutoff.
auditCount = 0;
auditCondition = (label, condition) -> (
    if condition =!= true then error("FAIL: " | label);
    auditCount = auditCount+1;
    print("PASS: " | label);
    );
R = QQ[nLen,mLen,contactNode,idx,bCoeff];
K = frac R;
nLen = sub(nLen,K); mLen = sub(mLen,K);
contactNode = sub(contactNode,K); idx = sub(idx,K); bCoeff = sub(bCoeff,K);
chainLeft = v -> bCoeff*(nLen+1-v)/(nLen+1)+v*(nLen+1-contactNode)/(nLen+1);
chainRight = v -> bCoeff*(nLen+1-v)/(nLen+1)+contactNode*(nLen+1-v)/(nLen+1);
auditCondition("contact chain boundary at B", chainLeft(0) == bCoeff);
auditCondition("contact chain opposite boundary", chainRight(nLen+1) == 0);
auditCondition("two formulas agree at contact node", chainLeft(contactNode) == chainRight(contactNode));
auditCondition("left-side harmonic recurrence", 2*chainLeft(idx)-chainLeft(idx-1)-chainLeft(idx+1) == 0);
auditCondition("right-side harmonic recurrence", 2*chainRight(idx)-chainRight(idx-1)-chainRight(idx+1) == 0);
auditCondition("unit source at arbitrary contact node",
    2*chainLeft(contactNode)-chainLeft(contactNode-1)-chainRight(contactNode+1) == 1);
source = (nLen+1-contactNode)/(nLen+1);
auditCondition("endpoint coefficient with arbitrary contact node",
    chainLeft(1) == nLen*bCoeff/(nLen+1)+source);
chainOther = v -> bCoeff*(mLen+1-v)/(mLen+1);
auditCondition("other chain has no source", 2*chainOther(idx)-chainOther(idx-1)-chainOther(idx+1) == 0);
auditCondition("other endpoint coefficient, including m=0",
    chainOther(1) == mLen*bCoeff/(mLen+1));
denominator = 3-nLen/(nLen+1)-mLen/(mLen+1);
auditCondition("positive denominator identity",
    denominator == 1+1/(nLen+1)+1/(mLen+1));
coefficientB = source/denominator;
auditCondition("exact B intersection equation",
    -3*coefficientB+nLen*coefficientB/(nLen+1)+source+mLen*coefficientB/(mLen+1) == 0);
auditCondition("strict gap from coefficient one",
    1-coefficientB == ((contactNode+1)/(nLen+1)+1/(mLen+1))/denominator);
ff = openOut "research/validation/2026-10-10-genus-two-nonendpoint-trisecant-independent-audit/result.json";
ff << "{\n  \"status\": \"PASS\",\n  \"engine\": \"Macaulay2 1.26.06\",\n  \"checked_conditions\": " << auditCount << ",\n  \"scope\": \"Symbolic all-length two-endpoint A-chain equations; n>=1, m>=0, 1<=k<=n inequalities and geometric hypotheses proved separately\",\n  \"coefficient_B\": \"((n+1-k)/(n+1))/(3-n/(n+1)-m/(m+1))\",\n  \"one_minus_coefficient_B\": \"((k+1)/(n+1)+1/(m+1))/(1+1/(n+1)+1/(m+1))\",\n  \"does_not_claim\": \"A finite graph enumeration, endpoint-trisecant coverage, lambda-zero exclusion, or the universal STCI theorem\"\n}\n";
close ff;
print("PASS: " | toString auditCount | " all-length rational identities");
