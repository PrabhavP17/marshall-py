# user_input= input("Enter the string: ")

# counter = 0

# while counter < len(user_input):
#     if user_input[counter]== "@":
#         print (counter)
        
#     counter += 1 

# user_input = input("Enter the string: ")
# user_shift = int(input("Enter the shift: "))

# input = int(input("Enter a number: "))

# counter = ""

# while counter != 1:

#     if input % 2 == 0:
#         input = input // 2
#         counter = input
    
#     elif input % 2 != 0:
#         input = (input*3) + 1
#         counter = input
    
    
#     print(counter)

# dusa = int(input("Enter the size of dusa:  "))
# yobi = 0
# while dusa >= yobi:
#     yobi = int(input("Enter the size of yobi:  "))
#     if dusa <= yobi:
#         print ("Dusa is running away")
#         print (f"Final size of dusa: {dusa} ")
#         break
#     elif dusa > 

#         dusa = dusa +yobi 
    
#     print (dusa)

# a_list = [3,1,4,1,5,9]
# b_list = a_list.copy() 

# b_list[-1] = "POPOPPOOLOL"

# print (a_list)


# print (b_list)

# a_list = [3,1,4,1,5,9]

# target1  = int(input("enter the numbe ryou want to find:"))
# found = False 

# for i in range(len(a_list)):
#     if a_list[i] == target1:
#         found = True
#         print (f"Found {target1} at index {i}")
#         break

# if not found:
#     print (f"{target1} not found")

# a_list = [3,1,4,1,5,9]
# a_list_sort()
# print(a_list)
# left = 0 
# right = len (a_list) - 1


word  = input("Enter the word: ")



sum  = 0

print (len(word))

for i in range(len(word)):
    
    if word [i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        sum += 1
        
    elif word[i].isalpha():
        sum+= 5
        
    else :
        sum += 0

print (sum)

score  = sum * len(word)
print(score)
