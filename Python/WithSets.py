a = [a for a in range(1,101) if a%3 == 0]
b = [b for b in range(1,101) if b%5 == 0]
a = set(a)
b = set(b) 
fizz = a.difference(b)
buzz = b.difference(a)
fizzbuzz = a.intersection(b)
for i in range (1,101):
    if i in fizz:
        print ('fizz',end = ',')
    elif i in buzz:
        print ('buzz',end = ',')
    elif i in fizzbuzz:
        print ('fizzbuzz',end = ',')
    else:
        print (i, end = ',')
