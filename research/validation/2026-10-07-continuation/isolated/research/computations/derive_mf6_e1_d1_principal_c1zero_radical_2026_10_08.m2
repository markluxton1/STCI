T=QQ[a,x0,x1,x2,x3];
F=x0^3*x2 - x0^3*x3 - 4*x0^2*x1*x2/3 + a*x0^2*x1*x2/3 + 8*x0^2*x1*x3/3 - 2*a*x0^2*x1*x3/3 + 32*x0^2*x2^2/9 - 17*a*x0^2*x2^2/9 - 47*x0^2*x2*x3/9 + 32*a*x0^2*x2*x3/9 + 17*x0^2*x3^2/9 - 20*a*x0^2*x3^2/9 - x0*x1^3 - 8*x0*x1^2*x2/3 + 2*a*x0*x1^2*x2/3 - x0*x1^2*x3 + a*x0*x1^2*x3 + 25*x0*x1*x2^2/9 - 13*a*x0*x1*x2^2/9 - 10*x0*x1*x2*x3/9 + 7*a*x0*x1*x2*x3/9 - 2*x0*x1*x3^2/9 + 14*a*x0*x1*x3^2/9 + x0*x2^3/9 - 7*a*x0*x2^3/9 + 7*x1^4/3 - a*x1^4/3 - 23*x1^3*x2/9 + 8*a*x1^3*x2/9 + 22*x1^3*x3/9 - 19*a*x1^3*x3/9 - 7*x1^2*x2^2/9 + 13*a*x1^2*x2^2/9 + x1^2*x2*x3/9 - 7*a*x1^2*x2*x3/9 - x1^2*x3^2/9 - 2*a*x1^2*x3^2/9 + x1*x2^3/9 + 2*a*x1*x2^3/9;
J=ideal(a^2+2,diff(x0,F),diff(x1,F),diff(x2,F),diff(x3,F));
I=radical J;
print I;
print(dim(T/I),degree(T/I));
"research/scratch/principal-c1zero-radical-2026-10-08.txt" << toString gens I << close;
