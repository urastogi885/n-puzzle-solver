import numpy as np


def convert_into_matrix(convert_list):
    return np.array(convert_list).reshape(3, 3)


class Puzzle:
    def __init__(self, puzzle_list):
        self.puzzle_list = puzzle_list
        self.open_nodes = []
        self.closed_nodes = []
        self.puzzle = convert_into_matrix(self.puzzle_list)

    def check_solvability(self):
        inversions = 0

        for i in range(len(self.puzzle_list) - 1):
            for j in range(i + 1, len(self.puzzle_list)):
                if self.puzzle_list[j] and self.puzzle_list[i] and self.puzzle_list[j] > self.puzzle_list[i]:
                    inversions += 1

        print('Inversions =', inversions)

        if inversions % 2 == 0:
            return True

        return False

