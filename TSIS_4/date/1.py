# # # 1

# # import datetime

# # print(datetime.datetime.now())

# # today = datetime.datetime.now()

# # day = datetime.timedelta(5)

# # print(today - day)

# # # 2
# # import datetime

# # today = datetime.datetime.now()

# # tomorrow = datetime.timedelta(1)

# # print(today - tomorrow)
# # print(today)
# # print(today + tomorrow)

# # # 3
# # import datetime

# # day = datetime.datetime.now()

# # print(day.strftime("%d.%m.%y %H:%M:%S"))

# # # 4

# import datetime

# today = datetime.datetime(int(input()),int(input()),int(input()),int(input()),int(input()),int(input()))

# day = datetime.datetime(int(input()),int(input()),int(input()),int(input()),int(input()),int(input()))

# diff = day - today

# diff_in_seconds = diff.total_seconds()

# print(diff_in_seconds)




import datetime

day1 = input()
day2 = input()

d = datetime.datetime.strptime(day1,"%d.%m.%Y")
x = datetime.datetime.strptime(day2,"%d.%m.%Y")
print(d)
# a = int(input())
# diff = datetime.timedelta(a)
# yesterday = d - diff
print(abs(d - x).total_seconds())