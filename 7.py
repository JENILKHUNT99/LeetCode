class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sing = -1 if x<0 else 1
        absvalue = abs(x)
        rev = int(str(absvalue)[::-1])
        
        if rev>2**31 or rev<-2**31:
            return 0

        return sing * rev