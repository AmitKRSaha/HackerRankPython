def checkIfelse(n):
    if n%2 != 0:
        print('Weird')
    else:
        if n in range(2,5):
            print ('Not Weird')
        if n in range(6, 20):
            print ('Weird')
        if n > 20:
            print ('Not Weird')

def arithmaticOperation(a, b):
    print(a+b)
    print(a-b)
    print(a*b)

def division(a,b):
    print(int(a/b))
    print(a/b)

def loops(n):
    for x in range(0, n):
        print(x * x)

def is_leap(year):
    leap = False
    
    if year%4 == 0 and year%100 == 0 and year%400 == 0:
        leap = True
    else:
        if year%4 == 0 and year%100 != 0 and year%400 != 0:
            leap = True
        else:
            leap = False
    
    print(leap)

def printInteger(n):
    print(*range(1,n+1),sep='')

def swap_case(s):
    finalCombination =''
    for x in s:
        if x.isupper():
            finalCombination = finalCombination + x.lower()
        else: 
            finalCombination = finalCombination + x.upper()
    print(finalCombination)

    


