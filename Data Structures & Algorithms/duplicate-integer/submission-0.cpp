class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool dupe = false;
        unordered_map<int, int> numbers;
        for (int num : nums) {
            numbers[num] += 1;
            if (numbers[num] > 1) {
                dupe = true;
                break;
            }
        }
        return dupe;
    }
};
