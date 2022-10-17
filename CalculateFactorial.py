"""next project use function
calculate factorial
for example 5! is 120 mean 5!=5*4*3*2*1=120"""
x=int(input("please enter number"))

def fac(x):
    fact=1
    for num in range(2,x+1):
        fact*=num
    print(fact)

fac(x)


