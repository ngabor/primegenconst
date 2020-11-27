"""
A program for calculating the prime genarator constant with
arbitrary precision, and check the sequence of generated numbers.
DOI: 10.1080/00029890.2019.1530554)

Author: Nagy Gabor
"""


#import decimal module for caculating with arbitrary precision
import decimal
from math import log

#some simple functions for prime numbers
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def nextprime(n):
    i=n
    while True:
       i+=1
       if isprime(i):
           return i

#Set the number of decimal digits
decdig=1000 # modify this number to change the precision
decimal.setcontext(decimal.Context(prec=decdig+2))
qlim=decimal.Decimal(0.1)**(decdig+3)

#Calculate the prime generator constant
c=decimal.Decimal(0)
nominator=1
p=2
while True:
    q=1/decimal.Decimal(nominator)
    if q<qlim:
        break
    c+=(p-1)*q
    nominator*=p
    p=nextprime(p)
c=round(c, decdig)

print(f'The prime generator constant with {decdig} digits:')
print(c)

#Calculate the sequence until the first number which is not prime
f=[c]
while isprime(int(f[-1])):
    f.append(int(f[-1])*(1+f[-1]%1))

pl=[int(x) for x in f[:-1]]
print(f'\nThis number provides {len(pl)} prime numbers:')
print(', '.join([str(pj) for pj in pl]))
print(f'The first wrong number: {int(f[-1])}')
print("\nThe count of prime's decimal digits:", sum([len(str(pj)) for pj in pl]) )
print("The sum of primes's logarithms (base=10):", sum([log(pj, 10) for pj in pl]))
    

    
    
