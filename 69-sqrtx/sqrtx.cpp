class Solution {
public:
    int mySqrt(int x) {
        long long l=0;
        long long m=0;
       long long ans=0,h=x;
         
        
        while(l<=h){
            m=(l+h)/2;
            if(m*m<=x){
                ans=m;
                l=m+1;
            }
            else{
                h=m-1;
            }
        }
            return ans;
    }

};