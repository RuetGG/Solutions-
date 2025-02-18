# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict


k = int(input())
s = input()
my_dict = defaultdict(int)
my_dict[0] = 1
count = 0
pre = 0
for char in s:
    pre += int(char)
    if pre - k in my_dict:
        count += my_dict[pre - k]
    my_dict[pre] += 1
print(count)