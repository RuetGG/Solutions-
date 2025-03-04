# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = sorted((val, idx) for idx, val in enumerate(a))
    d = sorted(b)
    mapping = {}
    for (val, idx), new_val in zip(c, d):
        mapping[idx] = new_val

    ans = [mapping[i] for i in range(n)]

    print(*ans)