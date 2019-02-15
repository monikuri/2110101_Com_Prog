s = input()
longest = 0
current_length = 0
last_char = ""
s = s.lower()
for c in s:
    if c != last_char:
        if current_length > longest:
            longest = current_length
        current_length = 1
        last_char = c
    else:
        current_length += 1
if current_length > longest:
    longest = current_length
print(longest)