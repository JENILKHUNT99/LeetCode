class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dig = int(''.join(map(str,digits)))+1
        Answer=[int(x) for x in str(dig)]
        return Answer
    