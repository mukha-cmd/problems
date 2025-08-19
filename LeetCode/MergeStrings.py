class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        min_len = min(len(word1), len(word2))
        counter_1 = 0
        counter_2 = 0
        result = ""
        for i in range(min_len):
            result += word1[i]
            result += word2[i]
        if (len(word1) < len(word2)):
            result += word2[min_len:len(word2)]
        if (len(word2) < len(word1)):
            result += word1[min_len:len(word1)]
        return result
#print(Solution().mergeAlternately("abcd", "pq"))