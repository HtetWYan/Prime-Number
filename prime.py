print(2)
print(3)
for i in range(1,n):
    x = (6 * i)- 1
    y = (6 * i) + 1
    if x % 5 != 0 and x % 7 != 0:
        print(x)
    if y % 5 != 0 and y % 7 != 0:
        print(y)
