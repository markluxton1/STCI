-- Exact algebra companion to the local endpoint ADE/contact proof.
-- The proof, including formal resolution charts, is in the linked note.
checks = 0;
verifyIdentity = (condition, label) -> (
    if not condition then error("FAIL: " | label);
    checks = checks + 1;
    print("PASS " | label);
    );

R0 = QQ[u,v,beta,gamma,d,e,A,a,b,y,q];
F = (a*b*(u*(b-a)-v*a*b)
    +y*((b-a)*(A+beta*b+gamma*b^2)+v*a-a*b^2*(d+e*b))
    +y^2*(d+e*b));
verifyIdentity(sub(F,{a=>b,y=>b^3})==0,"actual lifted curve lies on full equation");
P = -u*b-v*b^2;
Q = v-beta*b-(gamma+d)*b^2-e*b^3;
endpointR = beta*b^2+gamma*b^3;
endpointS = d+e*b;
F0 = sub(F,{A=>0});
verifyIdentity(F0 == P*a^2+Q*a*y+endpointS*y^2+u*b^2*a+endpointR*y,
      "exact binary quadratic over the b line");
verifyIdentity(sub(Q^2-4*P*endpointS,{b=>0})==v^2,"formal discriminant is a unit for v nonzero");

-- Clear denominators of alpha=(Q+q)/2 and t=2P/(Q+q).
aa = Q+q;
reln = q^2-Q^2+4*P*endpointS;
Xnum = aa*a+2*endpointS*y;  -- 2X
Ynum = aa*y+2*P*a;   -- aa*Y
verifyIdentity((Xnum*Ynum-2*aa*(P*a^2+Q*a*y+endpointS*y^2)) % ideal(reln)==0,
      "formal quadratic factorization after clearing denominators");
ellXnum = u*b^2*aa-2*endpointR*P; -- aa*q*ell_X
ellYnum = endpointR*aa-2*u*b^2*endpointS; -- 2*q*ell_Y
verifyIdentity((2*aa*q*(u*b^2*a+endpointR*y)
      -ellXnum*Xnum-ellYnum*Ynum) % ideal(reln)==0,
      "exact linear-term coefficients in the factor coordinates");
verifyIdentity(sub(ellXnum,{b=>0})==0,"ell_X numerator vanishes at b zero");
verifyIdentity(ellXnum % ideal(b^2)==0,"ell_X numerator divisible by b squared");
verifyIdentity(sub(ellXnum//b^2,{b=>0,q=>v})==2*u*v,
      "ell_X exact b-order two and leading coefficient u over v");
verifyIdentity(ellYnum % ideal(b^2)==0,"ell_Y numerator divisible by b squared");

-- Full first blowup, with a=b*z and y=b*w.
R1 = QQ[u,beta,gamma,d,e,b,z,w];
mapToBlowup = map(R1,R0,{u,0_R1,beta,gamma,d,e,0_R1,b*z,b,b*w,0_R1});
blowupF = mapToBlowup(F)//b^2;
expectedBlowup = ((d+e*b)*w^2+u*b*z*(1-z)
    +w*(beta*b*(1-z)+gamma*b^2*(1-z)-b^2*z*(d+e*b)));
verifyIdentity(blowupF==expectedBlowup,"exact D4 first blowup equation");
verifyIdentity(sub(diff(b,blowupF),{b=>0,w=>0})==u*z*(1-z),
      "only zero and one singularities in finite central chart");
verifyIdentity(sub(blowupF,{z=>1,w=>b^2})==0,
      "lifted actual curve persists in D4 blowup chart");

-- Inverse Cartan formulas; n and j are formal variables, not a finite sample.
R2 = QQ[n,j];
K2 = frac R2;
nn = sub(n,K2);
jj = sub(j,K2);
endDiag = nn/(nn+1);
endContact = (nn+1-jj)/(nn+1);
verifyIdentity(endContact/(3-endDiag)==(nn+1-jj)/(2*nn+3),
      "endpoint A_n Schur complement for every n and j");
internalDiag = 2*(nn-1)/(nn+1);
internalContact = 2/(nn+1);
verifyIdentity(internalContact/(3-internalDiag)==2/(nn+5),
      "actual internal A_n coefficient for every n");
D4 = matrix{{2_QQ,-1,-1,-1},{-1,2,0,0},{-1,0,2,0},{-1,0,0,2}};
G4 = inverse D4;
verifyIdentity(G4_(1,1)==1 and G4_(1,2)==1/2,
      "distinct outer D4 inverse Cartan entries");
verifyIdentity(G4_(1,2)/(3-G4_(1,1))==1/4,
      "D4 conductor correction coefficient one quarter");

print("PASS endpoint-local-ADE exact identities: " | toString checks);
assert(checks==16);
