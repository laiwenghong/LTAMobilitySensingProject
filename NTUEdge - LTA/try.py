# -*- coding: utf-8 -*-
"""try.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16ugNQdc1Lxcpg8rVxdINyyNh2fMoLbMi

# Start
"""

!pip install requests

#Import all csv files from github
import requests
url='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Load_Data/LoadData.py'
r=requests.get(url)
with open('LoadData.py','w') as f:
  f.write(r.text)

import LoadData as LD
#List of dataframes imported:
bukitPanjangToExpo_s6edge=LD.bukitPanjangToExpo_s6edge
bukitPanjangToExpo_iphone12pro=LD.bukitPanjangToExpo_iphone12pro
woodlandNorthToWoodlandSouth_s6edge=LD.woodlandNorthToWoodlandSouth_s6edge
woodlandNorthToWoodlandSouth_iphone12pro=LD.woodlandNorthToWoodlandSouth_iphone12pro
harbourFrontToPunggol_s6edge=LD.harbourFrontToPunggol_s6edge
harbourFrontToPunggol_iphone12pro=LD.purple
harbourfrontToDhobyGhautToMarinaBay_s6edge=LD.harbourfrontToDhobyGhautToMarinaBay_s6edge
harbourfrontToDhobyGhautToMarinaBay_iphone11=LD.harbourfrontToDhobyGhautToMarinaBay_iphone11

#Import all functions from github
url='https://raw.githubusercontent.com/kaiyang7766/ExploratoryDataAnalysis/main/Load_Data/LoadFunctions.py'
r=requests.get(url)
with open('LoadFunctions.py','w') as f:
  f.write(r.text)

from LoadFunctions import *

pip install ruptures

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.fftpack
from scipy.fft import fft, fftfreq
import ruptures as rpt

DT_Stations = ['DT1_Bukit_Panjang', 'DT2_Cashew', 'DT3_Hillview','DT5_Beauty_World', 'DT6_King_Albert_Park', 'DT7_Sixth_Avenue', 'DT8_Tan_Kah_Kee', 'DT9_Botanic_Gardens', 'DT10_Stevens','DT11_Newton','DT12_Little_India','DT13_Rochor','DT14_Bugis', 'DT15_Promenade','DT16_Bayfront','DT17_Downtown','DT18_Telok Ayer','DT19_Chinatown','DT20_Fort_Canning','DT21_Bencoolen','DT22_Jalan_Besar','DT23_Bendemeer','DT24_Geylang_Bahru','DT25_Mattar','DT26_MacPherson','DT27_Ubi','DT28_Kaki_Bukit','DT29_Bedok_North','DT30_Bedok_Reservoir','DT31_Tampines_West','DT32_Tampines','DT33_Tampines_East','DT34_Upper_Changi','DT35_Expo']
TE_Stations=['TE1_Woodlands_North','TE2_Woodlands','TE3_Woodlands_South']
NE_Stations=['NE1_HarbourFront','NE3_Outram_Park','NE4_Chinatown','NE5_Clarke_Quay','NE6_Dhoby_Ghaut','NE7_Little_India','NE8_Farrer_Park','NE9_Boon_Keng','NE10_Potong_Pasir','NE11_Woodleigh','NE12_Serangoon','NE13_Kovan','NE14_Hougang','NE15_Buangkok','NE16_Sengkang','NE17_Punggol']
Circle_Stations=['CC29_HarbourFront','CC28_Telok_Blangah','CC27_Labrador_Park','CC26_Pasir_Panjang','CC25_Haw_Par_Villa','CC24_Kent_Ridge','CC23_one-north','CC22_Buona_Vista','CC21_Holland_Village','CC20_Farrer_Road','CC19_Botanic_Gardens','CC17_Caldecott','CC16_Marymount','CC15_Bishan','CC14_Lorong_Chuan','CC13_Serangoon','CC12_Bartley','CC11_Tai_Seng','CC10_MacPherson','CC9_Paya_Lebar','CC8_Dakota','CC7_Mountbatten','CC6_Stadium','CC5_Nicoll_Highway','CC4_Promenade','CC3_Esplanade','CC2_Bras_Basah','CC1_Dhoby_Ghaut','CC2_Bras_Basah','CC3_Esplanade','CC4_Promenade','CE1_Bayfront','CE2_Marina_Bay']

