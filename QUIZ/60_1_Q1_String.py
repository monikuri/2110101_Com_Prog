file = open(input().strip())
pattern = ''
mode = -1
for i,s in enumerate(file):
   s = s.strip()
   if i == 0:
      if s == 'T2M':
         mode = 0
      elif s == 'M2T':
         mode = 1
      else:
         break
   elif i == 1:
      pattern = s
   else:
      invalid = False
      output = ''
      if mode == 0:
         for e in s:
            j = pattern.find('[' + e + ']')
            if j == -1:
               invalid = True
               break
            j += 3
            k = pattern.find('[',j)
            output += pattern[j:k] + ' '
      elif mode == 1:
         for code in s.split():
            j = pattern.find(']' + code + '[')
            if j == -1:
               invalid = True
               break
            output += pattern[j-1:j]
      if not invalid:
         print(output.strip())
      else:
         print('Invalid :',s)
if mode == -1:
   print('Invalid code')