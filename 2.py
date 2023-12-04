from collections import defaultdict
_, m = list(map(float, input().split()))
numbers = list(map(float, input().split()))
numbers.sort(reverse=True)

# print(len(numbers))
# create a tree of all options
# two options yes or no and two outcomes
tree = defaultdict(lambda: 0)
tree[0] = 1

prob_best = 0
for i in range(len(numbers)):
    current = defaultdict(lambda: 0)
    for key, val in tree.items():
        current[key + 1] += val * numbers[i]
        current[key - 1] += val * (1 - numbers[i])
        # case 2: we lose with prob 1 - numbers[i]
        # current.append([tree[j][0] - 1, tree[j][1] * (1 - numbers[i])])

    # calculate prob we of having at least m wins, check if prob is higher than pass_m_prob
    # replace tree with current and pass_m_prob with new prob
    prob = 0
    for key, value in current.items():
        if key >= m:
            prob += value
    # print(prob, past_prob, tree, current)
        # total_outcomes += value[1]
    if prob >= prob_best:
        prob_best = prob
    tree = current

print(prob_best)
