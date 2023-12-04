_ = input()
numbers = [int(i) for i in list(input())]
# print(numbers)
count = 0
choco = 0
for i in range(len(numbers)):
    if choco > 0 or numbers[i] == 1:
        choco -= 1
        count += 1
    if numbers[i] == 1:
        choco = 2
print(count)