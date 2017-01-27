
#  File: Goldbach.py

#  Description: This program finds the prime expressions of even number summations over four. 

#  Student Name: Courtney Thomas

#  Student UT EID: cct685

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 24 February 2016

#  Date Last Modified: 27 February 2016

#is_prime function given in class
def is_prime(n):
    if (n == 1):
        return False
    limit = int (n ** .5) + 1
    divisor = 2
    while (divisor < limit):
        if(n % divisor == 0):
            return False
        divisor = divisor + 1
    return True

def main():
    #prompt user to enter lower limit and upper limit
    lo = eval(input("Enter the lower limit: "))
    hi = eval(input("Enter the upper limit: "))
    #error check to see if input is even, lo is above four, and lo is greater than hi
    while(lo < 4 or lo % 2 != 0 or lo > hi or hi % 2 != 0):
        lo = eval(input("Enter the lower limit: "))
        hi = eval(input("Enter the upper limit: "))
        
    #initialize output
    output = ''
    cycle = 0
    #outer loop that goes from lo to hi 
    for counter in range (lo, hi + 1):
        #check that conter is always even
        if(counter % 2 != 0):
            continue
        #inner loop that finds numbers and tests if they are prime and add to counter
        for i in range(0, counter + 1):
            if(is_prime(i) == True):
                for j in range(i, counter):
                    if(is_prime(j) == True):
                        if((i+j) == counter):
                            #store output
                            if cycle == 0:
                                output = output + '= ' + str(i) + ' + ' + str(j)
                            else:
                                output = output + ' = ' + str(i) + ' + ' + str(j)
                            cycle +=1
        #print output
        print(str(counter), output)
        cycle = 0
        output = ''
       



    
main()
