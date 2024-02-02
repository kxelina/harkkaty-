class Distance:
    '''"Damerau-Levenshtein distance"- algoritmi luokka.'''

    def distance(self, a, b):
        '''Lasketaan kahden sanan (a,b) etäisyys "Damerau-Levenshtein distance"- algoritmillä.'''
        length_a = len(a)
        length_b = len(b)
        matrix = [[0 for j in range(length_b+1)]for i in range(length_a+1)]
        for i in range(0, length_a+1):
            matrix[i][0] = i
        for j in range(0, length_b+1):
            matrix[0][j] = j
        for i in range(1, length_a+1):
            for j in range(1, length_b+1):
                if a[i-1] == b[j-1]:
                    cost = 0
                else:
                    cost = 1
                matrix[i][j] = min(matrix[i-1][j]+1,
                                   matrix[i][j-1]+1,
                                   matrix[i-1][j-1]+cost)
                if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                    matrix[i][j] = min(matrix[i][j],
                                       matrix[i-2][j-2]+1)
        return matrix[length_a][length_b]
