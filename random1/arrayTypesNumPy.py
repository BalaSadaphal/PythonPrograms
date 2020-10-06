from numpy import *

arr1=array([1,2,3,4.0])

print(arr1.dtype)

arr2=linspace(1,5,3)

print(arr2)

arr3=arange(0,10,2)

print(arr3)

arr4=logspace(1,10,5)

print(arr4)

arr5=zeros(5)

print(arr5)

arr6=ones(6)

print(arr6)

arr6[4]=2
print(arr6)

print(__name__)