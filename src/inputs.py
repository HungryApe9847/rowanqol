def int_input():
    while True:
        num = int(input("Enter a number: "))
        if num.is_integer():
            break
    return num

def float_input():
    while True:
        num = float(input("Enter a number: "))
        if isinstance(num, float):
            break
    return num
