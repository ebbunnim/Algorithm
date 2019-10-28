arr = [0]*5
max_len = 0
for i in range(5):
    arr[i] = input()
    if len(arr[i]) >= max_len:
        max_len = len(arr[i])
print(arr)
print(max_len)
result = ''
for j in range(max_len):
    for i in range(5):
        if not arr[i][j]:
            continue
        result += arr[i][i]
print(result)