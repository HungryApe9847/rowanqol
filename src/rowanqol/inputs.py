def int_input(prompt):
    while True:
        num = int(input(prompt))
        if num.is_integer():
            break
    return num

def float_input(prompt):
    while True:
        num = float(input(prompt))
        if isinstance(num, float):
            break
    return num
