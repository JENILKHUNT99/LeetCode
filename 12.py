class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Roman = ""
        i=0
        N = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        R = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        while num>=0:
           if num>=N[i]:
            Roman+=R[i]
            num-=N[i]
           else:
            i+=1
            if i==13:
                break
        return Roman