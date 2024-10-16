//   arr n printing it

// #include<iostream>
// using namespace std ;
// int main(){
//     int a[10]={1,2,3,4,5,6,7,8,9,0};
//     for(int i=0;i<10;i++){
//         cout<<a[i];
//         cout<<endl;
//     }
//     return 0;
// }


// type 2
// #include <iostream>
// using namespace std;

// int main() {
//   int myNumbers[5] = {10, 20, 30, 40, 50};
//   for (int i = 0; i < sizeof(myNumbers) / sizeof(myNumbers[0]); i++) {
//     cout << myNumbers[i] << "\n";
//   }
//   return 0;
// }


// input in arr
// #include<iostream>
// using namespace std;
// int main(){
//     int a[10];
//     for (int i=0;i<10;i++){
//     cout<<"enter "<<i+1<<" element";
//     cin>>a[i];
//     }

//     for(int i=0;i<10;i++)
//        cout<<a[i]<<" ";
//     return 0;

// }

//    sum of arr

// #include<iostream>
// using namespace std;
// int main(){
//     int a[5]={2,4,6,8,-10},sum=0;

//     for(int i=0;i<5;i++){
//         sum=sum + a[i];
//     }
//     cout<<sum;
//     return 0;
// }

// max n min
// #include<iostream>
// using namespace std;
// int main() {
//   int  a[5]={0,3,-5,70,-9},max=a[0],min=a[0];

// for(int i=0;i<5;i++){
// if (min<=a[i]){
//     min=a[i];}

// if(max>=a[i]){
//     max=a[i];
// }

// }
// cout<<"max value in arr  :"<<max;
// cout<<endl;
// cout<<"min value in arr  :"<<min;
// return 0;
// }


//    coping arr

// #include<iostream>
// using namespace std;
// int main() {
// int a[5]={2,3,5,76,8},c[5];
// for (int i=0;i<5;i++){
// c[i]=a[i];

// cout<<c[i]<<" ";
// }
// return 0;
// }


// rev of arr
#include<iostream>
using namespace std;
void rev(int a[],int n){
    int t;
    for(int i=0;i<n/2;i++){
        t=a[i];
        a[i]=a[n-1-i];
        a[n-1-i]=t;
   }
for(int i=0;i<n;i++)
      cout<<a[i]<<" ";

}

int main() {
    int a[5]={1,2,3,4,5};
    int n=sizeof(a)/sizeof (a[0]); 
rev(a,n);
    return 0 ;
} 