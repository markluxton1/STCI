-- Independent universal-ideal audit.  No selected augmented minor, no
-- complex-root sampling, and no imported Python/SymPy package is used.
count = 0;
check = (label, condition) -> (
    if condition =!= true then error("FAIL: " | label);
    count = count+1;
    print("PASS: " | label);
    );

R31 = QQ[k,n1,n2,a0,a1,a2,a4,a5];
M31 = matrix {{1,2,k},{2,k,-2},{k,-2,-1}};
check("[3,1] full E2 determinant", det M31 == -k*(k^2+9));
check("[3,1] nonzero rank-two minor at every determinant root",
    ideal(k*(k^2+9), k^2+1) == ideal(1_R31));
-- If eta0=0, the last two kernel rows imply (k+4)eta1=0.
-- A nonzero such direction would force k=-4, which is not a determinant root.
check("[3,1] eta0=1 chart is exhaustive",
    ideal(k*(k^2+9), k+4) == ideal(1_R31));
I31 = ideal(
    1+2*n1+k*n2, 2+k*n1-2*n2, k-2*n1-n2,
    a0+a1*n1+a2*n2,
    a1+(a2+1)*n1+a4*n2,
    a2+a4*n1+a5*n2,
    a0-a1-2-a4+a5, a0+a1-2+a4+a5);
J31 = ideal(k,n1+1/2,n2-1,a2+1,a0-1-a1/2,a4+a1,a5-1+a1/2);
check("[3,1] ENTIRE universal net/support ideal equals survivor linear ideal", I31 == J31);
check("[3,1] survivor has exactly one affine parameter", dim(R31/I31) == 1);
check("[3,1] survivor direction is off intrinsic conic", ((n1^2-n2) % J31) == -3/4);

R22 = QQ[k,n1,n2,a0,a1,a2,a4,a5];
M22 = matrix {{1,-2,k},{-2,k,1},{k,1,1/4}};
check("[2,2] full E2 determinant", det M22 == -(2*k+1)*(2*k^2-k+8)/4);
check("[2,2] nonzero rank-two minor at every determinant root",
    ideal((2*k+1)*(2*k^2-k+8), k-4) == ideal(1_R22));
-- If eta0=0, the remaining rows imply (k+1/2)eta2=0 and
-- (1-k/4)eta2=0; these multipliers generate the unit ideal.
check("[2,2] eta0=1 chart is exhaustive", ideal(k+1/2,1-k/4) == ideal(1_R22));
I22 = ideal(
    1-2*n1+k*n2, -2+k*n1+n2, k+n1+n2/4,
    a0+a1*n1+a2*n2,
    a1+(a2+1)*n1+a4*n2,
    a2+a4*n1+a5*n2,
    -a1-6*a4+16*a5-4, a0-4*a4+12*a5-4);
J22 = ideal(k+1/2,n1,n2-2,a0-4*a5,a1-2+8*a5,a2+2*a5,a4+1-4*a5);
check("[2,2] ENTIRE universal net/support ideal equals survivor linear ideal", I22 == J22);
check("[2,2] survivor has exactly one affine parameter", dim(R22/I22) == 1);
check("[2,2] eta1=0 boundary retained and off intrinsic conic", ((n1^2-n2) % J22) == -2);

P = QQ[a,b,k,lam];
endpoint31 = matrix {{a,-b,k},{-b,k,0},{k,0,0}};
check("[3,1] endpoint-triple invisible E2 determinant", det endpoint31 == -k^3);
check("[3,1] endpoint-triple nonzero minor", det submatrix(endpoint31,{0,1},{0,1}) % ideal(k) == -b^2);
four = matrix {{1,0,k},{0,k,0},{k,0,0}};
check("[4] invisible E2 determinant", det four == -k^3);

Y = QQ[y0,y1,y2,y3,y4];
E = {y0*y2-y1^2,y0*y3-y1*y2,y0*y4-y1*y3,
     y1*y3-y2^2,y1*y4-y2*y3,y2*y4-y3^2};
