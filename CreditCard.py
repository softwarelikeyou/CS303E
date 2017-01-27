#  File: CreditCard.py

#  Description: This program determines the validity and type of a credit card number.

#  Student Name: Courtney Thomas

#  Student UT EID: cct685

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 8 April 2016

#  Date Last Modified: 9 April 2016
def sum_digits(n):
    sum_digits = (n // 10) + (n % 10)
    return sum_digits
def sum_n(a):
    sum_n = 0
    for i in range (0, len(a)):
        sum_n += a[i]
    return sum_n

    
def is_valid(cc_num):
    creditCard = cc_num
    list_card = []
    d0 = creditCard % 10
    creditCard = creditCard // 10
    d1 = creditCard % 10
    creditCard = creditCard // 10
    d2 = creditCard % 10
    creditCard = creditCard // 10
    d3 = creditCard % 10
    creditCard = creditCard // 10
    d4 = creditCard % 10
    creditCard = creditCard // 10
    d5 = creditCard % 10
    creditCard = creditCard // 10
    d6 = creditCard % 10
    creditCard = creditCard // 10
    d7 = creditCard % 10
    creditCard = creditCard // 10
    d8 =creditCard % 10
    creditCard = creditCard // 10
    d9 = creditCard % 10
    creditCard = creditCard // 10
    d10 = creditCard % 10
    creditCard = creditCard // 10
    d11 = creditCard % 10
    creditCard = creditCard // 10
    d12 = creditCard % 10
    creditCard = creditCard // 10
    d13 = creditCard % 10
    creditCard = creditCard // 10
    d14 = creditCard % 10
    creditCard = creditCard // 10
    d15 = creditCard % 10
    creditCard = creditCard // 10

    list_card.append(d15)
    list_card.append(d14)
    list_card.append(d13)
    list_card.append(d12)
    list_card.append(d11)
    list_card.append(d10)
    list_card.append(d9)
    list_card.append(d8)
    list_card.append(d7)
    list_card.append(d6)
    list_card.append(d5)
    list_card.append(d4)
    list_card.append(d3)
    list_card.append(d2)
    list_card.append(d1)
    list_card.append(d0)
    for i in range(0, len(list_card) -1):
        if i % 2 == 0:
            list_card[i] = 2 * list_card[i]
            
    for j in range (0, len(list_card) -1):
        if list_card[j] > 9:
            list_card[j] = sum_digits(list_card[j])
            
    luhn_sum = sum_n(list_card)
    if luhn_sum % 10 == 0:
        return True 
    else:
        return False
def cc_type(cc_num):
    
    cc_num = str(cc_num)
    if cc_num.startswith("4"):
        return "Visa"
    elif cc_num.startswith("34") or cc_num.startswith("37"):
        return ("American Express")
    elif cc_num.startswith("6011") or cc_num.startswith("65") or cc_num.startswith("644"):
        return ("Discover")
    elif cc_num.startswith('50') or cc_num.startswith('51') or cc_num.startswith('52') or cc_num.startswith('53') or cc_num.startswith('54') or cc_num.startswith('55'):
        return ("MasterCard")
    
def main():
    cc = eval(input("Enter a 15 or 16-digit credit card number: "))
    print()
    if len(str(cc)) < 15 or len(str(cc)) > 16:
        print("Not a 15 or 16-digit number")
        
        return
   
    if is_valid(cc) == True:
        print ("Valid " + cc_type(cc) + " credit card number")
    elif is_valid(cc) == False:
        print ("Invalid credit card number")
    
main()
    
                
    

        
    
