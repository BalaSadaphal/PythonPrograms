from main import print_hi

# l = list(input("Enter the list of nums").strip().split(","))
#
# print(l)


def fact(num):
    if (num > 1):
        return num * fact(num - 1)
    else:
        return 1


print(fact(3))


def factWrapper():
    return fact


wrapper = factWrapper()

i = wrapper(3)

print(i)

print_hi('hello there')
print("in: ",__name__)