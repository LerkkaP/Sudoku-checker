class SudokuChecker:
    def __init__(self, sudoku: list):
        self.sudoku = sudoku

    def square_correct(self) -> bool:
        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                square_values = set()
                for i in range(3):
                    for j in range(3):
                        value = self.sudoku[row_offset + i][col_offset + j]
                        if value > 0 and value in square_values:
                            return False
                        square_values.add(value)
        return True

    def column_correct(self) -> bool:
        for col in range(9):
            column_values = set()
            for row in range(9):
                value = self.sudoku[row][col]
                if value > 0 and value in column_values:
                    return False
                column_values.add(value)
        return True

    def row_correct(self) -> bool:
        for row in self.sudoku:
            row_values = set()
            for value in row:
                if value > 0 and value in row_values:
                    return False
                row_values.add(value)
        return True

    def check(self) -> bool:
        return self.square_correct() and self.column_correct() and self.row_correct()

if __name__ == "__main__":
    sudoku1 = [
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

    print(SudokuChecker(sudoku1).check()) 

    sudoku2 = [
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

    print(SudokuChecker(sudoku2).check())
