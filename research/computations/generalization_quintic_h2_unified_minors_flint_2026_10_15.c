#include <flint/flint.h>
#include <flint/fmpq_mpoly.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

/* Exact arithmetic preparation only.  Every input is an already captured
   polynomial; no accepted construction or verifier is rerun. */
static fmpq_mpoly_ctx_t ctx;
static const char *names[] = {"deltaPar", "vPar", "wPar"};
static char *read_text(const char *path) {
    FILE *f=fopen(path,"rb"); if(!f){perror(path);exit(2);} fseek(f,0,SEEK_END);
    long n=ftell(f); rewind(f); char *s=malloc((size_t)n+1);
    assert(s); assert(fread(s,1,(size_t)n,f)==(size_t)n);s[n]=0;fclose(f);return s;
}
static void read_poly(fmpq_mpoly_t f,const char *path) {
    char *s=read_text(path);int rc=fmpq_mpoly_set_str_pretty(f,s,names,ctx);
    free(s);if(rc){fprintf(stderr,"parse failure %s\n",path);exit(3);}
}
static void write_poly(const fmpq_mpoly_t f,const char *dir,const char *label) {
    char path[2048];snprintf(path,sizeof(path),"%s/%s.txt",dir,label);
    FILE *out=fopen(path,"wb");if(!out){perror(path);exit(4);}
    char *s=fmpq_mpoly_get_str_pretty(f,names,ctx);fputs(s,out);fputc('\n',out);
    flint_free(s);fclose(out);
}
static void det3(fmpq_mpoly_t out, fmpq_mpoly_t a[8],fmpq_mpoly_t b[8],fmpq_mpoly_t c[8],int i,int k,int l) {
    fmpq_mpoly_t x,y,z;fmpq_mpoly_init(x,ctx);fmpq_mpoly_init(y,ctx);fmpq_mpoly_init(z,ctx);
    fmpq_mpoly_mul(x,b[k],c[l],ctx);fmpq_mpoly_mul(y,b[l],c[k],ctx);fmpq_mpoly_sub(x,x,y,ctx);fmpq_mpoly_mul(out,a[i],x,ctx);
    fmpq_mpoly_mul(x,b[i],c[l],ctx);fmpq_mpoly_mul(y,b[l],c[i],ctx);fmpq_mpoly_sub(x,x,y,ctx);fmpq_mpoly_mul(z,a[k],x,ctx);fmpq_mpoly_sub(out,out,z,ctx);
    fmpq_mpoly_mul(x,b[i],c[k],ctx);fmpq_mpoly_mul(y,b[k],c[i],ctx);fmpq_mpoly_sub(x,x,y,ctx);fmpq_mpoly_mul(z,a[l],x,ctx);fmpq_mpoly_add(out,out,z,ctx);
    fmpq_mpoly_clear(x,ctx);fmpq_mpoly_clear(y,ctx);fmpq_mpoly_clear(z,ctx);
}
int main(int argc,char **argv) {
    if(argc!=2){fprintf(stderr,"usage: %s OUTPUT_DIR\n",argv[0]);return 1;}
    const char *outdir=argv[1]; char path[2048],label[128];
    fmpq_mpoly_ctx_init(ctx,3,ORD_DEGREVLEX);
    fmpq_mpoly_t q[8],prevq[8],r[8],unit[3],j,x,y,raw,nf,quot,mult,check,oldfirst;
    for(int i=0;i<8;i++){fmpq_mpoly_init(q[i],ctx);fmpq_mpoly_init(prevq[i],ctx);fmpq_mpoly_init(r[i],ctx);}
    for(int i=0;i<3;i++)fmpq_mpoly_init(unit[i],ctx);
    fmpq_mpoly_init(j,ctx);fmpq_mpoly_init(x,ctx);fmpq_mpoly_init(y,ctx);fmpq_mpoly_init(raw,ctx);fmpq_mpoly_init(nf,ctx);fmpq_mpoly_init(quot,ctx);fmpq_mpoly_init(mult,ctx);fmpq_mpoly_init(check,ctx);fmpq_mpoly_init(oldfirst,ctx);
    for(int i=0;i<7;i++){
        snprintf(path,sizeof(path),"research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient/Q-coefficient-%d.txt",i);
        read_poly(q[i],path);if(i>0)fmpq_mpoly_set(prevq[i],q[i-1],ctx);
    }
    fmpq_mpoly_set(prevq[7],q[6],ctx);
    read_poly(j,"research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01/Jbar-numerator.txt");
    assert(fmpq_mpoly_set_str_pretty(unit[0],"deltaPar",names,ctx)==0);
    assert(fmpq_mpoly_set_str_pretty(unit[1],"vPar^2-4*wPar",names,ctx)==0);
    assert(fmpq_mpoly_set_str_pretty(unit[2],"vPar^2+6*vPar*wPar+6*wPar^2+2*wPar",names,ctx)==0);
    for(int i=0;i<7;i++){
        fmpq_mpoly_gen(x,1,ctx);fmpq_mpoly_mul(r[i],q[i],x,ctx);fmpq_mpoly_scalar_mul_si(r[i],r[i],6-2*i,ctx);
        if(i>0){fmpq_mpoly_scalar_mul_si(y,q[i-1],14-2*i,ctx);fmpq_mpoly_add(r[i],r[i],y,ctx);}
        if(i<6){fmpq_mpoly_gen(x,2,ctx);fmpq_mpoly_mul(y,q[i+1],x,ctx);fmpq_mpoly_scalar_mul_si(y,y,-2*(i+1),ctx);fmpq_mpoly_add(r[i],r[i],y,ctx);}
    }
    snprintf(path,sizeof(path),"%s/statistics.tsv",outdir);FILE *stats=fopen(path,"wb");assert(stats);fputs("index\tdelta_exp\tDelta_exp\tK_exp\tdegree\tterms\n",stats);fflush(stats);
    for(int n=0;n<12;n++){
        if(n==0){fmpq_mpoly_mul(raw,q[5],r[6],ctx);fmpq_mpoly_mul(x,q[6],r[5],ctx);fmpq_mpoly_sub(raw,raw,x,ctx);fmpq_mpoly_mul(raw,raw,j,ctx);}
        else if(n<=5)det3(raw,q,prevq,r,n-1,5,6);
        else det3(raw,q,prevq,r,n-6,6,7);
        if(n==1){read_poly(oldfirst,"research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-03-flat-lex-size-probe/raw-generator-1.txt");assert(fmpq_mpoly_equal(raw,oldfirst,ctx));}
        snprintf(label,sizeof(label),"raw-generator-%d",n);write_poly(raw,outdir,label);
        fmpq_mpoly_set(nf,raw,ctx);fmpq_mpoly_one(mult,ctx);int exps[3]={0,0,0};
        if(!fmpq_mpoly_is_zero(nf,ctx)) for(int u=0;u<3;u++) while(fmpq_mpoly_divides(quot,nf,unit[u],ctx)){
            fmpq_mpoly_set(nf,quot,ctx);fmpq_mpoly_mul(mult,mult,unit[u],ctx);exps[u]++;
        }
        fmpq_mpoly_mul(check,nf,mult,ctx);assert(fmpq_mpoly_equal(check,raw,ctx));
        snprintf(label,sizeof(label),"normalized-generator-%d",n);write_poly(nf,outdir,label);
        fprintf(stats,"%d\t%d\t%d\t%d\t%ld\t%ld\n",n,exps[0],exps[1],exps[2],fmpq_mpoly_total_degree_si(nf,ctx),fmpq_mpoly_length(nf,ctx));fflush(stats);
        printf("PASS generator %d, removed only declared units, degree %ld terms %ld\n",n,fmpq_mpoly_total_degree_si(nf,ctx),fmpq_mpoly_length(nf,ctx));fflush(stdout);
    }
    fclose(stats);puts("COMPLETE exact shared 12-generator preparation and first-generator cross-engine binding");
    for(int i=0;i<8;i++){fmpq_mpoly_clear(q[i],ctx);fmpq_mpoly_clear(prevq[i],ctx);fmpq_mpoly_clear(r[i],ctx);}
    for(int i=0;i<3;i++)fmpq_mpoly_clear(unit[i],ctx);
    fmpq_mpoly_clear(j,ctx);fmpq_mpoly_clear(x,ctx);fmpq_mpoly_clear(y,ctx);fmpq_mpoly_clear(raw,ctx);fmpq_mpoly_clear(nf,ctx);fmpq_mpoly_clear(quot,ctx);fmpq_mpoly_clear(mult,ctx);fmpq_mpoly_clear(check,ctx);fmpq_mpoly_clear(oldfirst,ctx);fmpq_mpoly_ctx_clear(ctx);flint_cleanup();return 0;
}
