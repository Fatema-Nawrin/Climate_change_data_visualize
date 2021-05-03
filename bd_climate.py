

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
df=pd.read_csv('bd_climate.csv',parse_dates=['Date'],index_col='Date')
df2=pd.read_csv('uk_climate.csv',parse_dates=['Date'],index_col='Date')
fig, ax = plt.subplots()
seventies= df["1970-01-01":"1979-12-31"]
ax.plot(seventies.index,seventies['AvgTemp'])
ax.set_xlabel('Seventies')
ax.set_ylabel('Avg temp (Celsius)')
plt.show()
fig.savefig('a.jpg')


fig, ax = plt.subplots(figsize=(12, 8))
ax.hist(seventies['AvgTemp'],bins=15,histtype='stepfilled', color='pink')
plt.title('Average Temperature in Seventies(BD)')
plt.show()
fig.savefig('b.jpg')


fig, ax =plt.subplots(figsize=(8, 8))
seventies= df["1970-01-01":"1979-12-31"]
a=seventies.AvgTemp.mean()
print(a)
eighties= df["1980-01-01":"1989-12-31"]
b=eighties.AvgTemp.mean()
print(b)
nineties= df["1990-01-01":"1999-12-31"]
c=nineties.AvgTemp.mean()
print(c)
thousands= df["2000-01-01":"2009-12-31"]
d=thousands.AvgTemp.mean()
print(d)
years=['1970','1980','1990','2000']
y_pos = np.arange(len(years))
data=[a,b,c,d]
plt.bar(y_pos,data,color ='maroon',width = 0.3)
plt.xticks(y_pos, years)
plt.xlabel('Years')
plt.ylabel('Avg Temperature')
plt.title('Climate change in bd')
plt.show()
fig.savefig('c.jpg')


fig, ax =plt.subplots(figsize=(8, 8))
s_uk= df2["1970-01-01":"1979-12-31"]
p=s_uk.AvgTemp.mean()
print(p)
e_uk= df2["1980-01-01":"1989-12-31"]
q=e_uk.AvgTemp.mean()
print(q)
n_uk= df2["1990-01-01":"1999-12-31"]
r=n_uk.AvgTemp.mean()
print(r)
th_uk= df2["2000-01-01":"2009-12-31"]
s=th_uk.AvgTemp.mean()
print(s)
data2=[p,q,r,s]
plt.bar(y_pos2,data2,color ='pink',width = 0.3)
plt.xticks(y_pos2, years)
plt.xlabel('Years')
plt.ylabel('Avg Temperature')
plt.title('Climate change in uk')
plt.show()
fig.savefig('d.jpg')



fig, ax =plt.subplots(figsize=(8,6))
br1 = np.arange(len(data))
br2 = [x + barWidth for x in br1]
barWidth = 0.3
plt.bar(br1,data,color ='pink',width = barWidth ,label='bd')
plt.bar(br2,data2,color ='red',width = barWidth ,label='uk')
plt.xticks([r + barWidth for r in range(len(data))], years)
plt.legend()
plt.xlabel('Years')
plt.ylabel('Avg Temperature')
plt.title('Climate change Comparision')
plt.show()
fig.savefig('compare.jpg')






