/*
ID: yscript1
LANG: C
TASK: ariprog
*/
#include <stdio.h>
#include <stdlib.h>
#define NDEBUG
#ifdef DEBUG
#define PRINTD(fmt, args...)    fprintf(stderr, fmt, ## args)
#else
#define PRINTD(fmt, args...)    /* Don't do anything in release builds */
#endif
static int comp(const void* p1, const void* p2) {
    int* arr1 = (int*)p1;
    int* arr2 = (int*)p2;
    int diff1 = arr1[1] - arr2[1];
    if (diff1) return diff1;
    return arr1[0] - arr2[0];
}

void main() {
    FILE *fin  = fopen ("ariprog.in", "r");
    FILE *fout = fopen ("ariprog.out", "w");
    int n, m;
    int bisquares[125001], numbers[125001];
    int total = 0;
    int seqs[10001][2];
    int seq_num = 0;

    for(int i=0;i<125001;i++) { bisquares[i] = 0; numbers[i] = 0; }
    /* int n = 21;
    int m = 200; */
    fscanf(fin,"%d",&n);
    fscanf(fin,"%d",&m);
    /* printf("n=%d m=%d\n", n, m); */
    for(int i=0; i<=m; i++)
        for(int j=0; j<=m; j++)
            bisquares[i*i + j*j] = 1;
    
    for(int i=0;i<125001;i++)
    {
        if(bisquares[i]==1) {
            numbers[total] = i;
            total ++;
        }
    }
    for(int i=0; i<total; i++) {
        PRINTD("%d ", numbers[i]);
    }
    PRINTD("\n");
    
    /* printf("total=%d max=%d\n", total, numbers[total-1]); */
    for(int i=0;i< (total-n+1); i++) {
        for(int j=i+1; j<(total-n+2); j++) {
            int gap = numbers[j] - numbers[i];
            PRINTD("number[i]=%d gap=%d i=%d j=%d\n", numbers[i], gap, i, j);
            int next = 2;
            int valid = 1;
            while(next < n) {
                int nn = numbers[i] + next * gap;
                
                if ((nn > 125000) || ( bisquares[nn] == 0)) {
                    valid = 0;
                    break;
                }
                next = next + 1;
            }
            if(valid) {
                /* printf("%d %d\n",numbers[i],gap); */
                seqs[seq_num][0] = numbers[i];
                seqs[seq_num][1] = gap;
                seq_num ++;
            }
        }
    }
    if(seq_num > 0) {
        qsort(seqs, seq_num, 2*sizeof(int), comp);
        for(int i=0; i<seq_num; i++) {
            fprintf(fout,"%d %d\n",seqs[i][0], seqs[i][1]);
        }
    } else {
        fprintf(fout,"NONE\n");
    }
    fclose(fin);
    fclose(fout);
    exit(0);
}