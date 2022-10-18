import speRead as spe
import matplotlib.pyplot as plt
import numpy as np

intF = './TXT_Files/Acq300sec_'
endF = '.txt'
vals = []
X = []
Y = []
avgVal = 0
time = 0

for i in range(10):
    time = 300
    fileName = intF + '00' + str(i) + endF
    vals = spe.spread(fileName)
    avgVal = spe.average(vals)
#    time = spe.time(fileName, 15000, 15, 15, 15)
#    print(str(time) + ', ' + str(avgVal))
    time += i
#    X.append(spe.time(fileName, 15000, 15, 15, 15))
    X.append(time)
    Y.append(avgVal)
#    Y.append(np.log(avgVal))

for i in range(10, 100):
    time = 300
    fileName = intF + '0' + str(i) + endF
    vals = spe.spread(fileName)
    avgVal = spe.average(vals)
    time += i
#    time = spe.time(fileName, 15000, 15, 15, 15)
#    print(str(time) + ', ' + str(avgVal))
#    X.append(spe.time(fileName, 15000, 15, 15, 15))
    X.append(time)
    Y.append(avgVal)
#    Y.append(np.log(avgVal))

for i in range(10):
    time = 400
    fileName = intF + '10' + str(i) + endF
    vals = spe.spread(fileName)
    avgVal = spe.average(vals)
    time += i
#    time = spe.time(fileName, 15000, 15, 15, 15)
#    print(str(time) + ', ' + str(avgVal))
#    X.append(spe.time(fileName, 15000, 15, 15, 15))
    X.append(time)
    Y.append(avgVal)
#    Y.append(np.log(avgVal))

#file1 = open('speA300.txt', 'w')
#for i in range(len(Y)):
#    file1.write(str(Y[i]) + '\n')
#file1.close()

plt.plot(X, Y)
plt.title('300 Over Time')
plt.xlabel('Time [s]')
plt.ylabel('Peak Counts')
plt.savefig('total300')
