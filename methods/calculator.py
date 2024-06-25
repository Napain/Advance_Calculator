import os
import json
from methods.check_inputs import CheckMethods


class MyCalculator (CheckMethods): #The foundation of the project. The 5 initial methods for the calculator to function. 

    def __init__(self) :
        pass

    def add(self):
        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1._check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2._check_int()
        print (f"\n {x} + {y} = " , x+y)
        return x+y
    

    def substract(self):
        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1._check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2._check_int()
        print (f"\n {x} - {y} = ", x-y)
        return x-y
    
    def multilpy(self):
        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1._check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2._check_int()
        print (f"\n {x} x {y} = ", x*y)
        return x*y
    
    def divide(self):

        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1._check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2._check_zero()
        if y == True:
            y = chose_2._check_int()
            print (f"\n {x} / {y} = ", x/y)
        else :
            print("\nError : Division by 0")
    
    def long_calculation(self):

        print('-----------------------------------------------')
        print(" \n To exit or break. Type 'exit' or 'break' ")
        print('\n-----------------------------------------------')


        while True :
                         
            if os.path.isfile("fct_save.json") and os.access("fct_save.json", os.R_OK):

                with open ("fct_save.json", "r") as f:
                    previous = json.load(f)
        
                print ( previous['previous'], end= '')
                    
                next_box = CheckMethods(' ')
                
                if 'exit' in next_box.number.lower() or 'break' in next_box.number.lower():
                    
                    break
                
                next_box.number = previous['previous']  + next_box.number 

                try:            
                    result = self._check_eval(next_box.number) 

                except :
                    print('\n Error. division by 0 or wrong syntax')
                    break
            
                if result != False :
                
                    results = {"previous" : str(result) }
                    json_save = json.dumps(results)
                    with open ("fct_save.json", "w") as f:
                        f.write(json_save)

                if result == 0 or result == 0.0:

                    results = {"previous" : str(0.0) }
                    json_save = json.dumps(results)
                    with open ("fct_save.json", "w") as f:
                        f.write(json_save)
                        
                elif result == False :
                    
                    print('An unexpected error happenned. Please check your input ')
                    break
                        
            else :
                
                box = input(" PLease enter your long calculation :  ")
                result = self._check_eval(box) 
                
                if result :
                    print(f"The result of {box} = {result}" )
                            
                    print( result )
                    results = {"previous" : str(result) }
                    json_save = json.dumps(results)
                    with open ("fct_save.json", "w") as f:
                        f.write(json_save)
                        
                else:
                    
                    print('An unexpected error happenned. Please check your input ')
                    break
        


            


