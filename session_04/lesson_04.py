## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

# list = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]

# print(len(list))
# print(list)

# 2. Add "Grapes" to the list and print the list.

# list.append("Grapes")
# print(list)

# 3. Change "Pears" to "Strawberries" and print the list.

# list[2] = "Strawberries"
# print(list)

# 4. Remove "Apples" from the list and print the list.

# del (list[0])
# print(list)

# 5. Print out the current length of the list.

# print(len(list))

# 6. Order the list alphabetically.

# print(list)
# list.sort()

# 7. Print out the list again.

# print(list)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.

# fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
# print(fruits)

# for x in fruits:
#   print(x)

# 2. Print the numbers 1 to 100 (including the number 100).

# for num in range (101):
#   print (num);

# 3. Print all odd numbers from 1 to 100.
# for num in range(1, 100, 2):
#   print(num)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).

# not_held = [1916, 1940, 1944, 2020];

# for oly_yrs in range(1896, 2023, 4):
#   if oly_yrs not in not_held:
#     print(oly_yrs)
#   # else:
#   #   print ("not held")

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.

# rand = [4, 60, 21, 66, 47, 51, 86, 94, 18, 28]
# odd = 0
# even = 0

# print(len(rand))

# for number in rand:
#   if number % 2:
#     odd = odd + 1
#   else:
#     even = even + 1

# print("Even numbers in range: " + str(even))
# print("Odd numbers in range: " + str(odd))

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

# names = ["Ameya","Pranjal","Abhimanyu","Anirudh","Anuradha"]

# for list in names:
#   print ("Hello, " + list)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".

# word = "supercalifragilisticexpialidocious"
# for counter in range(len(word)):
#   print(word[counter])

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.

# num = [2, 3, 4, 5, 6]
# sqr = []

# for i in range(len(num)):
#   sqr.append(num[i] * num[i])
#   print(num[i])
#   print(sqr[i])

# print(num)
# print(sqr)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

# names = ["Ameya", "Pranjal", "Abhimanyu", "Anirudh", "Anuradha"]
# new_names = []

# for list in range(len(names)):
#   new_names.append("Dr. " + names[list])
#   print(new_names[list])

# print(new_names)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz".
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```

# for num in range(1, 101, 1):
#   if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
#   elif num % 3 == 0:
#     print("Fizz")
#   elif num % 5 == 0:
#     print("Buzz")
#   else:
#     print(num)
