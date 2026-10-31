-- New line geometry for the mixed-weight seed; no inherited jet test replayed.
R=QQ[h,t,w,q];
cc0=t^3-w;
cc2=w^3-t*(t*w+q)^2;
ff=h*q^3+cc2^2-cc0^2;
assert(sub(ff,{q=>0})==(w-t^3)^2*(w^4-1));
print "QUADRIC_RESTRICTION_FACTORIZATION_PASS";
T0=QQ[symbol lh,symbol lt,symbol lz,symbol lq];
T=T0/ideal(lz^4-1);
mapLine=map(T,R,{lh,lt,lz,lq});
assert(sub(mapLine ff,{lq=>0})==0);
assert(sub(mapLine cc2,{lq=>0})==-lz^2*mapLine cc0);
print "FOUR_LINE_AND_ATTACHMENT_IDENTITIES_PASS";
N=QQ[symbol kh,symbol nt,symbol nu,symbol nq];
normalMap=map(N,R,{kh,nt,nt^3+nu,nq});
nf=normalMap ff;
F2=4*nt^10*nq^2-4*nt^11*nq*nu+(nt^12-1)*nu^2;
assert(nf-F2==0 or all(terms(nf-F2),term->(
 exponent=first exponents term;
 exponent#2+exponent#3>=3)));
assert((-4*nt^11)^2-4*(4*nt^10)*(nt^12-1)==16*nt^10);
print "SPLIT_NODE_INITIAL_FORM_AND_DISCRIMINANT_PASS";
assert(sub(diff(w,sub(ff,{q=>0})),{w=>1})==4*(1-t^3)^2);
print "GENERIC_LINE_SMOOTHNESS_CONTROL_PASS";
print "MIXED_WEIGHT_FOUR_LINES_EXACT_IDENTITIES_PASS";
