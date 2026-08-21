class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        cur_count = Counter(s2[:len(s1)])
        if count == cur_count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            cur_count[s2[l]] -= 1
            cur_count[s2[r]] += 1
            
            if cur_count[s2[l]] == 0:
                del cur_count[s2[l]]
            
            if cur_count == count:
                return True
            l+=1

        return False