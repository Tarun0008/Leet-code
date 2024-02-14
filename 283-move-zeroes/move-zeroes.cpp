class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int f=0;
        int n=nums.size();
        for (int i=0;i<n;i++)
        {
            if(nums[i]!=0){
                int t=nums[i];
                nums[i]=nums[f];
                nums[f]=t;
                f++;

            }
            cout<<nums[i];
        }
    }
};