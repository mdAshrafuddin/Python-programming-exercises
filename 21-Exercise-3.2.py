"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

"""
hour = 0.0
rate = 0.0
pay  = 0.0

inp_hour = input('Enter Hour ')

try:
    hour = float(inp_hour)
except ValueError:
    print('Error, Please enter numeric input')
    quit()
try:
    rate = float('Enter Rate ')
except ValueError:
    print('Error, Please Enter numeric input')

if hour < 40:
    pay = hour * rate
else:
    overTime = hour - 40
    pay = (rate * 40) + (1.5 * rate * overTime)

print(pay)