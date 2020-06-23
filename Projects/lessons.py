'''
def sum(x,y,z):
    if x==y or x==z or y==z:
        sum=0
    else:
        sum=x+y+z
    return sum

print(sum(2,2,4))
print(sum(1,2,5))
'''
'''
class Object:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sum_of_int(self):
        print(self.num1+self.num2)

r1=Object(10,20)
r2=Object(15,39)

r1.sum_of_int()
r2.sum_of_int()
'''
'''
Bio=Name:Che
Age:35 years old
Address: 211 Richmond Hill
print(Bio)
'''
'''
def bio():
    name, age="Che",35
    Address= "211 Richmond Hill"
    print("Name: {}\nAge: {}\nAddress {}".format(name,age,Address))

bio()
'''
'''
def calculation():
    x,y=4,3
    print((x+y)*(x+y))

calculation()
'''
'''
#38
def calculation(x,y):
    calc=""
    print((x+y)*(x+y))

print(calculation(4,3))
'''
'''
def simple_interest(amt,int,years):
    print(amt*(1+(int*0.01)*years))

simple_interest(10000,.35,7)
'''
'''
import os.path
print(os.path.exists("test-botonew.py"))
'''
'''
import time
print()
print(time.ctime())
print()
'''
#from itertools import product
import random
list=['a', 'e', 'i', 'o', 'u']
random.shuffle(list)
print("".join(list))

#for comb in product(list, repeat=len(list)):
    #print("".join(comb))












