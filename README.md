# Sudoku Checker

Sudoku Checker is a Python class that allows you to validate whether a given Sudoku puzzle is correct according to the rules of Sudoku.

## Introduction

Sudoku is a popular logic-based number-placement puzzle. The objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids (also known as "boxes" or "regions") contains all the digits from 1 to 9 without repetition.

The Sudoku Checker Python class provided here allows you to verify if a given Sudoku puzzle is valid, following the rules of Sudoku. It checks for duplicates in each row, column, and the 3x3 subgrids.

## How to Use

1. Create a 9x9 Sudoku grid as a list of lists (2D list) in your Python script or module.

2. Instantiate the `SudokuChecker` class with the Sudoku grid as the argument.

3. Call the `check()` method of the `SudokuChecker` instance to verify the validity of the Sudoku puzzle.

4. The `check()` method returns `True` if the Sudoku puzzle is valid, and `False` otherwise.

**Example:**

```python
# Create a sample Sudoku grid
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

# Instantiate SudokuChecker with the Sudoku grid
checker = SudokuChecker(sudoku)

# Check if the Sudoku puzzle is valid
is_valid = checker.check()

# Print the result
if is_valid:
    print("The Sudoku puzzle is valid.")
else:
    print("The Sudoku puzzle is invalid.")