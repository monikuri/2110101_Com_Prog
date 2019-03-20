addr = {}
with open('address.txt') as f:
    for line in f:
        args = line.strip().split()
        name = args[0] + ' ' + args[1]
        phone = args[2]
        addr[name] = phone
while True:
    args = input().strip().split()
    if len(args) == 0:
        break
    # Phone no.
    if args[0].isdigit():
        found = False
        phone = args[0]
        for item in addr:
            if phone == addr[item]:
                print(item)
                found = True
                break
        if not found:
            print('Not Found')
    else:
        name = args[0] + ' ' + args[1]
        if name in addr:
            print(addr[name])
        else:
            print('Not Found')