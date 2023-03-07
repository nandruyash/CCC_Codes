def countInversions(arr, l, r):
    if l >= r:
        return 0

    m = (l + r) // 2
    count = countInversions(arr, l, m) + countInversions(arr, m+1, r)

    i = l
    j = m + 1
    temp = []
    inversions = 0

    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            inversions += m - i + 1

    temp.extend(arr[i:m+1])
    temp.extend(arr[j:r+1])
    arr[l:r+1] = temp

    return count + inversions

n = int(input())
arr = [int(input()) for _ in range(n)]

print(countInversions(arr, 0, n-1))