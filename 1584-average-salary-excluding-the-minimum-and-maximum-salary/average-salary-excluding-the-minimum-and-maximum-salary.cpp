class Solution {
public:
    double average(vector<int>& salary) {
      double s=0;
      int x=salary.size();
        sort(salary.begin(),salary.end());
        for(int i=1;i<x-1;i++)
          s+=salary[i];
        return s/(x-2);
        }
};