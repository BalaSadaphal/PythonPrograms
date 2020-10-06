from array import *

vals = array('l', [-2, 5, 8, 9, 7])

add, size = vals.buffer_info()
print(size)
print(vals.buffer_info())


size=int(input('Enter length of array : '))

arr=array('i',[])

for i in range(0,size):
    arr.append(int(input('Enter next num:')))

while(True):
    print(arr.index(int(input('Enter the num u want to find:'))))
    c=input("do u wanna contine:")
    if c in ('n','N',0):
        break
