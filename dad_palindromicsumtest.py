#reverse the digits of a number
def rev_num(num):
      rev_num = 0
      while (num > 0):
            rev_num = rev_num * 10 + (num % 10)
            num = num // 10
      return rev_num
#function that tests for palindrome
def is_palindromic(num):
      return (num == rev_num(num))

def main():
 #prompt the user to enter starting number
      start = eval(input('Enter starting number of the range: '))
      print()
    #prompt the user to enter ending number
      finish = eval(input('Enter ending number of the range: '))
      print()
    #error check that the numbers are positive
    #error check that the ending number is smaller than the starting number
      while((start < 1) or (finish < 1) or (start > finish)):
            start = eval(input('Enter starting number of the range: '))
            print()
            finish = eval(input('Enter ending number of the range: '))
            print()
      #reverse number test
      #initialize cycle_length
      max_num = 0
      max_cycle_length = 0
      counter = start
      num = counter
      while (counter <= finish):
            cycle_length = 0
            while (num > 1):
                  if (not is_palindromic (num)):
                        num = rev_num(num) + num
                        print('num = ', num)
                        cycle_length += 1
                  else:
                        print('cycle_length', cycle_length)
                        break
            if (cycle_length >= max_cycle_length):
                  max_cycle_length = cycle_length
                  max_num = counter
            print('counter = ', counter)
            counter += 1
            num = counter
      #print cycle_length
      print ("The number " + str(max_num) + " has the longest cycle length of " + \
      str(max_cycle_length) + ".")
      
main()

