s = input().lower()
search = input().lower().strip()
str_list = []
# Tokenize
token = ""
for c in s:
    if c not in [' ','\'','"','.',',']:
        token += c
    else:
        if len(token) > 0:
            str_list.append(token)
            token = ""
if len(token) > 0:
    str_list.append(token)
# Search
print('Found' if search in str_list else 'Not Found')