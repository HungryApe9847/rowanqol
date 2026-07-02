def read_file(filename, chars=None, lines=None, include_newline=True):
    with open(filename) as file:
        if lines is not None and lines > 0:
            if include_newline:
                lined_text = "".join(file.readlines()[:lines])
                return lined_text
            else:
                lined_text = "".join(file.readlines()[:lines]).rstrip("\n")
                return lined_text
        elif chars is not None and chars > 0:
            return file.read(chars)
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
