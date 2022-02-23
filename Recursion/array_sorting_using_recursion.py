def sort_list(lst):
    #base_condition
    if len(lst)==1:
        return

    #hypothesis(in this step we expect our function to perform certain thing): take out an element and recursively
    # call this function assuming it will return sorted array and
    # we just have to insert this element to its correct position
    temp = lst.pop(len(lst)-1)
    sort_list(lst)

    #induction:we assume after returning from sort_list function the list is sorted , so in induction we write
    # logic of what we want our function to do
    insert(lst, temp)

def insert(lst, x):
    #we will write this function also in form of recursion
    # 1.Base condition:
    if len(lst) == 0 or lst[-1] <= x:
        lst.append(x)
        return

    # 2.Hypothesis: (Here we expect our fuction to insert x at its correct poisiton) As condition lst[-1] <= x
    # failed, so we remove lst[-1] element and try to insert x in remaining list
    temp = lst.pop(len(lst)-1)
    insert(lst, x)

    # 3.Induction (what we want our function to do) : as we know we get a sorted list and x whom we have to insert
    # at correct postion. Now in above hypothesis we have assumed that x is inserted to its correct position now we
    # have to append all elements that we have popped previously
    lst.append(temp)

ar = [1,4,2,7,3]
sort_list(ar)
print(ar)

