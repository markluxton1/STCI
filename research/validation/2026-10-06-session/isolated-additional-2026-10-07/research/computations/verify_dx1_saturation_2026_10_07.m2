-- Generated from the persisted five obstruction polynomials.
-- Source SHA256: 913614d9c40933a86053f574326a46bd7e4d19cacde90207eca419c6dec500a1
R=QQ[a,b,x,MonomialOrder=>GRevLex];
Q1=-32*a^5 - 144*a^4*b^2*x - 1120*a^4*b*x - 2304*a^4*x + 16*a^4 - 384*a^3*b^2*x - 2304*a^3*b*x - 3072*a^3*x + 80*a^3 - 48*a^2*b^3*x^2 - 448*a^2*b^2*x^2 - 472*a^2*b^2*x - 960*a^2*b*x^2 - 2096*a^2*b*x - 1600*a^2*x + 88*a^2 - 64*a*b^3*x^2 - 512*a*b^2*x^2 - 288*a*b^2*x - 640*a*b*x^2 - 864*a*b*x + 768*a*x^2 - 192*a*x + 46*a - 4*b^4*x^3 - 64*b^3*x^3 - 36*b^3*x^2 - 352*b^2*x^3 - 304*b^2*x^2 - 81*b^2*x - 768*b*x^3 - 528*b*x^2 - 190*b*x - 576*x^3 + 9;
Q2=-16*a^4*b - 128*a^4 + 160*a^3*b^2*x + 1280*a^3*b*x + 64*a^3*b + 2304*a^3*x + 80*a^3 + 328*a^2*b^2*x + 2288*a^2*b*x + 176*a^2*b + 3168*a^2*x + 304*a^2 + 40*a*b^3*x^2 + 512*a*b^2*x^2 + 308*a*b^2*x + 2016*a*b*x^2 + 2032*a*b*x + 160*a*b + 2304*a*x^2 + 2448*a*x + 260*a + 20*b^3*x^2 + 256*b^2*x^2 + 92*b^2*x + 1008*b*x^2 + 604*b*x + 45*b + 1152*x^2 + 720*x + 72;
Q3=-16*a^4 - 32*a^3*b*x - 192*a^3*x - 48*a^3 - 96*a^2*b^2*x^2 + 24*a^2*b^2*x - 960*a^2*b*x^2 - 48*a^2*b*x - 2304*a^2*x^2 - 672*a^2*x - 72*a^2 + 8*a*b^3*x^2 + 48*a*b^2*x^2 + 60*a*b^2*x - 480*a*b*x^2 + 120*a*b*x - 1856*a*x^2 - 384*a*x - 44*a + 4*b^4*x^3 + 48*b^3*x^3 + 12*b^3*x^2 + 288*b^2*x^3 + 168*b^2*x^2 + 36*b^2*x + 704*b*x^3 + 384*b*x^2 + 116*b*x + 576*x^3 - 9;
Q4=-40*a^3*b - 80*a^3 - 40*a^2*b^3*x - 328*a^2*b^2*x - 1232*a^2*b*x - 128*a^2*b - 1472*a^2*x - 256*a^2 + 4*a*b^4*x^2 - 64*a*b^3*x^2 - 80*a*b^3*x - 704*a*b^2*x^2 - 572*a*b^2*x - 2560*a*b*x^2 - 2032*a*b*x - 126*a*b - 2880*a*x^2 - 2416*a*x - 252*a + 8*b^4*x^2 - 20*b^3*x^2 - 36*b^3*x - 304*b^2*x^2 - 198*b^2*x - 1040*b*x^2 - 612*b*x - 36*b - 1152*x^2 - 720*x - 72;
Q5=16*a^4 + 48*a^3*b^2*x + 256*a^3*b*x + 576*a^3*x + 64*a^3 + 36*a^2*b^4*x^2 + 384*a^2*b^3*x^2 + 1888*a^2*b^2*x^2 + 112*a^2*b^2*x + 4608*a^2*b*x^2 + 512*a^2*b*x + 5184*a^2*x^2 + 1216*a^2*x + 88*a^2 + 70*a*b^4*x^2 + 576*a*b^3*x^2 + 2096*a*b^2*x^2 + 60*a*b^2*x + 3456*a*b*x^2 + 160*a*b*x + 3040*a*x^2 + 528*a*x + 48*a + 2*b^5*x^3 - 4*b^4*x^3 + 36*b^4*x^2 - 80*b^3*x^3 + 192*b^3*x^2 - 352*b^2*x^3 + 400*b^2*x^2 - 736*b*x^3 + 192*b*x^2 - 48*b*x - 576*x^3 + 9;
u=b*x-a; t=x*u; alpha=2*a+1; beta=b+2;
L=ideal(Q1,Q2,Q3,Q4,Q5);
J=ideal(x*beta^2+alpha*beta-2*alpha^2,(4*x+2)*alpha*beta-3*alpha^2,beta^3,alpha*beta^2,alpha^2*beta,alpha^3);
assert((gens L) % J == 0);
assert((t*gens J) % L == 0);
assert((J:ideal(t))==J);
assert((L:ideal(t))==J);
assert(saturate(L,ideal(t))==J);
assert(alpha^3 % J == 0_R and beta^3 % J == 0_R);
assert((gens J) % ideal(alpha,beta)==0);
assert(saturate(L,ideal(t*alpha*beta))==ideal(1_R));
print "PASS: t J subset L subset J; J:t=J; L:t=J; L:t^infinity=J.";
print "PASS: radical J=(2a+1,b+2), full residual open set empty.";
Ra=QQ[b,x,MonomialOrder=>GRevLex];
phi=map(Ra,R,{-1/2,b,x});
assert(saturate(phi L,ideal(x*(b*x+1/2)))==ideal((b+2)^2));
Rb=QQ[a,x,MonomialOrder=>GRevLex];
psi=map(Rb,R,{a,-2,x});
assert(saturate(psi L,ideal(x*(-2*x-a)))==ideal((2*a+1)^2));
print "PASS: a=-1/2 and b=-2 boundary saturated ideals are the claimed squares.";
