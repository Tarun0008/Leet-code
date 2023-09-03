class Solution {
public:
    int strStr(string haystack, string needle) {
        int l1 = haystack.length();
        int l2 = needle.length();
        int val=0;
        for(int i=0 ; i<l1 ; i++){
            if(needle == haystack.substr(i,l2)){
                 val = i;
                 break;}
            else
                 val = -1;   
        }
        return val;
    }
};