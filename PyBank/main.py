import os
import csv

# path for files
#"Resources,"
budget_data_csv = os.path.join('Resources','budget_data.csv')
analysispybank = os.path.join('analysis','analysispybank.txt')

#financial statistics
totalmonths = 0
totalprofits = 0
difference = []
increase = []
decrease = []
current_change = 0
month = [0]
greatest = 0
least = 0

month_year_i = ""
month_year_d = ""


#movement of files & handling
with open (budget_data_csv, "r") as csvreader:
    reader = csv.reader(csvreader,delimiter = ",")
    Header = next(reader)
    firstrow = next(reader)
    totalmonths = totalmonths + 1
    totalprofits = totalprofits + int(firstrow [1])
    previous = int(firstrow[1])
   

    for row in reader:
        totalmonths = totalmonths + 1
        totalprofits = totalprofits + int(row[1])
        current_change = int(row[1]) - previous
        previous = int(row[1])
        difference = difference + [current_change]
        
        if totalmonths == 2:
            greatest = difference
            least = difference
            month_year_i = row[0] + month_year_i
            month_year_d = row[0] + month_year_d
        else:
            if difference > greatest:
                greatest = difference
                month_year_i = str(row[0])

                difference < least
                least = difference
                month_year_d = str(row[0])

average = sum(difference)/len(difference)
increase = max(difference)
decrease = min(difference)


#final output
output= "Financial Analysis\n"
output+="-------------------------------------------\n"
output+=f"Total Months: {totalmonths}\n"
output+=f"Total Profits: ${totalprofits}\n"
output+=f"Average Change: ${average:.2f}\n"
output+=f"Greatest Increase:{month_year_i} ,${increase:.0f}\n"
output+=f"Greatest Decrease: {month_year_d}, ${decrease:.0f}\n"


print(output)

with open (analysispybank, "w") as txtfile:
    txtfile.write(output)