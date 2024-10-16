    #include<iostream>
using namespace std;

/*
****
****
****
****                                                                                                                      */
void p1(int n){
  
for(int i=0;i<n;i++){

    for(int j=0;j<n;j++){
            cout <<"*";
}
cout<<endl;
}
}

/*
* 
* * 
* * *
* * * *
* * * * *                                    */
void p2(int n){
for(int i=0;i<n;i++){
    for(int j=0;j<=i;j++){
            cout <<"*";
}cout <<endl;
}
}     


/*
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5                      */

void p3(int n){ 
for(int i=0;i<n;i++){
    for(int j=0;j<=i;j++){
            cout <<j+1;
}
cout<<endl;
}
}

/*
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5                         */

void p4(int n){ 
for(int i=0;i<n;i++){
    for(int j=0;j<=i;j++){
            cout <<i+1;
}
cout<<endl;
}
}


/*
* * * * * 
* * * * 
* * * 
* * 
*                                                  */

void p5(int n){ 
for(int i=0;i<n;i++){
    for(int j=i;j<n;j++){
            cout <<"*";
}
cout<<endl;
}
}

/*
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1                     */

void p6(int n){ 
for(int i=0;i<n;i++){
    for(int j=i;j<n;j++){
            cout <<j+1;
}
cout<<endl;
}
}

/*
    *     
   ***    
  *****   
 *******  
*********                                   */

void p7(int n){ 
    for(int i=0;i<n;i++){
    for(int j=0;j<n-i-1;j++){
        cout<<" ";
        }
        for(int j=0;j<2*i+1;j++){
            cout <<"*";
        }
            for(int j=0;j<n-i-1;j++){
        cout<<" ";
        }
        cout<<endl;
}
cout<<endl;
}


/*
*********
 *******
  ***** 
   ***    
    *                                       */

void p8(int n){ 
    for(int i=0;i<n;i++){
    for(int j=0;j<i;j++){
        cout<<" ";
        }
        for(int j=0;j<2*(n-i)-1;j++){
            cout <<"*";
        }
            for(int j=0;j<i;j++){
        cout<<" ";
        }
        cout<<endl;
}
cout<<endl;
}
/*
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *                       */

    void p9(int n){ 
    for(int i=0;i<n;i++){
    for(int j=0;j<n-i-1;j++){
        cout<<" ";
        }
        for(int j=0;j<2*i+1;j++){
            cout <<"*";
        }
            for(int j=0;j<n-i-1;j++){
        cout<<" ";
        }
        cout<<endl;
}
    for(int i=0;i<n;i++){
    for(int j=0;j<i;j++){
        cout<<" ";
        }
        for(int j=0;j<2*(n-i)-1;j++){
            cout <<"*";
        }
            for(int j=0;j<i;j++){
        cout<<" ";
        }
        cout<<endl;

}
}

/*  
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *                              */

void p10(int n){ 
for(int i=0;i<n;i++){
    for(int j=0;j<=i;j++){
            cout <<"*";
}
cout<<endl;
}
for(int i=0;i<n-1;i++){
    for(int j=i;j<=n-2;j++){
            cout <<"*";
}
cout<<endl;
}

}

/*
1
01
101
0101
10101
010101                   */

void p11(int n){ 
for(int i=0;i<n;i++){
    for(int j=0;j<=i;j++){
            if ((i+j)%2==0){cout <<1;
            }       
            else{cout <<0;}

}cout<<endl;
}
}



void p11_1(int n){ 
    int start=1;
for(int i=0;i<n;i++) {
    if ((i%2)==0){
        start=1;
    }
    else{
        start=0;
        }
    for(int j=0;j<=i;j++){
            cout <<start;
            start=1-start;
}cout<<endl;
}
}
/*
1          1
12        21
123      321
1234    4321
12345  54321
123456654321
                      */

void p12(int n){ 
for(int i=0;i<n;i++){
    for(int j=0;j<i+1;j++){
            cout <<j+1;
}
    for(int j=0;j<2*(n-1-i);j++){
            cout <<" ";
}
    for(int j=0;j<i+1;j++){
            cout <<i-j+1;
}
cout<<endl;
}
}
/* 
1
2  3
4  5  6
7  8  9  10 
11  12  13  14  15
16  17  18  19  20  21                   */

void p13(int n){
    int c=1;
    for(int i=0;i<n;i++){ 
        for(int j=0;j<i+1;j++){
                cout<<c<<" ";
                c++;
        }cout<<endl;
    }
}

/*
A
A B
A B C
A B C D
A B C D E
A B C D E F               */

void p14(int n){
    
    for(int i=0;i<n;i++){ 
        for(char c='A';c<'A'+i+1;c++){
                cout<<c<<" ";
        } cout<<endl;
    }
}
/*
A B C D E F
A B C D E 
A B C D
A B C
A B
A                         */
void p15(int n){
    
    for(int i=0;i<n;i++){ 
        for(char c='A';c<'A'+(n-i);c++){
                cout<<c<<" ";
        } cout<<endl;
    }
}
/*
A 
B B
C C C
D D D D
E E E E E
F F F F F F
*/
void p16(int n){
    
        for(char c='A';c<'A'+n;c++){
                    for(char d='A';d<c+1;d++){ 
                cout<<c<<" ";
        } cout<<endl;
    }
}
/*
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA
                     */