len(Circle_Stations)

#new version of start time end time
DT_s6edge=datapreparation(bukitPanjangToExpo_s6edge, '2020-12-25 09:17:00.000','2020-12-25 10:23:51.000', resize=15, neednormalizepressure = True) #use findErrorDuration2
DT_iphone12pro=datapreparation(bukitPanjangToExpo_iphone12pro,'2020-12-25 09:16:50.000','2020-12-25 10:26:19.000',resize=1, neednormalizepressure = False) #enough 34 stations
TE_s6edge=datapreparation(woodlandNorthToWoodlandSouth_s6edge, '2020-12-25 08:23:27.000','2020-12-25 08:30:00.000', resize=9, neednormalizepressure = True) #First mode is PMD = Idle
TE_iphone12pro=datapreparation(woodlandNorthToWoodlandSouth_iphone12pro, '2020-12-25 08:23:01.000','2020-12-25 08:30:00.000',resize=1, neednormalizepressure = False) #First mode is PMD = Idle
NE_s6edge=datapreparation(harbourFrontToPunggol_s6edge, '2021-01-09 09:40:04.000','2021-01-09 10:17:00.000', resize=14, neednormalizepressure = True) #31 mode change after minusing error modes
NE_iphone12pro=datapreparation(harbourFrontToPunggol_iphone12pro,'2020-12-19 02:36:04.000','2020-12-19 03:11:00.000',resize=1, neednormalizepressure = False) #31 mode change after minusing error modes
circle_s6edge=datapreparation(harbourfrontToDhobyGhautToMarinaBay_s6edge, '2021-01-09 07:45:08.000','2021-01-09 09:15:02.000', resize=17, neednormalizepressure = True) #dont do circle first
circle_iphone11=datapreparation(harbourfrontToDhobyGhautToMarinaBay_iphone11, '2020-12-18 08:39:49.000','2020-12-18 10:11:00.000',resize=1, neednormalizepressure = False) #dont do circle first

DT_s6edge=datapreparation(bukitPanjangToExpo_s6edge, '2020-12-25 09:17:00.000','2020-12-25 10:23:51.000', resize=15, neednormalizepressure = True) #use findErrorDuration2
DT_iphone12pro=datapreparation(bukitPanjangToExpo_iphone12pro,'2020-12-25 09:16:50.000','2020-12-25 10:26:19.000',resize=1, neednormalizepressure = False) #enough 34 stations
TE_s6edge=datapreparation(woodlandNorthToWoodlandSouth_s6edge, '2020-12-25 08:23:27.000','2020-12-25 08:30:00.000', resize=9, neednormalizepressure = True) #First mode is PMD = Idle
TE_iphone12pro=datapreparation(woodlandNorthToWoodlandSouth_iphone12pro, '2020-12-25 08:23:01.000','2020-12-25 08:30:00.000',resize=1, neednormalizepressure = False) #First mode is PMD = Idle
NE_s6edge=datapreparation(harbourFrontToPunggol_s6edge, '2021-01-09 09:40:04.000','2021-01-09 10:16:05.000', resize=14, neednormalizepressure = True) #31 mode change after minusing error modes
NE_iphone12pro=datapreparation(harbourFrontToPunggol_iphone12pro,'2020-12-19 02:35:00.000','2020-12-19 03:11:00.000',resize=1, neednormalizepressure = False) #31 mode change after minusing error modes
circle_s6edge=datapreparation(harbourfrontToDhobyGhautToMarinaBay_s6edge, '2021-01-09 07:45:08.000','2021-01-09 09:17:00.000', resize=17, neednormalizepressure = True) #dont do circle first
circle_iphone11=datapreparation(harbourfrontToDhobyGhautToMarinaBay_iphone11, '2020-12-18 08:39:49.000','2020-12-18 10:10:30.000',resize=1, neednormalizepressure = False) #dont do circle first

