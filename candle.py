import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
from datetime import datetime
from pandas_datareader import data, wb as web

import pandas_datareader as pdr

list1 = []
list_time = []

df = pdr.DataReader("aapl", 'yahoo', datetime(2007, 10, 1), datetime(2009, 4, 1))
df.reset_index(inplace=True,drop=False)
for i in df['Date']:
	list_time.append(i)

for i in df['Close'].values:
	list1.append(i)

period1 = 20
period2 = 50
multiplier1 = 2.0/float(period1 + 1)
multiplier2 = 2.0/float(period2 + 1)

def ema_func(periods,multiplier):
	newlist = []
	j = 0
	ema = 0
	sma = 0
	len_list1 = len(list1);
	while j < periods:
		sma = sma + list1[j]
		j = j + 1
	sma = float(sma/periods)
	i = 0
	while(i < len_list1):
		if(i < periods):
			newlist.append(float(0))
		elif(i == periods):
			newlist.append(float(sma))
		else:
			if list1[i] is not None and newlist[i-1] is not None:
				ema = (list1[i]*multiplier) + (newlist[i-1]*(1 - multiplier))
				newlist.append(ema)
		i = i + 1;
	return newlist

ema_20 = ema_func(period1,multiplier1)
ema_50 = ema_func(period2,multiplier2)

trace1 = go.Scatter(x=list_time,y=ema_50)
trace2 = go.Scatter(x=list_time,y=ema_20)

fig = FF.create_ohlc(df.Open, df.High, df.Low, df.Close, dates=df.index)
py.plot(fig)

# plot_ly() %>% 
#   add_trace(x = list_time, y = ema_50, type="scatter", mode="lines") %>% 
#   add_trace(x = list_time, y = ema_20, type="scatter", mode = "lines")
#   add_trace()
 


