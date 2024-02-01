class Solution {
public:
    int getfirst(vector<int>& nums, int target) {
        int n = nums.size();
        int ans = -1;
        int l = 0, m, h = n - 1;

        while (l <= h) {
            m = l + (h - l) / 2;
            if (nums[m] < target) {
                l = m + 1;
            } else if (nums[m] == target) {
                ans = m;
                h = m - 1;
            } else {
                h = m - 1;
            }
        }

        return ans;
    }

    int getlast(vector<int>& nums, int target) {
        int n = nums.size();
        int ans = -1;
        int l = 0, m, h = n - 1;

        while (l <= h) {
            m = l + (h - l) / 2;
            if (nums[m] < target) {
                l = m + 1;
            } else if (nums[m] == target) {
                ans = m;
                l = m + 1;
            } else {
                h = m - 1;
            }
        }

        return ans;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        int first = getfirst(nums, target);
        int last = getlast(nums, target);
        return {first, last};
    }
};
