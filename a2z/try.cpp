    #include<iostream>
using namespace std;
/*
0 1 2 3 4 5 6 7 8 9 10

6 6 6 6 6 6 6 6 6 6 6  0
6 5 5 5 5 5 5 5 5 5 6  1
6 5 4 4 4 4 4 4 4 5 6  2
6 5 4 3 3 3 3 3 4 5 6  3
6 5 4 3 2 2 2 3 4 5 6  4
6 5 4 3 2 1 2 3 4 5 6  5
6 5 4 3 2 2 2 3 4 5 6  6
6 5 4 3 3 3 3 3 4 5 6  7
6 5 4 4 4 4 4 4 4 5 6  8
6 5 5 5 5 5 5 5 5 5 6  9
6 6 6 6 6 6 6 6 6 6 6  10
                                        */
int main(){    
    int n=6;
    
        for(int i=0;i<n;i++){
            int x=n;
            int y=n-i;
                for(int j=0;j<2*n-1;j++){ 
                if(j<n)   { if(i>j){
                        cout<<x<<" ";
                        x--;
                    }
                    else{
                        cout<<x<<" ";
                    }
                }
                else{
                    if (i==(n-1)){
                        cout<<y+1<<" ";
                        y++;
                    }else if((i+j-n)>=n-2){
                        cout<<y<<" ";
                        y++;
                    }
                    else{
                        cout<<y<<" ";
                    }

                }
                }cout<<endl;
                }

        for(int i=0;i<n-1;i++){
            int x=n;
            int y=2+i;
                 for(int j=0;j<2*n-1;j++){ 
                  
                  if(j<n){  
                    if((i+j)<4){
                        cout<<x<<" ";
                        x--;
                    }
                    else{
                        cout<<x<<" ";
                    }
                    }
                    else{
                     if(i<=(j-n)){
                        cout<<y<<" ";
                        y++;
                    }
                    else{
                        cout<<y<<" ";
                    }
                    }

                }cout<<endl;


                }
                return 0;
}     