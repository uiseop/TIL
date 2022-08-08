from collections import defaultdict
import sys

input = sys.stdin.readline

tree = defaultdict(int)

n = 0

while True:
    t = input().rstrip()
    if not t: break
    tree[t] += 1
    n += 1

sorted_tree = sorted(tree.items())
for t,c in sorted_tree:
    print(f"{t}  {format(round(100 * c/n,4), '.4f')}")