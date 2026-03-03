# File:		    mathpuzzle.py
# Author:	    Arturo Menchaca
# Date: 	    02/20/2026
# Description:  Generic program that verifies num1 * num2 = (num1 in reverse order). 
#               Based on math puzzle ABCD * 4 = DCBA.

def reverse_int_to_string_match(origNum, multiplier):
    product = str(origNum*multiplier)
    origNumStr_reversed = str(origNum)[::-1]
    verified = (product == origNumStr_reversed)    
    return verified

print("|---------------------------------------------------------------------------------------------------|")
print("|--  We will now verify if the product of a number and multiplier equates to the number reversed  --|")
print("|---------------------------------------------------------------------------------------------------|")
num1 = input("\nPlease enter a number (e.g. 1234), q to quit: ")
while num1!="q":
    num1 = int(num1)    
    num2 = int(input("Please enter a multiplier: "))

    compare = reverse_int_to_string_match(num1, num2)

    if compare:
        print(f"\n{num1*num2} is {num1} reversed when multiplied by {num2}")
    else:
        print(f"\nThe product of {num1} and {num2} is not a reversed form of {num1}")
    
    num1 = input("\nPlease enter number in the form of ABCD (e.g. 1234), q to quit:  ")