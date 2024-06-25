from methods.check_inputs import CheckMethods
import json
import os
from sympy import * 

class Calculus(CheckMethods): #The logic class necesary for solving easy calculus questions. 

    def __init__(self):
        pass

    def derivative(self):

        checking = CheckMethods('Input your equation : ')
        equation = checking._check_sympy_equation()
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
            equation = checking._check_sympy_equation()
            x=symbols('x')

            solution = integrate(equation,x)

            quick_str_check = str(solution)

            if 'Integral' in quick_str_check:

                print('\nThere is no analytical solution for this function, or the solution is undefiend. ')
                print('\n ---Maybe you inputed a wrong function type -help to see the correct function inputs ! ---')

            else:
                print(f'The solution of  {equation}  : \n \n----{solution} + C ----')
        else : 

            checking = CheckMethods('Input your equation : ')
            equation = checking._check_sympy_equation()
            lower_bound = CheckMethods('Input the lower bound of the integration :')
            if '-infity' in lower_bound.number :
                Lbound = '-oo'

            if 'infity' in lower_bound.number :
                print("Infinit cannot be a lower bound ")
                return ''
            Lbound = lower_bound._check_float()

            uper_bound = CheckMethods('Input the upper bound of the integration :')
            Lbound = '-oo'
            Ubound = 'oo'
                        
            if '-infity' in uper_bound.number :
                print("- Infinit cannot be a upper bound. \nTry inversing the bounds! ")
                return ''

            if 'infity' in uper_bound.number :
                Ubound = 'oo'

            
            Ubound = uper_bound._check_float()

            x=symbols('x')
            solution = integrate(equation,(x,Lbound,Ubound))

            quick_str_check = str(solution)

            if 'Integral' in quick_str_check:

                print('There is no analytical solution for this function, or the solution is undefiend. ')

            else:

                print(f'The solution of ({Lbound},{Ubound}) S {equation}  : \n \n----  {solution} ----')

    def solve_quadratic(self, saves = False):


        if saves == False :

            print('--- you want to solve -----')
            print('--- a*x²+b*x+c = 0 -----')

            a = CheckMethods('Please chose the first parameter a : ')
            first_a = a._check_float()
            b = CheckMethods(' Please chose the second parameter b : ')
            second_b = b._check_float()
            c = CheckMethods(' Please chose the third parameter c : ')            
            third_c = c._check_float()

            h = [None, ';|;'.join(['equation ', 's', 'solutions', '']).split(';')]
            x = Symbol('x')
            t = []
            for e, s in [ ((first_a*x**2 + second_b*x+third_c),x)]:

                how = [{}, dict(dict=True)]

                res = [solve(e, s, **f) for f in how]

                t.append([e, '|', s, '|'] + [ res[1], '|'])
            print('\n')
            print(TableForm(t, headings=h, alignments="<"))

            return e , s 

        else:

            user_choice = CheckMethods('Do you want to see last solution? Yes/No : ')

            if user_choice.number.lower() == 'yes' or user_choice.number.lower() == 'y':

                if os.path.isfile("roots_save.json") and os.access("roots_save.json", os.R_OK):

                    with open ("roots_save.json", "r") as f:
                        previous = json.load(f)

                    print(f"\n {previous['function']} has this solutions {previous['solution']}")

            elif user_choice.number.lower() == 'no' or user_choice.number.lower() == 'n': 

 
                a = CheckMethods('Please chose the first parameter a : ')
                first_a = a._check_float()
                b = CheckMethods(' Please chose the second parameter b : ')
                second_b = b._check_float()
                c = CheckMethods(' Please chose the third parameter c : ')            
                third_c = c._check_float()

                h = [None, ';|;'.join(['equation ', 's', 'solutions', '']).split(';')]
                x = Symbol('x')
                t = []
                the_save = ''
                dictionary = {}

                for e, s in [ ((first_a*x**2 + second_b*x+third_c),x)]:

                    the_save = sympify(e)
                    dictionary['function'] = str(the_save)
                    
                    how = [{}, dict(dict=True)]

                    res = [solve(e, s, **f) for f in how]
                    dictionary["solution"] = str(res[1])
                    t.append([e, '|', s, '|'] + [ res[1], '|'])
                print("\n")
                print(f"----------Here the dictionary {dictionary}--------")
                print("\n")
                json_sols = json.dumps(dictionary)
                with open ("roots_save.json", "w") as f:
                        f.write(json_sols)
                print('\n')
                print(TableForm(t, headings=h, alignments="<"))

                return e , s
            else:
                print("Sorry something wrong happend. Please Check your input")
                print('For this time the function would not be save ! ')

                a = CheckMethods('Please chose the first parameter a : ')
                first_a = a._check_float()
                b = CheckMethods(' Please chose the second parameter b : ')
                second_b = b._check_float()
                c = CheckMethods(' Please chose the third parameter c : ')            
                third_c = c._check_float()

                h = [None, ';|;'.join(['equation ', 's', 'solutions', '']).split(';')]
                x = Symbol('x')
                t = []
                the_save = ''
                dictionary = {}

                for e, s in [ ((first_a*x**2 + second_b*x+third_c),x)]:

                    the_save = sympify(e)
                    dictionary['function'] = str(the_save)
                    
                    how = [{}, dict(dict=True)]

                    res = [solve(e, s, **f) for f in how]
                    dictionary["solution"] = str(res[1])
                    t.append([e, '|', s, '|'] + [ res[1], '|'])


        
                         
            

                

                

        

