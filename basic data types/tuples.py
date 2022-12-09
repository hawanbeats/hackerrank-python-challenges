n = int(input())
s = [int(num) for num in input().strip().split(' ')]
s = tuple(s)
print(hash(s))
