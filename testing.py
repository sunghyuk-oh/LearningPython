from datetime import date, datetime

today = datetime.now()  # once indicator is flagged both times should be now()
yest = datetime(2021, 7, 14, 10, 14)

diff = today-yest

print(diff)


# start_str = day_time.strftime("%Y-%m-%d %H:%M:%S")  # convert start into string
# conv_start = datetime.strptime(
#     start_str, "%Y-%m-%d %H:%M:%S")  # Str -> datetime
# conv_end = datetime.strptime(day_time, "%Y-%m-%d %H:%M:%S")  # Str -> datetime
# print(conv_end - conv_start)  # datetime calc in useable format
