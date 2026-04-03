#Write a program to store seven fruits in a list entered by the user. 
fruits = []
for i in range(7):
    fruit = input("enter the fruits: ")
    fruits.append(fruit)
print("fruits are: ",fruits)

#Write a program to accept marks of 5 students and display them in a sorted manner. 
marks = []
for i in range(5):
    mark = int(input("enter the marks: "))
    marks.append(mark)
marks.sort()
print("sorted marks are ",marks)

#Write a program to sum a list with 4 numbers. 
numbers = []
for i in range(4):
    number = int(input("enter the numbers: "))
    numbers.append(number)
sum = numbers[0] + numbers[1] + numbers[2] + numbers[3]
print("sum of the numbers is: ",sum)

#Write a program to count the number of ones in the following tuple: A = (7, 1, 8, 1, 1, 9).
A = (7,1,8,1,1,9)
print(A.count(1))