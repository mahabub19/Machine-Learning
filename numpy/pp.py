import numpy as np

# nums = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])

# print(nums)
# print(nums.ndim)

# nums = np.array([0,1,2,3,4,5,6,7,8,9],dtype='i')
# nums2 = np.array([[1,8,3],[1,6,3]])
# num = nums.astype(bool)
# arr = nums.reshape(2,5)


# print(nums[-1])
# print(nums.ndim)
# print(nums2[0,1])

# print(nums[::2])
# print(nums2[1,1:2])
# print(nums)
# print(num)
# print(arr)
# for data in nums2:
#     print(data)

# a = "Man"
# b="Nishat"
# print(a + " " + b)

# arr = [1,2,3]
# for x in range(5,8):
#     arr.append(x**2)
    
    
# print(arr)

def func(y):
    sum=0
    for x in range(0,5):
        sum+=y*(x**2)
    return sum

print(func(1))