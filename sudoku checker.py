class SudokuChecker():
    def __init__(self, sudoku: list):
        self.sudoku = sudoku

    def square_correct(self, sudoku: list):
        list = []
        column = 0
        row = 0
        border = column + 3
        while True:
            for i in range(0, 9):
                start = sudoku[row][column]
                if start > 0 and start in list:
                    return False
                list.append(start)
                column += 1
                if column == border:
                    column = border - 3
                    row += 1
                if column == 2 and row == 2:
                    if sudoku[2][2] in list and sudoku[2][2] > 0:
                        return False
                    list = []
                    column += 1
                    row = 0
                    border = column + 3
                    continue
                if column == 5 and row == 2:
                    if sudoku[2][5] in list and sudoku[2][5] > 0:
                        return False
                    list = []
                    column += 1
                    row = 0
                    border = column + 3
                    continue
                if column == 2 and row == 5:
                    if sudoku[5][2] in list and sudoku[5][2] > 0:
                        return False
                    list = []
                    column += 1
                    row -= 2
                    border = column + 3
                    continue
                if column == 5 and row == 5:
                    if sudoku[5][5] in list and sudoku[5][5] > 0:
                        return False
                    list = []
                    column += 1
                    row -= 2
                    border = column + 3
                    continue
                if column == 8 and row == 5:
                    if sudoku[5][8] in list and sudoku[5][8] > 0:
                        return False
                    list = []
                    row += 1
                    column = 0
                    border = column + 3
                    continue
                if column == 2 and row == 8:
                    if sudoku[8][2] in list and sudoku[8][2] > 0:
                        return False
                    list = []
                    column += 1
                    row -= 2
                    border = column + 3
                    continue
                if column == 5 and row == 8:
                    if sudoku[8][5] in list and sudoku[8][5] > 0:
                        return False
                    list = []
                    column += 1
                    row -= 2
                    border = column + 3
                    continue
                if column == 8 and row == 2:
                    if sudoku[2][8] in list and sudoku[2][8] > 0:
                        return False
                    list = []
                    row += 1
                    column = 0
                    border = column + 3
                    continue
                if column == 8 and row == 8:
                    if sudoku[8][8] in list and sudoku[8][8] > 0:
                        return False
                    return True

    def column_correct(self, sudoku: list):
        list = []
        columm = 0
        while columm < 9:
            for row in sudoku:
                if row[columm] > 0 and row[columm] in list:
                    return False
                list.append(row[columm])
            if len(list) == 9:
                columm += 1
                list = []
                continue
        return True

    def row_correct(self, sudoku: list):
        list = []
        row = 0
        while row < 9:
            for luku in sudoku[row]:
                if luku > 0 and luku in list:
                    return False
                list.append(luku)
            if len(list) == 9:
                row += 1
                list = []
                continue
        return True

    def check(self, sudoku: list):
        if self.square_correct(sudoku) and self.column_correct(sudoku) and self.row_correct(sudoku):
            return True
        else:
            return False

    def solver(self, sudoku: list):
        pass
    
if __name__ == "__main__":

    sudoku = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]

    print(SudokuChecker(sudoku).check(sudoku))

    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(SudokuChecker(sudoku).check(sudoku))