DT_s6edge

def modeChanged(data):
  totalNumberOfModeChanged = 0
  timestampList = [[data['Mode'][0],data['Time'][0],data['Cleaned_Time'][0]]] #list of list
  timeStampLastMode = data['Cleaned_Time'][0]
  durationOfLastMode = 0
  current_mode = data['Mode'][0]
  for i in range(len(data)):
    mode = data['Mode'][i]
    if mode != current_mode:
      totalNumberOfModeChanged += 1
      duration = data['Cleaned_Time'][i] - timeStampLastMode
      timestampList[-1][2] = duration #only after next change of mode we are able to calculate the duration of last mode, without this the mode and duration output will be interchanged
      
      #insert end time for previous mode as current timestamp
      timestampList[-1].append(data['Time'][i])

      #insert new entries
      timestampList.append([mode,data['Time'][i],0]) #0 is just preparation for adding duration in the next loop

      #update new count
      current_mode = mode
      timeStampLastMode = data['Cleaned_Time'][i]
#  print("Total number of Mode changed is :",totalNumberOfModeChanged)
  return timestampList

def findErrorDuration(timestampList):
  errorCount = 0
  global errorList
  errorList = []
  for item in timestampList:
    if item[2] < 20:
      errorCount+=1
      errorList.append([item[1],item[2]])
  print("Total number of error entries is :",errorCount)
  print(errorList)
  return errorCount, errorList

def removeBackwardTimestampError(modeList):
  newModeList = [modeList[0]]
  removeList = []
  currentTime = modeList[0][1]
  modeList.pop(0)
  while modeList != []:
    if modeList[0][1] <= currentTime:
      removeList.append(modeList[0])
      modeList.remove(modeList[0])
    else:
      newModeList.append(modeList[0])
      currentTime = modeList[0][1]
      newModeList[-2][3] = currentTime
      modeList.remove(modeList[0])
  return newModeList

import datetime
def recalculateDuration(modelist):
  for i in range(len(modelist)-1):
    if isinstance(modelist[0][1],str) == True:
      endtime = datetime.datetime.strptime(modelist[i][3], '%Y-%m-%d %H:%M:%S')
      starttime = datetime.datetime.strptime(modelist[i][1], '%Y-%m-%d %H:%M:%S')
    else:
      endtime = modelist[i][3]
      starttime = modelist[i][1]
    time = endtime - starttime
    modelist[i][2] = time.total_seconds()
  return modelist

def removeErrorDuration(modelist):
  newlist = []
  for i in range(len(modelist)-1):
    if modelist[i][2] < 5: #less than 5 seconds
      pass
    else:
      newlist.append(modelist[i])
  newlist.append(modelist[-1]) #add last item in
  return newlist

def selectTimestampKey(modelist):
  newlist = []
  for i in modelist:
    newlist.append(i[1])
  return newlist

def findRepetitiveMode(modelist):
  repetitivelist = []
  mode = modelist[0][0]
  for i in range(1,len(modelist)):
    if modelist[i][0] == mode:
      print("Repetitve mode error at ",modelist[i])
      repetitivelist.append(modelist[i])
    else:
      mode = modelist[i][0]
  return repetitivelist

def removeRepetitiveMode(modelist, repetitivelist):
  newlist = []
  print("remove starting here!")
  for i in range(len(modelist)-1):
    if modelist[i] in repetitivelist:
      print(modelist[i],"is going to be removed")
      newlist[-1][3] = modelist[i][3]
    else:
      newlist.append(modelist[i])
#  print("newlist length is:", len(newlist))
  return newlist

def checkTimestampIsString(modelist):
  newlist = []
  if isinstance(modelist[0][1], str) == False:
    for i in range(len(modelist)-1):
      modelist[i][1] = str(modelist[i][1])
      modelist[i][3] = str(modelist[i][3])
      newlist.append(modelist[i])
    newlist.append(modelist[-1])
    newlist[-1][1] = str(newlist[-1][1])
    return newlist
  return modelist

