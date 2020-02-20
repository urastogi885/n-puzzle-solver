import ast
import puzzle as pzl
from sys import argv

script, start_config = argv


if __name__ == '__main__':
    # Define goal puzzle as list
    goal_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # Convert goal into matrix
    goal_matrix = pzl.convert_into_matrix(goal_list)
    # Get start config and convert it into a matrix
    start_node = ast.literal_eval(start_config)
    puzzle = pzl.Puzzle(start_node, goal_matrix)
    # Print the start config
    print('Initial node:\n', puzzle.initial_puzzle)
    print('Goal node:\n', puzzle.goal)
    # Check solvability of the initial node given by the user
    if not puzzle.check_solvability():
        print('UNSOLVABLE CONFIG GIVEN')
    else:
        print('Final weight for the node:', puzzle.get_final_weight(puzzle.initial_puzzle, 0))
