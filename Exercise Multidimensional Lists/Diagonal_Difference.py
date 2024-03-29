n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

primary, secondary = 0, 0

for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n - i - 1]

print(abs(primary - secondary))
