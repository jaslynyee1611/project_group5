# import Path from pathlib into cash_on_hand.py
from pathlib import Path
# import the csv file
import csv

def COH_function():
    """
    This function will calculate the difference in the cash on hand if cash on hand on the current day 
    is lower than the day before.
    """

    # use Path.cwd() to create a file path to read the cash on hand csv file
    fp_read = Path.cwd() / "csv_reports"/"cash-on-hand-usd.csv"
    # use Path.cwd() to create another file path to write into the summary_report.txt file
    fp_write = Path.cwd() / "summary_report.txt"

    # create two lists, CASH and COH_DAY to store in the extracted data from cash on hand csv file
    CASH = []
    COH_DAY = []

    # open the fp_write file with .open() with mode,"r", to read the cash on hand csv
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # using .reader(), to read the cash on hand csv file
        reader = csv.reader(file)
        next(reader)  # skip header

        # use a for loop for the reader to append the data into each list
        for row in reader:
            # use .append() to append the cash on hand in the csv file in row[1] into the CASH list created
            # use float() to convert value to a float data type 
            CASH.append(float(row[1]))
            # use .append() to append the days in the csv file in row[0] into the COH_DAY list created
            # use float() to convert the value to a float data type
            COH_DAY.append(float(row[0]))

    # assign the variable 'surplus' to 1
    surplus = 1
    # use len to assign the variable 'number_days' to the number of days in the data extracted from COH_DAY list
    number_days = len(COH_DAY)
    # create a range of days excluding 0 so that the code for loop would be 
    # within the range of the 5 days of data extracted
    range_days = range(1, number_days)

    # use a for loop for range_days to compare the cash on hand for the current day and the day before
    for x in range_days:
        # use the if statement to create a condition, to identify the days in which their cash on hand
        # is lower than the day before
        if CASH[x] < CASH[x - 1]:
            # use the subtraction operator '-' to calculate the difference between the identified days
            # assign the difference calculated to the variable 'diff'
            diff = CASH[x - 1] - CASH[x]
            # if the condition is satisfied, the variable 'surplus' will be assigned to 0
            surplus = 0

            # open the fp_write file path with .open() with mode,"a", to append into summary_report.txt
            with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                # use .write() to append the cash deficit with the identified day/s and difference/s
                file.write(f"\n[CASH DEFICIT] DAY: {COH_DAY[x]}, AMOUNT: USD{diff}")

    # using the if statement, if each day's cash on hand value is higher than the day before,
    # surplus will = 1
    # creating the condition, if surplus equates to 1
    if surplus == 1:
        # if condition is satisfied, use .open() with mode, "a", to append into summary_report.txt
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            # use .write() to append the cash surplus with the statement below
            file.write(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
