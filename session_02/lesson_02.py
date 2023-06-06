#Section A
## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable.
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.

#Define variables
# var_width = input ("What is the width of the rectangle?");
# var_height = input ("What is the height of the rectangle?");
# var_area = float(var_width) * float(var_height);

# print ("The area of your rectangle is: " + str(var_area));

# 2. Write code that prints the length of the string, 'python'.

# var_string = "python"
# print (len (var_string));

# 3. Print out the first and third letter of the word 'python'.

# print ("python" [0]);
# print ("python" [2]);

# 4. Ask the user to enter their name, and print out `Hello, <name>`.

# name = input ("What is your name?");
# print ("Hello, " + name);

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

# age = input ("How old are you Dinosaur??");
# new_age = int (age) + 15
# print ("You will be " + str (new_age) + " in 15 years time old fart !!");

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old.
#   In 15 years time you will be <age_in_15_years_time>`.
# name = input ("What is your name?");
# age = input ("How old are you Dinosaur??");
# new_age = int (age) + 15
# print ("Hello, " +name+ ", you are currently "+str(age)+ " years old.\nIn 15 years time you will be "+str(new_age)+" years old");

# 7. Ask the user to enter their hometown, print it out in uppercase letters.

# hometown = input ("What is your hometown, Homie ??: ");
# print (hometown.upper ());

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

# colour = input ("What is your fav colour?? ");
# print(len (colour));

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

# weather = input ("What's the weather like today?");
# month = input ("What month of the year is it?");
# print ("It is "+month+" and it is "+weather+" today");

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string:
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

# month = input ("What is last week's month?");
# temp1 = float(input ("What was the temperature (in celsuis) for last Monday?"));
# temp2 = float(input ("What was the temperature (in celsuis) for last Tuesday?"));
# temp3 = float(input ("What was the temperature (in celsuis) for last Wednesday?"));
# temp4 = float(input ("What was the temperature (in celsuis) for last Thursday?"));
# temp5 = float(input ("What was the temperature (in celsuis) for last Friday?"));
# avg_temp= (temp1+temp2+temp3+temp4+temp5)/5
# print ("It is "+month+" and the average temperature is "+str(avg_temp)+" degrees celsuis today");

# 11. Print out the above sentence but make the month upper case.

# print ("It is "+month.upper()+" and the average temperature is "+str(avg_temp)+" degrees celsuis today");

# 12. Create a variable that holds your favourite animals and print it out.
#    Make sure the animals are all on different lines and tabbed.

# fav_animal_1 = input ("What are you first fav animal?: ");
# fav_animal_2 = input ("What are you second fav animal?: ");
# fav_animal_3 = input ("What are you third fav animal?: ");
# print ("My favourite animals are: \n\t 1." + fav_animal_1 + "\n\t 2." + fav_animal_2 + "\n\t 3." + fav_animal_3);

# 13. Ask the user to enter their name as well as a number.
#    Print out the uppercase character at that position in the string.

# name = input ("What's your name?: ");
# number = int(input ("Provide a number?: "));
# print (name[number:int(number+1)].upper ());

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".

string = "WelcometoPython"
length = int(len(string))
print(str(length))
print(string[1:length:2])
