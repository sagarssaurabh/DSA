'''  we have to print all possible subset of a given input '''


def print_subset(out, inp):
    # base condition: when we have no letters left in input
    if len(inp) == 0:
        print(out)
        return

    # hypothesis: we have two choices at each step , either we consider inp[0] or not
    out1 = out
    out2 = out
    temp = inp[0]
    inp = inp[1:]
    print_subset(out1, inp)
    print_subset(out2+temp, inp)


output = ''
inputt = 'aac'
print_subset(output, inputt, )
