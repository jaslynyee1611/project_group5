## will be used as a module 

# import Path from pathlib into overheads.py
from pathlib import Path

# import the csv file
import csv
 
def OVERHD_function():
    """
    the function will find the highest overhead category and generate the name
    of the expense along with the percentage
    """

    # use Path.cwd() to create a file path to read the OVER_val csv file
    fp_read = Path.cwd()/"csv_reports"/"overheads-day-90.csv"
    # use Path.cwd() again to create another file path to write into the summary_report.txt file
    fp_write = Path.cwd() / "summary_report.txt"

    # create two lists, 'OVER_expenses' and 'OVER_val' to store the data extracted from the overheads csv file
    OVER_expenses = []
    OVER_val = []

    # open the fp_write file with .open() with mode,"r", to read the overhead csv file for data extraction
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # use .reader() to read the overheads csv file
        reader = csv.reader(file)
        next(reader)  # skip header

        # use a for loop for the reader to append the data into each list
        for row in reader:
            # use .append() to append the name of expenses in the csv in row[0] into
            # the OVER_expenses list created
            OVER_expenses.append(row[0])
            # use .append() to append the overhead values in the csv in row[1] into
            # the OVER_val list created
            # use float() to convert the value to a float data type 
            OVER_val.append(float(row[1]))

    # use max() to find the highest value in OVER_val and assign it to the variable 'highest_val'
    highest_val = max(OVER_val)

    # use a for loop for enumerate to loop the sequence and their value pairing
    for var in enumerate(OVER_val):
        # use the if statement to create a condition, if the value in OVER_val equates to the highest value
        if var[1] == highest_val:
            # if the condition above is satisfied, name of expense pairing with
            # the value into 'highest_exp' will be assigned
            highest_exp = OVER_expenses[var[0]]
            # open the fp_write file path with .open() with mode,"w", to write and into summary_report.txt
            # since this is the first output, use the mode, "w", to overwrite the existing data in the txt file
            with fp_write.open(mode="w", encoding="UTF8", newline="") as file:
                # use .write() to write the name of the expense 
                # use .upper() to capitalise the name of the expense
                # with the identified highest overhead value next to the name of highest expense 
                file.write(f"[HIGHEST OVERHEADS] {highest_exp.upper()}: {highest_val}%")

