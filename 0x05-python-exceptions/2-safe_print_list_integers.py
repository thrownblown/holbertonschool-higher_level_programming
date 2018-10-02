#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        idx = 0
        for value in my_list:
            try:
                if idx < x:
                    print("{:d}".format(value), end="")
                    idx += 1
                else:
                    break
            except (ValueError, TypeError):
                pass
        print("")
        return (idx)
