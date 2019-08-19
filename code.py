def bin_hex(binarystring):
    d = {'10':'a','11':'b','12':'c','13':'d','14':'e','15':'f'}
    binarystring = list(reversed(binarystring))
    l = []
    l1 = []
    l2 = []
    l3 = []
    for i in range((len(binarystring) // 4) + 1):
            l.append(''.join(binarystring[0:4]))
            del binarystring[0:4]
    for x in l:
            for y in x:
                    l1.append((2 ** int(x.index(y))) * int(y))
                    x = x.replace(y,' ',1)
    for i in range((len(l1) // 4) + 1):
            l2.append(sum(l1[0:4]))
            del l1[0:4]
    l2 = [str(x) for x in l2]
    l2.reverse()
    for x in l2:
            if x in d:
                    l3.append(d[x])
            else:
                    l3.append(x)
    l3 = ''.join(l3)
    if l3.count('0') != len(l3):
            l3 = l3.lstrip('0')
    return l3
