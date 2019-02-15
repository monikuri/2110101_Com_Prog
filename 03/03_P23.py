# Print repeated chars
def print_repeat(char,n):
   for i in range(n):
      print(char,end='')

n = int(input())
# Top (2 triangles)
for i in range(n//2):
   for j in range(3):
      if j == 1:
         print_repeat('.',1)
      else:
         print_repeat('.',(n//2)-(i+1))
         print_repeat('#',n - 2*(n//2-i-1))
         print_repeat('.',(n//2)-(i+1))
   print('')
         
# Mid (full row)
for i in range(n//2-2):
   print_repeat('#',2*n+1)
   print('')
# Bottom (inverted triangle)
for i in range(n+1):
   print_repeat('.',i)
   print_repeat('#',1+2*(n-i))
   print_repeat('.',i)
   print('')