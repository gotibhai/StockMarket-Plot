import plotly.plotly as py
import plotly.graph_objs as go

from datetime import datetime

x = [datetime(year=2013, month=01, day=01),
     datetime(year=2013, month=01, day=02),
     datetime(year=2013, month=01, day=03),
     datetime(year=2013, month=01, day=04),
     datetime(year=2013, month=01, day=05),
     datetime(year=2013, month=01, day=06),
     datetime(year=2013, month=01, day=07),
     datetime(year=2013, month=01, day=8),
     datetime(year=2013, month=01, day=9),
     datetime(year=2013, month=01, day=10),
     datetime(year=2013, month=01, day=11),
     datetime(year=2013, month=01, day=12),
     datetime(year=2013, month=01, day=13),
     datetime(year=2013, month=01, day=14),
     datetime(year=2013, month=01, day=15),
     datetime(year=2013, month=01, day=16),
     datetime(year=2013, month=01, day=17),
     datetime(year=2013, month=01, day=18),
     datetime(year=2013, month=01, day=19),
     datetime(year=2013, month=01, day=20),
     datetime(year=2013, month=01, day=21),
     datetime(year=2013, month=01, day=22),
     datetime(year=2013, month=01, day=23),
     datetime(year=2013, month=01, day=24),
     datetime(year=2013, month=01, day=25),
     datetime(year=2013, month=01, day=26),
     datetime(year=2013, month=01, day=27),
     datetime(year=2013, month=01, day=28),
     datetime(year=2013, month=01, day=29),
     datetime(year=2013, month=01, day=30),
     datetime(year=2013, month=01, day=31),
     datetime(year=2013, month=02, day=01),
     datetime(year=2013, month=02, day=02),
     datetime(year=2013, month=02, day=03),
     datetime(year=2013, month=02, day=04),
     datetime(year=2013, month=02, day=05)]

list1 = [1125.55,1122.70,1095.45,1081,1091.35,1083.50,1081.15,1110.15,1108.5,1107.5,1150.80,1174.70,1179.75,1157.70,1175.55,1173.75,1164.90,1129.60,1138.50,1137.65,1136.25,1137.05,1121.25,1139.65,1131.90,1139.90,1133.00,1083.40,1049.95,1055.70,1063.30,1050.80,1069.35,1074.05,1078.90,1105.25]
list2 = []
periods = int(raw_input("Please enter the number of periods: "))
multiplier = 2.0/float(periods + 1)
sma = 0
len_list1 = len(list1);
ema = 0
print "\nMultipler = "
print multiplier
j = 0
while j < periods:
	sma = sma + list1[j]
	print list1[j]
	j = j + 1
sma = float(sma/periods)
print "\n SMA = "
print sma
i = 0
while(i < len_list1):
	if(i < periods):
		list2.append(0)
	elif(i == periods):
		list2.append(sma)
	else :
		ema = (list1[i]*multiplier) + (list2[i-1]*(1 - multiplier))
		list2.append(ema)
	i = i + 1;

trace1 = go.Scatter(x=x,y=list2)
trace2 = go.Scatter(x=x,y=list1)

data = [trace1 , trace2]
py.plot(data)

for each in list2:
	print each

print "\nMultipler = "
print multiplier




