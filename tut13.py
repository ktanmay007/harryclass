# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print ("enter first number")
num1 = int(input())
print ("enter second number")
num2 = int(input())

opraters = input("Enter 'A' for adition, 'M' for multiplication , 'D' for division,"
            "'S' for subtraction:")

if num1==45 and num2==3 and opraters=="M":
    print ("answer is 555")

elif num1==56 and num2==9 and opraters=="A":
    print ("answer is 77")

elif num1==56 and num2==6 and opraters=="D":
    print("answer is 4")

elif opraters=="A":
    print ("answer is ",num1 + num2)

elif opraters=="D":
    print ("answer is",num1/num2)

elif opraters=="S":
     print("answer is",num1 - num2)

elif opraters=="M":
    print ("answer is",num1 * num2)


