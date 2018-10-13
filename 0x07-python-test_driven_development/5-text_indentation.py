#!/usr/bin/python3
def check_types(err, type_list, *argv):
    ''' if none throws a different err msg, do a separate none check '''
    for i in argv:
        if i is None:
            raise TypeError(err)
        t = type(i)
        if t not in type_list:
            raise TypeError(err)
    return (True)


def text_indentation(txt):
    ''' formats text '''
    check_types("text must be a string", [str], txt)
    txt = txt.replace("? ", "?").replace("?\n", "?")
    txt = txt.replace(". ", ".").replace(".\n", ".")
    txt = txt.replace(": ", ":").replace(":\n", ":")
    txt = txt.replace(":", ":\n\n").replace("?", "?\n\n").replace(".", ".\n\n")
    for line in txt.splitlines():
        print(line.strip())
    if not txt:
        print("")
