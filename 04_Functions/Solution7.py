def var_sum(*args):
    sum = 0
    for num in args:
        sum=sum+num
    return sum

print(var_sum(1,2,3,4,5,10,9))
