# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:55:07 2017

@author: jorei

Sieve of Eratosthenes 
- The sieve of Eratosthenes is one of the most 
efficient ways to find all of the smaller primes 
(below 10 million or so).
"""

def sieveoferat(number):
    N = number
    A = []
    for i in range(N):
        A.append(True)
        
    A[0] = False
    A[1] = False
    
    for i in range(2,N):
        if A[i]:
            j = i**2
            while j < N:
                A[j] = False
                j += i
            print(i,end=" ")
            
def main():
    while True:
        sieveoferat(int(input('\nPlease enter a number below which you want to find all primes: ')))
        
if __name__ == '__main__':
    main()