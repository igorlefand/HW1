import datetime
name = input("What is your name? ")
age = int(input ("What is your age? "))
if (age < 0 and age > 120):
    age = input("Something wrong, enter your age(from 0 to 120): ")
year = int(datetime.date.today().year)
birthdayYear = year + 120 - age
print (f"Yours 120's birthday in {birthdayYear}, {name}")