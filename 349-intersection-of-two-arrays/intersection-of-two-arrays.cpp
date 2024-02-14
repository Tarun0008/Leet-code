class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nums3;
         sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        
        nums1.erase(unique(nums1.begin(), nums1.end()), nums1.end());
        nums2.erase(unique(nums2.begin(), nums2.end()), nums2.end());
        for (int i = 0; i < nums1.size(); i++) {
            for (int j = 0; j < nums2.size(); j++) {
                if (nums1[i] == nums2[j]) {
                    nums3.push_back(nums1[i]);
                    break; 
                }
            }
        }
        return nums3;
    }
};
