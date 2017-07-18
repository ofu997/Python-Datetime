import time
import datetime

hourHere = datetime.datetime.now().hour

def LondonTimeConvert(time):
  London = time +8
  if London > 23:
    London -= 24
  else:
    London = London
  # this is necessary
  return London

def NewYorkTimeConvert(time):
  NY = time +3
  if NY > 23:
    NY -= 24
  else:
    NY = NY
  return NY


# call function LONDON
hourLondon = LondonTimeConvert(hourHere)


# call function NY
hourNY = NewYorkTimeConvert(hourHere)

# new york
print("The military hour in New York is " + str(hourNY) + " and the")
      
if hourNY > 8 and hourNY < 21:
  print("New York office is open")
else:
  print("New York office is closed")

# London
print("The military hour in London is " + str(hourLondon) + " and the")
      
if hourLondon > 8 and hourLondon < 21:
  print("London office is open")
else:
  print("London office is closed")


