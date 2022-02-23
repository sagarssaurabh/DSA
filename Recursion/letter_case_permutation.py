# PS : We are given a lower case input, and we need to find all permutation possible with case change
#  but input also contain digit, so we need to ignore them example a1b2 -> a1b2, a1B2,A1b2,A1B2
def letter_case_permutation(output, inp):
    # base condition: when input is empty
    if len(inp) == 0:
        print(output)
        return

    # hypothesis: we have to choices for each letter in input either change case of not, and digits to be ignored
    temp = inp[0]
    inp = inp[1:]
    if temp.isalpha():
        letter_case_permutation(output + temp.lower(), inp)
        letter_case_permutation(output + temp.upper(), inp)
    else:
        letter_case_permutation(output+temp, inp)


letter_case_permutation('', 'a1b2')
