# Data types, Numbers, Operations, Type conversion, f-strings

print('Welcome to the tip calculator')
bill = float(input('What is the total bill amount: '))
totalperson = int(input('Total number of people: '))
tippercent = int(input('Tip percentage you want to provide? 10 12 15: '))

print(type('max'))

tipamount = bill * tippercent/100
eachpersonpay = (bill+tipamount)/totalperson

print(round(eachpersonpay,2))




twodigitvalue = input('Enter two digit number: ')

firstnum = int(twodigitvalue[0])
secondnum = int(twodigitvalue[1])
total = str(firstnum + secondnum)

print('The sum is ' + total)

height = float(input('Enter your height in meter: '))
weight = int(input('Enter your weight in kg: '))

bmi = round((weight / height ** 2),2)
# function string
print(f'Your BMI is {bmi}') 


print('Lets check your remaining years\n')
age = int(input('Enter your age: '))

remainage = 90 - age

remaindays = remainage * 365
remainweeks = remainage * 52
remainmonth = remainage * 12

print(f'You have {remaindays} days, {remainweeks} weeks and {remainmonth} months left')