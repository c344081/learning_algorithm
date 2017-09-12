'''
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]


[
 [ 1, 2, 3 , 4],
 [ 5, 6, 7, 8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        results = []
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                results.append(matrix[rowBegin][i])
            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1):
                results.append(matrix[i][colEnd])
            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    results.append(matrix[rowEnd][i])
            rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    results.append(matrix[i][colBegin])
            colBegin += 1

        return results

matrix =[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

s = Solution()
list = s.spiralOrder(matrix)
print(list)