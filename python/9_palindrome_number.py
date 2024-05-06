from icecream import ic

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    s=str(x)
    l=len(s)
    r=''
    c=0
    while l > c:
        r+=s[l-1]
        l-=1
    rx=int(r)
    if rx == x:
        
        return True
    return False

x=-41414
ic(isPalindrome(x))

solution="""
class Solution(object):
    def isPalindrome(self, x):
        "
        :type x: int
        :rtype: bool
        "
        if x < 0:
            return False
        s=str(x)
        l=len(s)
        r=''
        c=0
        while l > c:
            r+=s[l-1]
            l-=1
        rx=int(r)
        if rx == x:
            return True
        return False

        """