from utility.ui import ScientificUI
from utility.ui import main_menu
from methods.calculator import MyCalculator

 
First_Object = MyCalculator()
Second_Object = ScientificUI()

if __name__ == '__main__':

    main_menu(First_Object,Second_Object )
        
