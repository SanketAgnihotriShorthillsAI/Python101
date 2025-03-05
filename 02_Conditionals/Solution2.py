age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")
price = 12 if age>=18 else 8
if day == "Wednesday" or day == "wednesday":
    price = price-2
else:
    price = price
print("The price is $" ,price)