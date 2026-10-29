-- Exact identities for two completed empty slices of the marked O(2,2) source.
-- The full sixteen-parameter locus is NOT computed by this file.
-- Run: M2 --script research/computations/stci_projection_locus_2026_10_29.m2
R=QQ[z,r,A,p];
-- Segre coordinates scaled to avoid rational functions in the parameter z.
aa=z^2;
bb=r*(z^2+A)+z*(1-p);
cc=r*(z^2+A)-z*p;
sd=z^2*r^2;
del=bb-cc;
D=A*r^4;
L=p*bb+(1-p)*cc;
U={aa^2+A*del^2,aa*L,sd*L,sd^2+D*del^2};
H=z^2*(z^2+A);
F=(1-2*p)*r*z^3+(2*A*r^2-p*(1-p))*z^2+(1-2*p)*r*A*z+A^2*r^2;
assert(del==z);
assert(bb*cc-aa*sd==F);
assert(U==apply({1,r,r^3,r^4},t->H*t));
assert(sub(F,{z=>0})==A^2*r^2);
assert(sub(F,{p=>1/2})==(2*A*r^2-1/4)*z^2+A^2*r^2);
print "COMMON_MIDDLE_LINEAR_FORM_IDENTITIES_PASS";
-- Empty eight-parameter slice with U0=a^2, U1=ab.
S=QQ[a,b,c,d,e0,e1,e2,e3];
del=b-c;
U2=d*c+del*(e0*a+e1*b+e2*c+e3*d);
assert(sub(U2,{a=>0,b=>0})==c*((1-e3)*d-e2*c));
assert(sub(U2,{a=>0,c=>0})==b*(e1*b+e3*d));
print "TWO_FIXED_COORDINATE_ENDPOINT_IDENTITIES_PASS";
print "NO_FULL_SIXTEEN_PARAMETER_CLASSIFICATION_CLAIMED";
