import re

sound = input()

answer = re.fullmatch('(100+1+|01)+',sound)

print("SUBMARINE" if answer else "NOISE")