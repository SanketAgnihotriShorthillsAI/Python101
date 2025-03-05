distance = int(input("Enter the distance to your destination: "))
if distance >15:
    print("Take a car")
elif 15>= distance >3:
    print("Take a bike")
else:
    print("Walk")