numbers = list(range(1, 46))
for i, item in enumerate(numbers):
    if (i + 1) % 6 == 0:
        print(item)
    else:
        print(item, end=' ')
