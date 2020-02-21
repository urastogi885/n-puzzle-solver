import numpy as np


def convert_into_matrix(convert_list):
    """
    Convert a list into a 3x3 numpy array
    :param convert_list: list to be converted into matrix
    :return: 3x3 numpy array
    """
    return np.array(convert_list).reshape(3, 3)


def convert_array2str(arr):
    """
    Convert a numpy array into a string with the array's elements separated by spaces
    :param arr: numpy n-D array
    :return: string with elements separated by spaces
    """
    string = ''
    for x in np.nditer(arr):
        string += str(x) + ' '

    # Remove the last unnecessary space
    return string[0:len(string) - 1] + '\n'


class Puzzle:
    def __init__(self, initial_list, goal_node):
        """
        Initialize the puzzle with a start node and final goal node
        :param initial_list: start node provided by the user
        :param goal_node: the pre-decided goal node
        """
        # Store puzzle and goal nodes as class members
        self.initial_list = initial_list
        self.initial_node = convert_into_matrix(self.initial_list)
        self.goal_node = goal_node
        # Define empty lists to store open and closed nodes
        self.open_nodes = []
        self.closed_nodes = []

    def check_solvability(self):
        """
        Check the solvability of the given puzzle config
        :return: Whether the puzzle is solvable
        """
        inversions = 0
        # Iterate through the start node to determine no. of inversions needed
        for i in range(len(self.initial_list) - 1):
            # Check for incorrect elements in the start node
            if self.initial_list[i] not in self.goal_node:
                print('Incorrect elements in the start node')
                return False
            for j in range(i + 1, len(self.initial_list)):
                # Ignore 0 while calculating inversions
                if self.initial_list[j] and self.initial_list[i] and self.initial_list[j] > self.initial_list[i]:
                    inversions += 1
        # If no. of inversions are even, puzzle is solvable
        if inversions % 2 != 0:
            return False

        return True

    def get_heuristic_score(self, node):
        """
        Implement heuristic function for a-star by calculating manhattan distance
        :param: node: current puzzle node under consideration
        :return: manhattan distance
        """
        manhattan_distance = 0

        # for i in range(0, 3):
        #     for j in range(0, 3):
        #         if node[i][j] != self.goal_node[i][j] and node[i][j] != 0:
        #             manhattan_distance += 1

        for x in np.nditer(self.goal_node):
            # Do not evaluate manhattan distance for 0
            if x != 0:
                # Get location of the element in goal and current nodes
                x_index_puzzle = np.where(node == x)
                x_index_goal = np.where(self.goal_node == x)
                # Accumulate the manhattan distance
                manhattan_distance += (abs(x_index_puzzle[0][0] - x_index_goal[0][0]) +
                                       abs(x_index_puzzle[1][0] - x_index_goal[1][0]))

        return manhattan_distance

    def get_final_weight(self, node, node_level):
        """
        Get final weight for a-star
        :param node: 3x3 array of the node
        :param node_level: level of puzzle node
        :return: final weight for a-star
        """
        # Add heuristic value and node level to get the final weight for the current node
        return self.get_heuristic_score(node) + node_level
