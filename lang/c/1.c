#include<stdio.h>
void main(){int a=1;
    for(int i=1;i<=5;i++){
            for(int j=i;j<i+i;j++){
              printf(" %d ",a);a++;  
            }
            printf("\n");
    }
}