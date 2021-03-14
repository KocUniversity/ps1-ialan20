n, B = list(map(int, input().strip().split()))
T = 0

max = 10000
min = 0

while True:
  y = 0
  while True:
    T = (max + min) / 2
    for i in range(1, n + 1):
      if (i % 2 == 0):
        p = 2 ** i + 1
      else:
        p = 3 ** i +1

      eq = (p ** (n - i))

      eq *= T
      
      y += eq
    
  break
print(T)            