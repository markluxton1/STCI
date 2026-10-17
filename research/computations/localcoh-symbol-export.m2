-- Export exact Ext^2 principal parts into fixed (q^4,B^4) stage.
S=QQ[x,y,z,w];
q=x*w-y*z; A=x^2*z-y^3; B=x*z^2-y^2*w; C=y*w^2-z^3;
I=ideal(q,A,B,C);
MI4=coker gens(I^4); MJ4=coker gens ideal(q^4,B^4);
f=map(MI4,MJ4,matrix{{1_S}});
g=Ext^2(f,S^1);
h=g*basis(-7,source g);
assert(numColumns h==30 and numRows h==1);
fn="/Users/markluxton/Projects/STCI/research/computations/localcoh-symbol-numerators.txt";
ff=openOut fn;
for j from 0 to 29 do ff << toString lift(h_(0,j),S) << endl;
close ff;
print("PASS: exported 30 degree-13 numerators to "|fn);
