#!/usr/bin/python3
""" `The N queens puzzle`:
     the challenge of placing N non-attacking queens
     on an N×N chessboard.
     Write a program that solves the N queens problem.
"""
import sys


def n_queens(N, row, col, board):
    """ Checking the rowon the left side """
    for x in range(col):
        if board[row][x]:
            return False
    """ checking the diagonal on the lef side """
    for x, y in zip(range(row, -1, -1), (col, -1, -1)):
        if board[x][y]:
            return False
    """ checking the lower diagonal on the left side """
    return all(not board[x][y] for x, y in
        zip(range(row, N), range(col, -1, -1)))

def n_queens_placed(N, board, col, results):
    """ checking if are queens are placed and return True """
    if col == N:
        result = []
        for x in range(N):
            for y in range(N):
                if board[x][y]:
                    result.append([x, y])
        results.append(result)
        return True

    solu = False
    for x in range(N):
        if n_queens(board, x, col, N):
            board[x][col] = 1
            solu = n_queens_placed(N, board, col + 1, results) or solu
            board[x][col] = 0
    return solu


def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    results = []

    if not n_queens_placed(N, board, 0, results):
        return []

    return results

def main():
    #If the user called the program with the wrong number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]

    # Check If N is not an integer
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)

    # Check If N is smaller than 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    results = solve_n_queens(N)

    # Print the results
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
