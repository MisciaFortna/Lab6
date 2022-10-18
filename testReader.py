import matplotlib.pyplot as plt
import csv
import sys

Y = []
X = []
temp = []
name = sys.argv[1]
image = sys.argv[2]

for times in range(8192):
    X.append(times)

with open(name, 'r') as datafile:
    plotting = csv.reader(datafile, delimiter='\n')

    for ROWS in plotting:
        temp.append(ROWS)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    value = len(temp) - 1
    temp.pop(value)
    for TIMES in temp:
        Y.append(int(TIMES[0]))

    #plt.plot(X, Y)
    plt.plot(Y)
    plt.title(name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(image)

#        X.append(int(ROWS[0]))
#    X.pop(0)
#    X.pop(0)
#    X.pop(0)

