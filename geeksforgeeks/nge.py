# https://www.geeksforgeeks.org/next-greater-element/

def nge(nums):
    stack = []
    n = len(nums)
    for i in range(n):

        if len(stack) == 0:
            stack.insert(0, nums[i])
        else:
            # stack isn't empty
            while len(stack) > 0 and stack[0] < nums[i]:
                popped = stack.pop(0)
                print(popped, "-->", nums[i])

            stack.insert(0, nums[i])

    while len(stack) > 0:
        print(stack.pop(0), "--> -1")

# test
nge([11, 13, 21, 3])
