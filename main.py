import itertools as itr


## Inserts operations to find the min
def find_min_operations(list_nums):
    if len(list_nums) == 1:
        return list_nums[0]
    next_inputs = []
    next_inputs.append([].append(list_nums[0] + list_nums[1], ) )


# Find the minimum given a list of numbers
def find_min(list_nums):
    if len(list_nums) == 1:
        return list_nums[0]
    for permutation in itr.permutations(list_nums):
        pass


if __name__ == '__main__':
    find_min([1,2,3,4] )

