a = input("Enter a integer a :")
b = input("Enter a integer b :")

a = float(a)
b = float(b)

# print("Addition:",a+b)
# print("mutipliacation:",a*b)
# print("subtraction:",a-b)
# print("Division:",a/b)
operation = input("Enter 'A' for addtion , 'M' for multiplication , 'S' for subtraction and 'D' for Division:")

if operation=="A":
    print("Addition:",a+b)
elif operation == "M":
    print("mutipliacation:",a*b)
elif operation == "S":
    print("subtraction:",a-b)
elif operation=="D":
    print("Division:",a/b)
else :
    print("Enter Valid Input CASE SENSITIVE")