name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
address= input("Enter Your Address: ")
if name is not None and age is int and address is not None:
    print("Hello Ms/Mr ", name, "Age:" , age, "locateed in", address, "thanks fo rbeing one of our community,\t\tEnjoy.")
else:
    breakpoint()