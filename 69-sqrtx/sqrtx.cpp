class Solution {
public:
    int mySqrt(int x) {
       long long ans,h=x,l,m;
         
        
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