import time

time.time()  # returns the current time in seconds since the Epoch (January 1st, 1970)

time.localtime()  # returns the current time in a time.struct_time object

time.gmtime()  # returns the current time in UTC in a time.struct_time object

time.ctime()  # converts a time in seconds since the Epoch to a string in local time
