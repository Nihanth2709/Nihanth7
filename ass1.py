# Write a python program to display a user entered name followed by Good Afternoon using input () function. 
name = input("enter your name: ")
print("Good Afternoon!",name)

#Write a program to fill in a letter template given below with name and date. letter = ''' Dear <|Name|>, You are selected! <|Date|> '''
Name = input("enter your name: ")
date = input("enter the date: ")
letter = f''' Dear {Name}, You are selected! {date} '''
print(letter)

# Write a program to detect double space in a string.
string = input("enter a word: ")
if "  " in string:
    print("double space is present in the word")
else:
    print("no double space is present in the word")

# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 
maths = int(input("enter the maths marks: "))
science = int(input("enter the science marks: "))
english = int(input("enter the english marks: "))
total = maths + science + english
if (total <= 40):
    print("excellent, you have passed")
elif (total > 33):
    print("excellent, you have passed")
else:
    print("you have failed")

#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams. 
list = ["Make a lot of money”, “buy now”, “subscribe this”, “click this"]
comment = input("enter the comment: ")
if list in comment:
   print("it is a spam comment")
else:
    print("it is not a spam comment")

#Write a program to find whether a given username contains less than 10 characters or not. 
username = input("enter the name: ")
if len(username) < 10:
    print(username,"contains more than 10 characters")
else:
     print(username,"contains less than 10 characters")

# Write a program which finds out whether a given name is present in a list or not. 
fruits = ["apple","mango","banana","grapes"]
fruit_name = input("enter the fruit name: ")
if fruit_name in fruits:
    print(fruit_name,"is present")
else:
    print(fruit_name,"is not present")

#Write a program to calculate the grade of a student from his marks from the 
#following scheme: 
#90 – 100 => Ex 
#80 – 90 => A 
#70 – 80 => B 
#60 – 70  =>C 
#50 – 60 => D 
#<50 => F

grade = input("enter the grade of student: ")
if grade > 90:
    print(" grade:excellent")
elif grade > 80:
    print(" grade:A")
elif grade > 70:
    print(" grade:B")
elif grade > 60:
    print(" grade:C")
if grade >= 50:
    print(" grade:D")
else:
    print("grade:fail(F)")

#Write a program to find the greatest of four numbers entered by the user. 
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
num4 = int(input("enter the fourth number: "))
greater = num1
if num1 < num2:
    greater = num2
if greater < num3:
    greater = num3
if greater < num4:
    greater = num4
print(greater,"is greater than all")

