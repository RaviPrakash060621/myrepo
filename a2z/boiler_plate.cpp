#include<iostream>
using namespace std;
/*
 0 1 2 3 4  

 2 3 4 5 6  0
 3 3 4 5 6  1
 4 4 4 5 6  2
 5 5 5 5 6  3
 6 6 6 6 6  4
            5                       */
int main(){

int n =6;
        for(int i=0;i<n-1;i++){
            int y=2+i;
                for(int j=0;j<n-1;j++){ 
                    if(i<=j){
                        cout<<y<<" ";
                        y++;
                    }
                    else{
                        cout<<y<<" ";
                    }
                }cout<<endl;
                }
    return 0;
}     