import sys
import speRead as sp
import matplotlib.pyplot as plt

file1 = sys.argv[1]
file2 = sys.argv[2]
temp = 0
X = []
Y = []
noise = []
data = []

data = sp.spread(file1)
noise = sp.spread(file2)

for i in range(len(data)):
    temp = data[i] - noise[i]
    Y.append(temp)
    if Y[i] < 0:
        Y[i] = 0

for i in range(len(data)):
    X.append(i)


plt.plot(X, Y)
plt.title('Without Noise')
plt.xlabel('Time [s]')
plt.ylabel('Peak Counts')
plt.savefig('Noiseless')
