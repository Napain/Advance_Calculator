from sympy import * 


class CheckMethods: #Here you'll find the logic that use the program to make sure the user is not wrong using or giving any input. 

    def __init__(self, the_string):

        self.number = input(the_string)

    def _check_int(self):

        while self.number.isdigit() != True: 

            self.number = input('Please enter positiv integer : ')

        return int(self.number)
        
    def _check_float(self):

        while True:
            try:
                self.number = float(self.number)
                return(self.number)
            except ValueError:
                self.number = input('Please input a number :')

    def _check_zero(self):
        if self.check_int() == 0:
            print ('Error : Division by zero not possible ')
            return False
        else:
            return True

    def _check_eval(self, box):

        valid_operations = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/",".","%"]

        for item in box:
            if item in valid_operations:
                no_E = True
            else :
                print("\nError")
                print('-----------------------------------------------')
                print(" \n To exit or break. Type 'exit' or 'break' ")
                print('\n-----------------------------------------------')
                no_E = False
                break 

        if no_E :
            return eval(box)
        else:
            return False
    
    def _check_sympy_equation (self):


        print('-------------Checking the sympyfication ----------\n ')

                    
        try :

            fct = sympify(self.number)

        except :

            print('You enter an invalid syntax. : type -help for list of function')

            return False
        
        return fct
    


