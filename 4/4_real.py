p, q = [int(i) for i in input().split()]
def is_odd(n):
    return n % 2 == 1

def is_even(n):
    return n % 2 == 0

def manual(p, q):
    if is_odd(p) and is_odd(q):
        return 1
    if is_even(p):
        return 0
    
    if p > q:
        return 0
    else:
        return 2

print(manual(p, q))