#!/usr/bin/python3
"""
Solves the N queens puzzle using backtracking.
"""
import sys


def init_board(n):
    """Creates an n x n board filled with 0s."""
    return [[0] * n for _ in range(n)]


def is_safe(board, row, col, n):
    """Checks if a queen can be placed at (row, col)."""
    for i in range(row):
        for j in range(n):
            if board[i][j] == 1 and (
                j == col or
                abs(i - row) == abs(j - col)
            ):
                return False
    return True


def solve(board, row, n, solutions):
    """Recursively attempts to place queens row by row."""
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, solutions)
            board[row][col] = 0


def main():
    """Validates arguments and runs the N queens solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = []
    solve(board, 0, n, solutions)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
