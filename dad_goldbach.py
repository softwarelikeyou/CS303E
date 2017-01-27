def is_prime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if (n % x == 0):
            return False
    return True

def main():
    lo = eval(input("Enter the lower limit: "))
    hi = eval(input("Enter the upper limit: "))
    while(lo < 4 or lo % 2 != 0 or lo > hi or hi % 2 != 0):
        lo = eval(input("Enter the lower limit: "))
        hi = eval(input("Enter the upper limit: "))
        
    output = ''
    for counter in range(lo, hi+1):
       if (counter % 2 != 0):
           continue
       for i in range(0, counter + 1):
           if (is_prime(i) == True):
               for j in range(i, counter):
                  if (is_prime(j) == True):
                     if (i + j == counter):
                        output = output + ' = ' + str(i) + ' + ' + str(j)

       print(str(counter), output.lstrip())
       output = ''
       
main()
