class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        indexes = {}
        start = 0
        end = 1
        biggest_substr = 0
        indexes[s[start]] = start
        while end != len(s):
            if s[end] in indexes:
                if end-start > biggest_substr:
                    biggest_substr = end-start
                
                start = max(indexes[s[end]]+1,start)
                
            indexes[s[end]] = end
            end+=1
        
        return biggest_substr if biggest_substr > end-start else end-start
                

        