from methods.check_inputs import CheckMethods
import numpy as np
from sympy.plotting import plot 
from sympy import * 
import json
import os

class Plot(CheckMethods): #Need to check the plot any with plot errors

    def __init__(self):
        pass

    def linspace(self):
        first_x = CheckMethods("Please choose the min value of x: ")
        x_min = first_x._check_float()
        second_x = CheckMethods("Please choose the max value of x: ")
        x_max = second_x._check_float()
        return x_min, x_max
    
    def plot_linear_graph(self):

        print('You have chose the linear graph : f(x) = ax+b')
        print('Please enter the values\n')

        x_min, x_max = self.linspace()
        slope = CheckMethods("Please choose the first parameter a :  ")
        a = slope._check_float()
        origin = CheckMethods("Please choose the second paramater b : ")
        b = origin._check_float()        
        x = Symbol('x')
        plot(((a*x+b),(x,x_min,x_max )),line_color = 'red' , title = 'Linear ') 

    def plot_sin(self):

        print('You have chose the linear graph : f(x) = a*sin(x+phi)')
        print('Please enter the values\n')

        x_min, x_max = self.linspace()
        slope = CheckMethods("Please choose the first parameter a :  ")
        a = slope._check_float()
        origin = CheckMethods("Please choose the phase phi of your sin : ")
        b = origin._check_float()
        x = Symbol('x')
        plot(((a*sin(x+b)),(x,x_min,x_max )),line_color = 'red' , title = 'Linear ')

    def plot_cos(self):

        print('You have chose the linear graph : f(x) = a*cos(x+phi)')
        print('Please enter the values\n')

        x_min, x_max = self.linspace()
        slope = CheckMethods("Please choose the first parameter a :  ")
        a = slope._check_float()
        origin = CheckMethods("Please choose the phase phi of your cos: ")
        b = origin._check_float()
        x = Symbol('x')
        plot(((a*cos(x+b)),(x,x_min,x_max )),line_color = 'red' , title = 'Linear ') 

    def euler(self):

        print('You have chose the linear graph : f(x) = a*exp((x-c)/b)')
        print('Please enter the values\n')

        x_min, x_max = self.linspace()
        slope = CheckMethods("Please choose the first parameter a :  ")
        a = slope._check_float()
        variance = CheckMethods('Enter your mean c : ')
        c = variance._check_float()
        origin = CheckMethods("Please choose the parameter b  : ")
        if origin._check_zero():
            b = origin._check_float()
        else :
            return('Error, division by 0')
        
        x = Symbol('x')
        plot((a*exp((x-c)/b)),(x,x_min,x_max ),line_color = 'red' , title = 'Linear ') 


    def Normal_distribution(self):

        print('You have chose the linear graph : f(x) = [1/sigma*sqrt(2pi)]*exp(-(x-mean)²/2*sigma²)')
        print('Please enter the values\n')

        x_min, x_max = self.linspace()

        mean = CheckMethods("Please choose the mean :  ")
        a = mean._check_float()

        sigma = CheckMethods("Please choose the Standar deviation : ")
        if sigma._check_zero():
            b = sigma._check_float()
        else :
            return('Error, division by 0')
        x = Symbol('x')
        division = 1/b*np.sqrt(2*np.pi)
        plot(division*exp(-(np.square(x-a)/2*np.square(b))),(x,x_min,x_max ),line_color = 'red' , title = 'Linear ') 

    def any_plot(self, save = False):

        print('------This plot is going to be printed outside the box -----')        

        if save == True:

            while True :

                new_plot = input('Do youn want to continue with the last function ? Y or N : ')

                if new_plot.lower() == 'y' or new_plot.lower()=='yes':
                    yes = True
                    break
                elif new_plot.lower() == 'n' or new_plot.lower()== 'no':
                    yes = False
                    break
                else :
                    print('Please enter a yes or no ')

            if yes == True :

                if os.path.isfile("fct_plot.json") and os.access("fct_plot.json", os.R_OK):

                    with open ("fct_plot.json", "r") as f:
                        the_fct = json.load(f)
                        print(the_fct, the_fct['function'])
                    print(f'The previous function was {the_fct['function']} -------\n')
                    fct = sympify(the_fct['function'])
                    x_min = the_fct['x_min']
                    x_max = the_fct['x_max']

                    x = symbols('x')
            
                    plot(fct,(x,x_min,x_max) ,line_color = 'red')
                
                else:
                    print('Sorry, it seems there was no previous equation before ')


                    fct = input('input your equation :  ')
                    
                    try :

                        the_fct = fct
                        x_min, x_max = self.linspace()
                        fct = sympify(fct)

                    except :

                        print('You enter an invalid syntax. : type -help for list of function')

                        return False
                    
                    x = Symbol('x')
                    dictionary = {"function" : the_fct , "x_min": x_min, "x_max": x_max }
                    json_plot = json.dumps(dictionary)
                    plot(fct,(x,x_min,x_max), line_color = 'red')
                    
                    with open ("fct_plot.json", "w") as f:
                        f.write(json_plot)

            if yes == False:

                print(' -----------The new equation will be save --------- ')


                checking = CheckMethods('Input your equation : ')
                equation = checking._check_sympy_equation()
                
                function = str(equation)
                print( ":---------------------",equation, ":---------------------")
                x_min, x_max = self.linspace()
                dictionary = {"function" : function , "x_min": x_min, "x_max": x_max }
                json_save = json.dumps(dictionary)
                x = symbols('x') 
                try:
                    plot(equation,(x,x_min,x_max), line_color = 'red')

                    status = True 
                    
                    
                except:
                    print('Something went wrong. You must have inputed a wrong function. Type -help to display a list of function ')
                    print('---------------The function will not be save----------')
                if status == True:
                     with open ("fct_plot.json", "w") as f:
                        f.write(json_save)

        else: 
            
            checking = CheckMethods('Input your equation : ')
            equation = checking._check_sympy_equation()
            function = str(equation)
            if equation != False:
                print( ":---------------------",equation, ":---------------------")
                x_min, x_max = self.linspace()
                x = symbols('x') 
                plot(equation,(x,x_min,x_max), line_color = 'red')
                # try :

            #     fct = sympify(fct)

            # except :

            #     print('You enter an invalid syntax. : type -help for list of function')

            #     return False
             
            # plot(fct, line_color = 'red')

