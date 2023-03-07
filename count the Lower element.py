n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

for bj in b:
    # binary search to find the index of the largest element in a that is <= bj
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] <= bj:
            left = mid + 1
        else:
            right = mid - 1
    # print the number of elements in a that are <= bj
    print(left, end=" ")