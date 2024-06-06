from Methods.check_methods import CheckMethods


class MyCalculator (CheckMethods):

    def __init__(self) :
        pass

    def add(self):
        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1.check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2.check_int()
        print (f"\n {x} + {y} = " , x+y)
        return x+y
    

    def substract(self):
        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1.check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2.check_int()
        print (f"\n {x} - {y} = ", x-y)
        return x-y
    
    def multilpy(self):
        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1.check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2.check_int()
        print (f"\n {x} x {y} = ", x*y)
        return x*y
    
    def divide(self):

        chose_1 = CheckMethods("Chose the first number : ")
        x = chose_1.check_int()
        chose_2 = CheckMethods("Chose the second number : ")
        y = chose_2.check_zero()
        if y == True:
            y = chose_2.check_int()
            print (f"\n {x} / {y} = ", x/y)
        else :
            print("\nError : Division by 0")
    
    def long_calculation(self):

        box = input(" PLease enter your long calculation :  ")
        result = self.check_eval(box) 
        if result :
            print(f"The result of {box} = {result}" )
        

# class scientifque_calculator(Pick):

#     def __init__(self):
#         pass

#     def the_scientific_caculator(self):
#         self.pick_one()



            


