import speRead as spe
import matplotlib.pyplot as plt
import numpy as np

intF = './TXT_Files/Acq14400sec_'
endF = '.txt'
noiseFile = './TXT_Files/Background14400sec.txt'
vals = []
X = []
Y = []
avgVal = 0
time = 720000 / 50

# Acq300
for i in range(10):
    fileName = intF + '00' + str(i) + endF
    vals = spe.noiseReduc(fileName, noiseFile)
    avgVal = spe.average(vals)
    time += i
    X.append(time)
    Y.append(avgVal)

for i in range(10, 36):
    fileName = intF + '0' + str(i) + endF
    vals = spe.noiseReduc(fileName, noiseFile)
    avgVal = spe.average(vals)
    time += i
    X.append(time)
    Y.append(avgVal)

file1 = open('speA14400.txt', 'w')
for i in range(len(Y)):
    file1.write(str(X[i]) + ',' + str(Y[i]) + '\n')
file1.close()

plt.plot(X, Y)
plt.title('Total Over Time')
plt.xlabel('Time [s]')
plt.ylabel('Peak Counts')
plt.savefig('totalSpe')
