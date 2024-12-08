from collections import Counter

def find_first_odd_flavor(n, flavors):
    flavor_count = Counter(flavors)

    for flavor in flavors:
        if flavor_count[flavor] % 2 != 0:
            return flavor

    return "All are even"

n = int(input())
flavors = [input().strip() for _ in range(n)]
result = find_first_odd_flavor(n, flavors)
print([result])
