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

def _build_options(items, msg):
    item_number = 1
    override = False
    for item in items:
        item_string = "\n" + str(item_number) + ": " + item
        if msg[-1] == ":" or override == True:
            msg += item_string
            override = True
        item_number += 1
    return msg



def choice_input(prompt: str, items: list, error_msg: str = "Only select one of:"):
    prompt = _build_options(items, prompt)
    if prompt[-1] != ":":
        raise TypeError("prompt must end with ':'")
    choice = int_input(prompt, error_msg=error_msg)
    return choice
