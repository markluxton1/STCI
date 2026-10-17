-- Exact audit of the candidate degree-five A4 anticanonical model.
-- All ideal equalities, saturations, and chart identities are over QQ.
-- The script certifies this literal model, not every quintic projection.
checks = 0;
ck = (label,condition) -> (
    if not condition then error("FAIL " | label);
    checks = checks+1;
    );
zeroCheck = (label,value) -> ck(label,value == 0);

R = QQ[z0,z1,z2,z3,z4,z5];
T = QQ[x,y,z];
parametrization = {y*z^2-x^3,x*y*z,y^2*z,x^2*y,x*y^2,y^3};
phi = map(T,R,parametrization);
kernelIdeal = ker phi;
quadrics = {
    z4^2-z3*z5,
    z2*z4-z1*z5,
    z2*z3-z1*z4,
    z2^2-z3*z4-z0*z5,
    z1*z2-z3^2-z0*z4
    };
I = ideal quadrics;
scan(quadrics,q -> zeroCheck("quadratic vanishes in parametrization",phi q));
ck("five quadrics equal full elimination kernel",I == kernelIdeal);
ck("surface homogeneous dimension",dim(R/I) == 3);
ck("surface degree",degree(R/I) == 5);
ck("surface projectively saturated",saturate(I,ideal vars R) == I);
scan(0..8,n -> ck("degree-five genus-one Hilbert function",
    hilbertFunction(n,R/I) == 1+5*n*(n+1)//2));
modelResolution = res coker gens I;
ck("resolution length",length modelResolution == 3);
scan(0..3,i -> ck("resolution rank",rank(modelResolution#i) == ({1,5,5,1})#i));
scan(0..3,i -> ck("resolution shifts",
    degrees(modelResolution#i) == apply(rank(modelResolution#i),j -> {({0,2,3,5})#i})));

-- Entire projective singular scheme: codimension-three Jacobian minors.
singularIdeal = saturate(I+minors(3,jacobian I),ideal vars R);
expectedSingular = ideal(z5,z4,z3^2,z2*z3,z2^2,z1*z2,
    z0*z2+2*z1*z3,z1^2-z0*z3);
pointIdeal = ideal(z1,z2,z3,z4,z5);
ck("entire saturated projective singular scheme",singularIdeal == expectedSingular);
ck("unique singular point radical",radical singularIdeal == pointIdeal);
ck("singular homogeneous dimension",dim(R/singularIdeal) == 1);
ck("singular scheme length",degree(R/singularIdeal) == 4);
ck("no singular point outside z0 chart",
    saturate(singularIdeal+ideal(z0),ideal vars R) == ideal(1_R));

-- Exact polynomial presentation on z0=1.
A = QQ[a,b,c,d,e];
chartMap = map(A,R,{1_A,a,b,c,d,e});
chartIdeal = chartMap I;
f = b*c-a^2*b+a*c^2;
chartPresentation = ideal(d-a*b+c^2,e-b^2+c*d,f);
ck("z0 chart complete intersection presentation",chartIdeal == chartPresentation);
chartSingular = saturate(chartMap singularIdeal,ideal(1_A));
ck("z0 chart singular ideal",
    chartSingular == ideal(d,e,c-a^2,b+2*a^3,a^4));
U = QQ[aa,uu,vv];
forward = map(U,A,{aa,vv-aa*uu-2*aa^3,uu+aa^2,
    aa*(vv-aa*uu-2*aa^3)-(uu+aa^2)^2,
    (vv-aa*uu-2*aa^3)^2-(uu+aa^2)*(aa*(vv-aa*uu-2*aa^3)-(uu+aa^2)^2)});
zeroCheck("A4 hypersurface exact transform",forward(f)-(uu*vv+aa^5));
backward = map(A,U,{a,c-a^2,b+a*c+a^3});
zeroCheck("inverse a coordinate",backward(aa)-a);
zeroCheck("inverse b coordinate",backward(forward(b))-b);
zeroCheck("inverse c coordinate",backward(forward(c))-c);
zeroCheck("inverse u coordinate",forward(backward(uu))-uu);
zeroCheck("inverse v coordinate",forward(backward(vv))-vv);
ck("A4 singular algebra",
    ideal(uu*vv+aa^5,diff(aa,uu*vv+aa^5),diff(uu,uu*vv+aa^5),diff(vv,uu*vv+aa^5))
    == ideal(uu,vv,aa^4));

-- A second chart gives the parametrization's rational inverse.
V = QQ[v0,v1,v2,v3,v4];
z5Map = map(V,R,{v0,v1,v2,v3,v4,1_V});
ck("z5 chart polynomial plane",
    z5Map I == ideal(v0-v2^2+v4^3,v1-v2*v4,v3-v4^2));

-- The conic yz+x^2=0 lifts to a rational normal quartic.
B = QQ[s,t];
quarticParametrization = {t^4-s*t^3,-s*t^3,-s^2*t^2,s^2*t^2,s^3*t,s^4};
curveMap = map(B,R,quarticParametrization);
curveIdeal = ker curveMap;
scan(quadrics,q -> zeroCheck("candidate quartic lies on surface",curveMap q));
ck("quartic homogeneous dimension",dim(R/curveIdeal) == 2);
ck("quartic degree",degree(R/curveIdeal) == 4);
scan(0..5,n -> ck("rational normal quartic Hilbert function",
    hilbertFunction(n,R/curveIdeal) == 4*n+1));
lineIdeal = ideal(z2,z3,z4,z5);
ck("tangent line lies on surface",isSubset(I,lineIdeal));
ck("actual hyperplane section is quartic plus line",
    I+ideal(z2+z3) == intersect(curveIdeal,lineIdeal));
meeting = saturate(curveIdeal+lineIdeal,ideal vars R);
ck("scheme intersection is tangent length two",
    meeting == ideal(z2,z3,z4,z5,z1^2));
ck("tangent intersection degree",degree(R/meeting) == 2);

-- Exact base cluster: four curvilinear conditions at [0:0:1].
baseIdeal = saturate(ideal parametrization,ideal vars T);
ck("entire projective base ideal",
    baseIdeal == ideal(y^2,x*y,x^3-y*z^2));
ck("base locus radical",radical baseIdeal == ideal(x,y));
ck("base locus length",degree(T/baseIdeal) == 4);
ck("complete cubic system dimension",hilbertFunction(3,T/baseIdeal) == 4);
BA = QQ[xx,yy];
baseMap = map(BA,T,{xx,yy,1_BA});
ck("curvilinear four-point cluster",
    baseMap(ideal parametrization) == ideal(yy-xx^3,xx^4));

print("KERNEL_QUADRICS " | toString gens trim I);
print("HILBERT_SERIES " | toString hilbertSeries(R/I));
print("RESOLUTION_BETTI " | toString betti modelResolution);
print("SATURATED_SINGULAR_SCHEME " | toString gens trim singularIdeal);
print("CURVE_LINE_MEETING " | toString gens trim meeting);
print("BASE_CLUSTER " | toString gens trim baseIdeal);
print("PASS: " | toString checks | " exact quintic A4 model conditions over QQ");
exit 0;
