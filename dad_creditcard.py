## This function checks if a credit card number is valid
def is_valid(cc_num):
    parts = list(str(cc_num))
    parts.reverse()
    
    odds = list()
    for i in range(len(parts)-1,-1,-1):
        if isEven(i) == False:
            odds.append(sumDigits(int(parts[i])*2))

    evens = list()
    for i in range(len(parts)-1,-1,-1):
        if isEven(i) == True:
            evens.append(int(parts[i]))

    total = 0
    for odd in odds:
        total += int(odd)
    for even in evens:
        total += int(even)
    
    if total % 10 == 0:
        return True
    else:
        return False
    
## This function returns the type of credit card
def cc_type(cc_num):
    if str(cc_num).startswith('34') or str(cc_num).startswith('37'):
        return 'American Express'
    if str(cc_num).startswith('6001') or str(cc_num).startswith('644') or str(cc_num).startswith('65'):
        return 'Discover'
    if str(cc_num).startswith('50') or str(cc_num).startswith('51') or str(cc_num).startswith('52') or str(cc_num).startswith('53') or str(cc_num).startswith('54') or str(cc_num).startswith('55'):
        return 'MasterCard'
    if str(cc_num).startswith('4'):
        return 'Visa'    
  
def isEven(number):
    return number % 2 == 0

def sumDigits(number):
    result = 0
    parts = list(str(number))
    for part in parts:
        result += int(part)
    return result

def main():
    
    cc = int(input("Enter 15 or 16-digit credit card number: "))
    if len(str(cc)) < 15:
        print('\nNot a 15 or 16-digit number')
        return
    if len(str(cc)) > 16:
        print('\nNot a 15 or 16-digit number')
        return
    
    if is_valid(cc) == True:
        print('\nValid', cc_type(cc), 'credit card number')
    else:
        print('\nInvalid credit card number')
main()
