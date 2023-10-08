def square_numbers(l):
    for i in l:
        yield i * i


nums = square_numbers([1, 2, 3, 4, 5])

nums_2 = (x * x for x in [1, 2, 3, 4, 5])
print(nums)
print(nums_2)

print(next(nums))
print(next(nums_2))

for num in nums_2:
    print(num)
