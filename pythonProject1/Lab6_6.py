import itertools
SCORES = [40,91,85,15]
for subset in itertools.combinations(SCORES, 2):
    print(subset)

