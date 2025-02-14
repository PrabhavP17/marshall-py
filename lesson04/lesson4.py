# Lesson 4
import math
fence_sec_1= input("Enter the number of fence in section 1: ")
fence_sec_2= input("Enter the number of fence in section 2: ")
fence_sec_3= input("Enter the number of fence in section 3: ")

fence_sec_1 = len(fence_sec_1)
fence_sec_2 = len(fence_sec_2)
fence_sec_3 = len(fence_sec_3)

total_fence = int(fence_sec_1 + fence_sec_2 + fence_sec_3)
print(f"The total length of the fence is: {total_fence}")

boxes = math.ceil(total_fence / 12)

if total_fence <= 12:
    leftover = 12 - total_fence

else:
    leftovers = total_fence % 12  
    print(f"The are, {leftovers}, leftover cans of paint")

price = (boxes * 14.95)

print(f"The total price of the paint is: {price}")






