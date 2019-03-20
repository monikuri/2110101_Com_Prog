n = int(input())
words = []
freq_map = {}
for i in range(n):
    # todo: change to \t
    pos, word = input().split('\t')
    words.append(word)
    prefix = word[:2]
    if prefix not in freq_map:
        freq_map[prefix] = []
    freq_map[prefix].append(i)
prefix = ''
max_len = -1
for key in freq_map:
    pref_len = len(freq_map[key])
    if prefix == '':
        prefix = key
        max_len = pref_len
        continue
    if pref_len > max_len or (pref_len == max_len and key < prefix):
        max_len = pref_len
        prefix = key
print(prefix)
print(max_len)
for index in freq_map[prefix]:
    print(words[index])