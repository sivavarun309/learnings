#Function
# Reusing of the code, insteed of writing multiple times

def add(a, b, c=0):

    return a+b+c

def iffun(a):
    if a==1:
        return "A is 1"
    else:
        if a==2:
            return " A is 2"
        else:
            return "A is something else"

#lambda function
#Single line function

ifstat = lambda a: "A is 1" if a==1 else "A is 2" if a==2 else "A is something else"





def add(a=1, b=2, *args,**kwargs):
    print("A is ",a)
    print("B is ",b)
    print("Args ",args)
    print("KW   ",kwargs)


#add(4,5,5,6,7,7,c=10,e=20)

#Dictionary function
di = {'a':10,'b':20,'c':30}
#for k, v in di.items():
#    print(k,v)

#Recursion:
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(5))
'''
factorial(5)

5 * factorial(4)

5 * 4 * factorial(3)

5 * 4 * 3 * factorial(2)

5 * 4 * 3 * 2 * factorial(1)

5 * 4 * 3 * 2 * 1

4 * 3 + 5 - 1 = 120
'''

#map, filter, reduce

c = list(map(factorial,[5,6,7,8,9,10,11,12,13,14]))



a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list

temp = lambda x: x * 2
res = list(map(temp, a))

#print(res)

a = [10,24,33,55]

def greater25(a,b):
    if a > b:
        return a
    else:
        return b
    
#temp = list(filter(greater25,a))

from functools import reduce

def add(a,b,c):
    return a+b+c

a = [1,2,3,4,5,1,3]

sum = 0 
#for i in a:
#    sum = add(sum,i)

temp = reduce(greater25,a)
        
print(temp)
