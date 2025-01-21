# #1.1

for i in range (0,3):
    print("Sahil")

# #2.1

a=10
b=20
c=30
print(a+b+c)

# #2.2

x="sahil"
y="kumar"

print(str(x)+str(y))


# #4.1
f=int(input("enter a number"))

for i in range(1,11):
    print(f," * ",i," = ",f*i)

# #4.2
g=int(input("enter a number"))
m=int(input("enter a number"))

for i in range (1,m+1):
    print(g," * ",i," = ",g*i)


# #4.3
n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    s=s+i
print(s)

# #5.1
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))

print(max(a,b,c))

# #5.2
n=int(input("enter a number"))

s=0

for i in range (1,n+1):
    if i%7==0 and i%9==0:
        s=s+i

print(s)

#5.3

b=int(input("enetr a number"))

def is_prime(a):
    f=0
    for i in range(2,a//2+1):
        if a%i==0:
            f=1
            break
    if f==0:
        # print("prime")
        return True
    else:
        # print("not Prime")
        return False

# sumP=0
for i in range(2,b+1):
    if is_prime(i):
        sumP=sumP+i

print("sum of prime nummber is ",sumP)



#6.1
def sum_of_odds(n):
    total_sum = 0
    for i in range(1, n + 1, 2):
        total_sum += i
    return total_sum

n = int(input("enter a number "))
result = sum_of_odds(n)
print(result)

#6.2
def addPrimeNumbers(a):
    for i in range(2,a):
        if(is_prime(i)):
            sumOfPrimes+=i
    print("sum of the prime numbers upto ", a, " is ->", sumOfPrimes)