from itertools import combinations

def combs(input):
    return sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])  
