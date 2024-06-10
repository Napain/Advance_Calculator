from Methods.Check_inputs import CheckMethods
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

        quick_str_check = str(solution)

        if 'Derivative' in quick_str_check:

            print('There is no analytical solution for this function. ')


        else:
            print(f'''The solution of     d( {equation})     =      {solution}
                 ----------                
                    dx ''')
        
        
    def Integrals(self, definitive = False):


        if definitive == False:

            checking = CheckMethods('Input your equation : ')
            equation = checking.check_sympy_equation()
            x=symbols('x')

            solution = integrate(equation,x)

            quick_str_check = str(solution)

            if 'Integral' in quick_str_check:

                print('There is no analytical solution for this function, or the solution is undefiend. ')

            else:
                print(f'The solution of  {equation}  : \n \n----{solution} + C ----')
        else : 

            checking = CheckMethods('Input your equation : ')
            equation = checking.check_sympy_equation()
            lower_bound = CheckMethods('Input the lower bound of the integration :')
            uper_bound = CheckMethods('Input the upper bound of the integration :')
            Lbound = lower_bound.check_bounds()
            Ubound = uper_bound.check_bounds()
            
            if Ubound == False or Lbound == False:
                print('\nError')
                return ''

            x=symbols('x')
            solution = integrate(equation,(x,Lbound,Ubound))
            quick_str_check = str(solution)

            if 'Integral' in quick_str_check:

                print('There is no analytical solution for this function, or the solution is undefiend. ')

            else:
                print(f'The solution of  {equation}  : \n \n----{solution} ----')

    def solve_non_linear(self):
        pass

