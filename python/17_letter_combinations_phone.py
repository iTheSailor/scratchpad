from icecream import ic

class Solution(object):
    def letterCombinations(self, d):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if len(d) == 0: return []
        r=['']
        l=len(d)
        i = 0
        for i in d:
            c = []
            for d in r:
                for e in dct[i]:
                    c.append(d+e)
            r = c        
        return r

sol = Solution()
sol.letterCombinations(d='23')