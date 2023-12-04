from collections import defaultdict
_, m = list(map(float, input().split()))
numbers = list(map(float, input().split()))
numbers.sort(reverse=True)

tree = [1]

prob_best = 0
for i in range(len(numbers)):
    nn = len(tree)
    current = [0] * (nn + 2)
    prob = 0
    for j in range(nn):
        up = tree[j] * numbers[i]
        down = tree[j] * (1 - numbers[i])

        jj = j + 1

        current[jj + 1] += up
        current[jj - 1] += down


        # up = val * numbers[i]
        # down = val * (1 - numbers[i])
        # current[key + 1] += up
        # current[key - 1] += down
        key = jj - ((nn - 1) // 2)

        if key >= m:
            prob += up
        if key - 1 >= m:
            prob += down
    
    # print(prob)

    if prob >= prob_best:
        prob_best = prob
    tree = current

print(prob_best)
