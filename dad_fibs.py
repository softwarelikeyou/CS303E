#  File: FibonacciBase.py

#  Description: Fibonacci Sequence as a Base for Representing Numbers

#  Student Name: Courtney C. Thomas

#  Student UT EID: 

#  Course Name: CS 303E

#  Unique Number: 1.0

#  Date Created: 4/30/2016

#  Date Last Modified: 4/30/2016

def fib_gen(n):
    fibs = [1]

    if n == 1 :
        return fibs

    if n == 2:
        fibs.append(n)
        return fibs

    fibs = [1,2]
    i = 1
    while True:
        current = fibs[i-1] + fibs[i]
        if current > n:
            break
        fibs.append(current)
        i += 1

    fibs.reverse()
    return fibs

def convert_fib_base(number):
    fibonaccis = fib_gen(number)
    start = number
    fibs = []
    for fib in fibonaccis:
        if start - fib >= 0:
            fibs.append(fib)
            start -= fib
    bits = ""
    for fib in fibonaccis:
        if fib in fibs:
            bits = bits + '1'
        else:
            bits = bits + '0'
    return bits

def main():
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            continue
        
    print(number,'=', convert_fib_base(number), '(fib)')
main()
