# Prolog
# Author:  TOAN LE
# Email:  tle153@student.gsu.edu
# Section: 036 CRN 84165
'''
  Purpose:
      convert meters to centimeters, using fact that there are 100 centimeters  in 1 meter
  Pre-conditions (input):
      number of meters (floating point)
  Post-conditions (output):
      number of centimeters, floating point with 2 decimals rounded
'''

def main():
# Design and implementation

#  1.  Output a message to identify the program, and a blank line
    print("Conversion of meters to centimeters")
    print()

#  2.  Input amount of meters from user

    meters = float(input("How many meters? "))

#  3.  Calculate number of centimeters
    # 100 centimeters in 1 meter
    centimeters = meters * 100

#  4. Output resulting inches and given number of feet
    print()
    print(meters, "meters is {:.2f} centimeters".format(centimeters ))

main()
# end of program file
#

#SYNTAX error
'''
1. it was missing a parentheses
2. line 27
    centimeters = meters * 100
    ^
    SyntaxError: invalid syntax
3. added a parentheses to the end of line 23
'''

#SEMANTICS error
'''
4. meters to centimeters has to be multiplied by 100, not add 100. 
5. line 23
6. changed the plus "+" sign to multiply/star "*"
'''
