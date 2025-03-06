char = int(input("Enter the characters in your password: "))
if char > 10:
    print("Password is strong")
elif 6<= char <= 10:
    print("Password is medium")
else:
    print("Password is weak")