# Library import
from datetime import date
                                
# Greeting
print("Welcome to the Absence Calculator\n")

# Input
input1 = input("Please indicate your current absences: ")
input2 = input("Please now enter your current working days: ")

# Date
currentDate = date.today()

# calculation
output = (int(input1))/(int(input2))
output2 = output * 100

# Output
print("Your current absenteeism rate is " + (str(output2)) + " on " + (str(currentDate)))
