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
if (total = 40):
    print("excellent, you have passed")
elif (total < 40):
    