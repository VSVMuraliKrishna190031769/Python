#include<stdio.h>
int main(){
    printf("Enter a value ");
    int n=7,i,j;
    scanf("%d",&n);printf("\n");
    for(i=1;i<=n*2-1;i++){
        if(i==n){
            for(j=1;j<=n*2-1;j++){
                printf("+ ");
            }
            printf("\n");
        }
        for(j=1;j<n;j++){
            printf("  ");
        }
        printf("+\n");
    }
    
    return 0;
}
