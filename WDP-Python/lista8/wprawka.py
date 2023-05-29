liczby = {
  1 : 'jeden',
  2 : 'dwa',
  3 : 'trzy',
  4 : 'cztery',
  5 : 'pięć',
  6 : 'sześć',
  7 : 'siedem',
  8 : 'osiem',
  9 : 'dziewięć',
  10 : 'dziesięć',
  11 : 'jedenaście',
  12 : 'dwanaście',
  13 : 'trzynaście',
  14 : 'czternaście',
  15 : 'piętnaście',
  16 : 'szesnaście',
  17 : 'siedemnaście',
  18 : 'osiemnaście',
  19 : 'dziewiętnaście',
  20 : 'dwadzieścia',
  30 : 'trzydzieści',
  40 : 'czterdzieści',
  50 : 'pięćdziesiąt',
  60 : 'sześćdziesiąt',
  70 : 'siedemdziesiąt',
  80 : 'osiemdziesiąt',
  90 : 'dziewięćdziesiąt',
  100 : 'sto',
  200 : 'dwieście',
  300 : 'trzysta',
  400 : 'czterysta',
  500 : 'pięćset',
  600 : 'sześćset',
  700 : 'siedemset',
  800 : 'osiemset',
  900 : 'dziewięćset'
}


def tekstowa(n):
  s = ''
  
  if n%100 < 20:
    s = liczby[n]
  else:
    jednosci = n%10
    setki = (n//100)*100
    dziesiatki = n - setki - jednosci
  
    if setki in liczby:
      s += liczby[setki]
    if dziesiatki in liczby:
      s += ' ' + liczby[dziesiatki]
    if jednosci in liczby:
      s += ' ' + liczby[jednosci]
    
  return s

def czy_liczba(n):
  for e in n:
    if e < '0' or e > '9':
      return False
  return True
    
def napis_z_liczbami(L):
  s = ''
  for e in L:
    if czy_liczba(e):
      e = tekstowa(int(e))
    
    s += ' ' + e
  return s
      
  

L = ['ala', 'ma', '125', 'kotów', 'i', '12', 'psów']

print(napis_z_liczbami(L))
