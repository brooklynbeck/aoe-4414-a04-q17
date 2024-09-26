# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Takes time in year/month/day/hour/minute/second into JD time
# Parameters:
# year : integer year
# month : integer month
# day : integer day
# hour : integer hour
# minute : integer minute
# second : float second
# Output:
# Prints jd time as a float
#
# Written by Brooklyn Beck
# Other contributors: None
#
# import Python modules
import math # math module
import sys # argv
# "constants"


# initialize script arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')

# parse script arguments
if len(sys.argv)==7:
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  hour = int(sys.argv[4])
  minute = int(sys.argv[5])
  second = float(sys.argv[6])
else:
  print(\
  'Usage: '\
  'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

# main script

jd = day - 32075 + 1461*(year+4800-(14-month)//12)//4 + 367*(month-2+(14-month)//12*12)//12 - 3*((year+4900-(14-month)//12)//100)//4
d_frac = (second + 60*(minute+60*hour))/86400
jd_frac = jd-0.5 + d_frac

print(jd_frac)
