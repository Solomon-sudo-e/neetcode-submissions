class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> numbers;
        for(int num : nums) {
            if(numbers[num] >= 1) {
                return true;
            }
            numbers[num]++;
        }
        return false;
    }
};
