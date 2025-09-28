 
'''

Code            	Description	                          Example Output
%Y	            Year (4 digits)	                              2025
%y	            Year (last 2 digits)	                       25
%m	            Month (01-12)	                               09
%B	            Full month name	                            September
%b	            Abbreviated month name	                      Sep
%d	            Day of the month (01-31)	                  03
%A	            Full weekday name	                        Wednesday
%a	            Abbreviated weekday name	                  Wed
%H	            Hour (24-hour clock, 00-23)	                  14
%I	            Hour (12-hour clock, 01-12)	                  02
%p	            AM or PM	                                  PM
%M	            Minute (00-59)	                              45
%S	            Second (00-59)	                              30
%f	            Microsecond (000000-999999)	                 123456
%z	            UTC offset	                                 +0530
%c	            Locale’s date and time representation      Wed Sep 3 14:45:30 2025
%x	            Locale’s date representation	             09/03/25
%X	            Locale’s time representation	             14:45:30



'''

                 # EXPLANATION
'''

datetime.date     → only date

datetime.time     → only time

datetime.datetime → both date + time

strftime()        → format date → string

strptime()        → parse string → date

timedelta         → add/subtract days, hours, etc.

calendar          → month/year calendars

pytz              → timezones

'''






# Example Usage:

'''
from datetime import datetime

# Current date and time
now = datetime.now()

# Format the datetime object
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_date)

# Custom formats
print("Year:", now.strftime("%Y"))
print("Month (Full Name):", now.strftime("%B"))
print("Day of the Week:", now.strftime("%A"))
print("12-hour Time:", now.strftime("%I:%M %p"))



Example Output:


Formatted Date and Time: 2025-09-03 14:45:30
Year: 2025
Month (Full Name): September
Day of the Week: Wednesday
12-hour Time: 02:45 PM



Notes:
The strftime() method is highly customizable and supports a wide range of format codes.
It is commonly used for creating human-readable date and time strings for logs, reports, or user interfaces.

'''



# weekday name

import datetime
x = datetime.datetime.now()

print(x.strftime("%A"))             # Thursday