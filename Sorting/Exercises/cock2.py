def divide_array(arr):
    zero_second_values = []
    rest_tuples = []
    for cost, weight in bunches:
        if weight == 0:
            zero_second_values.append((cost, weight, 0))
        else:
            rest_tuples.append((cost, weight, cost / weight))
    return zero_second_values,rest_tuples
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if (left[i][0] / left[i][1]) > (right[j][0] / right[j][1]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def maximum_cost(N, W, bunches):
    zero_array, rest_array = divide_array(bunches)
    bags_rest = merge_sort(rest_array)
    total_array = zero_array + bags_rest
    total_cost = 0
    toatal_weight = 0

    for cost, weight, cost_per_weight in total_array:
        if toatal_weight >= W:
            break

        if toatal_weight + weight <= W:
            total_cost += cost
            toatal_weight += weight
        else:
            cap = W - toatal_weight
            total_cost += (cost * cap) / weight
            toatal_weight = W

    return int(total_cost)

if __name__=='__main__':
    N, W = map(int,input().split())
    bunches = []
    for i in range(N):
        bunches.append(tuple(map(int,input().split())))
    cost = maximum_cost(N,W,bunches)
    print(cost)