#include<stdio.h>
void main(){
    int t=4000,w;
    printf("your acc. has %d ",t);
    printf("\nenter amount to withdraw");
    scanf("%d",&w);
    if (w<t){
             if(w%500==0){
            printf("withdrawal successfull");
            t=t-w;
            printf("\nnow acc. blc. is %d",t);
            }
            else {
            printf("u can only withdraw in 500's");
            }
        }
        else{
             printf("insufficient amount");
        }
}
