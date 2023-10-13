
def upper_decorator(func):
    def inner():
        result = func()
        return result.upper()
    return inner

@upper_decorator
def say_hello():
    return "hello world"

print(say_hello())

@upper_decorator
def say_bye():
    return "bye world"

print(say_bye())