import random
nums = []
sum = 0
start_index = 0
for i in range(1000):
    res = random.randint(1,1000)
    nums.append(res)
print(nums)

for j in range(10):
    sum += nums[j]
print(sum)
max_sum = sum

for k in range(10,1000):
    sum = nums[k] + sum - nums[k-10]
    if max_sum < sum:
        max_sum = sum
        start_index = k-9

print(max_sum)
print(f"({start_index}, {start_index + 9})")
print(f"Values: {nums[start_index:start_index + 10]}")

    

