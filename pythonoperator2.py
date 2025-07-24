print("Greater among 3 number ")
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
z=int(input("Enter 3rd number: "))
if x>y and x>z:
    print(x, "is greater ")
elif y>x and y>z:
    print(y, "is greater ")
else:
    print(z, "is greater ")