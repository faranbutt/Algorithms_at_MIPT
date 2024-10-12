import random
def quick_sort(bunches):
    zero_second_values = []
    rest_tuples = []
    for cost, weight in bunches:
        if weight == 0:
            zero_second_values.append((cost, weight, 0))
        else:
            rest_tuples.append((cost, weight, cost / weight))
    def quick_sort_bags(bunches):
        if len(bunches) > 1:
            return bunches
        else:
            pivot = bunches[random.randint(0,len(bunches)-1)]
            print(pivot)
            left = [x for x in bunches if x[2] > pivot[2]]
            right = [x for x in bunches if x[2] < pivot[2]]
            middle = [x for x in bunches if x[2] == pivot[2]]
            return quick_sort_bags(left) + middle + quick_sort_bags(right)
    sorted_c = quick_sort_bags(rest_tuples)
    return zero_second_values + sorted_c
# def sorted_coc(bags):
#     return sorted(bunches, key=lambda x: (x[0] / x[1]) if x[1] > 0 else float('inf'), reverse=True)
# def bubble_sort(data):
#     zero_second_values = []
#     rest_tuples = []
#     for cost, weight in data:
#         if weight == 0:
#             zero_second_values.append((cost, weight, 0))
#         else:
#             rest_tuples.append((cost, weight, cost / weight))
#     for i in range(len(rest_tuples)):
#         for j in range(0, len(rest_tuples)-i-1):
#           if rest_tuples[j][2] < rest_tuples[j+1][2]:
#               rest_tuples[j], rest_tuples[j+1] = rest_tuples[j+1], rest_tuples[j]
#     return zero_second_values+rest_tuples

def maximum_cost(N, W, bunches):
    bags = quick_sort(bunches)
    print(bags)
    total_cost = 0
    toatal_weight = 0

    for cost, weight, cost_per_weight in bags:
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
