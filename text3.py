import math

def num(n):
    #equation 1
    sum = [0] * n
    sum[0], sum[1] = 0, 1
    
    # The equation used
    int = 2
    while int < n:
        sum[int] = 2 * sum[int - 1] + sum[int - 2]
        int += 1
    
    print(sum)

# Calculate and display the first 10 Pell numbers
n = 10
seq = num(n)
print("First", n, seq)