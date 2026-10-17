/* New characteristic-zero polynomial inverse. No finite samples prove claims. */
#include <flint/flint.h>
#include <flint/fmpz_poly.h>
#include <flint/fmpz_poly_mat.h>
#include <flint/fmpq_poly.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
static void mark(const char *s) { printf("%s\n",s); fflush(stdout); }
static void fm(fmpq_poly_t c,const fmpq_poly_t a,const fmpq_poly_t b,const fmpq_poly_t f) { fmpq_poly_mul(c,a,b); fmpq_poly_rem(c,c,f); }
int main(int argc,char **argv) {
 assert(argc==4); FILE *in=fopen(argv[1],"r");assert(in); long nn;assert(fscanf(in,"%ld",&nn)==1);slong n=nn;
 fmpz_poly_t d,fz,den;fmpz_poly_init(d);fmpz_poly_init(fz);fmpz_poly_init(den);
 assert(fmpz_poly_fread(in,d));assert(fmpz_poly_fread(in,fz));
 fmpz_poly_mat_t M,N,L,R,I;fmpz_poly_mat_init(M,n,n);fmpz_poly_mat_init(N,n,n);fmpz_poly_mat_init(L,n,n);fmpz_poly_mat_init(R,n,n);fmpz_poly_mat_init(I,n,n);
 for(slong i=0;i<n;i++)for(slong j=0;j<n;j++)assert(fmpz_poly_fread(in,fmpz_poly_mat_entry(M,i,j)));fclose(in);
 mark("FLINT fraction-free input read; starting polynomial inverse");clock_t start=clock();
 assert(fmpz_poly_mat_inv(N,den,M));
 printf("Polynomial inverse returned; denominator degree %ld; CPU %.3f seconds\n",fmpz_poly_degree(den),(double)(clock()-start)/CLOCKS_PER_SEC);fflush(stdout);
 fmpz_poly_mat_mul(L,M,N);fmpz_poly_mat_mul(R,N,M);fmpz_poly_mat_one(I);fmpz_poly_mat_scalar_mul_fmpz_poly(I,I,den);
 assert(fmpz_poly_mat_equal(L,I));assert(fmpz_poly_mat_equal(R,I));
 mark("PASS both exact Z[k] adjugate identities");
 FILE *raw=fopen(argv[2],"w");assert(raw);fprintf(raw,"%ld\n",n);fmpz_poly_fprint(raw,den);fputc('\n',raw);
 for(slong i=0;i<n;i++)for(slong j=0;j<n;j++){fmpz_poly_fprint(raw,fmpz_poly_mat_entry(N,i,j));fputc('\n',raw);}fclose(raw);
 fmpq_poly_t f,qd,qden,g,u,v,temp,sum,expected,qM;fmpq_poly_init(f);fmpq_poly_init(qd);fmpq_poly_init(qden);fmpq_poly_init(g);fmpq_poly_init(u);fmpq_poly_init(v);fmpq_poly_init(temp);fmpq_poly_init(sum);fmpq_poly_init(expected);fmpq_poly_init(qM);
 fmpq_poly_set_fmpz_poly(f,fz);fmpq_poly_set_fmpz_poly(qd,d);fmpq_poly_rem(qd,qd,f);fmpq_poly_set_fmpz_poly(qden,den);fmpq_poly_rem(qden,qden,f);
 fmpq_poly_xgcd(g,u,v,qden,f);assert(fmpq_poly_is_one(g));fmpq_poly_rem(u,u,f);fm(u,u,qd,f);
 fmpq_poly_xgcd(g,v,temp,qd,f);assert(fmpq_poly_is_one(g));
 fmpq_poly_struct *inv=flint_malloc(n*n*sizeof(fmpq_poly_struct));
 for(slong i=0;i<n*n;i++){fmpq_poly_init(inv+i);fmpq_poly_set_fmpz_poly(temp,fmpz_poly_mat_entry(N,i/n,i%n));fm(inv+i,temp,u,f);}
 for(int side=0;side<2;side++)for(slong i=0;i<n;i++)for(slong j=0;j<n;j++){
  fmpq_poly_zero(sum);
  for(slong k=0;k<n;k++){
   fmpq_poly_set_fmpz_poly(qM,fmpz_poly_mat_entry(M,side?k:i,side?j:k));
   fm(temp,qM,inv+(side?i*n+k:k*n+j),f);fmpq_poly_add(sum,sum,temp);
  }
  if(i==j)fmpq_poly_set(expected,qd);else fmpq_poly_zero(expected);
  assert(fmpq_poly_equal(sum,expected));
 }
 mark("PASS degree15 unit checks and both specialized inverse identities");
 FILE *out=fopen(argv[3],"w");assert(out);fprintf(out,"%ld\n",n);
 for(slong i=0;i<n*n;i++){fmpq_poly_fprint(out,inv+i);fputc('\n',out);}fclose(out);
 printf("PASS exact inverse saved; total CPU %.3f seconds\n",(double)(clock()-start)/CLOCKS_PER_SEC);fflush(stdout);
 return 0;
}
