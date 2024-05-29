from datetime import date

#get their name
name=input("What's your name?")

#remove the spaces before and 1st is capital letter
name=name.strip().title()

#now ask 4 their birthdate
print('Hey,', name)
birthdateyear = int(input ("Tell me your birth year:"))
birthdatemonth = int(input("And what's your birthdate month?"))
birthdateday = int(input("Now the exactly day:"))

#get today date
today = date.today()
print("Today is:", today, "and your birthday is:")

#get birthdate - no input treatments yet
print(birthdateyear,birthdatemonth,birthdateday,sep="-")

#use today's date to get their age - wont tell you hasnt born yet
age=(today.year - birthdateyear - ((today.month, today.day) < (birthdatemonth, birthdateday)))

#now print their age
print('So... you are',age,'years old, right?')