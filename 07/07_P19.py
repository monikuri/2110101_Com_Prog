inventory = []
with open('inventory.txt') as f:
    for line in f:
        line_data = line.strip().split(';')
        line_data[2] = int(line_data[2])
        inventory.append(line_data)
while True:
    args = input().strip().split()
    if args[0] == 'Q':
        print('Bye!')
        break
    elif args[0] in ['T','U']:
        found = False
        for i, item in enumerate(inventory):
            if item[0] == args[1]:
                found = True
                inventory[i][2] = (item[2] if args[0] == 'T' else 0) + int(args[2])
                print(inventory[i])
                break
        if not found:
            print('Product code does not exist.')
    elif args[0] == 'A':
        if args[1] not in [e[0] for e in inventory]:
            item = [args[1],args[2],int(args[3])]
            inventory.append(item)
            print(item)
        else:
            print('Duplicate product code.')
    elif args[0] == 'D':
        found = False
        for i, item in enumerate(inventory[:]):
            if item[0] == args[1]:
                found = True
                inventory.pop(i)
                print(args[1],'deleted')
                break
        if not found:
            print('Product code does not exist.')