def add(a,b):
    return a+b
import functools
li=[1,2,3,4]
print(functools.reduce(add,li))