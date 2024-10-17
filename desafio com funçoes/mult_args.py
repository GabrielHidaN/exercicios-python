def mult_args(*args):
    total = 1
    for numero in args:
        total *= numero 
    return total

mult = mult_args(1,2,3,4,5)
print(mult)