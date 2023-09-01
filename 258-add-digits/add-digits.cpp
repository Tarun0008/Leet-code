class Solution {
public:
    int addDigits(int num) {
int z=0;
int c=0;
   func: 
   while(num>0)
      {
      z+=num%10;
      num/=10;
    }
    if(z>9)
    {
    num=z;
    z=0;
    goto func;
    }
     cout<<z;
      return z;
    }
   
};