def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        bytes(word1)
        bytes(word2)

        m = len(word1)
        n = len(word2)

        data = [[0] * (n + 1) for row in range(m + 1)]

        for q in range(m + 1):
            data[q][0] = q
        for q in range(n + 1):
            data[0][q] = q

        for q in range(1, m + 1):
            ch1 = word1[q - 1]
            for p in range(1, n + 1):
                ch2 = word2[p - 1]
                if ch1 == ch2:
                    temp = 0
                else:
                    temp = 1
                data[q][p] = min(data[q - 1][p] + 1, data[q][p - 1] + 1, data[q - 1][p - 1] + temp)

        return data[m][n]

print minDistance()