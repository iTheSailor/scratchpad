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