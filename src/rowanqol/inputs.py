def int_input(prompt, error_msg="Enter an integer."):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print(error_msg)
    return num

def float_input(prompt, error_msg="Enter a float."):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print(error_msg)
    return num
