import time

def slow_function():
    time.sleep(5)
    return "Operation Completed"


print(slow_function())