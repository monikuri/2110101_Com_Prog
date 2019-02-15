a1, b1, c1 = [int(i) for i in input().split()]
a2, b2, c2 = [int(i) for i in input().split()]
if a1*b2 - a2*b1 != 0:
    print('one solution')
else:
    if a1 == 0 and a2 == 0 and b1 == 0 and b2 == 0:
        print('no solution')
    elif b1 == 0 and b2 == 0:
        if a1 == 0 or a2 == 0:
            print('no solution')
        elif -c1/a1 == -c2/a2:
            print('many solution')
        else:
            print('no solution')
    elif a1 == 0 and a2 == 0:
        if b1 == 0 or b2 == 0:
            print('no solution')
        elif -c1/b1 == -c2/b2:
            print('many solution')
        else:
            print('no solution')
    elif c1/b1 == c2/b2:
        print('many solutions')
    else:
        print('no solution')