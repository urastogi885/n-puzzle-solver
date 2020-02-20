import ast
import random
import puzzle as pzl
from sys import argv

script, start_config = argv


if __name__ == '__main__':
    # Define goal puzzle as list
    goal_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # Convert goal into matrix
    goal_matrix = pzl.convert_into_matrix(goal_list)
    # Get start config and convert it into a matrix
    start_list = ast.literal_eval(start_config)
    puzzle = pzl.Puzzle(start_list)
    # Print the start config
    print(puzzle.puzzle)
    # Check solvability of start config and print it
    print('Puzzle is', 'Solvable' if puzzle.check_solvability() else 'Not Solvable')
