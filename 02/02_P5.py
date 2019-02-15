x = []
for i in range(6):
    x.append(float(input()))
mn = x[0]
mx = x[0]
for i in range(6):
    if(x[i] < mn):
        mn = x[i]
    if(x[i] > mx):
        mx = x[i]
print(mn,mx)