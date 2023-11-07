import math


def find_sum():
    with open("nums.txt", "r") as file:
        rows = file.readlines()
        nums = (row.partition('#')[0].rstrip() for row in rows)
        nums = (row for row in nums if row)
        nums = (float(row) for row in nums)

        nums = (x for x in nums if math.isfinite(x))
        nums = (max(0., x) for x in nums)
        res = sum(nums)
        print(f"The sum is {res}")


find_sum()
