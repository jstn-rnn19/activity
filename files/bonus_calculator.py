service = int(input("Enter your year of service: "))
rating = input("Enter your Performance Rating (Excellent, Good, Average, Poor): ")

if service < 1:
    print("no bonus")
elif service > 5:
    if rating.lower() == "excellent":
        print("You will receive a 30% salary bonus")
    elif rating.lower() == "good":
        print("You will receive a 20% salary bonus")
    elif rating.lower() == "average":
        print("You will receive a 10% salary bonus")
    elif rating.lower() == "poor":
        print("No bonus")
    else:
        print("Invalid input")

elif service >= 1 and service <= 5:
    if rating.lower() == "excellent":
        print("You will receive a 20% salary bonus")
    elif rating.lower() == "good":
        print("You will receive a 10% salary bonus")
    elif rating.lower() == "average":
        print("You will receive a 5% salary bonus")
    elif rating.lower() == "poor":
        print("No bonus")
    else:
        print("Invalid input")
else:
    print("invalid input")