#!/usr/bin/python3

""" Solve the N queens problem """

import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed on board[row][col]

    Arguments:
    board -- the current state of the chessboard
    row -- the row to check
    col -- the column to check

    Returns:
    True if a queen can be placed at (row, col), False otherwise
    """

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """
    Solve the N queens problem recursively.

    Args:
        board: The N x N chessboard represented as a 2D list.
        col: The current column being processed.
        solutions: A list to store the valid solutions.

    Returns:
        True if a solution is found, False otherwise.
    """
    N = len(board)

    # Base case: If all queens are placed, add the solution
    if col == N:
        # Extract the positions of the queens from the board
        solution = [[i, j] for i in range(N)
                    for j in range(N) if board[i][j] == 1]
        solutions.append(solution)
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            # Place a queen at (row, col)
            board[row][col] = 1

            # Recursively solve for the next column
            solve_nqueens(board, col + 1, solutions)

            # Backtrack by removing the queen from (row, col)
            board[row][col] = 0


def print_solutions(solutions):
    """
    Print all solutions

    Args:
        solutions (list): List of solutions to be printed
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")  # Print the correct usage
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        # Print an error message for invalid input
        print("N must be a number")
        sys.exit(1)

    # Print an error message for N less than 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    board = [[0] * N for _ in range(N)]  # Initialize the chessboard
    solutions = []
    solve_nqueens(board, 0, solutions)  # Find all solutions

    # Print the solutions
    print_solutions(solutions)
