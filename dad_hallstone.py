def main():
    start = eval(input('Enter starting number of the range: '))
    end = eval(input('Enter ending number of the range: '))

    bad_start = 'false'
    bad_end = 'false'
    bad_order = 'false'
    while True:
        if start < 1: 
            bad_start = 'true'
        else:
            bad_start = 'false'
        if end < 1:
            bad_end = 'true'
        else:
            bad_end = 'false'
        if start > end:
            bad_order = 'true'
        else:
            bad_order = 'false'
        if bad_start == 'true' or bad_end == 'true' or bad_order == 'true':
            print('Starting and Ending ranges must be greater than zero and Starting range must be less than Ending range.')
            start = eval(input('Enter starting number of the range: '))
            end = eval(input('Enter ending number of the range: '))
            continue
        else:
            break
    max_n = 0
    max_length = 0
    #Iterate all numbers in the range
    for n in range(start, end + 1):
        cycle_length = 0
        while n != 1:
            if n % 2 == 0: 
                n = n//2
                max_length += 1
                cycle_length = n
            else:
                n = 3 * n + 1
                max_length += 1
                cycle_length = n
            if n == 1:
                print(n)
        if (cycle_length > max_length):
            max_length = cycle_length
            max_n = n
    print('The number', max_n, 'has the longest cycle length of', str(max_length))
main()
