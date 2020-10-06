def fun1(*args):
    for i in args:
        print(i, end="--")


f = fun1

a = (2, 4, 6)
f(*a)


def keyWordArgs(**args):
    for key, value in args.items():
        print(f"{key}:{value}")


keyWordArgs(key1='value1', key2='value2')

a = 10


def scopeTest():
    a = 15
    globals()['a'] = 11
    print(f"in scopeTest function, a :: {a}")


scopeTest()
print(f"outside function, a:: {a}")