line4 = {y0=>0,y1=>0,y2=>0};
-- lambda is a scalar parameter in the proof; line containment does not
-- require it, since each involved literal quadric vanishes on the line.
check("[4] every pencil term contains the singular line",
    all({E#0,E#1,E#2,E#3}, e -> sub(e,line4) == 0));
check("[4] full E0 gradient vanishes on line", all(gens Y, v -> sub(diff(v,E#0),line4) == 0));
T31 = E#0-E#2+E#3+E#5;
Q31 = E#0+2*E#1-2*E#4-E#5;
line31 = {y0=>y2,y4=>y2,y3=>y1};
check("[3,1] both quadrics contain actual singular line", sub(T31,line31) == 0 and sub(Q31,line31) == 0);
check("[3,1] full T gradient vanishes on line", all(gens Y, v -> sub(diff(v,T31),line31) == 0));

X = QQ[x0,x1,x2,x3,z];
phi = map(X,Y,{x0,x1,z,x2,x3});
Q1 = phi(2*E#1+E#3-E#4);
Q2 = phi(E#0-2*E#1-E#2/2+E#4+E#5/4);
L = diff(z,Q2);
R = sub(Q2,{z=>0});
A = diff(z,Q1+z^2);
R1 = sub(Q1,{z=>0});
ell = diff(z,phi(E#3)-Q1);
q = sub(phi(E#3)-Q1,{z=>0});
check("[2,2] actual monic projection equation", Q1 == -z^2+A*z+R1);
check("[2,2] actual linear projection equation", Q2 == L*z+R);
check("[2,2] actual Cartier-double quadric reduction", phi(E#3)-Q1 == ell*z+q);
plane = {x0=>-2*x1+x2-x3/4};
Rc = sub(R,plane);
Hessian = matrix apply({x1,x2,x3}, u -> apply({x1,x2,x3}, v -> diff(u,diff(v,Rc))/2));
check("[2,2] entire conductor conic smooth", det Hessian == 243/128);
Tr = sub(2*q+A*ell,plane);
Nr = sub(q^2+A*q*ell-R1*ell^2,plane);
Ds = sub(A^2+4*R1,plane);
check("[2,2] exact trace/norm/discriminant identity", Tr^2-4*Nr == Ds*sub(ell,plane)^2);
slice = {x1=>0,x3=>1};
p = 18*x2^2-1;
Ts = sub(Tr,slice);
Ns = sub(Nr,slice);
check("[2,2] independent conic section x1=0", sub(Rc,slice) == -p/8);
check("[2,2] norm nonzero at both independent points", ideal(p,Ns) == ideal(1_X));
check("[2,2] independent all-powers obstruction T2/N=22+72x2",
    ((Ts^2-(22+72*x2)*Ns) % ideal(p)) == 0);
check("[2,2] independent section has two distinct roots", ideal(p,diff(x2,p)) == ideal(1_X));
check("[2,2] quadratic cover is separable at both independent points", ideal(p,sub(Ds,slice)) == ideal(1_X));

ff = openOut "research/validation/2026-10-10-repeated-partitions-independent-audit/result.json";
ff << "{\n  \"status\": \"PASS\",\n  \"engine\": \"Macaulay2 1.26.06\",\n  \"checked_conditions\": " << count << ",\n  \"independence\": \"Universal net/support ideal equality for [3,1] and [2,2]; exhaustive eta0 chart; different conductor section x1=0\",\n  \"conductor_section\": \"18t^2-1=0\",\n  \"trace_square_over_norm\": \"22+72t\",\n  \"scope\": \"Complete [4],[3,1],[2,2] conditional on the stated ribbon-net and actual projection/conductor inputs\",\n  \"does_not_claim\": \"Upstream interface completeness, [2,1,1], higher carrier degrees, or universal STCI resolution\"\n}\n";
close ff;
print("PASS: " | toString count | " independent exact conditions");
