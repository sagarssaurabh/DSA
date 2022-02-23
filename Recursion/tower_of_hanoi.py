# PS: we are given three tower source, helper and destination and we need to move n disks from source to
# destination with certain criteria:
# 1.All disks are of different weights and most heavy should be at bottom and most light disk at the top
# 2.a heavier disk cannot be placed over a lighter one
# 3.we can only move one disk at a time

def tower_of_hanoi(number_of_disks, source, helper, destination):
    # base condition : when there is no disk left at source
    if number_of_disks == 0:
        return

    # hypothesis: we move n-1 disks from source to helper , so source is source , destination becomes helper and
    # helper becomes destination
    tower_of_hanoi(number_of_disks-1, source, destination, helper)

    # move nth disk from source to destination
    print('moving disk from ', source, '->', destination)

    # induction:we can assume that above call have moved n-1 disks from source to helper now we need to move these
    # disks from helper to destination , so helper becomes source, source becomes helper and destination is destination
    tower_of_hanoi(number_of_disks-1, helper, source, destination)


s = 1
h = 2
d = 3
tower_of_hanoi(12, s, h, d)
