flag = 0
n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = float(input("Enter element : "))
    arr.append(d)
for i in range(0, n - 2):
    for j in range(i+1, n - 1):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] < 2 and arr[i] + arr[j] + arr[k] > 1:
                flag = 1
                break
        if flag==1:
            break
    if flag==1:
        break

if flag == 1:
    print("Possible: ", arr[i], arr[j], arr[k])
else:
    print("Not possible")
