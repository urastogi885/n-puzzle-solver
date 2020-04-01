# Import necessary standard libraries
import ast
import numpy as np
from sys import argv
from time import time
# Import custom-built classes
from utils import puzzle as pzl
from utils.node import Node

# Define arguments to run the code
# start_config: a list of numbers representing the start node for the puzzle
script, start_config = argv


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
        # Define start node
        start_node = Node(puzzle.initial_node, puzzle.get_final_weight(puzzle.initial_node, 0), 0, 0, -1, None)
        # Store start node in open and generated nodes list
        puzzle.open_nodes.append(start_node)
        puzzle.generated_nodes.append(start_node)
        # Store start time for exploration
        start_time = time()
        # Start exploration to find goal node
        while len(puzzle.open_nodes):
            # Get the node with lowest weight
            current_node = puzzle.open_nodes.pop()
            # Add current node to closed nodes and delete it from open nodes
            puzzle.closed_nodes.append(current_node)
            # Check if current node is goal node
            if np.all(puzzle.goal_node == current_node.arr):
                break
            # Generate child nodes and iterate through them
            for child_node in current_node.generate_child_nodes():
                node_repeated = False
                # Update final weight of the child node
                child_node.weight = puzzle.get_final_weight(child_node.arr, child_node.level)
                # Check for repetition of child node in closed nodes
                for node in puzzle.closed_nodes:
                    if np.all(node.arr == child_node.arr):
                        node_repeated = True
                        break
                # Append child node to the list of open nodes
                # Do no append child node if repeated
                if not node_repeated:
                    puzzle.open_nodes.append(child_node)
                    puzzle.generated_nodes.append(child_node)
            # Sort the open nodes using their weights
            puzzle.open_nodes.sort(key=lambda x: x.weight, reverse=True)
        # Display exploration time on console/terminal window
        print('Exploration time:', time() - start_time)
        # Generate path and necessary text files
        puzzle.generate_path()
        puzzle.store_nodes_info()
        print('Check moves to reach goal in output_files/nodePath.txt')
