-- Exact finite quartic multiplication tensor for C0 over QQ.
-- Run from repository root: M2 --script research/computations/localcoh-incidence-tensor.m2
-- Rows encode precisely F*alpha=u and G*alpha=v in diagonal Cech stage4.
S=QQ[x,y,z,w];
q=x*w-y*z; A=x^2*z-y^3; B=x*z^2-y^2*w; C=y*w^2-z^3;
I=ideal(q,A,B,C);
MI4=coker gens(I^4); MJ4=coker gens ideal(q^4,B^4);
f=map(MI4,MJ4,matrix{{1_S}}); g=Ext^2(f,S^1);
h=g*basis(-7,source g); H=lift(h,S);
assert(numColumns H==30 and numRows H==1);
assert(numColumns basis(-7,kernel g)==0);
-- basis(4,I) is expressed in the four generator coordinates of I.
Wc=basis(4,I); GI=gens I;
W=matrix{for j from 0 to numColumns Wc-1 list
    sum(0..3,i->GI_(0,i)*Wc_(i,j))};
assert(numColumns W==18 and numRows W==1);
assert(all(0..17,j->degree W_(0,j)=={4}));
P=gens gb ideal(q^4,B^4);
products=matrix{flatten(for i from 0 to 29 list
    (for j from 0 to 17 list ((H_(0,i)*W_(0,j)) % P)))};
T=matrix{{(x*z*(q*B)^3) % P,(y*w*(q*B)^3) % P}};
combinedCols=products|T;
cc=sub((coefficients combinedCols)#1,QQ);
rows=transpose gens gb image transpose cc;
assert(numRows rows==74 and numColumns rows==542);
assert(rank sub((coefficients products)#1,QQ)==74);
E3=Ext^2(coker gens(I^3),S^1);
assert(numColumns basis(-3,E3)==74);
-- Verify compression preserves row space, including the two target columns.
assert(rank(cc||rows)==74);
fn="research/computations/localcoh-incidence-tensor.txt";
ff=openOut fn;
ff << "30 18 74 542" << endl;
for r from 0 to 73 do for c from 0 to 541 do
    if rows_(r,c)!=0 then ff << r << " " << c << " " << toString rows_(r,c) << endl;
close ff;
fn="research/computations/localcoh-incidence-bases.txt";
ff=openOut fn;
ff << "ancestor stage4 numerators" << endl;
for j from 0 to 29 do ff << toString H_(0,j) << endl;
ff << "quartic multipliers" << endl;
for j from 0 to 17 do ff << toString W_(0,j) << endl;
close ff;
print("PASS: 74 exact equations for each target; 30 ancestors and 18 quartics.");
print("PASS: tensor image equals the complete 74-dimensional E3_-3 piece.");
