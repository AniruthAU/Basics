n = 12345
reversed_number = 0

while(n > 0):
    ld = n%10

    reversed_number = (reversed_number * 10)+ld
    print(reversed_number)

    n = n//10

print(reversed_number)