def sort_bags(bunches):
    arr = []
    for cost, weight in bunches:
        if weight > 0:
            arr.append((cost, weight, cost / weight))
        else:
            arr.append((cost, weight, 0))

    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j][2] > arr[max_index][2]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


def maximum_cost(N, W, bunches):
    bags = sort_bags(bunches)
    total_cost = 0
    current_weight = 0

    for cost, weight, cost_per_gram in bags:
        if weight == 0:
            total_cost += cost
        elif current_weight >= W:
            break
        elif current_weight + weight <= W:
            total_cost += cost
            current_weight += weight
        else:
            cap = W - current_weight
            total_cost += (cost * cap) // weight
            current_weight = W

    return total_cost


if __name__ == '__main__':
    N, W = map(int, input().split())
    bunches = []

    for i in range(N):
        bunches.append(tuple(map(int, input().split())))

    cost = maximum_cost(N, W, bunches)
    print(cost)
