class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        for i in range(len(s2)):
            if s2[i] in count:
                temp = count.copy()
                k = i
                while temp and k != len(s2):
                    temp[s2[k]] -= 1
                    if temp[s2[k]] == 0:
                        del temp[s2[k]]
                    k+=1
                if not temp:
                    return True
        return False