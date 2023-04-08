# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:11:16 2022

@author: negromontebs
"""
from datetime import datetime
from datetime import timedelta
import serial
from scipy.signal import find_peaks
import pandas as pd
import matplotlib.pyplot as plt
import warnings

#serial port of Arduino
arduino_port = "COM6" 
#arduino uno runs at 9600 baud
baud = 9600 
#name of the CSV file generated:
fileName="test1.csv" 
ser = serial.Serial(arduino_port, baud)

if not ser.isOpen():
    ser.open()
print('com6 is open', ser.isOpen())

#how many samples to collect
samples = 10 
print_labels = False
#start at 0 because our header is 0 (not real data)
line = 0

# detects time
now = datetime.now()
later = now + timedelta(seconds = 45)
current_time = now.strftime("%H:%M:%S.%f")

while now <= later:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("Current Time =", current_time)
    getData=str(ser.readline())
    data=getData[0:][2:-5]

    file = open(fileName, "a")
    file.write(str(now) + ',' + data + "\n") #write data with a newline
    line = line+1

print("Data collection complete!")
ser.close()
file.close()

# csv path, add it here:
path = "path"
df = pd.read_csv(path)
df = df.set_axis(['Time','Temp'],axis='columns')
df = df.drop_duplicates(subset='Time', keep ='last', ignore_index = True)
df['Count']=df['Time']
df['T(ms)']=df['Time']

# Calculates the minutes and seconds:
temp= []
time_ms = []

warnings.filterwarnings('ignore')
  
for index in df.index:
# replace the date+time for just the time
    df['Time'] = df['Time'].replace(df['Time'][index],df['Time'][index][11:])
    time = df['Time'][index]
    if index == 0:
      # sets the first measurement as 00:00
      start = datetime.strptime(time,'%H:%M:%S.%f')
      df['Count'][index] = '00:00.000'
      df['T(ms)'][index] = '0'
    else:
      pt = datetime.strptime(time,'%H:%M:%S.%f')
      diff = pt-start # calculate the difference between the start and time of measurement
      df['Count'][index] = str(diff)[2:-3]
      df['T(ms)'][index] = str(diff.total_seconds()*1000) # calculates the ms 
    temp.append(df['Temp'][index])
    time_ms.append(df['T(ms)'][index])
    
# 1st plot: 
df.plot(x = 'T(ms)', y='Temp', kind = 'line', figsize = (20,10), title = 'Temperature (C) x time (Milliseconds)', legend = 'Temperature',xlabel = 'Time (milliseconds)', ylabel = 'Temperature (C)')
plt.show()

def plot_peaks(df2,cut,mode):
  # this function cuts the time for the default (-20s) or for the chosen one and plots the peaks. Also returns the respiratory rate
  if cut=='Y':
    start = 10
    end = 4
    # defines start and end from users choices:
    while start>=end:
      start = float(input('Start from (s): '))*1000
      end = float(input('End at (s): '))*1000

    # cuts for the time frame chosen:
    for i in range(len(df2)):
      time = float(df2['T(ms)'][i])
      if start>time:
        df2 = df2.drop(i)
      elif end<time:
        df2 = df2.drop(i)

  elif cut=='N':
    start = 20000
    # cuts for default:
    for i in range(len(df2)):
      time = float(df2['T(ms)'][i])
      if start>time:
        df2 = df2.drop(i)
  df2 = df2.reset_index(drop=True)

  # if it was measured by nose, the prominence considered is 0.2, if it was for mouth, is 0.5
  # this is due to the difference between measurement type
  if mode=='nose':
    peaks, properties = find_peaks(df2['Temp'], prominence = 0.2)
  else:
    peaks, properties = find_peaks(df2['Temp'], prominence = 0.5)
  
  # calculates the respiratory rate by counting the peaks calculated above, multiplying by 60 (seconds) and dividing by the diference between the start and end time
  first = float(df2['T(ms)'][0])
  last = df2.iloc[-1]
  seconds =(float(last['T(ms)'])-first)/1000
  x = len(peaks)*60/seconds
  print('This count round has ', round(x),'breathes detected per minute')

  df2.plot(x = 'T(ms)', y='Temp', kind = 'line', figsize = (20,10), title = 'Temperature (C) x time (Milliseconds)', legend = 'Temperature',xlabel = 'Time (milliseconds)', ylabel = 'Temperature (C)')
  plt.plot(peaks, df2['Temp'][peaks], ".")
  plt.show()
  
plotar = plot_peaks(df,'No','mouth')