import ast
import numpy as np
import puzzle as pzl
from sys import argv
from node import Node

# Define arguments to run the code
# start_config: start node for the puzzle
script, start_config = argv


def store_nodes_info(game):
    """
    function to store information regarding all generated nodes
    :param game: instance of puzzle class
    :return: nothing
    """
    # Open files to store information of nodes
    nodes = open('output_files/Nodes.txt', 'w+')
    nodes_info = open('output_files/NodesInfo.txt', 'w+')
    # Store relevant open nodes information
    for node in game.open_nodes:
        nodes.write(pzl.convert_array2str(node.arr))
        nodes_info.write(str(node.index) + ' ' + str(node.parent_index) + ' 0\n')
    # Store relevant closed nodes information
    for node in game.closed_nodes:
        nodes.write(pzl.convert_array2str(node.arr))
        nodes_info.write(str(node.index) + ' ' + str(node.parent_index) + ' 0\n')
    # Close all files
    nodes.close()
    nodes_info.close()


def generate_path(game):
    """
    Generate path using backtracking
    :param game: instance of puzzle class
    :return: nothing
    """
    # Open files to store information of nodes
    node_path = open('output_files/nodePath.txt', 'w+')
    # Define empty list to store path nodes
    # This list will be used to generate the node-path text file
    path_list = []
    # Get all data for goal node
    closed_node = game.closed_nodes[-1]
    # Append the matrix for goal node
    path_list.append(closed_node.arr)
    # Iterate until we reach the initial node
    while not np.array_equal(closed_node.arr, game.initial_node):
        # Search for parent node in the list of closed nodes
        for node in game.closed_nodes:
            if np.array_equal(node.arr, closed_node.parent_node):
                # Append parent node
                path_list.append(closed_node.parent_node)
                # Update node to search for next parent
                closed_node = node
    # Iterate through the list in reverse order
    # Add path nodes to the text file
    for i in range(len(path_list) - 1, -1, -1):
        node_path.write(pzl.convert_array2str(path_list[i]))


if __name__ == '__main__':
    # Define goal puzzle as list
    goal_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # Convert goal into matrix
    goal_matrix = pzl.convert_into_matrix(goal_list)
    # Get start config and convert it into a matrix
    start_node = ast.literal_eval(start_config)
    # Check if correct no. of elements have been given for the puzzle
    if len(start_node) != 9:
        print('You entered', len(start_node), 'elements for the puzzle!')
        print('Please enter exactly 9 elements each separated by a comma')
        quit()
    puzzle = pzl.Puzzle(start_node, goal_matrix)
    # Print the start config
    print('Initial node:\n', puzzle.initial_node)
    print('Goal node:\n', puzzle.goal_node)
    # Check solvability of the initial node given by the user
    if not puzzle.check_solvability():
        print('UNSOLVABLE CONFIG PROVIDED')
    else:
        print('\n\nSolving...')
        start_node = Node(puzzle.initial_node, puzzle.get_final_weight(puzzle.initial_node, 0), 0, 0, -1, None)
        puzzle.open_nodes.append(start_node)
        while True:
            # Get the node with lowest weight
            current_node = puzzle.open_nodes[0]
            # Add current node to closed nodes and delete it from open nodes
            puzzle.closed_nodes.append(current_node)
            del puzzle.open_nodes[0]
            # Check if current node is goal node
            if np.all(puzzle.goal_node == current_node.arr):
                print('Done')
                break
            # Generate child nodes and iterate through them
            for child_node in current_node.generate_child_nodes():
                node_repeated = False
                # Check for repetition of child node in closed nodes
                for closed_node in puzzle.closed_nodes:
                    if np.array_equal(closed_node.arr, child_node.arr):
                        node_repeated = True
                # Append child node to the list of open nodes
                # Do no append child node if repeated
                if not node_repeated:
                    child_node.weight = puzzle.get_final_weight(child_node.arr, child_node.level)
                    puzzle.open_nodes.append(child_node)
            # Sort the open nodes using their weights
            puzzle.open_nodes.sort(key=lambda x: x.weight, reverse=False)
        # Generate path and necessary text files
        generate_path(puzzle)
        store_nodes_info(puzzle)
