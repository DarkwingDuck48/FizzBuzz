for x in range(1,int(input())):
    print("Fizz"[x%3*4:]+"Buzz"[x%5*4:]or x,end = ",")
