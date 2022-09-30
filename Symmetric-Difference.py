"""
Given two sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

set1_size = input()
my_set1 = set(map(int, input().split()))
set2_size = input()
my_set2 = set(map(int, input().split()))


diff1 = my_set1.difference(my_set2)
diff2 = my_set2.difference(my_set1)

diff_union = list(diff1.union(diff2))

print(f"1: {diff_union}")
# printing symmetric difference values
for i in range(len(diff_union)-1, 0, -1):
    for j in range(i):
        if diff_union[j] > diff_union[j+1]:
            temp = diff_union[j]
            diff_union[j] = diff_union[j+1]
            diff_union[j+1] = temp
print(f"3: {diff_union}")


def sort_list(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j]:
                temp = list[j]
                list[j] = list[j]
                list[j] = temp
    return list


new_list = sort_list(diff_union)
print(f"2: {new_list}")
