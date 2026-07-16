#!/usr/bin/python3
"""
Solves the N queens puzzle on an N x N chessboard.
Usage: nqueens N
"""
import sys


def print_solutions(solutions):
    """Prints the coordinates of the Queens."""
    for solution in solutions:
        formatted = [[i, solution[i]] for i in range(len(solution))]
        print(formatted)


def is_safe(board, row, col):
    """Checks if a queen can be safely placed at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """Backtracking helper to solve N-Queens."""
    if row == n:
        solutions.append(list(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def main():
    """Main execution entrypoint."""
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

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
