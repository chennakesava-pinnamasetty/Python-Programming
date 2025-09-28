
# The time module in Python provides functions to work with time, dates, delays, and performance measurements.
# It deals mostly with timestamps (number of seconds since 1 Jan 1970 → called the epoch).

# 1

# time.time()

# import time
# print(time.time())
                                # 1756791376.3634744




# 2

# time.ctime([secs])
       # Converts a timestamp into a readable string.
'''
import time

print(time.ctime)              # <built-in function ctime>
print(time.ctime(0))           # Thu Jan  1 05:30:00 1970

'''


# 3
# time.sleep(seconds)

'''
import time

print("start")               # start
time.sleep(3)                  # wait for 3 seconds
print("end after 3 sec")     # end after 3 sec

'''


# 4
   
   # This gives current time and day,month.

'''
import time

print(time.ctime())                 # Thu Sep  4 14:05:58 2025
 '''

                                                        
                                                        # DATE TIME


# 1

'''
import datetime
x = datetime.datetime.now()
print(x)                           # 2025-09-04 14:14:05.401797

'''

# 2

'''
import datetime

x = datetime.date.today()
print(x)                  # 2025-09-04
print(x.year)             # 2025
print(x.today)            # <built-in method today of type object at 0x00007FF8777C15B0>
print(x.month)            # 9
print(x.day)              # 4

'''

                                # DIFF
       '''                         
import time
print(time.ctime())        # Thu Sep  4 14:19:41 2025

'''