def errorRemovingPipeline(data):
  modeChangedList = modeChanged(data)
  print("The length after modeChanged is :", len(modeChangedList))

  newModeChangedList = removeBackwardTimestampError(modeChangedList)
  print("The length after removeBackwardTimestampError is :", len(newModeChangedList))

  recalculatedModeList = recalculateDuration(newModeChangedList)
  print("The length after first recalculated is :", len(recalculatedModeList))

  recalculatedAndRemovedList = removeErrorDuration(recalculatedModeList)

  repetitiveList = findRepetitiveMode(recalculatedAndRemovedList)
  if repetitiveList != []:
    recalculatedAndRemovedList = removeRepetitiveMode(recalculatedAndRemovedList, repetitiveList)

  print("The length after recalculated and repetitive mode removed is :", len(recalculatedAndRemovedList))
  finalList = checkTimestampIsString(recalculatedAndRemovedList)

  finalList[-1].append('0')

  return finalList

def appendStation(modelist,stationlist):
  tempStationList = stationlist[:] #copy without referencing, if not stationlist will get pop and cannot be reused
  for item in modelist:
    if item[0] == "Idle" or item[0] == "PMD": #put PMD because TE line got PMD as Idle
      print(tempStationList[0])
      item.append(tempStationList[0])
      tempStationList.pop(0)
    else:
      item.append("Moving")
  return modelist

def addStationToDf(data,modelist):
  data['Station'] = '0'
  while modelist != []:
    for i in range(len(data['Time'])):
      if str(data['Time'][i]) == modelist[0][1]:
        data['Station'][i] = modelist[0][4]
        print(data['Station'][i],'is added!!!')
        modelist.pop(0)
        break
  return data

def fillEmptyStationToDf(data):
  temp = data['Station'][0]
  for i in range(len(data['Station'])):
    if data['Station'][i] != '0':
      temp = data['Station'][i]
    else:
      data['Station'][i] = temp
  return data

#combine 2 functions together
def modifyColumnStation(data,modelist):
  data1 = addStationToDf(data,modelist)
  print("add station done!!!")
  data2 = fillEmptyStationToDf(data1)
  print("fill empty done!!!")
  return data2

print(type(DT_s6edge['Time'][0]))
print(type(DT_iphone12pro['Time'][0]))
print(type(TE_s6edge['Time'][0]))
print(type(TE_iphone12pro['Time'][0]))
print(type(NE_s6edge['Time'][0]))
print(type(NE_iphone12pro['Time'][0]))
print(type(circle_s6edge['Time'][0]))
print(type(circle_iphone11['Time'][0]))

"""#Testing Procedure"""

data1 = DT_s6edge
data2 = DT_iphone12pro
#DT_s6edge
#DT_iphone12pro
#TE_s6edge
#TE_iphone12pro
#NE_s6edge
#NE_iphone12pro
#circle_s6edge
#circle_iphone11

data1

#testing procedure
list1 = modeChanged(data1) #but idk why when u called list1 it returns [], but list1 can be used to proceed for list2 onwards
list2 = removeBackwardTimestampError(list1)
list3 = recalculateDuration(list2)
list4 = removeErrorDuration(list3)
repetitiveList = findRepetitiveMode(list4)
if repetitiveList != []:
    list4 = removeRepetitiveMode(list4, repetitiveList)
list5 = checkTimestampIsString(list4)

list6 = modeChanged(data2) #but idk why when u called list1 it returns [], but list1 can be used to proceed for list2 onwards
list7 = removeBackwardTimestampError(list6)
list8 = recalculateDuration(list7)
list9 = removeErrorDuration(list8)
repetitiveList = findRepetitiveMode(list9)
if repetitiveList != []:
    list9 = removeRepetitiveMode(list9, repetitiveList)
list10 = checkTimestampIsString(list9)

list10

print(len(list5),len(list10))

count = 0
for i,j in zip(list5,list10):
  print(i[0],i[0])
  if i[0] == "Idle":
    count += 1
print("count =", count)

for i in list10:
  print(i[0])

