import ast
import puzzle as pzl
from sys import argv
from node import Node

# Define arguments to run the code
# start_config: start node for the puzzle
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
        print('\n\nSolving...\n\n')
        start_node = Node(puzzle.initial_node, puzzle.get_final_weight(puzzle.initial_node, 0), 0, 0, -1)
        puzzle.open_nodes.append(start_node)
        # Open various files
        node_path = open('output_files/nodePath.txt', 'w+')
        nodes = open('output_files/Nodes.txt', 'w+')
        nodes_info = open('output_files/NodesInfo.txt', 'w+')
        while True:
            # Get current node
            current_node = puzzle.open_nodes[0]
            # Add current node to node path
            node_path.write(pzl.convert_array2str(current_node.node))
            if puzzle.get_heuristic_value(current_node.node) == 0:
                break
            for child_node in current_node.generate_child_nodes():
                if pzl.convert_array2str(child_node.node) not in nodes.readlines():
                    child_node.weight = puzzle.get_final_weight(child_node.node, child_node.level)
                    puzzle.open_nodes.append(child_node)
                else:
                    print(child_node.node)

            puzzle.closed_nodes.append(current_node)
            del puzzle.open_nodes[0]
            puzzle.open_nodes.sort(key=lambda x: x.weight, reverse=False)
            for node in puzzle.open_nodes:
                nodes.write(pzl.convert_array2str(node.node))
                nodes_info.write(str(node.index) + ' ' + str(node.parent_index) + ' 0\n')

        # Close all files
        node_path.close()
        nodes.close()
        nodes_info.close()
