# target = int(input("Enter the distance to the hole in yards: "))
# clubs = int(input("Enter the number of clubs: "))

# # i = 0
# club_lengths = []  
# while clubs > 0:
#     club_size = int(input("Enter the distance of the club: "))
#     # i += 1
#     clubs = clubs - 1
#     club_lengths.append(club_size)

# club_lengths.sort()
# print(club_lengths)

# while target != 0:
#     if target > club_lengths[clubs-1]:
#         target = target - club_lengths[clubs-1]
#         print (f"Remaining distance: {target}")
#     elif target < club_lengths[clubs-1]:

        


        


    



# # clubLength = sorted(club)
# # clubs:
# #     target = target - clubLength[i]
# #     clubs -= 1

# # if target > clubLength[-1]:
# #     new  target = distance % clubLength[-1]
# #     if new target > clubLength[-2]:
        
time = int(input("Enter the total time we have: "))

ttl_chores = int(input("Enter the total number of chores: "))

count = 0

choretime = []  

while ttl_chores > 0:
    chore_times = int(input("Enter the time for each chore: "))
    ttl_chores = ttl_chores - 1
    choretime.append(chore_times)
choretime.sort()
print(choretime)

t= 0 
i = 0 
while t < time :
    if time >= choretime[i]:
        t = t + choretime[i]
        print(f"Remaining time: {time - t}")
        count += 1
        i += 1
    else:
        break
print(f"Total chores completed: {count}")


