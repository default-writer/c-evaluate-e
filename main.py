'''Дано число A (> 1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 1/2 + … + 1/K будет меньше A, и саму эту сумму. '''

def S(A):
  if A == 0: return 0
  return S(A-1) + 1/A

def f(I, S, K):
  s=S
  k=K
  if i == 1:
    return 1.0, 1
  if s >= 0:
    while s < I:
      k += 1
      s += 1/k
  return s, k

s = 0
k = 1
k_old = 0

for i in range(1,16):
  k_old = k
  s, k = f(i, s, k)
  print(k, s - 1/k)

print(f"e = {k/k_old}")
