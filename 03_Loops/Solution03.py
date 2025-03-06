n= int(input("Enter a number: "))
for i in range(1,11):
        if i==5:
            continue
        else:
            print(str(n), "x", str(i), "=", n*i)

