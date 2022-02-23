def reverse_stack(st):
    #base condition
    if len(st) == 1:
        return

    # Hypothesis
    tos = st.pop(len(st)-1)
    reverse_stack(st)

    #induction
    insert(st, tos)

def insert(st, x):
    #base condition
    if len(st) == 0:
        st.append(x)
        return

    #hypothesis
    temp = st.pop(len(st)-1)
    insert(st, x)

    #induction
    st.append(temp)


st = [1, 4, 2, 3]
print("before reverse: ", st)
reverse_stack(st)
print("after reverse: ", st)
