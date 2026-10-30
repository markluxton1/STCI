R=QQ[symbol ah,symbol at,symbol au,symbol aq,symbol ae];
X=at^3+au; Y=at*X+aq;
C0=-au; C2=X^3-at*Y^2;
F=ah*aq^3+C2^2-C0^2;
assert(sub(F,{aq=>0})==au^2*((at^3+au)^4-1));
Fquad=sum select(terms F,term->(
 ev=first exponents term; ev#2+ev#3==2));

assert(Fquad==((at^6-1)*au-2*at^5*aq)*((at^6+1)*au-2*at^5*aq));
assert((-4*at^11)^2-4*(4*at^10)*(at^12-1)==16*at^10);
print "AUDIT_QUADRIC_FACTOR_AND_SPLIT_NODE_PASS";
T=QQ[symbol bh,symbol bt,symbol bz,symbol bq];
J=ideal(bz^4-1);
D0=bt^3-bz; D2=bz^3-bt*(bt*bz+bq)^2;
assert(sub(D2+bz^2*D0,{bq=>0})%J==0);
assert(sub(bh*bq^3+D2^2-D0^2,{bq=>0})%J==0);
assert(ideal(bt^3-bz,3*bt^2,bz^4-1)==ideal(1_T));
print "AUDIT_ALL_FOUR_LINES_AND_SIMPLE_ATTACHMENTS_PASS";
print "AUDIT_LINE_IDENTITIES_PASS";
