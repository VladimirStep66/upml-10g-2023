def v11(n, arr):
    for i in range(n):
        arr.append(int(input()))
    min_el = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_el:
            min_el = arr[i]
    return min_el
