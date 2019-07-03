for i in range(1,101):
    if i%3==0 and i%5==0:
        print ("fizzbuzz -", end=" ")
        continue
    if i%3==0 and not i%5==0:
        print("fizz -",end=" ")
        continue
    if not i%3==0 and i%5==0:
        print("buzz -",end=" ")
        continue
    print(i," -",end=" ")
    
