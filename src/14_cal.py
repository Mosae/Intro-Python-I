"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.
This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
import sys
import calendar
from datetime import datetime
#receive user input as argument input (we're not going to be usinf the input)
# num_args  = len(sys.argv)
now = datetime.now()
x = input("Enter month and year: ").split(' ')
print(x)
if x[0] == '':
    print(now)
elif x[0] != '':
    print(calendar.month(now.year, int(x[0])))
elif len(x) > 1:
    print(calendar.month(int(x[1]), int(x[0])))
else:
    print('Expects two arguments, month and date')

# #init an instance of the text calendar class
# cal = calendar.TextCalendar()

# #if num of args == 0:
# if num_args = 1:
#   #print current month and year
#   pass
#   # month = datetime.now().month
#   # year = datetime.now().year
#   #we want to print out the month with the calendar
  
# #if user gives one arg:
# elif num_args == 2:
#   #assume args is month
#   month = int(sys.argv[1])
#   year = datetime.now().year
#   #print that month and current year
#   # is user specified 2 args:
# elif num_args == 3:
#   #print that month of the year
#   month = int(sys.argv[1])
#   year = int(sys.argv[2])
#   # otherwise
# else: 
#     print("usage: cal.py [month] [year]")
#     sys.exit(1)


#   cal.prmonth(year, month)