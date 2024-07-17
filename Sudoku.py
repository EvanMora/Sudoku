class Sudoku:
    def __init__(self, matrix):
        self.data = matrix
        self.colubms = getcols(self.data)
        self.rows = getrows(self.data)
        self.square = []


def getsquare():
    pass


def getcols(matrix):
    colubm = set()
    colubms = []
    for i in range(len(matrix)):
        for row in matrix:
            colubm.add(row[i])
        colubms.append(colubm.copy())
        colubm.clear()
    return colubms

def getrows(matrix):
    for i in range(len(matrix)):
        matrix[i] = set(matrix[i])
    return matrix

if __name__ == '__main__':
    sudoku1 = Sudoku([
        [0, 4, 0, 0, 0, 5, 9, 8, 0],
        [0, 3, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
        [4, 7, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 3, 7, 8, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 9, 3],
        [3, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 5, 0],
        [0, 8, 7, 2, 0, 0, 0, 6, 0],
    ])
    print(sudoku1.colubms)
    print(sudoku1.rows)