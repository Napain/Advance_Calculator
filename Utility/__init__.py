#This just initilize the UI.
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
            
            else : 
                print("Please enter a valid input ")
