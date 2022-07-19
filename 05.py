a = input()

def solution(a):
    for c in a:
        if c != "." and c != '':
            a += c
    size = len(a)
    for i in range(size//2):
        if a[i] != a[size-1-i]:
            return 0
    return 1

print(solution(a))
