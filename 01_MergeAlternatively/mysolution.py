#  RUNTIME: 7ms (beats 97.63%)  MEMORY: 11.76MB (beats 100.00%)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m = ""
        l1 = len(word1)
        l2 = len(word2)
        gl = max([l1, l2])
        c = 0
        while c != gl:
            if c < l1:
                m += word1[c]
            if c < l2:
                m += word2[c]
            c += 1
        return m