DT_Stations = ['DT1_Bukit_Panjang', 'DT2_Cashew', 'DT3_Hillview','DT5_Beauty_World', 'DT6_King_Albert_Park', 'DT7_Sixth_Avenue', 'DT8_Tan_Kah_Kee', 'DT9_Botanic_Gardens', 'DT10_Stevens','DT11_Newton','DT12_Little_India','DT13_Rochor','DT14_Bugis', 'DT15_Promenade','DT16_Bayfront','DT17_Downtown','DT18_Telok Ayer','DT19_Chinatown','DT20_Fort_Canning','DT21_Bencoolen','DT22_Jalan_Besar','DT23_Bendemeer','DT24_Geylang_Bahru','DT25_Mattar','DT26_MacPherson','DT27_Ubi','DT28_Kaki_Bukit','DT29_Bedok_North','DT30_Bedok_Reservoir','DT31_Tampines_West','DT32_Tampines','DT33_Tempines_East','DT34_Upper_Changi','DT35_Expo']
TE_Stations=['TE1_Woodlands_North','TE2_Woodlands','TE3_Woodlands_South']
NE_Stations=['NE1_HarbourFront','NE3_Outram_Park','NE4_Chinatown','NE5_Clarke_Quay','NE6_Dhoby_Ghaut','NE7_Little_India','NE8_Farrer_Park','NE9_Boon_Keng','NE10_Potong_Pasir','NE11_Woodleigh','NE12_Serangoon','NE13_Kovan','NE14_Hougang','NE15_Buangkok','NE16_Sengkang','NE17_Punggol']
Circle_Stations=['CC29_HarbourFront','CC28_Telok_Blangah','CC27_Labrador_Park','CC26_Pasir_Panjang','CC25_Haw_Par_Villa','CC24_Kent_Ridge','CC23_one-north','CC22_Buona_Vista','CC21_Holland_Village','CC20_Farrer_Road','CC19_Botanic_Gardens','CC17_Caldecott','CC16_Marymount','CC15_Bishan','CC14_Lorong_Chuan','CC13_Serangoon','CC12_Bartley','CC11_Tai_Seng','CC10_MacPherson','CC9_Paya_Lebar','CC8_Dakota','CC7_Mountbatten','CC6_Stadium','CC5_Nicoll_Highway','CC4_Promenade','CC3_Esplanade','CC2_Bras_Basah','CC1_Dhoby_Ghaut','CC2_Bras_Basah','CC3_Esplanade','CC4_Promenade','CE1_Bayfront','CE2_Marina_Bay']

len(Circle_Stations)

DT_s6edge=datapreparation(bukitPanjangToExpo_s6edge, '2020-12-25 09:17:00.000','2020-12-25 10:23:51.000', resize=15, neednormalizepressure = True) #use findErrorDuration2

test_final = DT_s6edge
test_final

DT_s6edge_temp = errorRemovingPipeline(DT_s6edge)
DT_s6edge_final = appendStation(DT_s6edge_temp,DT_Stations)
DT_s6edge_final

trydata = addStationToDf(test_final,DT_s6edge_final)
trydata

trydata2 = fillEmptyStationToDf(trydata)
trydata2

count = 0
while DT_s6edge_final != []:
  for i in range(len(test_final['Time'])):
    if test_final['Time'][i] == DT_s6edge_final[0][1]:
      test_final['Station'][i] = DT_s6edge_final[0][4]
      DT_s6edge_final.pop(0)
      count += 1
      print('same!!!', count)
      break

temp = test_final['Station'][0]
for i in range(len(test_final['Station'])):
  if test_final['Station'][i] != '0':
    temp = test_final['Station'][i]
  else:
    test_final['Station'][i] = temp

test_final

appendedList = appendStation(finalList,DT_Stations)
appendedList

for i in list5:
  if i[0] == "Idle":
    i.append(DT_Stations[0])
    DT_Stations.pop(0)
  else:
    i.append("Moving")

list5
list5[-1].insert(3,"0")

for index, row in test_final.iterrows():
  for i in list5:
    if row['Time'] == i[1]:
      row["Station_appended"] = i[4]
      print(row["Station_appended"])
      list5.remove(i)

"""#Demo of functions"""

DT_s6edge

