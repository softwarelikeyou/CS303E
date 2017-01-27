def main():
    start = eval(input('Enter starting number of the range: '))
    finish = eval(input('Enter ending number of the range: '))

    bad_start = 'false'
    bad_finish = 'false'
    bad_order = 'false'
    while True:
        if start < 1: 
            bad_start = 'true'
        else:
            bad_start = 'false'
        if finish < 1:
            bad_finish = 'true'
        else:
            bad_finish = 'false'
        if start > finish:
            bad_order = 'true'
        else:
            bad_order = 'false'
        if bad_start == 'true' or bad_finish == 'true' or bad_order == 'true':
            print('Starting and Ending ranges must be greater than zero and Starting range must be less than Ending range.')
            start = eval(input('Enter starting number of the range: '))
            finish = eval(input('Enter ending number of the range: '))
            continue
        else:
            break

    print('start = ', start)
    print('finish   = ', finish)

    max_num = 0
    max_cycle_length = 0
    counter = start
    while( counter <= finish):
        cycle_length = 0
        num = counter
        while(num > 1):
            #write the collatz condition
            if (num % 2 == 0):
                num = ( num // 2 )
            elif (num % 2 == 1):
                num = (3 * num + 1)
            cycle_length += 1 #increment cycle_length
        #compare the cycle lenth with max cycle length
        if(cycle_length >= max_cycle_length): 
            max_cycle_length = cycle_length
            max_num = counter
            #and replace max cycle lengthif cycle length is greater or equal
        counter = counter + 1
    print("The number", max_num, "has the longest cycle length of", max_cycle_length)

main()
