import numpy as np


class Node:
    def __init__(self, puzzle_node, node_weight, node_level, node_index, parent_node_index):
        """
        Initialize node class with start node and weight of the start node
        :param puzzle_node: 3x3 array of the current node
        :param node_weight: final weight of the puzzle node
        :param node_level: level of the node
        :param node_index: index of the node in search tree
        :param parent_node_index: index of the parent node in search tree
        """
        self.node = puzzle_node
        self.weight = node_weight
        self.level = node_level
        self.index = node_index
        self.parent_index = parent_node_index

    def generate_child_nodes(self):
        """
        Generate child nodes from the current node
        :return: a list of all child nodes
        """
        # Define an empty list to store child nodes
        child_nodes = []
        # Get index of zero in the current node
        index_zero = np.where(self.node == 0)
        x, y = index_zero[0][0], index_zero[1][0]
        # Define all the possible actions
        actions = [[x + 1, y]   # Right
                   [x - 1, y]   # Left
                   [x, y + 1]   # Up
                   [x, y - 1]]  # Down
        # Perform each action on the current node to generate child node
        for i in range(len(actions)):
            child = self.get_child(self.node, x, y, actions[i][0], actions[i][1])
            # Check if child node is generated
            if child is not None:
                # Define all the properties of the child node and append to the child nodes' list
                child_node = Node(child, self.level + 1, 0, self.index + i + 1, self.index)
                child_nodes.append(child_node)

        return child_nodes

    def get_child(self, node, x1, y1, x2, y2):
        """
        Get child node
        :param node: current node
        :param x1: initial x-position of 0 in the current node
        :param y1: initial y-position of 0 in the current node
        :param x2: final x-position of 0 in the current node
        :param y2: final y-position of 0 in the current node
        :return: child node
        """
        # Check if new position of 0 are within the array
        if 0 <= x2 < len(self.node) and 0 <= y2 < len(self.node):
            # Make copy of the current node
            child_node = node.copy()
            # Shuffle array to update position 0 and get the child node
            temp = child_node[x2][y2]
            child_node[x2][y2] = child_node[x1][y1]
            child_node[x1][y1] = temp
            return child_node

        return None
