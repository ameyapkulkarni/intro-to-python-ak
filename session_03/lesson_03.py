# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

# name = input ("What is your name?:");
# if name == "Bob":
#     print ("Welcome " + name + "!");
# else:
#   print ("Who are you stranger?");

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

# name = input ("What is your name?:");
# if name != "Alice":
#   print ("You're not Alice!!");
# else:
#   print ("Welcome " + name + "!");

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
#   If they get it wrong, print "Password failure".

# pwd = input("Please enter password:")
# if pwd == "qwerty123":
#   print("You have successfully logged in")
# else:
#   print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

# number = int(input("Please enter any random number:"))
# if number % 2 == 0:
#   print("Even")
# else:
#   print("Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

# number1 = int(input("Please enter any random number:"))
# number2 = int(input("Please enter any random number:"))

# if number1 + number2 > 21:
#   print("Bust")
# else:
#   print("Safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

# length = int(input("Please enter length of shape:"))
# width = int(input("Please enter width of shape:"))

# if length == width:
#   print("Shape is a square")
# else:
#   print("Shape is not a square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years.
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# current_pay = float(input("Please enter current salary?"))
# yrs_of_service = int(input("Please enter years of active service?"))
# bonus = (0.1 * current_pay)

# if yrs_of_service > 3:
#   print("Congrats!! You're eligible for a Bonus which amounts to £" +
#         str(bonus))
# else:
#   print("Sorry, You're not eligible for a Bonus")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.

# number = int(input("Please enter a number: "))

# if number >= 0:
#   print(str(number**3))
# else:
#   print(str(number / 2))

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob",
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

# name = input("What is your name?:")
# if name == "Alice":
#   print("Hello " + name + "!")
# elif name == "Bob":
#   print("You're not Bob! I'm Bob")
# else:
#   print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

# age = int(input("How old are you?: "))

# if age == 0:
#   print("You're not born yet!")
# elif age < 11:
#   print("You're too young to go to this school")
# elif age >= 11 and age <= 16:
#   print("You can can come to this school")
# else:
#   print("You're too old for school")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

# month = input("Please enter the month: ")

# if month == "March" or month == "April" or month == "May":
#   print(month + " is in Spring")
# else:
#   print("I don't know")

# if month == "March" or month == "April" or month == "May":
#   print(month + " is in Spring")
# elif month == "December" or month == "January" or month == "February":
#   print(month + " is in Winter")
# elif month == "June" or month == "July" or month == "August":
#   print(month + " is in Summer")
# elif month == "September" or month == "October" or month == "November":
#   print(month + " is in Autumn")
# else:
#   print("I don't know")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

# num1 = int(input("Please enter a random number: "))
# num2 = int(input("Please enter another random number: "))

# if num1 % 2 == 0 and num2 % 2 == 0:
#   print("Even")
# elif num1 % 2 != 0 and num2 % 2 != 0:
#   print("Odd")
# else:
#   print(str(num1 * num2))

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

# num1 = int(input("Please enter a random number: "))
# num2 = int(input("Please enter another random number: "))

# if num1 > num2:
#   print(str(num1))
# elif num1 < num2:
#   print(str(num2))
# else:
#   print(str(num1) + " == " + str(num2))

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years,
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years.
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# current_pay = float(input("Please enter current salary? "))
# yrs_of_service = int(input("Please enter years of active service? "))

# if yrs_of_service > 7:
#   print("Congrats!! You're eligible for a Bonus of £" +
#         str(0.20 * current_pay))
# elif yrs_of_service > 5:
#   print("Congrats!! You're eligible for a Bonus of £" +
#         str(0.15 * current_pay))
# elif yrs_of_service >= 3 and yrs_of_service <= 5:
#   print("Congrats!! You're eligible for a Bonus of £" +
#         str(0.10 * current_pay))
# else:
#   print("Sorry, you're not eligible for a Bonus")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest.
#   If all three ages are the same, print that.

# per1 = input("Please enter name of person1: ")
# age1 = int(input("Please enter age of person1: "))

# per2 = input("Please enter name of person2: ")
# age2 = int(input("Please enter age of person2: "))

# per3 = input("Please enter name of person3: ")
# age3 = int(input("Please enter age of person3: "))

# if age1 > age2 and age2 > age3:
#   print(per1 + " is the oldest and they are " + str(age1) + " years old." +
#         per3 + " is the youngest and they are " + str(age3) + " years old.")
# elif age1 > age2 and age3 > age2:
#   print(per1 + " is the oldest and they are " + str(age1) + " years old." +
#         per2 + " is the youngest and they are " + str(age2) + " years old.")
# elif age2 > age1 and age3 > age1:
#   print(per2 + " is the oldest and they are " + str(age2) + " years old." +
#         per1 + " is the youngest and they are " + str(age1) + " years old.")
# elif age2 > age1 and age1 > age3:
#   print(per2 + " is the oldest and they are " + str(age2) + " years old." +
#         per3 + " is the youngest and they are " + str(age3) + " years old.")
# elif age3 > age1 and age1 > age2:
#   print(per3 + " is the oldest and they are " + str(age3) + " years old." +
#         per2 + " is the youngest and they are " + str(age2) + " years old.")
# elif age3 > age1 and age2 > age1:
#   print(per3 + " is the oldest and they are " + str(age3) + " years old." +
#         per1 + " is the youngest and they are " + str(age1) + " years old.")
# else:
#   print("All three people have same ages")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson1 = input("Please enter name of lesson 1: ")
marks1 = int(input("Please enter marks for lesson 1: "))
lesson2 = input("Please enter name of lesson 2: ")
marks2 = int(input("Please enter marks for lesson 2: "))
lesson3 = input("Please enter name of lesson 3: ")
marks3 = int(input("Please enter marks for lesson 3: "))

if marks1 > 80:
  print("Grade A")
elif marks1 < 80 and marks1 >= 60:
  print("Grade B")
elif marks1 < 60 and marks1 >= 50:
  print("Grade C")
elif marks1 < 50 and marks1 >= 45:
  print("Grade D")
elif marks1 < 45 and marks1 >= 25:
  print("Grade E")
elif marks1 < 25:
  print("Grade F")
else:
  print("Oops!! Looks like you didn't get a Grade")


if marks2 > 80:
  print("Grade A")
elif marks2 < 80 and marks2 >= 60:
  print("Grade B")
elif marks2 < 60 and marks2 >= 50:
  print("Grade C")
elif marks2 < 50 and marks2 >= 45:
  print("Grade D")
elif marks2 < 45 and marks2 >= 25:
  print("Grade E")
elif marks2 < 25:
  print("Grade F")
else:
  print("Oops!! Looks like you didn't get a Grade")

if marks3 > 80:
  print("Grade A")
elif marks3 < 80 and marks3 >= 60:
  print("Grade B")
elif marks3 < 60 and marks3 >= 50:
  print("Grade C")
elif marks3 < 50 and marks3 >= 45:
  print("Grade D")
elif marks3 < 45 and marks3 >= 25:
  print("Grade E")
elif marks3 < 25:
  print("Grade F")
else:
  print("Oops!! Looks like you didn't get a Grade")