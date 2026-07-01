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

def y_n_input(prompt, error_msg="Enter y or n.", bool_return=False):
    while True:
        value = input(prompt).strip().lower()
        if value in ["y", "n"]:
            if bool_return:
                if value == "y":
                    value = True
                else:
                    value = False
            break
        else:
            print(error_msg)
    return value