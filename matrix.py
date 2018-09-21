from pprint import pprint

class matrix():
    '''class for matrix maths input list of lists'''
    def __init__(self, matrix: list):
        self.matrix = matrix
    def dim(self) -> tuple:
        '''returns the dimesions and the validity'''
        i = len(self.matrix[0])
        valid = all(i == len(item) for item in self.matrix)
        j = len(self.matrix)
        return (i, j, valid)
    
    def swapRows(self, row1:int, row2:int):
        t = self.matrix[row1]
        self.matrix[row1] = self.matrix[row2]
        self.matrix[row2] = t
        pass
    def copyRows(self):
        nMatrix = self.matrix
        for row in range(0, len(nMatrix)):
            for i in range(0, len(nMatrix[row]) - 1):
                nMatrix[row].append(nMatrix[row][i])
        return matrix(nMatrix)
    def det2(self) -> float:
        partial1 = 1
        partial2 = 1
        for j in range(0, len(self.matrix)):
            for i in range(0,1):
                partial = partial * self.matrix[i][i]
            
            
        return det
        
    def scaleRow(self, row:int, scalar:float):
        for i in range(0, len(self.matrix[row])):
            self.matrix[row][i] = scalar*self.matrix[row][i]
    
    def addInto(self, row1: int, row2:int):
        for i in range(0, len(self.matrix[row1])):
            self.matrix[row1][i] = self.matrix[row1][i] + self.matrix[row2][i]
    
    def printAll(self):
        for item in self.matrix:
            print(item)
        pass

    def gauss(self):
        A = self.matrix
        n = len(A)

        for i in range(0, n):
            # Search for maximum in this column
            maxEl = abs(A[i][i])
            maxRow = i
            for k in range(i+1, n):
                if abs(A[k][i]) > maxEl:
                    maxEl = abs(A[k][i])
                    maxRow = k

            # Swap maximum row with current row (column by column)
            for k in range(i, n+1):
                tmp = A[maxRow][k]
                A[maxRow][k] = A[i][k]
                A[i][k] = tmp

            # Make all rows below this one 0 in current column
            for k in range(i+1, n):
                c = -A[k][i]/A[i][i]
                for j in range(i, n+1):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]

        # Solve equation Ax=b for an upper triangular matrix A
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = A[i][n]/A[i][i]
            for k in range(i-1, -1, -1):
                A[k][n] -= A[k][i] * x[i]
        return x

