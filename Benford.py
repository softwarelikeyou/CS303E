#  File: Benford.py

#  Description: This program finds the frequency of digits in a set of data.

#  Student Name: Courtney Thomas

#  Student UT EID: cct685

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 22 April 2016

#  Date Last Modified: 22 April 2016

#function that finds first digit
def first_digit(n):
    while(n >= 10):
        n = n // 10
    return n
#function that sums a list
def sum_list(l):
    sum_n = 0
    for i in range (len(l)):
        l[i] = int(l[i])
        sum_n += l[i]
    return sum_n

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  # fill the rest
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()
  
  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]

    # make entries in the dictionary
    digit = str(first_digit(int(pop_num)))
    pop_freq[digit] += 1
    
    
    

  # close the file
  in_file.close()
  #find percentage of each frequency
  list_dict = list(pop_freq.values())
  total = sum_list(list_dict)
  freq_1 = pop_freq['1']
  freq_2 = pop_freq ['2']
  freq_3 = pop_freq ['3']
  freq_4 = pop_freq ['4']
  freq_5 = pop_freq ['5']
  freq_6 = pop_freq ['6']
  freq_7 = pop_freq ['7']
  freq_8 = pop_freq ['8']
  freq_9 = pop_freq ['9']
  percent_1 = round(((freq_1 / total) * 100), 1)
  percent_2 = round(((freq_2 / total) * 100), 1)
  percent_3 = round(((freq_3 / total) * 100), 1)
  percent_4 = round(((freq_4 / total) * 100), 1)
  percent_5 = round(((freq_5 / total) * 100), 1)
  percent_6 = round(((freq_6 / total) * 100), 1)
  percent_7 = round(((freq_7 / total) * 100), 1)
  percent_8 = round(((freq_8 / total) * 100), 1)
  percent_9 = round(((freq_9 / total) * 100), 1)
  
  # write out the result
  print("Digit" + "\t" + "Count" + "\t" + "%")
  print("1" + "\t" + str(freq_1) + "\t" + str(percent_1))
  print("2" + "\t" + str(freq_2) + "\t" + str(percent_2))
  print("3" + "\t" + str(freq_3) + "\t" + str(percent_3))
  print("4" + "\t" + str(freq_4) + "\t" + str(percent_4))
  print("5" + "\t" + str(freq_5) + "\t" + str(percent_5))
  print("6" + "\t" + str(freq_6) + "\t" + str(percent_6))
  print("7" + "\t" + str(freq_7) + "\t" + str(percent_7))
  print("8" + "\t" + str(freq_8) + "\t" + str(percent_8))
  print("9" + "\t" + str(freq_9) + "\t" + str(percent_9))
  
main()
