# Library import
from datetime import date
import matplotlib.pyplot as plt
                                

def mainInicial():
    print("################################################")
    print("Welcome to the absenteeism rate calculator!\n ")
    # Greeting
    print("by: Willkommen zum Fehlzeitenrechner\n")
    print("Contrib: Bárbara Cardoso")
    print("################################################\n")


#Input - get a float input
def getInput():
    try:
        input1 = float(input("Please indicate your current absences: "))
        input2 = float(input("Please now enter your current working days: "))
        return calculation(input1,input2)
    except:
        print("Error, please execute again ")


def getDate():
    # Date
    currentDate = date.today()
    return currentDate

# calculation
def calculation(input1, input2):
    output = input1/input2
    output2 = output * 100
    return printOutput(output2)

# Output with 2 decimal places
def printOutput(output2):
    print("Your current absenteeism rate is {:.2f} % on {}".format (((output2)),str(getDate())))
    return graph(output2)


#plot pie graphic
def graph(output2):
    labels = 'Absences', 'Working'
    sizes = [output2, (output2 - 100.00)*-1] # absence % and work %
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    # Create pie plot
    ax1.set_title("Pie graphic absenteeism rate")
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # show
    plt.show()

if __name__ == "__main__":
    mainInicial()
    getInput()

