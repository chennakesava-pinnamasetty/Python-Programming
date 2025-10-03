'''import calendar

# Get user input
month = int(input("Enter the month :"))
year = int(input("Enter theyear :"))

# Display the calendar
print("\n Calender Date ")
print(calendar.month(year,month))'''

''' === output ===
Enter the month :8
Enter theyear :2002

 Calender Date 
    August 2002
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31 '''


import calendar
from datetime import datetime

'''special_events = {
    1 : "New Year's Day 🎉",
    7 : "Friendship Day 🤝",
    14: "Valentine's Day ❤️",
    25: "Christmas Day 🎄"
}'''

day = int(input("Enter date (1 - 31): "))
month = int(input("Enter the month ( 1-12) : "))
year = int(input("Enter the year :" ))

weekday = calendar.day_name[datetime(year,month,day).weekday()]
#event = special_events.get(day,"No special events today.")

print(f"{day}/{month}/{year} is a {weekday}")
#print(f"special : {event}")


'''    === OUTPUT ===
Enter date (1 - 31): 15
Enter the month ( 1-12) : 8
Enter the year :2025
15/8/2025 is a Friday
'''
