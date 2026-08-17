#include <stdio.h>
#include <stdlib.h>

void readarray(int a[10][10], int m, int n);
void sum_array(int a[10][10], int b[10][10], int sum[10][10], int m, int n);
void display(int a[10][10], int m, int n);

int main() {
    int a[10][10], b[10][10], sum[10][10], m, n;
    printf("Enter the number of rows: ");
    scanf("%d", &m);
    printf("Enter the number of columns: ");
    scanf("%d", &n);

    printf("Enter elements of first matrix:\n");
    readarray(a, m, n);
    printf("Enter elements of second matrix:\n");
    readarray(b, m, n);

    sum_array(a, b, sum, m, n);

    printf("Sum of the matrices:\n");
    display(sum, m, n);

    return 0;
}

void readarray(int a[10][10], int m, int n) {
    int i, j;
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &a[i][j]);
}

void sum_array(int a[10][10], int b[10][10], int sum[10][10], int m, int n) {
    int i, j;
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            sum[i][j] = a[i][j] + b[i][j];
}

void display(int a[10][10], int m, int n) {
    int i, j;
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++)
            printf("%d ", a[i][j]);
        printf("\n");
    }
}
