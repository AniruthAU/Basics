n = 2
import math

cnt = 0

for i in range(1, int(math.sqrt(n)) + 1):
    # If n is divisible by i
    # without any remainder.
    if n % i == 0:
        # Increment the counter.
        cnt = cnt + 1

        # If n is not a perfect square,
        # count its reciprocal factor.
        if n // i != i:
            cnt = cnt + 1
