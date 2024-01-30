#!/usr/bin/python3
import sys 

def solve_queens(n):
    solutions = []
    cols = set()
    pos_diag = set() 
    neg_diag = set()

    board = [['.'] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy = [''.join(row) for row in board]
            solutions.append(copy)
            return
        
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = '.'

    backtrack(0)
    return solutions

if __name__ == "__main__":
    # Same input validation as previous solution

    n = int(sys.argv[1])
    solutions = solve_queens(n)
    for sol in solutions:
        print(sol)
