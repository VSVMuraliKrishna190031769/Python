#include <stdio.h>

int main()
{
    int n,i,j,k;
    scanf("%d",&n);int c=0;
    for(i=n;i>0;i--){
        c++;k=0;
        for(j=1;j<n*2;j++){
            if(j>i-1 && j==i+k*2 && k<c){
                printf("*");
                k++;
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}

