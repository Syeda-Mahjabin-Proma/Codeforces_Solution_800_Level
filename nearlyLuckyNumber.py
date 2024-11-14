num = int(input())
count = 0
for val in str(num):
    if val == "4":
        count += 1
    if val == "7":
        count += 1

if count == 4 or count == 7:
    print("YES")

else:
    print("NO")
