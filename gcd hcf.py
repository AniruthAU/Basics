def find_gcd(a,b):

    while a > 0 and b > 0:
        if a> b:
            a = a%b

        else:
            b = b%a
    if a == 0:
        return  b
    else:
        return  a

# print(find_gcd(20,15))

a = 20
b = 15
for i in range(min(a,b),0 , -1 ):
    if a % i == 0 and b%i ==0 :
        print(i)

