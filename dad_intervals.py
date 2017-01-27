def main():
    tups = []
    file = 'intervals.txt'
    lines = [line.rstrip('\n') for line in open(file)]
    for line in lines:
        values = line.split(" ")
        tup = (int(values[0]), int(values[1]))
        tups.append(tup)
    tups = sorted(tups)

    # pass 1
    remove = []
    for i, (i_lo, i_hi) in enumerate(tups):
        for k, (k_lo, k_hi) in enumerate(tups):
            if (k_lo >= i_lo and k_lo < i_hi) and (k_hi < i_hi and k_hi > i_lo):
                remove.append(tups[k])
    for r in remove:
        for t in tups:
            if t == r:
                tups.remove(r)

    # pass 2
    add = []
    remove = []
    tups = sorted(tups)
    for i, (i_lo, i_hi) in enumerate(tups):
        for k, (k_lo, k_hi) in enumerate(tups):    
            if (k_lo > i_lo and k_lo < i_hi) and (k_hi > i_hi and k_hi > i_lo):
                tup = (i_lo, k_hi)
                add.append(tup)
                remove.append(tups[i])
                remove.append(tups[k])
    for r in remove:
        for t in tups:
            if t == r:
                tups.remove(r)
    for a in add:
        tups.append(a)

    # pass 3
    tups = sorted(tups)
    add = []
    remove = []
    for i, (i_lo, i_hi) in enumerate(tups):
        for k, (k_lo, k_hi) in enumerate(tups):    
            if (k_lo > i_lo and k_lo < i_hi) and (k_hi > i_hi and k_hi > i_lo):
                tup = (i_lo, k_hi)
                add.append(tup)
                remove.append(tups[i])
                remove.append(tups[k])
    for r in remove:
        for t in tups:
            if t == r:
                tups.remove(r)
    for a in add:
        tups.append(a)
        
    tups = sorted(tups)
    print('Non-intersecting Intervals:')
    for t in tups:
        print(t)
    print()
    print('Non-intersecting Intervals in order of size:')
    size = []
    for i, (i_lo, i_hi) in enumerate(tups):
        t = (abs(i_hi-i_lo), i)
        size.append(t)
    for i, (value) in enumerate(sorted(size)):
        print(tups[value[1]])
main()
