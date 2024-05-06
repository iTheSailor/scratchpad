from icecream import ic

class Solution(object):
    def isMatch(self, s, p):
        if not p:
            return not s

        initial = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    (initial and self.isMatch(s[1:], p)))
        else:
            return initial and self.isMatch(s[1:], p[1:])

# Additional examples can be uncommented to test other scenarios
# s='mississippi'
# p='mis*is*ip*.'
# s='aab'
# p='.*'
# s='aaa'
# p='a.a'
# s="bbbba"
# p=".*a*a"
# s='a'
# p='.'
s="aaaaaaaaaaaaaaaaaaab"
p="a*a*a*a*a*a*a*a*a*a*"
ic(Solution().isMatch(s,p))
