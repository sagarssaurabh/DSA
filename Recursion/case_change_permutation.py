# PS : We are given a lower case input, and we need to find all permutation possible with case change
# example ab -> ab, aB,Ab,AB
def case_change_permutation(output, inp):
    # base condition: when input is empty
    if len(inp) == 0:
        print(output)
        return

    # hypothesis: we have to choices for each letter in input either change case of not
    temp = inp[0].lower()
    inp = inp[1:]
    case_change_permutation(output+temp, inp)
    case_change_permutation(output+temp.upper(), inp)


case_change_permutation('', 'Ab')
