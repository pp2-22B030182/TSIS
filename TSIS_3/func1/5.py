from itertools import permutations
st = input()


def permutate(string):
    for i in permutations(string):
        print(''.join(i))


permutate(st)