# PS: we are given n which is number of opening and closed paranthesis. we have to print all possible
# valid balanced combination using those paranthesis

def balanced_paranthesis(output, opening, closing):
    # base condition: when opening and closing brackets both are zero
    if opening == 0 and closing == 0:
        print(output)
        return

    # hypothesis:At every step we can choose either opening or closing and we can use opening bracket
    # any time but closing brackets only when it is greater than opening otherwise it will not generate
    # valid combination.
    if opening:
        opening -= 1
        output += '('
        balanced_paranthesis(output, opening-1, closing)

    if closing > opening:
        closing -= 1
        output += ')'
        balanced_paranthesis(output, opening, closing-1)

n=3
open_bracket = n
close_bracket = n
outpt = ''
balanced_paranthesis(outpt, open_bracket, close_bracket)