/* NEW exact corank-one dual from accepted pencil plus exact explicit inverse.
 * f15-specialized arithmetic uses FLINT rational polynomials, never numerical roots.
 */
#include <flint/flint.h>
#include <flint/fmpq_poly.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
typedef struct {slong r,c; fmpq_poly_struct *v;} Mat;
#define E(M,i,j) ((M).v+(i)*(M).c+(j))
static fmpq_poly_t modulus;
static Mat mat(slong r,slong c){Mat a={r,c,flint_malloc(r*c*sizeof(fmpq_poly_struct))};for(slong i=0;i<r*c;i++)fmpq_poly_init(a.v+i);return a;}
static void mark(const char*s){puts(s);fflush(stdout);}
static void fm(fmpq_poly_t c,const fmpq_poly_t a,const fmpq_poly_t b){fmpq_poly_mul(c,a,b);fmpq_poly_rem(c,c,modulus);}
static void fi(fmpq_poly_t c,const fmpq_poly_t a){fmpq_poly_t g,u;fmpq_poly_init(g);fmpq_poly_init(u);fmpq_poly_xgcd(g,c,u,a,modulus);assert(fmpq_poly_is_one(g));fmpq_poly_rem(c,c,modulus);fmpq_poly_clear(g);fmpq_poly_clear(u);}
static Mat mm(Mat a,Mat b){assert(a.c==b.r);Mat c=mat(a.r,b.c);fmpq_poly_t t;fmpq_poly_init(t);for(slong i=0;i<a.r;i++)for(slong j=0;j<b.c;j++)for(slong k=0;k<a.c;k++)if(!fmpq_poly_is_zero(E(a,i,k))&&!fmpq_poly_is_zero(E(b,k,j))){fm(t,E(a,i,k),E(b,k,j));fmpq_poly_add(E(c,i,j),E(c,i,j),t);}fmpq_poly_clear(t);return c;}
static int zero(Mat a){for(slong i=0;i<a.r*a.c;i++)if(!fmpq_poly_is_zero(a.v+i))return 0;return 1;}
static int equal(Mat a,Mat b){if(a.r!=b.r||a.c!=b.c)return 0;for(slong i=0;i<a.r*a.c;i++)if(!fmpq_poly_equal(a.v+i,b.v+i))return 0;return 1;}
static Mat readmat(FILE*in){long rr,cc;assert(fscanf(in,"%ld%ld",&rr,&cc)==2);Mat a=mat(rr,cc);fmpq_poly_t n,d,id;fmpq_poly_init(n);fmpq_poly_init(d);fmpq_poly_init(id);for(slong i=0;i<a.r*a.c;i++){assert(fmpq_poly_fread(in,n));assert(fmpq_poly_fread(in,d));if(!fmpq_poly_is_zero(n)){fi(id,d);fm(a.v+i,n,id);}}fmpq_poly_clear(n);fmpq_poly_clear(d);fmpq_poly_clear(id);return a;}
static void axpy(Mat out,Mat x,const fmpq_poly_t coeff){assert(out.r==x.r&&out.c==x.c);fmpq_poly_t t;fmpq_poly_init(t);for(slong i=0;i<x.r*x.c;i++){fm(t,x.v+i,coeff);fmpq_poly_add(out.v+i,out.v+i,t);}fmpq_poly_clear(t);}
static Mat scaled(Mat x,const fmpq_poly_t coeff){Mat out=mat(x.r,x.c);axpy(out,x,coeff);return out;}
static Mat evaldual(Mat n,Mat U){assert(n.r==74&&n.c==3&&U.r==74&&U.c==1);Mat out=mat(1,3);fmpq_poly_t t;fmpq_poly_init(t);for(slong d=0;d<3;d++)for(slong i=0;i<74;i++){fm(t,E(n,i,d),E(U,i,0));fmpq_poly_add(E(out,0,d),E(out,0,d),t);}fmpq_poly_clear(t);return out;}
static void checkdual(Mat n,Mat A,Mat B){fmpq_poly_t sum,t;fmpq_poly_init(sum);fmpq_poly_init(t);for(slong d=0;d<=3;d++)for(slong j=0;j<18;j++){fmpq_poly_zero(sum);if(d<3){for(slong i=0;i<18;i++){fm(t,E(n,i,d),E(A,i,j));fmpq_poly_add(sum,sum,t);}for(slong i=0;i<56;i++){fm(t,E(n,18+i,d),E(B,i,j));fmpq_poly_add(sum,sum,t);}}if(d>0)fmpq_poly_add(sum,sum,E(n,j,d-1));assert(fmpq_poly_is_zero(sum));}fmpq_poly_clear(sum);fmpq_poly_clear(t);}
static Mat lineardual(Mat r,Mat A,Mat D){Mat n=mat(74,3),rA=mm(r,A),rAD=mm(rA,D),rD=mm(r,D);for(slong i=0;i<18;i++)fmpq_poly_set(E(n,i,0),E(r,0,i));for(slong i=0;i<56;i++){fmpq_poly_neg(E(n,18+i,0),E(rAD,0,i));fmpq_poly_neg(E(n,18+i,1),E(rD,0,i));}return n;}
static Mat quadraticdual(Mat Fh,Mat Fa,Mat A,Mat D){Mat n=mat(74,3),hA=mm(Fh,A),aA=mm(Fa,A),hAD=mm(hA,D),aAD=mm(aA,D),hD=mm(Fh,D),aD=mm(Fa,D);for(slong i=0;i<18;i++){fmpq_poly_set(E(n,i,0),E(Fh,0,i));fmpq_poly_neg(E(n,i,1),E(Fa,0,i));}for(slong i=0;i<56;i++){fmpq_poly_neg(E(n,18+i,0),E(hAD,0,i));fmpq_poly_sub(E(n,18+i,1),E(aAD,0,i),E(hD,0,i));fmpq_poly_set(E(n,18+i,2),E(aD,0,i));}return n;}
static void writepoly(FILE*f,const fmpq_poly_t p){char*s=fmpq_poly_get_str_pretty(p,"k");fputs(s,f);flint_free(s);}
int main(int argc,char**argv){assert(argc==5);clock_t start=clock();fmpq_poly_init(modulus);assert(fmpq_poly_set_str(modulus,"16  -610 285598 811630 1345117 1296458 897946 301686 -34359 -166406 -114414 -54222 -9465 990 2646 810 243")==0);
 FILE*in=fopen(argv[1],"r");assert(in);Mat A=readmat(in),B=readmat(in),v=readmat(in),w=readmat(in),T=readmat(in);fclose(in);assert(A.r==18&&A.c==18&&B.r==56&&B.c==18&&T.r==74&&T.c==74);mark("FLINT exact pencil and accepted row transform read");
 int rows[17]={0,16,7,8,17,12,5,18,4,19,49,13,11,14,20,54,55};int cols[17]={17,6,5,16,0,7,4,1,13,8,10,2,3,9,11,12,14};int missing=15;
 Mat D=mat(18,56);in=fopen(argv[2],"r");assert(in);long nn;assert(fscanf(in,"%ld",&nn)==1&&nn==17);for(slong i=0;i<17;i++)for(slong j=0;j<17;j++)assert(fmpq_poly_fread(in,E(D,cols[i],rows[j])));fclose(in);
 Mat DB=mm(D,B),h=mat(18,1);for(slong i=0;i<18;i++)fmpq_poly_neg(E(h,i,0),E(DB,i,missing));fmpq_poly_set_coeff_si(E(h,missing,0),0,1);assert(fmpq_poly_is_one(E(h,missing,0)));assert(zero(mm(B,h)));
 fmpq_poly_t want,tmp,delta,idelta,one,minusone;fmpq_poly_init(want);fmpq_poly_init(tmp);fmpq_poly_init(delta);fmpq_poly_init(idelta);fmpq_poly_init(one);fmpq_poly_init(minusone);fmpq_poly_one(one);fmpq_poly_set_coeff_si(minusone,0,-1);
 for(slong i=0;i<18;i++)for(slong j=0;j<18;j++){fmpq_poly_zero(want);if(i==j)fmpq_poly_one(want);if(j==missing)fmpq_poly_sub(want,want,E(h,i,0));assert(fmpq_poly_equal(want,E(DB,i,j)));}
 Mat a=mm(A,h);int ii=-1,jj=-1;for(int i=0;i<17&&ii<0;i++)for(int j=i+1;j<18&&ii<0;j++){fm(delta,E(h,i,0),E(a,j,0));fm(tmp,E(h,j,0),E(a,i,0));fmpq_poly_sub(delta,delta,tmp);if(!fmpq_poly_is_zero(delta)){ii=i;jj=j;}}
 assert(ii>=0);fi(idelta,delta);Mat Fh=mat(1,18),Fa=mat(1,18);fm(E(Fh,0,ii),E(a,jj,0),idelta);fm(E(Fh,0,jj),E(a,ii,0),idelta);fmpq_poly_neg(E(Fh,0,jj),E(Fh,0,jj));fm(E(Fa,0,ii),E(h,jj,0),idelta);fmpq_poly_neg(E(Fa,0,ii),E(Fa,0,ii));fm(E(Fa,0,jj),E(h,ii,0),idelta);
 assert(fmpq_poly_is_one(E(mm(Fh,h),0,0)));assert(zero(mm(Fh,a)));assert(zero(mm(Fa,h)));assert(fmpq_poly_is_one(E(mm(Fa,a),0,0)));
 Mat c=mm(D,w),Fhc=mm(Fh,c);fmpq_poly_neg(tmp,E(Fhc,0,0));axpy(c,h,tmp);assert(equal(mm(B,c),w));assert(zero(mm(Fh,c)));mark("PASS exact complement, observability and target compatibility");
 Mat U=mat(74,1);for(slong i=0;i<18;i++)fmpq_poly_set(E(U,i,0),E(v,i,0));for(slong i=0;i<56;i++)fmpq_poly_set(E(U,18+i,0),E(w,i,0));
 Mat ns[16],ls[16];int pos=0;for(int j=0;j<18;j++)if(j!=ii&&j!=jj){Mat rr=mat(1,18);fmpq_poly_one(E(rr,0,j));fmpq_poly_neg(tmp,E(h,j,0));axpy(rr,Fh,tmp);fmpq_poly_neg(tmp,E(a,j,0));axpy(rr,Fa,tmp);assert(zero(mm(rr,h))&&zero(mm(rr,a)));ns[pos]=lineardual(rr,A,D);checkdual(ns[pos],A,B);ls[pos]=evaldual(ns[pos],U);pos++;}
 Mat ng=quadraticdual(Fh,Fa,A,D);checkdual(ng,A,B);Mat gg=evaldual(ng,U);mark("PASS all16 linear and1 quadratic exact annihilator identities");
 Mat N=mat(74,3);int normalized=0,first=-1;
 for(int i=0;i<16&&!normalized;i++)if(fmpq_poly_is_zero(E(ls[i],0,1))&&!fmpq_poly_is_zero(E(ls[i],0,0))){fi(tmp,E(ls[i],0,0));N=scaled(ns[i],tmp);normalized=1;printf("normalization branch: constant linear evaluation %d\n",i);}
 for(int i=0;i<16&&first<0;i++)if(!fmpq_poly_is_zero(E(ls[i],0,1)))first=i;
 if(!normalized&&first>=0){fmpq_poly_t alpha,ib,at,ratio;fmpq_poly_init(alpha);fmpq_poly_init(ib);fmpq_poly_init(at);fmpq_poly_init(ratio);fi(ib,E(ls[first],0,1));fm(alpha,E(ls[first],0,0),ib);fmpq_poly_neg(alpha,alpha);
  for(int i=0;i<16&&!normalized;i++){fm(at,alpha,E(ls[i],0,1));fmpq_poly_add(at,at,E(ls[i],0,0));if(!fmpq_poly_is_zero(at)){fm(ratio,E(ls[i],0,1),ib);fmpq_poly_neg(ratio,ratio);N=scaled(ns[first],ratio);axpy(N,ns[i],one);fi(tmp,at);N=scaled(N,tmp);normalized=1;printf("normalization branch: incompatible linear evaluations %d,%d\n",first,i);}}
  if(!normalized){fm(at,E(gg,0,2),alpha);fmpq_poly_add(at,at,E(gg,0,1));fm(at,at,alpha);fmpq_poly_add(at,at,E(gg,0,0));if(!fmpq_poly_is_zero(at)){
   /* (gg-gg(alpha))/l = (g2/b)*lambda + (g1+g2*alpha)/b. */
   fmpq_poly_t q0,q1;fmpq_poly_init(q0);fmpq_poly_init(q1);fm(q1,E(gg,0,2),ib);fm(q0,E(gg,0,2),alpha);fmpq_poly_add(q0,q0,E(gg,0,1));fm(q0,q0,ib);fmpq_poly_neg(q0,q0);fmpq_poly_neg(q1,q1);axpy(N,ng,one);
   for(slong r=0;r<74;r++)for(slong d=0;d<3;d++){fm(tmp,E(ns[first],r,d),q0);fmpq_poly_add(E(N,r,d),E(N,r,d),tmp);if(d<2){fm(tmp,E(ns[first],r,d),q1);fmpq_poly_add(E(N,r,d+1),E(N,r,d+1),tmp);}}
   fi(tmp,at);N=scaled(N,tmp);normalized=1;puts("normalization branch: linear-quadratic Bezout");
  }}
 }
 if(!normalized&&first<0&&fmpq_poly_is_zero(E(gg,0,1))&&fmpq_poly_is_zero(E(gg,0,2))&&!fmpq_poly_is_zero(E(gg,0,0))){fi(tmp,E(gg,0,0));N=scaled(ng,tmp);normalized=1;puts("normalization branch: constant quadratic evaluation");}
 FILE*ob=fopen(argv[4],"w");assert(ob);for(int i=0;i<16;i++){fprintf(ob,"linear %d ",i);for(int d=0;d<2;d++){fputc('(',ob);writepoly(ob,E(ls[i],0,d));fprintf(ob,")%s",d?"*lambda\n":"+");}}fputs("quadratic ",ob);for(int d=0;d<3;d++){fputc('(',ob);writepoly(ob,E(gg,0,d));fprintf(ob,")%s",d==0?"+":d==1?"*lambda+":"*lambda^2\n");}fclose(ob);
 if(!normalized){mark("NO EXCLUSION: obstruction evaluations have common zero; preserve full incidence");return 2;}
 checkdual(N,A,B);Mat norm=evaldual(N,U);assert(fmpq_poly_is_one(E(norm,0,0))&&fmpq_poly_is_zero(E(norm,0,1))&&fmpq_poly_is_zero(E(norm,0,2)));
 Mat Norig=mat(74,3);for(slong i=0;i<74;i++)for(slong j=0;j<74;j++)if(!fmpq_poly_is_zero(E(T,j,i)))for(slong d=0;d<3;d++){fm(tmp,E(T,j,i),E(N,j,d));fmpq_poly_add(E(Norig,i,d),E(Norig,i,d),tmp);}
 assert(fmpq_poly_is_one(E(Norig,72,0))&&fmpq_poly_is_zero(E(Norig,72,1))&&fmpq_poly_is_zero(E(Norig,72,2)));
 FILE*out=fopen(argv[3],"w");assert(out);for(slong r=0;r<74;r++){fprintf(out,"%ld ",r);for(slong d=0;d<3;d++){fputc('(',out);writepoly(out,E(Norig,r,d));fprintf(out,")%s",d==0?"+":d==1?"*lambda+":"*lambda^2\n");}}fclose(out);
 printf("PASS canonical normalized degree<=2 dual and original coordinate72=1; CPU %.3f seconds\n",(double)(clock()-start)/CLOCKS_PER_SEC);mark("Independent original tensor identities remain required");return 0;
}
