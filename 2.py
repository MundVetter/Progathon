from collections import defaultdict
_, m = list(map(float, input().split()))
numbers = list(map(float, input().split()))
numbers.sort(reverse=True)

tree = defaultdict(lambda: 0)
tree[0] = 1

prob_best = 0
for i in range(len(numbers)):
    current = defaultdict(lambda: 0)
    prob = 0
    for key, val in tree.items():
        up = val * numbers[i]
        down = val * (1 - numbers[i])
        current[key + 1] += up
        current[key - 1] += down

        if key + 1 >= m:
            prob += up
        if key - 1 >= m:
            prob += down
    
    # print(prob)

    if prob >= prob_best:
        prob_best = prob
    tree = current

print(prob_best)
