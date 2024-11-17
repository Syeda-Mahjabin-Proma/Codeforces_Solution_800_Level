n, h = map(int, input().split())
arr = list(map(int, input().split()))
check = []
temp = 0
for i in range(len(arr)):
    if arr[i] % h == 0:
        temp += arr[i]//h
    else:
        temp += arr[i]//h + 1

print(temp)
