s = input().replace(' ','').lower()
print('yes' if s[::-1] == s else 'no')  