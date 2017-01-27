def replace_hyphens(st):
    clean_list = []
    for char in st:
        if char != '-':
            clean_list.append(change_x(char))
        return clean_list

def change_x(char):
    if char.upper() == 'X':
        return '10'
    return char.upper()

def length_ten(st):
    if len(st) != 10:
        return False
    else:
        return True
    
def digit_test (st):
    for char in st:
        if char.isdigit() == True:
            continue
        else:
            return False
    return True
def single_digits(st):
    for char in st:
        if char < 0 or char > 10:
            return False
    return True
def div_11(last_sum):
    if last_sum % 11 == 0:
        return True
    else:
        return False
def fix_format(lines):
    result = 0
    for st in lines:
        if len(st) > result:
            result = len(st)
    return result
def partial_sum(a):
    partial_list = []
    for i in range (1, len(a)):
        a[i] = a[i - 1] + a[i]
    return partial_list

def is_valid_isbn(st):
    for line in st:
    #check if length is exactly 10
        if length_ten(line) == False:
            return False
    #check if st[0:9] are all digits
        if digit_test(line) == False:
            return False
    #check if the last character, X or x
        last_char = st[9]
        if last_char.isdigit() == False:
            return False
        if digit_test(change_x(line)) == False:
            return False
        
        s1 = partial_sum(line)
        s2 = partial_sum(s2)
        if div_11(s2[9]) == False:
            return False
    return True

def longest(lines):
  result = 0
  for line in lines:
    if len(line) > result:
      result = len(line)
  return result

    #create an empty list
    
    #append the first 9 characters as integers to that list
    #if the last character is an x append to 10
    #get partial sums
    #get partial sums
    #check if the last number in the partial sum is divisble by 11
    #return result (True or False)
def main():
    #open file isbn.txt for reading
    source = open('isbn.txt', 'r')
    #open file isbnOut.txt for writing
    result = open('isbnOut.txt', 'w')
    lines = [line.strip() for line in source]
    padding = longest(lines)
    #write a for loop to read line by line
    for line in lines:
        st = replace_hyphens(line)
        if is_valid_isbn(st) == False:
            result.write(line.ljust(padding) + 'invalid' + '\n')
        else: 
            result.write(line.ljust(padding) + 'valid' + '\n')
    #strip each line
    #replace all hyphens with blanks
    #send that line to a function that determine if it is a valid isbn
    #write out result in isbnOut
    #(outside loop) close files
    source.close()
    result.close()
                               
main()
