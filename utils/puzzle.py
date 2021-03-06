import numpy as np


def convert_into_matrix(convert_list: list) -> np.ndarray:
    """
    Convert a list into a 3x3 numpy array
    :param convert_list: list to be converted into matrix
    :return: a square numpy array
    """
    size = int(np.sqrt(len(convert_list)))
    return np.array(convert_list).reshape(size, size)


def get_goal_matrix(size: int) -> np.ndarray:
    """
    Using the size of the puzzle, generate goal matrix
    :param size: an integer indicating size of puzzle
    :return: a square numpy array
    """
    goal_list = [i for i in range(1, size)]
    goal_list.append(0)
    return convert_into_matrix(goal_list)


def convert_array2str(arr: np.ndarray) -> str:
    """
    Convert a numpy array into a string with the array's elements separated by spaces
    :param arr: a numpy N-D array
    :return: string with elements separated by spaces
    """
    string = ''
    # Get length of array
    arr_size = len(arr)
    # Iterate over the array to generate string with columns first
    for i in range(arr_size):
        for j in range(arr_size):
            string += str(arr[j][i]) + ' '

    # Remove the last unnecessary space and add new line character
    return string[0:len(string) - 1] + '\n'


class Puzzle:
    """
    A class to solve given N-puzzle
    """

    def __init__(self, initial_list: list, goal_node: np.ndarray):
        """
        Initialize the puzzle with a start node and final goal node
        :param initial_list: start node provided by the user
        :param goal_node: the pre-decided goal node
        """
        # Store puzzle and goal nodes as class members
        self.initial_list = initial_list
        self.puzzle_length = len(self.initial_list) - 1
        self.initial_node = convert_into_matrix(self.initial_list)
        self.goal_node = goal_node
        # Define empty lists to store open, closed nodes, and generated nodes
        self.open_nodes = []
        self.closed_nodes = []
        self.generated_nodes = []

    def check_solvability(self) -> bool:
        """
        Check the solvability of the given puzzle config
        :return: Whether the puzzle is solvable
        """
        inversions = 0
        # Iterate through the start node to determine no. of inversions needed
        for i in range(self.puzzle_length):
            # Check for incorrect elements in the start node
            if self.initial_list[i] not in self.goal_node:
                print('Incorrect elements in the start node')
                return False
            for j in range(i + 1, len(self.initial_list)):
                # Ignore 0 while calculating inversions
                if self.initial_list[j] and self.initial_list[i] and self.initial_list[i] > self.initial_list[j]:
                    inversions += 1
        # If puzzle length is even and no. of inversions are even, puzzle is solvable
        if self.puzzle_length % 2 == 0:
            if inversions % 2 == 0:
                return True
        # If puzzle length is odd
        else:
            zero_pos = len(self.initial_node) - int(np.where(self.initial_node == 0)[0])
            if zero_pos % 2 == 0 and inversions % 2 != 0:
                return True
            elif zero_pos % 2 != 0 and inversions % 2 == 0:
                return True

        return False

    def get_heuristic_score(self, node: np.ndarray) -> int:
        """
        Implement heuristic function for a-star by calculating manhattan distance
        :param: node: current puzzle node under consideration
        :return: manhattan distance
        """
        manhattan_distance = 0

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

    def get_final_weight(self, node: np.ndarray, node_level: int) -> int:
        """
        Get final weight for a-star
        :param node: 3x3 array of the node
        :param node_level: level of puzzle node
        :return: final weight for a-star
        """
        # Add heuristic value and node level to get the final weight for the current node
        return self.get_heuristic_score(node) + node_level

    def generate_path(self) -> None:
        """
        Generate path using backtracking and store it column-wise in a text file
        :return: nothing
        """
        # Open files to store information of nodes
        node_path = open('output_files/nodePath.txt', 'w+')
        # Define empty list to store path nodes
        # This list will be used to generate the node-path text file
        path_list = []
        # Get all data for goal node
        closed_node = self.closed_nodes[-1]
        # Append the matrix for goal node
        path_list.append(closed_node.arr)
        # Iterate until we reach the initial node
        while not np.all(closed_node.arr == self.initial_node):
            # Search for parent node in the list of closed nodes
            for node in self.closed_nodes:
                if np.all(node.arr == closed_node.parent_node):
                    # Append parent node
                    path_list.append(closed_node.parent_node)
                    # Update node to search for next parent
                    closed_node = node
                    break
        # Iterate through the list in reverse order
        # Add path nodes to the text file
        for j in range(len(path_list) - 1, -1, -1):
            node_path.write(convert_array2str(path_list[j]))

    def store_nodes_info(self) -> None:
        """
        function to store information regarding all generated nodes
        :return: nothing
        """
        # Open files to store information of nodes
        nodes = open('output_files/Nodes.txt', 'w+')
        nodes_info = open('output_files/NodesInfo.txt', 'w+')
        # Store relevant information of all generated nodes
        for generated_node in self.generated_nodes:
            nodes.write(convert_array2str(generated_node.arr))
            nodes_info.write(str(generated_node.index) + ' ' + str(generated_node.parent_index) + ' 0\n')
        # Close all files
        nodes.close()
        nodes_info.close()
