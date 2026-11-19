-- Equation (4), in the coordinate ring of the source or its affine cone.
markedSections = (sourceRing,imagUnit) -> (
    coords := gens sourceRing;
    (a,b,c,d) := toSequence take(coords,4);
    basisQuadrics := transpose matrix{{a^2,a*b,a*c,a*d,b*c,b*d,c*d,d^2}};
    flatten entries (matrix{
        {-1,2*imagUnit,2+2*imagUnit,1,0,0,0,0},
        {-1-imagUnit,imagUnit-1,3*imagUnit,2+2*imagUnit,1,0,0,0},
        {2-2*imagUnit,-1-imagUnit,-2,3*imagUnit-3,5*imagUnit,2+2*imagUnit,1,0},
        {4,-4*imagUnit,0,-5,4*imagUnit-4,6*imagUnit,2+2*imagUnit,1}
        } * basisQuadrics)
);
