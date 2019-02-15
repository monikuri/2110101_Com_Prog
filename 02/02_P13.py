import math
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
time = (h2*60 + m2) - (h1*60+ m1)
if time <= 15:
    print(0)
elif time <= 3*60:
    print(math.ceil(time/60)*10)
elif time <= 6*60:
    print(30 + math.ceil((time - 3*60)/60)*20)
else:
    print(200)