#Write a program that takes a list with duplicate elements and returns a new list with only the unique elements, keeping the original order.
list1 =[1,2,2,3,4,3,5]
list2 =[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list1)
print(list2)

#Given a list of numbers (including negatives), create a new list containing the squares of each number, sorted in ascending order
list = [-1,-3,2,4]
list_square = []
for i in list:
    i = i*i
    list_square.append(i)
list_square.sort()
print(list)
print(list_square)

#Create a tuple of integers. Ask the user for a target number, then find all pairs of numbers within the tuple that sum up to that target.
tuple = (1,2,3,4,5)
num = int(input("enter the number: "))
for i in range(5):
    for j in range(i+1,5):
        if tuple[i] + tuple[j] == num:
            print(tuple[i],tuple[j])

#Given a tuple like (1, 2, (3, 4), 5), write a program to "flatten" it into a simple list: [1, 2, 3, 4, 5].
tuple1 = (1,2,(3,4),5)
flatten = []
for i in tuple1:
    if type(i) == tuple:
        for j in i:
            flatten.append(j)
    else:
        flatten.append(i)
flatten1 = tuple(flatten)
print(tuple1)
print(flatten1)
