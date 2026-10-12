-- Exact local-chart identities for the degree-five del Pezzo parametrization.
-- Scope: the Z0 != 0 chart, not the global kernel or global singular locus.
globalRing = QQ[Z0,Z1,Z2,Z3,Z4,Z5];
sourceRing = QQ[xx,yy,zz];
parameterMap = map(sourceRing,globalRing,{
    yy*zz^2-xx^3,xx*yy*zz,yy^2*zz,xx^2*yy,xx*yy^2,yy^3
    });
globalRelations = {
    Z1*Z5-Z2*Z4,
    Z3*Z5-Z4^2,
    Z1*Z4-Z2*Z3,
    Z0*Z5-Z2^2+Z3*Z4,
    Z0*Z4-Z1*Z2+Z3^2
    };
scan(globalRelations,r -> assert(parameterMap(r)==0));

chartRing = QQ[chartA,chartB,chartC,chartD,chartE];
dehomogenizeMap = map(chartRing,globalRing,{1,chartA,chartB,chartC,chartD,chartE});
chartRelations = apply(globalRelations,r -> dehomogenizeMap(r));
smallRing = QQ[ta,tb,tc];
eliminateMap = map(smallRing,chartRing,{
    ta,tb,tc,ta*tb-tc^2,tb^2-tc*(ta*tb-tc^2)
    });
hypersurfaceEquation = tb*(ta^2-tc)-ta*tc^2;
assert(apply(chartRelations,r -> eliminateMap(r)) == {
    -tc*hypersurfaceEquation,-tb*hypersurfaceEquation,
    hypersurfaceEquation,0,0
    });

a4Ring = QQ[za,zu,zv];
toA4Map = map(a4Ring,smallRing,{za,zv-za*zu-2*za^3,zu+za^2});
fromA4Map = map(smallRing,a4Ring,{ta,tc-ta^2,tb+ta*tc+ta^3});
assert(toA4Map(hypersurfaceEquation)==-zu*zv-za^5);
scan(gens smallRing,r -> assert(fromA4Map(toA4Map(r))==r));
scan(gens a4Ring,r -> assert(toA4Map(fromA4Map(r))==r));

-- The rational inverse on chartE != 0 follows from the same relations.
chartIdeal = ideal chartRelations;
assert((chartE^2-chartB^2*chartE+chartD^3) % chartIdeal == 0);
assert((chartA*chartE-chartB*chartD) % chartIdeal == 0);
assert((chartC*chartE-chartD^2) % chartIdeal == 0);
print "PASS: 20 exact identities; chart is k[za,zu,zv]/(zu*zv+za^5).";
exit 0;