void p17(int n){
    
        for(int i=0;i<n;i++){
                    for(char d='A';d<'A'+(n-i-1);d++){ 
                cout<<" ";}

                    for(char d='A';d<'A'+i+1;d++){
                cout<<d;}
                if(i>0){
                    for(char d='A'+i-1;d>'A'-1;d--){
                    cout<<d;
                }
                }
                     for(char d='A';d<'A'+(n-i-1);d++){ 
                cout<<" ";}
         cout<<endl;
    }
}

/*       2nd method            */
void p17_1(int n){
    
        for(int i=0;i<n;i++){
                    for(int j=0;j<n-i-1;j++){ 
                cout<<" ";}

                char c='A';
                
                for(int j=0;j<2*(i)+1;j++){    
                cout<<c;
                if(j<i){
                    c++;
                    ;
                }
                else{c--;
                }




        }
                     for(int j=0;j<n-i-1;j++){ 
                cout<<" ";}
         cout<<endl;
    }
}
/*
F
E F
D E F
C D E F
B C D E F
A B C D E F                   */
void p18(int n){
    
        for(int i=0;i<n;i++){
                    for(char c='A'+n-i-1;c<'A'+n-1;c++){ 
                cout<<c<<" ";
    }
        cout<<endl;
}
}

/*
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************                                                        */

void p19(int n){
    
        for(int i=0;i<n;i++){
                for(int j=i;j<n;j++){ 
                cout<<"*";
                }
                for(int j=0;j<2*i;j++){ 
                cout<<" ";
                }
                for(int j=i;j<n;j++){ 
                cout<<"*";
                }
                cout<<endl;
        }
            for(int i=0;i<n;i++){
                for(int j=0;j<=i;j++){ 
                cout<<"*";
                }
                for(int j=0;j<2*(n-i-1);j++){ 
                cout<<" ";
                }
                for(int j=0;j<=i;j++){ 
                cout<<"*";
                }
                cout<<endl;
        }
}


/*
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *
                                       */
void p20(int n){
    
        for(int i=0;i<n;i++){
                for(int j=0;j<=i;j++){ 
                cout<<"*";
                }
                for(int j=0;j<2*(n-i-1);j++){ 
                cout<<" ";
                }
                for(int j=0;j<=i;j++){ 
                cout<<"*";
                }
                cout<<endl;
        }
            for(int i=0;i<n-1;i++){
                for(int j=i;j<n-1;j++){ 
                cout<<"*";
                }
                for(int j=0;j<2*(i+1);j++){ 
                cout<<" ";
                }
                for(int j=i;j<n-1;j++){ 
                cout<<"*";
                }
                cout<<endl;
        }
}
/*
******
*    *
*    *
*    *
*    *
******

                                                */
void p21(int n){
        for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){ 
                if(i==0 || i==n-1){
                cout<<"*";}
                else{
                    if(j==0 || j==n-1){
                        cout<<"*";}
                        else{
                            cout<<" ";
                        }
                }
                }

                cout<<endl;
        }
}

void p21_1(int n){
        for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){ 
                if(i==0 || i==n-1 || j==0 || j==n-1){
                cout<<"*";}
                else{
                            cout<<" ";
                        }
                }cout<<endl;
                }

                
        }

/*
0 1 2 3 4 5 

6 6 6 6 6 6   0
6 5 5 5 5 5   1
6 5 4 4 4 4   2
6 5 4 3 3 3   3
6 5 4 3 2 2   4
6 5 4 3 2 1   5                       */

void p22(int n){
        for(int i=0;i<n;i++){
            int x=n;
                for(int j=0;j<n;j++){ 
                    if(i>j){
                        cout<<x<<" ";
                        x--;
                    }
                    else{
                        cout<<x<<" ";
                    }
                }cout<<endl;
                }
}



/*
 0 1 2 3 4  

 6 6 6 6 6  0
 5 5 5 5 6  1
 4 4 4 5 6  2
 3 3 4 5 6  3
 2 3 4 5 6  4
 2 3 4 5 6  5                       */

void p23(int n){
        for(int i=0;i<n;i++){
            int x=n-i;
                for(int j=0;j<n-1;j++){ 
                    if (i==(n-1)){
                        cout<<x+1<<" ";
                        x++;
                    }else if((i+j)>=n-2){
                        cout<<x<<" ";
                        x++;
                    }
                    else{
                        cout<<x<<" ";
                    }
                }cout<<endl;
                }
}   


/*
6 6 6 6 6 6 6 6 6 6 6 
6 5 5 5 5 5 5 5 5 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 2 1 2 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 5 5 5 5 5 5 5 5 6 
6 6 6 6 6 6 6 6 6 6 6
                                        */
void p24(int n){    
    
//            upper half of pattern   
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

//            lower half of pattern
        for(int i=0;i<n-1;i++){
            int x=n;
            int y=2+i;
                 for(int j=0;j<2*n-1;j++){ 
                  
                  if(j<n){  
                    if((i+j)<n-2){
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
}  


int main(){
int n;
    cout <<"enter value of u : ";
    cin >> n;
// p1(n);
// p2(n);
// p3(n);
// p4(n);
// p5(n);
// p6(n);
// p7(n);
// p8(n);
// p9(n);
// p10(n);
// p11(n);
// p11_1(n);
// p12(n);
// p13(n);
// p14(n);
// p15(n);
// p16(n);
// p17(n);
// p17_1(n);
// p18(n);
// p19(n);
// p20(n);
// p21(n);
// p21_1(n);
// p22(n);
// p23(n);
p24(n);
    return 0;
}                                     
