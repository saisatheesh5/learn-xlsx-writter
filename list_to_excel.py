#import required libraries
import xlsxwriter as xw

#creating a list for data
expenses = (["Rent",2000],["Gas",1050],["Food",2500],["Gym",1500])

#creating a workbook and worksheet
workbook = xw.Workbook("expense.xlsx")
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in expenses:
    worksheet.write(row,0,item)
    worksheet.write(row,1,cost)
    row+=1

worksheet.write(row,col,"Total")
worksheet.write(row,col+1, '=SUM(B1:B4)')

workbook.close()
