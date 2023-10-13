def f1():
    n=10;
    return n

#print(f1())

def f2():
    yield 10
    yield 20
    yield 30
    yield 40

res=f2();

print(next(res))
print(next(res))
print(next(res))
print(next(res))
