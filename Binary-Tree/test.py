
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(matrix)

### Rows
print(len(matrix))

### Columns
print(len(matrix[0]))

m = len(matrix)
n = len(matrix[0])

left, right = 0, m * n - 1
print(left)
print(right)

## Formula for getting the row  and column index

mid = (left + right) // 2

row, col = divmod(mid, n)

## Formula for getting the row index

i = mid // n

print(i)

## Formula for getting the column index

j = mid % n

print(j)
