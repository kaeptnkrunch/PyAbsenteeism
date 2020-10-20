# Library import
from datetime import date
import matplotlib.pyplot as plt


def mainInicial():

    # Greeting
    print("################################################")
    print("Welcome to the absenteeism rate calculator!\n ")
    print("This is a simple calculator which helps you visualize your absenteeism")
    print("################################################\n")


# Input - get a float input
def getInput():
    try:
        absent_days = float(input("Please indicate your current absences: "))
        total_days = float(input("Please now enter your current working days: "))

        reasons = ["Sickness/ Medical", "Family emergency", "Home Emergency", "Others"]
        reasons_record = {}
        reason_days = 0
        print("-------------------------------------------------")
        print("Please choose the option for your reason(s)for being absent: ")
        reason = ""
        while reason != "5":

            print("-------------------------------------------------")
            for index, key in enumerate(reasons):
                print("{}.) {}".format(index + 1, key))
            print("5.) Exit")
            print("-------------------------------------------------")
            reason = input("Option number: ")

            if reason != "5":
                days = float(input("Number of days absent: "))
                reason_days += days

                if reason_days > absent_days:
                    raise Exception(
                        "Reason days greater than total days. Please enter appropriate values."
                    )

                reasons_record[reasons[int(reason) - 1]] = (
                    reasons_record.get(reasons[int(reason) - 1], 0) + days
                )

        return calculation(absent_days, total_days, reasons_record)
    except Exception as e:
        print("Error: ", e)
        print("Please try again")


def getDate():
    # Date
    currentDate = date.today()
    return currentDate


# calculation
def calculation(absent_days, total_days, reasons_record):

    absent_days_ratio = absent_days / total_days
    absent_days_percentage = absent_days_ratio * 100

    return printOutput(absent_days_percentage, reasons_record, absent_days)


# Output with 2 decimal places
def printOutput(absent_days_percentage, reasons_record, absent_days):
    print(
        "Your current absenteeism rate is {:.2f} % on {}".format(
            ((absent_days_percentage)), str(getDate())
        )
    )
    return graph(absent_days_percentage, reasons_record, absent_days)


# plot pie graphic
def graph(absent_days_percentage, reasons_record, absent_days):
    labels = "Absences", "Working"
    sizes = [
        absent_days_percentage,
        (100.0 - absent_days_percentage),
    ]  # absence % and work %
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    # Create pie plot
    ax1.set_title("Pie graphic absenteeism rate")
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90,
    )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    if len(reasons_record) != 0:
        # Reasons Pie Chart
        fig2, ax2 = plt.subplots()
        reasons_absent = sum(reasons_record.values())
        if absent_days != reasons_absent:
            reasons_record["Others"] = absent_days - reasons_absent
        sizes = [day / absent_days for day in reasons_record.values()]
        explode = tuple([1 / (i * 10) for i in range(1, len(reasons_record) + 1)])
        ax2.set_title("Reasons for absent days")
        ax2.pie(
            sizes,
            explode,
            labels=reasons_record.keys(),
            autopct="%1.1f%%",
            shadow=True,
            startangle=90,
        )
        ax2.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    # show
    plt.show()


if __name__ == "__main__":
    mainInicial()
    getInput()
