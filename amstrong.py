n = 153
n1 = n
amstrong = 0

# for i in n:
#     cube = i*i*i
#     amstrong = amstrong+cube
#
# print(amstrong)

while (n > 0):
    temp = n%10
    amstrong = temp*temp*temp+amstrong
    n = n//10

if amstrong == n1:
    print("Amstrong")
