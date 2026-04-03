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