#  RUNTIME: 11ms (beats 89.98%) MEMORY: 11.68MB (beats 100.00%)
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m = ''
        if not str1 + str2 == str2 + str1:
            return ''
        else:           
            l1, l2 = len(str1), len(str2)
            for n in range(l1, 0, -1):
                if l1 % n == 0 and l2 % n == 0:
                    g = n
                    for i in range(g):
                        m += str2[i]
                    return m
