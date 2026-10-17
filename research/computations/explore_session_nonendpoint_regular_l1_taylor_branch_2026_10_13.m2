-- Bounded rational branch substitution; the branch's necessity is owned by
-- the parent quotient-fiber proof, not inferred by this exact calculation.
coefRing=QQ[delta,a,B,q];
prefix="research/validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/nonendpoint_single_root_u";
uu=apply(0..7,n->value get(prefix|toString n|".txt"));
branchBase=QQ[na,nq]; branchField=frac branchBase;
ds=(nq^2-6*nq+6)*(nq-2)/(nq*(nq-1));
ks=ds+ds^2*(2*nq-3)/(3*(nq-1)*(nq-2));
bs=ks-na*nq;
branchMap=map(branchField,coefRing,{ds,na,bs,nq});
assert(branchMap(uu#0)==0);
print "PASS automatic first coefficient vanishes on specified branch";
scan({1,2,3,7},n->(
  cn=branchMap(uu#n);
  print("u"|toString n|" numerator="|toString factor numerator cn);
  print("u"|toString n|" denominator="|toString factor denominator cn);
  print("u"|toString n|" a-degree="|toString max apply(exponents numerator cn,ee->ee#0));
  ("/private/tmp/nonendpoint_regular_l1_u"|toString n|".txt") << toString cn << close;
));
print "PASS COMPLETE bounded rational coefficient extraction";
