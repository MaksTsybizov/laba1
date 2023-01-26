# -- coding: utf-8 --
ez1 = ez2 = 0
r = int(input())
while r != 0:
    if r > ez1:
        ez2 = ez1
        ez1 = r
    elif ez2 < r:
        ez2 = r
    r = int(input())
print(ez2)
