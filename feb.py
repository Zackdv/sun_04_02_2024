a=int(input('Enter First Number:'))
b=int(input('Enter Second Number:'))

def div(arith):
    def inner(a,b):
        result=arith(a,b)
        return result
    return inner

def dive(arith):
    def inner(a,x):
        result=arith(a,x)
        return result
    return inner

@div
def divi(a,b):
    divi=a/b
    return divi

@dive
def dov(a,x):
    divi=a/x
    return divi

if b>0:
    result=divi(a,b)
    print('The Division',result)

elif b==0:
    print(a,'cannot be divided',b)
    x=int(input('Please Enter Second Number Again:'))
    result=dov(a,x)
    print('The Division:',result)
















