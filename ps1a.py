n, B = list(map(int, input().strip().split()))
T = 0

while True:
  y = 0
  for i in range(1, n + 1):
    if (i % 2 == 0):
      p = 2 ** i + 1
    else:
      p = 3 ** i +1

    eq = (p ** (n - i))

    eq *= T
    
    y += eq
    
  if y < B:
    T += 1
    if(T > 10000):
      print("-1")
  else:
    break
print(T)