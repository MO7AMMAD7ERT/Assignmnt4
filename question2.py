import math

number1 = int(input("Ente First Number: "))
number2 = int(input("Ente Second Number: "))
print("choose The Operation: "
      "\n\t1_ addition (+)"
      "\n\t2_Subtractin (-)"
      "\n\t3_Multiplication (*)"
      "\n\t4_Division (/)"
      "\n\t5_Power (^)"
      "\n\t6_Mod (%)")
choice = int(input())

if choice ==1:
    result = number1 + number2
    print(result)
elif choice ==2:
    result = number1 - number2
    print(result)
elif choice ==3:
    result = number1 * number2
    print(result)
elif choice ==4:
    result = number1 / number2
    print(result)
elif choice ==5:
    result = number1**number2
    print(result)
elif choice ==6:
    result = number1 % number2
    print(result)
print("What to do with the result")
print("\n1-Normal rounding, up, or lower number"
      "\n2-Taking the number without a decimal point")
choice2 = int(input())
if choice2 == 1:

    print("1- upper rounding number"
          "\n2-lower rounding number")
    choice3 = int(input())
    if choice3 ==1:
        rounded = math.ceil(result)
        print(rounded)
    elif choice3 == 2:
        rounded = math.floor(result)
        print(rounded)
elif choice2 ==2:
    rounded = round(result)
    print(rounded)

