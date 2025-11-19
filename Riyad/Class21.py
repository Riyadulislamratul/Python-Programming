# 1
"""num = [1,2,3,4,6,8]
newNum = []

for index in range(len(num)):
    if num[index] % 2 == 0:
        newNum.append(num[index]**2)

print(newNum)"""

# 2
"""num = [10,11,12,13,14,15]
even = []
odd = []
for index in range(len(num)):
    if num[index] % 2 == 0:
        even.append(num[index])
    else:
        odd.append(num[index])
print(even)
print(odd)"""

#3
"""fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])"""

"""numList = [1, 5, 67, 78, 84]
sum = 0
for i in numList:
    sum += i
print(sum)"""

"""num = [1,2,3,4,5,6,7,8,9]
sum = 1
for i in num:
    sum *= i
print(sum)"""

# 3
# num = [10, 20, 4, 45, 99]

# 4 
"""num = [1,2,2,3,4,4,5]
for i in num:
    if num == num[i]:
        num.remove(num)
print(num)"""

"""nameList = ["md riyadul islam ratul", "shuvo hossen"]
for name in nameList:
    print(name.title())"""

# numList = [1,5,9,13,6,8,15,20,23,35,49]
# new = []
# for num in numList:
#     if num % 5 != 0:
#         new.append(num)
# print(new)
"""num = [1,2,2,3,4,4,5]
newNum = []
for i in num:
    if num[i] != newNum:
        newNum.append(num)
    i += 1
print(newNum)"""
num = [1,2,2,3,4,4,5]
newNum = []
for i in num:
    if num == newNum:
        continue
    i += 1
print(newNum)