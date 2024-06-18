from methods.plots import Plot
from methods.calculus import Calculus

def main_menu(My_calculator, Scientific):

        while True :

            print ('\n ------------- Welcome to the simple calculator  -------------')
            print ('----- 1 : Summe ---------')
            print ('----- 2 : Substract ---------')
            print ('----- 3 : Multiple ---------')
            print ('----- 4 : Divide  ---------')
            print ('----- 5 : Long Calculation ---------')
            print ('----- 6 : Enter Scientific Calculator ---------')
            print ('----- 7 : Exit ---------')


            user = input('------Chose your operation here : ')


            if user == '1':
                My_calculator.add()

            elif user == '2' :
                My_calculator.substract()

            elif user == '3' :
                My_calculator.multilpy()

            elif user == '4' :

                My_calculator.divide()
            
            elif user == '5':
                My_calculator.long_calculation()
                
            elif user == '6':
                Scientific.pick_one()

            elif user == '7' or user.lower() == 'exit':
                break
            elif user == '-help':
                print("valid numbers {1,2,3,4,5,6,7}\n") 
                print("syntax for function : \n- sin(x)\n- cos(x)\n- exp(x)\n- ln(x)\n- ** = ^ ")
                print("\n save method only save your last equation!")
            else : 
                print("Please enter a valid input ")



class PLotUI(Plot):

    def __init__(self):
        pass
    
    def pick_plot(self):
        
        while True : 
            print ('\n ------------- Choose your plot!  -------------')
            print ('\n ------------- To save your equation, type -save and -unsave to erase -------------')
            print ('----- 1 : Linear ---------')
            print ('----- 2 : Sin(x) ---------')
            print ('----- 3 : Cos(x) ---------')
            print ('----- 4 : e^(x) ---------')
            print ('----- 5 : Normal distribution  ---------')
            print ('------6: Enter your own plot! ---------')
            print ('----- 7 : Exit ---------')

            user = input('------Chose your operation here : ')

            if user == '1':
                self.plot_linear_graph()
            elif user == '2':
                self.plot_sin()
            elif user == '3':
                self.plot_cos()
            elif user == '4':
                self.euler()
            elif user == '5':
                self.Normal_distribution()
            elif user =='6':
                saves = input('would you like to save the function ? Y or N : ')
                if saves.lower() == 'y' or saves.lower() == 'yes':
                    self.any_plot(save=True)
                elif saves.lower() == 'n' or saves.lower() == 'no':
                    self.any_plot(save=False)
                else:
                    print('Something unexpected happend. Perhaps you input a non valid caracter.')
                    print('The function equation will not be save ')
                    self.any_plot()
            elif user == '7' or user.lower() == 'exit': 
                break
            elif user == '-help':
                print("valid numbers {1,2,3,4,5,6,7}\n") 
                print("syntax for function : \n- sin(x)\n- cos(x)\n- exp(x)\n- ln(x)\n- ** = ^ ")
                print("\n save method only save your last equation!")
            else:
                print("Please enter a valid number {1,2,3,4,5,6,7,8,9} or -help for more info")

class CalculusUI(Calculus):

    def __init__(self):
        pass

    def pick_calculus(self):
        
        while True : 
            print ('\n ------------- Choose your plot!  -------------')
            print ('\n ------------- To save your equation, type -save and -unsave to erase -------------')
            print ('----- 1 : First Derivative ---------')
            print ('----- 2 : Integral without Bounds  ---------')
            print ('----- 3 : Integral with Bounds ---------')
            print ('----- 4 : Solve Cuadratic equation ---------')
            print ('----- 5 : Solve and Save last solution  ---------')
            print ('----- 6 : Exit ---------')

            user = input('------Chose your operation here : ')

            if user == '1':
                self.derivative()
            elif user == '2':
                self.Integrals()
                
            elif user == '3':
                self.Integrals(definitive=True)
            elif user == '4':
                self.solve_quadratic()
            elif user == '5':
                self.solve_quadratic(saves=True)
            elif user == '6' or user.lower() == 'exit':
                break
            elif user == '-help':
                print("valid numbers {1,2,3,4,5,6,7}\n") 
                print("syntax for function : \n- sin(x)\n- cos(x)\n- exp(x)\n- ln(x)\n- ** = ^ ")
                print("\n save method only save your last equation!")
            else:
                print("Please enter a valid number {1,2,3,4,5,6,7,8,9} or -help for more info")

class ScientificUI(CalculusUI, PLotUI):
            
    def __init__(self):
         pass
    
    def pick_one(self ):

        while True :
                print ('\n ------------- Choose your operation !  -------------')
                print ('----- 1 : Plot equations ---------')
                print ('----- 2 : Calculus ---------')
                print ('----- 3 : Exit ---------')


                user = input('------Chose your operation here : ')

                if user == '1':
                    self.pick_plot()
                    break
                elif user == '2':
                    self.pick_calculus()
                    break
                elif user == '3' or user.lower()== 'exit':
                    break
                elif user == '-help':
                    print("valid numbers {1,2,3,4,5,6,7}\n") 
                    print("syntax for function : \n- sin(x)\n- cos(x)\n- exp(x)\n- ln(x)\n- ** = ^ ")
                    print("\n save method only save your last equation!")
                else : 
                    print('Please input a valid option. For more info enter -help')





