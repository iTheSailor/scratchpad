def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    a=0
    z=len(s)-1
    b=0
    x=len(p)-1
    for i in range(0, len(p)):
        for j in range (0, len(s)):
            if a == z or a>z:
                return True
            else:
                if p[b] == s[a] or p[b] == '.':
                    
                    a+=1
                    b+=1
                    if p[x] == s[z] or p[x] == '.':
                        
                        
                        z -=1
                        x -=1
                elif p[b] != s[a] and p[b+1] == '*':
                    a+=1
                elif p[b] == '*':
                    if p[b] != s[a] and s[a] == s[a-1]:
                        a+=1
                    # elif s[a] != s[a-1]
                        
                    
    return False

from icecream import ic

class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        l=len(h)
        a=0
        z=l-1
        r=l-2
        d=min(h[a+1], h[z])
        e=min(h[a], h[z])
        f=min(h[a], h[z-1])
        m = e * r
        ic(sol.storeMax(m))
        ic(m, a, e, h, l)
        if d > e and d > f:
            a+=1
            h = h[a:l]
            sol.maxArea(h)
        if f > e and f > d:
            z-=1
            h=h[:l]
            ic(h)
            sol.maxArea(h)
        


    def storeMax(self, m):
        maximum = 0
        if m > maximum:
            maximum = m

        return maximum




        







height=[1,8,6,2,5,4,8,3,7]
sol = Solution()
sol.maxArea(height)