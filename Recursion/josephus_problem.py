# PS: N person are standing in circle, given a number k, starting from 1st person we have to kill
# every kth person and this will go on until single person is remaining. we have to return its index
def josephus(person, step, index):
    # Base Condition: when we have single person remaining we have our answer
    if len(person) == 1:
        print(person[0], 'is winner')
        return

    # hypothesis :
    index = (index+step) % len(person)
    x = person.pop(index-1)
    print(x, 'is killed.')
    josephus(person, step, index)


n = 11
k = 7
persons = [i for i in range(1, n+1)]
josephus(persons, k-1, 1)
