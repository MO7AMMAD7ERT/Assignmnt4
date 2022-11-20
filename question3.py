number1 = int(input("Enter the First number: "))
number2 = int(input("Enter the Second number: "))
number3 = int(input("Enter the Third number: "))
number4 = int(input("Enter the Fourth number: "))
number5 = int(input("Enter the Fifth number: "))
lst = [number1, number2, number3, number4, number5]


def find_max(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    print("Maximum element in the list is :",max)
    return max

def find_mini(list):
    max = list[0]
    for a in list:
        if a < mini:
            mini = a
    print("Minimum element in the list is :",mini)
    return mini

find_max(lst)
find_mini(lst)

