# 8-Puzzle Problem Solver
[![Build Status](https://travis-ci.org/urastogi885/8-puzzle-problem.svg?branch=master)](https://travis-ci.org/urastogi885/8-puzzle-problem)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/urastogi885/8-puzzle-problem/blob/master/LICENSE)

## Overview

This project implements a solver for the 8-puzzle problem. The goal is to find the minimum number of steps to reach the
final goal of [[1 2 3], [4 5 6], [7 8 0]] from an initial configuration provided by the user. It also checks whether the
given configuration is solvable.

Note that the bank tile is denoted by 0.

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
python3 main.py 6,4,7,8,5,0,3,2,1
````
- The program will display initial and goal nodes, *Solving...* when it starts solving and *Done* after it is finished. 
- Please note that the *initial configuration* has to be provided as an argument while typing the python command to
execute the solver.
- The *initial configuration* has to be provided as 9 elements separated by a comma. *DO NOT INCLUDE ANY SPACE AFTER THE
COMMAS*

