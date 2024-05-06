from icecream import ic

class Solution(object):
    def intToRoman(self, n):
        """
        :type num: int
        :rtype: str
        """
        r=''
        while n >0:
            if n >= 1000:
                n-=1000
                r+='M'
            elif n >= 900:
                n-=900
                r+='CM'
            elif n >=500:
                n-=500
                r+='D'
            elif n>=400:
                n-=400
                r+='CD'
            elif n>= 100:
                n-=100
                r+='C'
            elif n>=90:
                n-=90
                r+='XC'
            elif n>=50:
                n-=50
                r+='L'
            elif n>=40:
                n-=40
                r+='XL'
            elif n >=10:
                n-=10
                r+='X'
            elif n >=9:
                n-=9
                r+= 'IX'
            elif n >= 5:
                n-=5
                r+='V'
            elif n >=4:
                n-=4
                r+='IV'
            elif n >=1:
                n-=1
                r+='I'
        ic(r)
        return r
        
n=2109
sol = Solution()
sol.intToRoman(n)