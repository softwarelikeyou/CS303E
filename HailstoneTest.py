def main():
    #prompt the user to enter the starting number
    start = eval(input("Enter starting number of the range: "))
    print()
    #prompt the user to enter the ending number
    finish = eval(input("Enter ending number of the range: "))
    print ()
    #initialize variable to hold number and max cycle length
    max_num = 0
    max_cycle_length = 0
    #determine the number having the longest cycle length
    #write a loop that goes through all the numbers in that range
    counter = start
    while( counter <= finish):
      #determine the cycle length for each number
        cycle_length = 0
        num = counter
        while(num > 1):
            #write the collatz condition
            if (num % 2 == 0):
                f(n) = ( n // 2 )
            elif (num % 2 == 1):
                    f(n) = (3 * n + 1)

            #increment cycle_length
      #compare the cycle lenth with max cycle length
        if(cycle_length >= max_cycle_length)
      #and replace max cycle lengthif cycle length is greater or equal
        counter = counter + 1
    #print the result
    print()
    print("The number", max_num, "has the longest cycle length of", max_cycle_length)
    #print ("The number " + str(max_num) + " has the longest cycle length of " + \
  #str(max_cycle_length) + ".") #add period
main ()
