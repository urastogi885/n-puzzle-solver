import ast
import numpy as np


def check_solvability(puzzle_list):
    inversions = 0

    for i in range(len(puzzle_list) - 1):
        for j in range(i + 1, len(puzzle_list)):
            if puzzle_list[j] and puzzle_list[i] and puzzle_list[j] > puzzle_list[i]:
                inversions += 1

    print('Inversions =', inversions)

    if inversions % 2 == 0:
        return True

    return False


if __name__ == '__main__':
    # Get the puzzle matrix
    input_str = input("Enter nine numbers in this form: 1,2,3,4,5,6,7,8,0 \n")
    input_list = ast.literal_eval(input_str)
    first_matrix = np.array(input_list).tolist()
    puzzle_matrix = np.array(input_list).reshape(3, 3)
    print(puzzle_matrix)
    # Check its solvability and print it
    print('Puzzle is', 'Solvable' if check_solvability(first_matrix) else 'Not Solvable')