modeChangedList = modeChanged(DT_s6edge)
modeChangedList

newModeChangedList = removeBackwardTimestampError(modeChangedList)

newModeChangedList

recalculatedModeList = recalculateDuration(newModeChangedList)
recalculatedModeList

recalculatedAndRemovedList = removeErrorDuration(recalculatedModeList)
recalculatedAndRemovedList

timestampKey = selectTimestampKey(recalculatedAndRemovedList)
timestampKey

"""# Function testing phase"""

DT_s6edge_temp = errorRemovingPipeline(DT_s6edge)
DT_s6edge_keyvalues = appendStation(DT_s6edge_temp,DT_Stations)
DT_s6edge = modifyColumnStation(DT_s6edge,DT_s6edge_keyvalues)

DT_s6edge.describe()

DT_s6edge.nunique()

DT_s6edge['Station'].value_counts()

DT_s6edge['Station'].unique()

DT_iphone12pro_temp = errorRemovingPipeline(DT_iphone12pro)
DT_iphone12pro_keyvalues = appendStation(DT_iphone12pro_temp,DT_Stations)
DT_iphone12pro = modifyColumnStation(DT_iphone12pro,DT_iphone12pro_keyvalues)

DT_iphone12pro

DT_iphone12pro['Station'].value_counts()

TE_s6edge_temp = errorRemovingPipeline(TE_s6edge)
TE_s6edge_keyvalues = appendStation(TE_s6edge_temp,TE_Stations)
TE_s6edge = modifyColumnStation(TE_s6edge,TE_s6edge_keyvalues)

TE_s6edge

TE_s6edge['Station'].value_counts()

TE_iphone12pro_temp = errorRemovingPipeline(TE_iphone12pro)
TE_iphone12pro_keyvalues = appendStation(TE_iphone12pro_temp,TE_Stations)
TE_iphone12pro = modifyColumnStation(TE_iphone12pro,TE_iphone12pro_keyvalues)

TE_iphone12pro

TE_iphone12pro['Station'].value_counts()

NE_s6edge_temp = errorRemovingPipeline(NE_s6edge)

NE_s6edge_temp = errorRemovingPipeline(NE_s6edge)
NE_s6edge_keyvalues = appendStation(NE_s6edge_temp,NE_Stations)
NE_s6edge = modifyColumnStation(NE_s6edge,NE_s6edge_keyvalues)

NE_s6edge

len(NE_Stations)

NE_iphone12pro_temp = errorRemovingPipeline(NE_iphone12pro)
NE_iphone12pro_keyvalues = appendStation(NE_iphone12pro_temp,NE_Stations)
NE_iphone12pro_keyvalues[0][1]
NE_iphone12pro['Time'][0]

rslt_df = NE_iphone12pro[NE_iphone12pro['Time'] == '2020-12-19 02:36:04.040000'] 
if rslt_df['Time'] == '2020-12-19 02:36:04.040000':
  rslt_df['Station'] = 'abcd'
  print('is added!!!')
rslt_df

rslt_df['Time'] == '2020-12-19 02:36:04.040000'

rslt_df

NE_iphone12pro

NE_iphone12pro_keyvalues

NE_iphone12pro_temp = errorRemovingPipeline(NE_iphone12pro)
NE_iphone12pro_keyvalues = appendStation(NE_iphone12pro_temp,NE_Stations)
#before this is okay already
NE_iphone12pro = modifyColumnStation(NE_iphone12pro,NE_iphone12pro_keyvalues)

NE_iphone12pro

circle_s6edge_temp = errorRemovingPipeline(circle_s6edge)
circle_s6edge_keyvalues = appendStation(circle_s6edge_temp,Circle_Stations)
circle_s6edge = modifyColumnStation(circle_s6edge,circle_s6edge_keyvalues)

circle_s6edge

circle_iphone11_temp = errorRemovingPipeline(circle_iphone11)
circle_iphone11_keyvalues = appendStation(circle_iphone11_temp,Circle_Stations)
circle_iphone11 = modifyColumnStation(circle_iphone11,circle_iphone11_keyvalues)

circle_iphone11

