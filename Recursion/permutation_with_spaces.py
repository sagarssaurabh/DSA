# We are given an input, and we need to find all permutation with and without spaced between each letter

def permutation_with_spaces(out, inp):
    # base condition: when inp length is 0
    if len(inp) == 1:
        out = out + inp
        print(out)
        return

    out1 = out + inp[0]
    out2 = out + inp[0]
    inp = inp[1:]
    permutation_with_spaces(out1+' ', inp)
    permutation_with_spaces(out2, inp)


output = ''
inputt = 'abc'
permutation_with_spaces(output, inputt)
