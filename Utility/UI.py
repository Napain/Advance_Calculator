from Methods.Plots import Plot
from Methods.Calculus import Calculus


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

            # elif user == '-save':
            #     self.any_plot(save=True)
            #     continue
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
            print ('----- 2 : Integral  ---------')
            print ('----- 3 : Cos(x) ---------')
            print ('----- 4 : e^(x) ---------')
            print ('----- 5 : Exit ---------')

            user = input('------Chose your operation here : ')

            if user == '1':
                self.derivative()
            elif user == '2':
                self.Integrals(definitive=True)
                
            elif user == '3':
                print('Note done yet We are sorry')
                print (' -------------------------------------------- \n')
                break
            elif user == '4':
                print('Note done yet We are sorry')
                print (' -------------------------------------------- \n')
                break
            elif user == '5' or user.lower() == 'exit':
                break

            elif user == '-help':
                print("valid numbers {1,2,3,4,5,6,7}\n") 
                print("syntax for function : \n- sin(x)\n- cos(x)\n- exp(x)\n- ln(x)\n- ** = ^ ")
                print("\n save method only save your last equation!")

            # elif user == '-save':
            #     self.any_plot(save=True)
            #     continue
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





