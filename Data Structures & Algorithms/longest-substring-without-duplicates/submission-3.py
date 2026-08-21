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
            # print(f"start: {start}, end: {end}, indexes: {indexes}, biggest: {biggest_substr}")
            if s[end] in indexes:
                if end-start > biggest_substr:
                    # print(f"Subtraction: {end} - {start}")
                    biggest_substr = end-start
                
                start = max(indexes[s[end]]+1,start)
                indexes[s[end]] = end
            else:
                indexes[s[end]] = end
            end+=1
        
        return biggest_substr if biggest_substr > end-start else end-start
                

        