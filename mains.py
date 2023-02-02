# import modules
import filetouch, profit_loss, overheads, cash_on_hand

# use file.touch() to create the summary_report.txt file
filetouch.create("summary_report.txt")

# call the functions from the 3 imported modules 
overheads.OVERHD_function()
cash_on_hand.COH_function()
profit_loss.PNL_function()

