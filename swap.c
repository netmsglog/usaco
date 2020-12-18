/*
ID: yscript1
LANG: C
TASK: swap
*/
#include <stdio.h>
#include <stdlib.h>
#define DEBUG
#ifdef DEBUG
#define PRINTD(fmt, args...)    fprintf(stderr, fmt, ## args)
#else
#define PRINTD(fmt, args...)    /* Don't do anything in release builds */
#endif

void reverse(int *arr, int start, int end) {
    int t;
    while(start < end) {
        t = arr[start];
        arr[start] = arr[end];
        arr[end] = t;
        start ++;
        end --;
    }
}

void dump_cow(int *cows, int n) {
    for(int i=0; i<n; i++) {
        PRINTD("%d ", cows[i]);
    }
    PRINTD("\n");
}

void main() {
    FILE *fin  = fopen ("swap.in", "r");
    FILE *fout = fopen ("swap.out", "w");
    int cows[101];
    int n, k, a1, a2, b1, b2;
    
    fscanf(fin,"%d %d",&n, &k);
    fscanf(fin,"%d %d",&a1, &a2);
    fscanf(fin,"%d %d",&b1, &b2);

    for(int i=0; i<n; i++)
        cows[i] = i + 1;

    for(int i=0; i<k; i++) {
        reverse(cows, a1-1, a2-1);
        /* dump_cow(cows, n); */
        reverse(cows, b1-1, b2-1);
        /* dump_cow(cows, n); */
    }
    
    dump_cow(cows,n);
    
    fclose(fin);
    fclose(fout);
    exit(0);
}