# 8-Puzzle Problem Solver
[![Build Status](https://travis-ci.org/urastogi885/8-puzzle-problem.svg?branch=master)](https://travis-ci.org/urastogi885/8-puzzle-problem)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/urastogi885/8-puzzle-problem/blob/master/LICENSE)

## Overview

This project implements a solver for the 8-puzzle problem. The goal is to find the minimum number of steps to reach the
final goal of [[1 2 3], [4 5 6], [7 8 0]] from an initial configuration provided by the user. It also checks whether the
given configuration is solvable.

Note that the bank tile is denoted by 0.

## Todo

- Update code to solve an N-puzzle problem
- Add animation to show an automated solution

## Dependencies

- Python3
- Python3-tk
- Python3 Libraries: Numpy

## Install Dependencies

- Install *Python3*, *Python3-tk*, and the necessary libraries: (if not already installed)

````
sudo apt install python3 python3-tk
pip3 install numpy
````

- Check if your system successfully installed all the dependencies
- Open terminal using ````Ctrl+Alt+T```` and enter ````python3````
- The terminal should now present a new area represented by ````>>>```` to enter python commands
- Now use the following commands to check libraries: (Exit python window using ````Ctrl+Z```` if an error pops up while 
running the below commands)

````
import tkinter
import numpy as np
````

## Run

- Using the terminal, clone this repository, go into the project directory, and run the main program:

````
git clone https://github.com/urastogi885/8-puzzle-problem
cd 8-puzzle-problem
python3 main.py 8,6,7,2,5,4,3,0,1
````

- The program will take about 2.5 minutes for the above case. This is one of the most difficult cases for the 8-puzzle
problem. 
- Please note that the *initial configuration* has to be provided as an argument while typing the python command to
execute the solver.
- The *initial configuration* is provided in a row-by-row format.
- The *initial configuration* has to be provided as 9 elements separated by a comma. *DO NOT INCLUDE ANY SPACE AFTER THE
COMMAS*

## Debug

- For an unsolvable test case, the program instantly prints *UNSOLVABLE CONFIG PROVIDED* on the terminal window and
stops running.
- For a solvable test case, exploration time will be printed on the terminal window and path to goal configuration
will be stored in *output_files/nodePath.txt* where first 3 numbers represent the first column and so on.
- The output is stored in column-by-column format.
