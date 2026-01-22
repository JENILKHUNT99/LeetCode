class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        SValues={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        for i in range(len(s)-1):
            if SValues[s[i]]<SValues[s[i+1]]:
                result-=SValues[s[i]]
            else:
                result+=SValues[s[i]]
            
        return result+SValues[s[-1]]