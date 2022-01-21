def do_stuff(num):
    return num + 5

def do_stuff2(num2):
    try:
        return int(num2) + 5
    except ValueError as err:
        return err