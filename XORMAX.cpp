#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
	    string a,b;
	    cin >> a >> b;
	    int a_1=0,a_0=0,b_0=0,b_1=0;
	    
	    for(int i=0; i<a.length(); i++){
	        if(a[i]=='1'){
	            a_1++;
	        }
	        if(a[i]=='0'){
	            a_0++;
	        }
	        if(b[i]=='1'){
	            b_1++;
	        }
	        if(b[i]=='0'){
	            b_0++;
	        }
	       
	    }
	   
	   int max = min(a_1,b_0)+min(a_0,b_1);
	   
	   for(int i=0; i<a.length(); i++){
	       if(i<max){
	           cout<<"1";
	       }
	       else{
	           cout << "0";
	       }
	   }cout<<endl;
	    
	}
	return 0;
}
