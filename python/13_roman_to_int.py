from icecream import ic

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        s += 'f'
        for i in s:
            ic(s, r)
            if s[0] == 'M':
                r+=1000
                s = s[1:]
            elif s[0] == 'C':
                if s[1] == 'M':
                    r+=900
                    s = s[2:]
                elif s[1] == 'D':
                    r+=400
                    s = s[2:]
                else:
                    r+=100
                    s = s[1:]
            elif s[0] == 'D':
                r+=500
                s = s[1:]
            elif s[0]=='X':
                if s[1] == 'C':
                    r+=90
                    s = s[2:]
                elif s[1] == 'L':
                    r+=40
                    s = s[2:]
                else:
                    r+=10
                    s = s[1:]
            elif s[0] == "L":
                r+=50
                s = s[1:]
            elif s[0] == "I":
                if s[1] == "X":
                    r+=9
                    s = s[2:]
                elif s[1] == 'V':
                    r+=4
                    s = s[2:]
                else:
                    s = s[1:]
                    r+=1
            elif s[0] == 'V':
                r+=5
                s = s[1:]
            elif s[0] == 'f':
                ic(r)       
                return r

            

s='MCMXCIV'
sol = Solution()
sol.romanToInt(s)