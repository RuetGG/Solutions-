if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    x = float('-inf')
    size = len(arr)

for y in arr:
    if y < max(arr) and y > x:
        x = y
print(x)
