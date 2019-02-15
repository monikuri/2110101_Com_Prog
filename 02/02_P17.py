n = int(input())
if n < 0 or n > 80:
    print('Error: Out of range')
else:
    out = ""
    out = str(n%3) + out
    n //= 3
    out = str(n%3) + out
    n //= 3
    out = str(n%3) + out
    n //= 3
    out = str(n%3) + out
    print(out)