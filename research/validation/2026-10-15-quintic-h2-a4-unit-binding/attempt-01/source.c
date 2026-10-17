#include <flint/flint.h>
#include <flint/fmpq_mpoly.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* New exact relation among saved coefficient artifacts; no old verifier. */
static fmpq_mpoly_ctx_t ctx;
static const char *names[]={"deltaPar","vPar","wPar"};
static void read_poly(fmpq_mpoly_t f,const char *path){
 FILE *fp=fopen(path,"rb");assert(fp);fseek(fp,0,SEEK_END);long n=ftell(fp);rewind(fp);
 char *s=malloc((size_t)n+1);assert(s);assert(fread(s,1,(size_t)n,fp)==(size_t)n);s[n]=0;fclose(fp);
 assert(fmpq_mpoly_set_str_pretty(f,s,names,ctx)==0);free(s);
}
static void write_poly(const fmpq_mpoly_t f,const char *dir,const char *label){
 char path[2048];snprintf(path,sizeof(path),"%s/%s.txt",dir,label);FILE *fp=fopen(path,"wb");assert(fp);
 char *s=fmpq_mpoly_get_str_pretty(f,names,ctx);fputs(s,fp);fputc('\n',fp);flint_free(s);fclose(fp);
}
int main(int argc,char **argv){
 assert(argc==2);fmpq_mpoly_ctx_init(ctx,3,ORD_DEGREVLEX);
 fmpq_mpoly_t f[3],primitive[3],unit[3],quot,prod,left,right,tmp;
 for(int i=0;i<3;i++){fmpq_mpoly_init(f[i],ctx);fmpq_mpoly_init(primitive[i],ctx);fmpq_mpoly_init(unit[i],ctx);}
 fmpq_mpoly_init(quot,ctx);fmpq_mpoly_init(prod,ctx);fmpq_mpoly_init(left,ctx);fmpq_mpoly_init(right,ctx);fmpq_mpoly_init(tmp,ctx);
 read_poly(f[0],"research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient/Q-coefficient-6.txt");
 read_poly(f[1],"research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01/Jbar-numerator.txt");
 read_poly(f[2],"research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01/Delta1-numerator.txt");
 assert(!fmpq_mpoly_set_str_pretty(unit[0],"deltaPar",names,ctx));
 assert(!fmpq_mpoly_set_str_pretty(unit[1],"vPar^2-4*wPar",names,ctx));
 assert(!fmpq_mpoly_set_str_pretty(unit[2],"vPar^2+6*vPar*wPar+6*wPar^2+2*wPar",names,ctx));
 int exps[3][3]={{0}},difference[3];
 for(int i=0;i<3;i++){
  fmpq_mpoly_set(primitive[i],f[i],ctx);
  for(int u=0;u<3;u++)while(fmpq_mpoly_divides(quot,primitive[i],unit[u],ctx)){
   fmpq_mpoly_set(primitive[i],quot,ctx);exps[i][u]++;
  }
 }
 fmpq_mpoly_mul(prod,primitive[1],primitive[2],ctx);
 assert(fmpq_mpoly_divides(quot,primitive[0],prod,ctx));
 assert(!fmpq_mpoly_is_zero(quot,ctx));assert(fmpq_mpoly_total_degree_si(quot,ctx)==0);
 fmpq_mpoly_set(left,f[0],ctx);fmpq_mpoly_mul(right,f[1],f[2],ctx);fmpq_mpoly_mul(right,right,quot,ctx);
 for(int u=0;u<3;u++){
  difference[u]=exps[0][u]-exps[1][u]-exps[2][u];
  if(difference[u]>=0){assert(fmpq_mpoly_pow_ui(tmp,unit[u],difference[u],ctx));fmpq_mpoly_mul(right,right,tmp,ctx);}
  else {assert(fmpq_mpoly_pow_ui(tmp,unit[u],-difference[u],ctx));fmpq_mpoly_mul(left,left,tmp,ctx);}
 }
 assert(fmpq_mpoly_equal(left,right,ctx));
 write_poly(quot,argv[1],"nonzero-rational-ratio");
 char path[2048];snprintf(path,sizeof(path),"%s/unit-exponents.json",argv[1]);FILE *out=fopen(path,"wb");assert(out);
 fprintf(out,"{\n  \"q6_exponents\": [%d,%d,%d],\n  \"Jbar_numerator_exponents\": [%d,%d,%d],\n  \"Delta1_numerator_exponents\": [%d,%d,%d],\n  \"ratio_exponents\": [%d,%d,%d],\n  \"unit_order\": [\"delta\",\"discriminant\",\"cover_K\"]\n}\n",exps[0][0],exps[0][1],exps[0][2],exps[1][0],exps[1][1],exps[1][2],exps[2][0],exps[2][1],exps[2][2],difference[0],difference[1],difference[2]);fclose(out);
 puts("PASS q6 = c * delta^e0 * discriminant^e1 * K^e2 * Jbar_num * Delta1_num, with c a nonzero rational");
 puts("PASS literal polynomial equality after multiplying only negative declared-unit powers");
 puts("COMPLETE new A4 coefficient unit binding; no geometric emptiness claim");
 for(int i=0;i<3;i++){fmpq_mpoly_clear(f[i],ctx);fmpq_mpoly_clear(primitive[i],ctx);fmpq_mpoly_clear(unit[i],ctx);}
 fmpq_mpoly_clear(quot,ctx);fmpq_mpoly_clear(prod,ctx);fmpq_mpoly_clear(left,ctx);fmpq_mpoly_clear(right,ctx);fmpq_mpoly_clear(tmp,ctx);fmpq_mpoly_ctx_clear(ctx);flint_cleanup();return 0;
}
