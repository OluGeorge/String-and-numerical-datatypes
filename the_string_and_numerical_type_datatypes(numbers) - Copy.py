# -*- coding: utf-8 -*-
"""The string and numerical type Datatypes(numbers).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xnDriSugb9IYucJGFBuw8nNZ0x98pSQN
"""

new_string = 'Hello World!'
Fizz = new_string [0:5]
print(Fizz)
print(new_string)

PEOPLE = "Person 1 \nPerson 2"

print(PEOPLE)

WAGE = "Person 1: \t R123.22"
WAGE2 = "Person 2: \t R523.98"

print(WAGE)

print(WAGE, end=' ')
print(WAGE2)

manip_string = "***Welcome$to$the$world$of$programming***"

manip_string = manip_string.replace("$", " ")
print("manip_string.replace(""$"", " "): {}".format(manip_string))

manip_string = manip_string.strip('*')
print("manip_string.strip(""*""): {}".format(manip_string))

manip_string = manip_string.upper()
print(f"manip_string.upper(): {manip_string}")

manip_string = manip_string.lower()
print(f"manip_string.lower(): {manip_string}")

"""#### replace.py

"""

# To relace an exclamation mark with a space
sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog.'
sentence = sentence.replace('!',' ')
print(sentence)

# To convert a sentence to bold letters
sentence = sentence.upper()
print(sentence)

print (sentence[::-1])

"""manipulation.py"""

str_manip = input('Enter a sentence:')
print(len(str_manip))

str_manip= str_manip.replace('e','@')
print(str_manip)

str_manip = input('Enter a sentence:')
print(str_manip[19:15:-1])

str_manip = input('Enter a sentence:')
olu = str_manip[0:4]
print(str(olu))

str_manip = input('Enter a sentence:')
George = str_manip[-2:]
print(str(George))

print(str(olu+George).strip())

"""numbers.py"""

# Input the first integer
num1 = int(input("Enter the first integer: "))

# Input the second integer
num2 = int(input("Enter the second integer: "))

# Input the third integer
num3 = int(input("Enter the third integer: "))

# Calculate the sum of the integers
sum_of_integers = num1 + num2 + num3

# Display the result
print(f"The sum of the three integers is: {sum_of_integers}")

# calculate the first number minus the second number
Answer1 = num1 - num2
print(f"The first number minus second number is: {Answer1}")

# the third number multiplied by the first number
Answer2 = num3 * num1
print(f'The third number multiplied by first number is: {Answer2}')

# the sum of the three numbers  divided by 3
Answer3 = (num1+num2+num3)/3
print(f'the sum of the three numbers divided by 3 is: {Answer3}')