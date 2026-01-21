import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    line = input().strip()

    if " " in line:
        s = list(map(int, line.split()))
    else:
        s = list(map(int, line))

    ones = sum(s)
    ops = []

    for x in range(1, n // 2 + 1):
        done = False

        for l in range(n - x):
            if s[l] == 1 and s[l + x] == 1:
                s[l] ^= 1
                s[l + x] ^= 1
                ones -= 2
                ops.append(l + 1)  # 1-based index
                done = True
                break

        if not done:
            ops.append(0)

    print(*ops)
