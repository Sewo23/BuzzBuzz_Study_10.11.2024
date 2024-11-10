
'''
Kod ma za zadanie wypisać liczby od 1 do 100,
gdzie wyspisać w miejsce wielokrotności, kolejno:
3 - 'Fizz'
5 - 'Buzz'
3 i 5 - 'FizzBuzz'
'''

for num in range (1,101):
  if num % 3 == 0 and num % 5 == 0:
    print ('FizzBuzz')
  elif num % 3 == 0:
    print ('fizz')
  elif num % 5 == 0:
    print ('buzz')
  else:
    print (num)