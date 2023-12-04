n, m = list(map(int, input().split()))
numbers = list(map(float, input().split()))
numbers.sort(reverse=True)
# numbers = [int(i * 10**7) for i in numbers]

# print(numbers)
# print(len(numbers))
# @profile
def main():
    tree = []
    keys = []
    for i in range(n + 1):
        tree.append([0] * (n + 1))
        keys.append(range(-i - 1, i + 2, 2))
    tree[0][0] = 1
    # print(keys)

    prob_best = 0
    for i in range(n):
        # keys = range(-i - 1, i + 2, 2)
        nn = i + 1
        prob = 0
        for j in range(nn):
            up = tree[i][j] * numbers[i]
            down = tree[i][j] * (1 - numbers[i])

            print(i, j, up, down)
            tree[i + 1][j + 1] += up
            tree[i + 1][j] += down

            if keys[i][j + 1] >= m:
                prob += up
            if keys[i][j] >= m:
                prob += down

        if prob >= prob_best:
            prob_best = prob

    # print(tree)
    print(prob_best)
main()