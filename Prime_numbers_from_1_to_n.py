#write a program to print all the prime numbers between 1 to n.
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter input :"))
if n>1:
    print("2")
for i in range(3,n+1):
    if isprime(i):
        print(i)
if n==1:
    print("There are no prime numberS")
