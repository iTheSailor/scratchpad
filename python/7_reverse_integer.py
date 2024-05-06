from icecream import ic

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    upper=pow(2,31)-1
    lower=pow(-2,31)
    ic(upper,lower)
    w=0
    if x>0 or x==0:
        w=1
    y=str(abs(x))
    z=len(y)-1
    q=0
    t=''
    while z>-1:
        t+=y[z]
        z-=1
        ic(t)
    ic(int(t))
    j=int(t)
    if w==0:
        j=j*-1
    ic(j)

reverse(-123)

solution="""class Solution(object):
    def reverse(self, x):
        '
        :type x: int
        :rtype: int
        '
        upper=2**31 -1
        lower=-2**31
        w=0
        if x>0 or x==0:
            w=1
        y=str(abs(x))
        z=len(y)-1
        q=0
        t=''
        while z>-1:
            t+=y[z]
            z-=1
        j=int(t)
        if w==0:
            j=j*-1
        if j<lower or j>upper:
            return 0
        return j
        

Keyword arguments:
argument -- description
Return: return_description
"""
