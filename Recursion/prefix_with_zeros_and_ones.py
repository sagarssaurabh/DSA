# PS: we are given a number n, we have to generate a binary number for which in every prefix number of zeroes
# is less than equal to ones
def binary_prefix(output, zeros, ones, n):
    # base condition : when n is equal to zero then we have n bit of binary number in output
    if n == 0:
        print(output)
        return

    binary_prefix(output+'1', zeros, ones + 1, n-1)
    if zeros < ones:
        binary_prefix(output+'0', zeros + 1, ones, n - 1)


N = 4
zero = one = 0
binary_prefix('', zero, one, N)
