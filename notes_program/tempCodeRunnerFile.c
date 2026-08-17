#include<stdio.h>
#include<stdlib.h>
void readarray(int a[10][10],int m,int n);
void sum_array(int a[10][10],int b[10][10],sum[10][10],int m,int n);
int main()
{
    int a[10][10],b[10][10],m,n,sum[10][10];
    printf("enter the number of rows :");
    scanf("%d",&m);
    printf("enter the number of columns :");    
    scanf("%d",&n);
    readarray(a,m,n);
    readarray(b,m,n);
    
    sum_array(a,b,sum,m,n);
    
}
void readarray(int a[10][10],int m,int n)
{
    int i,j;
    printf("enter the elements of the array :");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    
}
void sum_array(int a[10][10],int b[10][10],int m,int n)
{
    
    int i,j,sum=[10][10];
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            sum[i][j]=a[i][j]+b[i][j];
        }
    }
    
}