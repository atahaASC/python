from random import *

name = input("What is your name?")

wives = ["Taylor Swift", "America", "George W. Bush", "Ben Carson", "Kanye"]
cars = ["Bentley", "Bugatti", "Broom", "Toyota", "Jeep"]

wifeValue = input("What is your spouse's name?")
carValue = input("What car do you want?")

wife = random.choice(wives)
car = random.choice(cars)

if name == "Jared" or name == "jared":
    print("\nYour spouse's name is Victoria.")
else:
    print("\nYour spouse's name is " + wife + ".")
    
if wife == "George W. Bush" or wife == "Ben Carson":
    print("\nYour car is the Republican Campaign Bus.")
elif wife == "Victoria":
    print("\nYour car is nothing. That relationship won't work out Jared, neither will the car.America")
elif wife == "Kanye":
    print("\nYour car is a pair of Yeezies. Kanye doesn't need no car.")
elif wife == "America":
    print("\nYour car is freedom and liberty. It will take you far.")
else:
    print("\nYour car is " + carValue + ".")