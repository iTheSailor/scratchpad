from icecream import ic
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    x=0
    l=len(s)
    ic(s)
    n=numRows
    h={i: '' for i in range(0, n)}
    j=0    
    ic(h, h[1], h[j],x, l, s[x])
    k=0
    if n ==1:
        return s
    while x < l:    
        if j==0:
            h[j]+=s[x]
            ic(h)
            k=0
        elif j==n-1:
            h[j]+=s[x]
            k=1
        else:
            h[j]+=s[x]

        if k==0:
            j+=1
        if k==1:
            j-=1
        ic(h,x, s[x],j,h[j],k)
        x+=1
    f=[]
    for key in h:
        f.append(h[key])
    result = ''.join(f)
    ic(result)
    ic('PAHNAPLSIIGYIR')
    return result




s='PAYPALISHIRING'

convert(s=s,numRows=3)


solution="""
class Solution(object):
    def convert(self,s, numRows):
        "
        :type s: str
        :type numRows: int
        :rtype: str
        "
        x = 0
        l = len(s)
        n = numRows
        h = {i: '' for i in range(0, n)}
        j = 0
        k = 0
        if n ==1:
            return s
        while x < l:
            if j == 0:
                h[j] += s[x]
                k = 0
            elif j == n-1:
                h[j] += s[x]
                k = 1
            else:
                h[j] += s[x]
            if k == 0:
                j += 1
            if k == 1:
                j -= 1
            x += 1
        f = []
        for key in h:
            f.append(h[key])
        result = ''.join(f)

        return result
"""