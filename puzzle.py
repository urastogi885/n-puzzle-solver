import numpy as np


def convert_into_matrix(convert_list):
    return np.array(convert_list).reshape(3, 3)


class Puzzle:
    def __init__(self, puzzle_list, goal_matrix):
        self.puzzle_list = puzzle_list
        self.open_nodes = []
        self.closed_nodes = []
        self.initial_puzzle = convert_into_matrix(self.puzzle_list)
        self.goal = goal_matrix

    def check_solvability(self):
        """
        Check the solvability of the given puzzle config
        :return: Whether the puzzle is solvable
        """
        inversions = 0

        for i in range(len(self.puzzle_list) - 1):
            for j in range(i + 1, len(self.puzzle_list)):
                if self.puzzle_list[j] and self.puzzle_list[i] and self.puzzle_list[j] > self.puzzle_list[i]:
                    inversions += 1

        if inversions % 2 == 0:
            return True

        return False

    def get_heuristic_value(self, puzzle_node):
        """
        Implement heuristic function for a-star by calculating manhattan distance
        :param: puzzle_node: current puzzle node under consideration
        :return: manhattan distance
        """
        manhattan_distance = 0

        for x in np.nditer(self.goal):
            if x != 0:
                x_index_puzzle = np.where(puzzle_node == x)
                x_index_goal = np.where(self.goal == x)
                manhattan_distance += (abs(x_index_puzzle[0][0] - x_index_goal[0][0]) +
                                       abs(x_index_puzzle[1][0] - x_index_goal[1][0]))

        return manhattan_distance

    def get_final_weight(self, puzzle_node, node_level):
        """
        Get final weight for a-star
        :param puzzle_node: current puzzle node under consideration
        :param node_level: level of puzzle node
        :return: final weight for a-star
        """
        return self.get_heuristic_value(puzzle_node) + node_level
