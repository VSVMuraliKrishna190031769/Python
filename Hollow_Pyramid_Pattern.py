#include <stdio.h>

int main()
{
    int n,i,j,k;
    printf("Enter a value \n");
    scanf("%d",&n);
    for(i=0;i<n-1;i++){
        printf(" ");
    }printf("*\n");
    if(n==1){
        return 0;
    }
    int c=1;
    for(i=n-1;i>1;i--){
        k=0;
        for(j=1;j<n*2;j++){
            if(j>i-1 && (j==i||j==i+c+1) && k<2){
                printf("*");
                k++;
            }
            else{
                printf(" ");
            }
        }
        c+=2;
        printf("\n");
    }
    for(i=0;i<n;i++){
        printf("* ");
    }
    return 0;
}

