import matplotlib.pyplot as plt
import pandas as pd

fin = open('therm.out')
count = 0
columns = []
data = []
for line in fin.readlines():
    line = line.rsplit()
    if count==0:
        # put it into header        
        columns = line
    else:
        data.append(line)        
    count += 1

df = pd.DataFrame(data, columns=columns)

legends = []
for i in range(12):
    dat = df.iloc[i,:]
    t = float(dat.TIME)
    T0 = float(dat.T0)
    T1 = float(dat.T1)
    T2 = float(dat.T2)
    T3 = float(dat.T3)
    T4 = float(dat.T4)
    T5 = float(dat.T5)
    T6 = float(dat.T6)
    T7 = float(dat.T7)
    T8 = float(dat.T8)
    T9 = float(dat.T9)
    T10 = float(dat.T10)
    x = [0,1,2,3,4,5,6,7,8,9,10]
    y = [T0,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10]    
    plt.plot(x,y,'o-')
    legends.append('t='+str(t))

plt.legend(legends)    
plt.xlabel('Location [inside=0, outside=10]')
plt.ylabel('Temperature (C)')
plt.title('Tepmerature Distribution through casing wall')
plt.show()
