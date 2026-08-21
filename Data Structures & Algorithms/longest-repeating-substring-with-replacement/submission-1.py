class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = Counter()
        res = 0
        max_freq = 0
        for i in range(len(s)):
            count[s[i]] += 1
            max_freq = max(count[s[i]], max_freq)

            while (i-l+1)-max_freq > k:
                count[s[l]]-=1
                l+=1
            res = max(res, i-l+1)

        return res