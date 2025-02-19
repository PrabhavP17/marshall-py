# Lesson 5

intl_money = input("Enter the amount of money in your pocket: ")
intl_money = float(intl_money)
cookies_sold = input("Enter the number of cookies sold: ")

b_cookies = 0
c_cookies = 0

for current_cookie in cookies_sold:
    if current_cookie == "c":
        c_cookies += 1
    elif current_cookie == "b":
        b_cookies += 1
    else: 
        print(f"{current_cookie} is an invalid cookie type")


total_cookies = b_cookies + c_cookies
profit = (b_cookies * 1.25) + (c_cookies * 0.75)
end_money = intl_money + profit

print(f"The total number of cookies sold is: {total_cookies}")
print(f"The total profit is: {profit}")
print(f"The total amount of money in your pocket is: {end_money}")
