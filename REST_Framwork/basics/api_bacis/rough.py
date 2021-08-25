str1="A hello B to C"
n = str1.split(' ')
print(n)
def square(n):
    return n**2
    '''Takes in a number n, returns the square of n'''
    
print(square.__doc__)
from functools import reduce
sequences = [5, 8, 10, 20, 50, 100]
sum = reduce (lambda x, y: x+y, sequences)
print(sum)

a=[1,'a',2,'b',3,'c']
indices = (1,3,4)
for i in indices:
    print(a[i])

i=1
n=2
while i<=10:
    print(n,"*", i, "=", n*i)
    i=i+1
    
for num in range(6):
    for i in range(num):
        print(num,end=" ")#print number
    #new line after each row to display pattern correctly
    print("\n")