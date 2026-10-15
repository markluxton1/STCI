#include <flint/flint.h>
#include <flint/fmpq_mpoly.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Format-only export of the captured normalized generators.  This program
   does not reconstruct generators, divide factors, or perform elimination.
   Its exact FLINT reparse check compares every output to its input in QQ[d,v,w]. */
static fmpq_mpoly_ctx_t ctx;
static const char *names[] = {"deltaPar", "vPar", "wPar"};
typedef struct { ulong e[3]; char *coefficient; } term;

static char *read_text(const char *path, long *size) {
    FILE *in = fopen(path, "rb");
    if (!in) { perror(path); exit(2); }
    assert(fseek(in, 0, SEEK_END) == 0);
    *size = ftell(in); assert(*size >= 0); rewind(in);
    char *s = malloc((size_t)*size + 1); assert(s);
    assert(fread(s, 1, (size_t)*size, in) == (size_t)*size);
    s[*size] = 0; fclose(in); return s;
}

static int lex_desc(const void *aa, const void *bb) {
    const term *a = aa, *b = bb;
    for (int i = 0; i < 3; ++i)
        if (a->e[i] != b->e[i]) return a->e[i] > b->e[i] ? -1 : 1;
    return 0;
}

static void times_power(FILE *out, int variable, ulong exponent) {
    if (!exponent) return;
    fprintf(out, "*%s", names[variable]);
    if (exponent != 1) fprintf(out, "^%lu", exponent);
}

/* Sparse exponent-gap Horner recursion: each coefficient at one level is
   itself a Horner expression in the remaining variables. */
static void emit(FILE *out, const term *terms, slong lo, slong hi, int variable) {
    assert(lo < hi);
    if (variable == 3) {
        assert(hi == lo + 1);
        fprintf(out, "(%s)", terms[lo].coefficient); return;
    }
    slong groups = 1;
    for (slong i = lo + 1; i < hi; ++i)
        groups += terms[i].e[variable] != terms[i - 1].e[variable];
    fputc('(', out);
    for (slong i = 1; i < groups; ++i) fputc('(', out);
    slong start = lo, end = lo + 1;
    while (end < hi && terms[end].e[variable] == terms[start].e[variable]) ++end;
    emit(out, terms, start, end, variable + 1);
    ulong previous = terms[start].e[variable];
    while (end < hi) {
        start = end;
        while (end < hi && terms[end].e[variable] == terms[start].e[variable]) ++end;
        ulong current = terms[start].e[variable];
        assert(previous > current);
        times_power(out, variable, previous - current);
        fputc('+', out);
        emit(out, terms, start, end, variable + 1);
        fputc(')', out);
        previous = current;
    }
    times_power(out, variable, previous);
    fputc(')', out);
}

int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "usage: %s OUTPUT_DIR INPUT_FILE [INPUT_FILE ...]\n", argv[0]); return 1;
    }
    fmpq_mpoly_ctx_init(ctx, 3, ORD_DEGREVLEX);
    fmpq_mpoly_t input, check;
    fmpq_mpoly_init(input, ctx); fmpq_mpoly_init(check, ctx);
    fmpq_t coefficient; fmpq_init(coefficient);
    char path[4096];
    snprintf(path, sizeof(path), "%s/statistics.tsv", argv[1]);
    FILE *stats = fopen(path, "wb"); assert(stats);
    fputs("index\tdegree\tterms\tflat_bytes\thorner_bytes\texact_equal\n", stats);
    for (int index = 0; index < argc - 2; ++index) {
        long flat_size, horner_size;
        char *flat = read_text(argv[index + 2], &flat_size);
        assert(fmpq_mpoly_set_str_pretty(input, flat, names, ctx) == 0);
        free(flat);
        slong count = fmpq_mpoly_length(input, ctx);
        term *terms = malloc((size_t)count * sizeof(term)); assert(terms || !count);
        for (slong i = 0; i < count; ++i) {
            assert(fmpq_mpoly_term_exp_fits_ui(input, i, ctx));
            fmpq_mpoly_get_term_exp_ui(terms[i].e, input, i, ctx);
            fmpq_mpoly_get_term_coeff_fmpq(coefficient, input, i, ctx);
            terms[i].coefficient = fmpq_get_str(NULL, 10, coefficient);
        }
        qsort(terms, (size_t)count, sizeof(term), lex_desc);
        snprintf(path, sizeof(path), "%s/horner-generator-%d.txt", argv[1], index);
        FILE *out = fopen(path, "wb"); assert(out);
        if (count) emit(out, terms, 0, count, 0); else fputs("0", out);
        fputc('\n', out); assert(!ferror(out)); assert(fclose(out) == 0);
        char *horner = read_text(path, &horner_size);
        assert(fmpq_mpoly_set_str_pretty(check, horner, names, ctx) == 0);
        assert(fmpq_mpoly_equal(input, check, ctx)); free(horner);
        slong degree = fmpq_mpoly_total_degree_si(input, ctx);
        fprintf(stats, "%d\t%ld\t%ld\t%ld\t%ld\ttrue\n", index, degree, count, flat_size, horner_size);
        fflush(stats);
        printf("PASS exact format-only Horner equality generator %d degree %ld terms %ld bytes %ld -> %ld\n",
               index, degree, count, flat_size, horner_size); fflush(stdout);
        for (slong i = 0; i < count; ++i) flint_free(terms[i].coefficient);
        free(terms);
    }
    assert(!ferror(stats)); assert(fclose(stats) == 0); fmpq_clear(coefficient);
    fmpq_mpoly_clear(input, ctx); fmpq_mpoly_clear(check, ctx);
    fmpq_mpoly_ctx_clear(ctx); flint_cleanup();
    puts("COMPLETE exact format-only nested Horner export, no generator reconstruction or elimination");
    return 0;
}
