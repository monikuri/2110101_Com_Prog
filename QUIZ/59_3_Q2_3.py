dna = input().strip().upper()
task = input()
invalid = False
for c in dna:
    if c not in 'ATGC':
        invalid = True
        break
if invalid:
    print('Invalid DNA')
else:
    if task == 'R':
        new_dna = ""
        dna_map = {'A':'T','G':'C','T':'A','C':'G'}
        for c in dna:
            new_dna += dna_map[c]
        print(new_dna[::-1])
    elif task == 'F':
        f = {'A':0,'T':0,'G':0,'C':0}
        for c in dna:
            f[c] += 1
        print("A=%d, T=%d, G=%d, C=%d"%(f['A'],f['T'],f['G'],f['C']))
    elif task == 'D':
        pair = input().strip().upper()
        count = 0
        for i in range(0,len(dna)-1):
            if dna[i:i+2] == pair:
                count += 1
        print(count)