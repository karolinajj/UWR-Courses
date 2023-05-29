
def p1(n):
  n = n+1
  return [(a,b,c) for a in range(1,n) for b in range(1,n) for c in range(1,n) if (a*a + b*b == c*c and a < b)]

def primes(n):
  n = n+1
  return [a for a in range(2,n) if all(a % i != 0 for i in range(2,a))]

def flatten(L):
  return [L[i][j] for i in range(len(L)) for j in range(len(L[i]))]

def transpose(M):

  return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]



print(p1(10))
print(flatten([[1,2,4],['a']]))
print(primes(11))

M = [[1,2,4],[4,5,6]]
print(transpose(M))
