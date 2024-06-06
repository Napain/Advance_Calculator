from Methods.check_methods import CheckMethods
import numpy as np
from sympy.plotting import plot 
from sympy import * 

class Calculus(CheckMethods):

    def __init__(self):
        pass

    def derivative(self):

        checking = CheckMethods('Input your equation : ')
        equation = checking.check_sympy_equation()
        x=symbols('x')

        solution = diff (equation,x)

        print(f'The solution of {equation} is {solution}')
        
        
    def solve_matrix(self):
        pass

    def solve_non_linear(self):
        pass

