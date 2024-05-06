from icecream import ic

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    upper=2**31 -1
    lower=-2**31
    l=len(s)
    j=0
    k='0'
    nums=['0','1','2','3','4','5','6','7','8','9']
    syms=[' ', '+', '-']
    a=1
    flag=True
    for j in range(0,l):
        while flag:
            o=len(k)
            ic(o,l,j)
            if j == l:
                flag=False
            elif s[j] not in nums:
                if s[j] not in syms:
                    print('ding')
                    flag = False
                if o>1:
                    flag=False
                elif s[j] == ' ':
                    j+=1
                elif s[j] == '-' and o==1:
                    a=0
                    k+='0'
                    j+=1
                elif s[j] == '+' and o==1:
                    k+='0'    
                    j+=1
                       
            else:
                k+=s[j]
                j+=1
    j=int(k)
    if a==0:
        j=j*-1
    if j > upper:
        return upper
    if j < lower:
        return lower
    ic(j)
    return j
s=" "
myAtoi(s)

solution="""
class Solution(object):
    def myAtoi(self, s):
        "
        :type s: str
        :rtype: int
        "
        upper=2**31 -1
        lower=-2**31
        l=len(s)
        j=0
        k='0'
        nums=['0','1','2','3','4','5','6','7','8','9']
        syms=[' ', '+', '-']
        a=1
        flag=True
        for j in range(0,l):
            while flag:
                o=len(k)
                if j == l:
                    flag=False
                elif s[j] not in nums:
                    if s[j] not in syms:
                        flag = False
                    if o>1:
                        flag=False
                    elif s[j] == ' ':
                        j+=1
                    elif s[j] == '-' and o==1:
                        a=0
                        k+='0'
                        j+=1
                    elif s[j] == '+' and o==1:
                        k+='0'    
                        j+=1
                        
                else:
                    k+=s[j]
                    j+=1
        j=int(k)
        if a==0:
            j=j*-1
        if j > upper:
            return upper
        if j < lower:
            return lower
        return j
        """