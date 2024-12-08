from collections import deque

def min_of_max_in_subarrays(arr, k):
    n = len(arr)
    dq = deque()  
    max_values = []

   
    for i in range(k):
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)

    for i in range(k, n):
        max_values.append(arr[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)

    max_values.append(arr[dq[0]])

    return min(max_values)

k = int(input())
n = int(input())
arr = list(map(int,input().split()))

result = min_of_max_in_subarrays(arr, k)
print(result)
