# Simple Calculator Application
import arithmetic_operation_1
import logical_operation_1
import Bitwise_operation_1
import comparison_operation_1
import conversion_operation_1
import identity_operation_1
import algebraic_operation_1
import advanced_arithmetic_1
import string_operation_1
import list_operation_1
import tuple_operation_1
import dictionary_operation_1

def CalculatorMainMenu():
    print("Start Simple Calculator Application")
    print("")
    print("|=======================================|")
    print("| Menu:                                 |")
    print("|=======================================|")
    print("| 1. Arithmetic Calculator              |")
    print("| 2. Logical Operation Calculator       |")
    print("| 3. Comparison Calculator              |")
    print("| 4. Bitwise Operation Calculator       |")
    print("| 5. Identity Operation Calculator      |")
    print("| 6. Conversion Calculator              |")
    print("| 7. Algebraic Calculator               |")
    print("| 8. Advanced Arithmetic Calculator     |")
    print("| 9. String Calculator                  |")
    print("| 10. List Calculator                   |")
    print("| 11. Tuple Calculator                  |")
    print("| 12. Dictionary Calculator             |")
    print("| -1: Quit                              |")
    print("| ======================================|")
    
def GetCalculatorMenu():
    choice = 1
    while choice > 0:
        CalculatorMainMenu()
        choice = int(input("Enter Operation: "))
        if (choice == -1):
            break
        
        if ((choice > 12) or (choice < -1)):
            print("ERROR: Invalid Choice of Operation")
            print("Please Try again")
            choice = 1
            continue
        
        if choice == 1:
            arithmetic_operation_1.GetArithmeticCalculatorMenu()
        elif choice == 2:
            logical_operation_1.GetLogicalCalculatorMenu()
        elif choice == 3:
            comparison_operation_1.GetComparisonCalculatorMenu()
        elif choice == 4:
            Bitwise_operation_1.GetBitwiseCalculatorMenu()
        elif choice == 5:
            identity_operation_1.GetIdentityCalculatorMenu()
        elif choice == 6:
            conversion_operation_1.GetConversionCalculatorMenu()
        elif choice == 7:
            algebraic_operation_1.GetAlgebraicCalculatorMenu()
        elif choice == 8:
            advanced_arithmetic_1.GetAdvancedArithmeticCalculatorMenu()
        elif choice == 9:
            string_operation_1.GetStringCalculatorMenu()
        elif choice == 10:
            list_operation_1.GetListCalculatorMenu()
        elif choice == 11:
            tuple_operation_1.GetTupleCalculatorMenu()
        elif choice == 12:
            dictionary_operation_1.GetDictionaryCalculatorMenu()
        else:
            pass


if __name__ == '__main__':
    GetCalculatorMenu()
    print("End Program: Have a good day")
    print("")

