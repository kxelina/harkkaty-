# from entities.trie import Trie

class Distance:
    # def length(self, a, b):
    #     length_a = len(a)
    #     length_b = len(b)
    #     return self.distance(length_a, length_b)

    def distance(self, a, b):
        # if a and b == 0:
        #     return 0
        # if b > 0:
        #     return b
        # return a+b
        length_a = len(a)
        length_b = len(b)
        # if a == 0:
        #     return b
        # if b == 0:
        #     return a
        matrix = [[0 for j in range(length_b+1)]for i in range(length_a+1)]
        # print("aloitus")
        # print(matrix)
        # print(length_a+1)
        for i in range(0, length_a+1):
            # print(i)
            matrix[i][0] = i
        for j in range(0, length_b+1):
            matrix[0][j] = j
        # print(matrix)
        for i in range(1, length_a+1):
            for j in range(1, length_b+1):
                # print(i, j, a[i-1], b[j-1])
                if a[i-1] == b[j-1]:
                    cost = 0
                else:
                    cost = 1
                matrix[i][j] = min(matrix[i-1][j]+1,
                                   matrix[i][j-1]+1,
                                   matrix[i-1][j-1]+cost)
                # print(f"eka:{matrix[i-1][j]+1}-{a[i-2]}-{b[j-1]}")
                # print(f"toinen:{matrix[i][j-1]+1}--{a[i-1]}-{b[j-2]}")
                # print(f"kolmas:{matrix[i-1][j-1]+cost}-{a[i-2]}-{b[j-2]}")
                # print(f"{matrix}-{i}-{j}-{cost}-else-{matrix[i][j]}")
                if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                    matrix[i][j] = min(matrix[i][j],
                                       matrix[i-2][j-2]+1)
                    # print(f"hello- {matrix[i][j]}")
        # print("loppu")
        # print(matrix, length_a, length_b, i, j)
        return matrix[length_a][length_b]
