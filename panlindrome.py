n = 3443

original_n = n  # Store the original value of n

palindrome_check = 0

while(n > 0):
    ld = n % 10
    palindrome_check = (palindrome_check * 10) + ld
    n = n // 10

print("Reversed number:", palindrome_check)

# Compare palindrome_check with the original value of n
var = ("yes" if palindrome_check == original_n else "no")
print("Is it a palindrome?", var)
