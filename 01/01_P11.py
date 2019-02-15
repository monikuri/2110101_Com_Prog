h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
# Time in second 
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
# Diff 
dt = t2 - t1
dh = dt // (60*60)
dm = (dt - dh*(60*60)) // 60
ds = dt - dh*(60*60) - dm*60
print(str(dh)+":"+str(dm)+":"+str(ds))