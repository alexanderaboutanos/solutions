#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to
# be validated according to the following rules:
#
#   1. Each row must contain the digits 1-9 without repetition.
#   2. Each column must contain the digits 1-9 without repetition.
#   3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits
#      1-9 without repetition.
#
# Note: a partially filled board can be valid without being solvable. Only
# the filled cells are checked.
#
# Example 1: the standard partially filled board -> true
# Example 2: same board with board[0][0] = "8"  -> false
#            (two 8s in the top-left 3 x 3 box)
#
# Constraints:
#   board.length == 9
#   board[i].length == 9
#   board[i][j] is a digit 1-9 or '.'.
#
# @lc code=start

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                rowT = ("row", r, d)
                colT = ("col", c, d)
                boxT = ("box", r // 3, c // 3, d)
                if rowT in seen or colT in seen or boxT in seen:
                    return False
                else:
                    seen.update([rowT, colT, boxT])

        return True

# @lc code=end
