from icecream import ic

class Solution(object):
    def longestCommonPrefix(self, s):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ""
        x = min(s)
        if x == "": return r
        if len(s) == 1:
            return x
        for i in range(len(x)):
            l = x[i]
            for n in range(len(s)):
                if s[n][i] != l:
                    return r
            r += l
        return r

         


s =["flower","flow","flight"]
sol = Solution()
ic(sol.longestCommonPrefix(s))
        