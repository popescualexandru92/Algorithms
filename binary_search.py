import numpy as np

np.random.seed(1)

a = np.random.randint(0, 100, 50)
a = sorted(a)

print(a)

find = 15

steps = 0


def search(a, ls, ld, target):
    global steps
    steps += 1
    if ls <= ld:
        mid = ls+(ld-ls)//2
        print(mid)
        if target == a[mid]:
            print("found")
            return a[mid]

        elif target < mid:
            return search(a, ls, mid-1, target)
        else:
            return search(a, mid+1, ld, target)
    else:
        print("Not found")
        


search(a, 0, len(a)-1, 2)
print(steps)
