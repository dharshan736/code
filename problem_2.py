def bees_between_flowers(s, startIndex, endIndex):
    n = len(s)
    bee_prefix = [0] * (n + 1)
    left_flower = [-1] * n
    right_flower = [-1] * n

    last_flower = -1
    for i in range(n):
        if s[i] == '|':
            last_flower = i
        left_flower[i] = last_flower
        bee_prefix[i + 1] = bee_prefix[i] + (1 if s[i] == '*' else 0)

    last_flower = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_flower = i
        right_flower[i] = last_flower

    results = []
    for start, end in zip(startIndex, endIndex):
        start -= 1  
        end -= 1

        left = right_flower[start]
        right = left_flower[end]

        if left != -1 and right != -1 and left < right:
            results.append(bee_prefix[right + 1] - bee_prefix[left + 1])
        else:
            results.append(0)

    return results

# Input handling
s = input()
n = int(input())
startIndex = list(map(int,input().split()))
endIndex = list(map(int,input().split()))

results = bees_between_flowers(s, startIndex, endIndex)
print(results)
