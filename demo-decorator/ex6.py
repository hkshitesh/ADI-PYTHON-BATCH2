def division(a,b):
    print(a/b)


def divison_deco(func):
    def inner(x,y):
        if x<y:
            x,y = y,x
        return func(x,y)
    return inner


divsion = divison_deco(division)

divsion(345,500)
