import sys
input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    s = list(map(int, input().strip()))
    ones_pos = set(i for i, v in enumerate(s) if v == 1)

    ops = []
    m = n // 2

    for x in range(1, m + 1):
        if len(ones_pos) <= 7:
            ops.append(0)
            continue

        done = False

        # Try to find a pair (i, i+x) both are 1
        # We iterate over ones positions (fast enough because ones decrease quickly)
        for i in list(ones_pos):
            j = i + x
            if j < n and j in ones_pos:
                # flip both 1->0
                ones_pos.remove(i)
                ones_pos.remove(j)
                ops.append(i + 1)  # 1-based l
                done = True
                break

        if not done:
            ops.append(0)

    out.append(" ".join(map(str, ops)))

print("\n".join(out))
