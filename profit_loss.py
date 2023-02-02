## will be used as a module 

# import Path from pathlib 
from pathlib import Path 
# import csv file
import csv
 
def PNL_function():
    """
    The function will help us to calculate the difference in the net profit column 
    if net profit on the current day is lower than the day before.
    """

    # use Path.cwd() to create a file path to read the profit and loss csv file
    fp_read = Path.cwd()/ "csv_reports"/"profit-and-loss-usd.csv"
    # use Path.cwd() again to create another file path to write into the summary_report.txt file
    fp_write = Path.cwd() / "summary_report.txt"

    # create two lists, 'PNL_day' and 'PNL_profit" to store the data extracted from the profit and loss csv file 
    PNL_day = []
    PNL_profit = []

    # open the fp_read file with .open() with mode,"r", to read the profit and loss csv for data extraction
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    
    # use .reader() to read the profit and loss csv file
      reader = csv.reader(file)
      next(reader)  # skip header

      # use a for loop for the reader to append the data into each list
      for row in reader:
        # use .append() to append the days in the csv in row[0] into the PNL_day list created
        # use float() to convert the value to a float data type 
        PNL_day.append(float(row[0]))
        # use .append() to append the net profit in the csv in row[4] into the PNL_profit list created
        # use float() to convert the value to a float data type
        PNL_profit.append(float(row[4]))

    # assign the variable 'surplus' to 1
    surplus = 1
    # use len to assign the variable 'PNL_num_days' to the number of days in the data 
    PNL_num_days = len(PNL_day)
    # create a range of days excluding 0 so that the code for loop would not be out
    # of range
    PNL_range_days = range(1, PNL_num_days)

    # use a for loop for PNL_range_days to compare the profit for current day and the day before 
    for num in PNL_range_days:
      # use the if statement to create a condition, to identify the days in which their net profit
      # is lower than the day before
      if PNL_profit[num] < PNL_profit[num - 1]:
        # if the condition applies, use subtraction operator '-' to calculate the difference of the identified days and
        # assign the differences to the variable 'diff'
        diff = PNL_profit[num - 1] - PNL_profit[num]
        # if the condition is satisfied, the variable 'surplus' will be reassigned to 0
        surplus = 0
        # open the fp_write file path with .open() with mode,"a", to append into summary_report.txt
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            # use .write() to append profit deficit with the identified day/s and difference/s
            file.write(f"\n[PROFIT DEFICIT] DAY: {PNL_day[num]}, AMOUNT: USD{diff}")

    # using the if statement, if each day's net profit is higher than the day before, 
    # surplus will = 1
    # creating the condition, if surplus equates to 1
    if surplus == 1:
      # if condition is satisfied, use .open() with mode, "a", to append into summary_report.txt
      with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
        # use .write() to append the profit surplus with the statement below
        file.write(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

