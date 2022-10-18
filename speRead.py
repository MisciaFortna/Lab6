# Program Name: speReader.py
# Creation Date: 10/13/2022
# Revision Date: 10/15/2022
# Author: Miscia Fortna
# Purpose: 
#   @ spread(): takes spectral data from CHN_2_TXT and returns list of channels
#   @ average(): from list of channels, returns average peak count over 10 channels
#   @ time(): returns total time for a given file, its total runtime, and the base time in H, M, and S
#   @ date(): returns a list for the CHN start time in [HH, MM, SS]
#   @ eFit(): takes list of known channels, list of known energies and returns list of x-axis values in terms of energy
import csv
from scipy.interpolate import lagrange


def spread(fileName):
    Y = []
    X = []
    temp = []

    for times in range(8192):
        X.append(times)

    with open(fileName, 'r') as datafile:
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
        for TIMES in temp:
            Y.append(int(TIMES[0]))
    return Y

def average(spectral):
    mCha = spectral.index(max(spectral))
    avgR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    avgR[5] = spectral[mCha]
    for i in range(1, 6):
        avgR[5 + i] = spectral[mCha + i]
        avgR[5 - i] = spectral[mCha - i]
    avgCount = sum(avgR) / len(avgR)
    return avgCount


def time(fileName, totTime, baseH, baseM, baseS):
    with open(fileName) as fp:
        for i, line in enumerate(fp):
            if i == 2:
                x = line
            elif i > 2:
                break
    
    temp = x.replace('# Start time : ', '')
    temp = temp.replace('b\'', '')
    temp = temp.replace('\'', '')
    temp = temp.replace(':', ' ')
    temp = temp.replace('\n', '')
    tempLi = list(temp.split(" "))
    tempLi = [int(item) for item in tempLi]

    if tempLi[0] < baseH:
        tempLi[0] += 24
    
    time = 3600 * tempLi[0] + 60 * tempLi[1] + tempLi[2] - 3600 * baseH - 60 * baseM - baseS + totTime / 50
    
    return time

def date(fileName):
    with open(fileName) as fp:
        for i, line in enumerate(fp):
            if i == 2:
                x = line
            elif i > 2:
                break
    
    temp = x.replace('# Start time : ', '')
    temp = temp.replace('b\'', '')
    temp = temp.replace('\'', '')
    temp = temp.replace(':', ' ')
    temp = temp.replace('\n', '')
    tempLi = list(temp.split(" "))
    tempLi = [int(item) for item in tempLi]
    return tempLi

def eFit(cSet, eSet):
    eX = []
    poly = lagrange(cSet, eSet)
    for i in range(8192):
        eX.append(poly(i))
    return eX

def noiseReduc(dataFile, noiseFile):
    temp = 0
    nY = []
    data = spread(dataFile)
    noise = spread(noiseFile)

    for i in range(len(data)):
        temp = data[i] - noise[i]
        nY.append(temp)
        if nY[i] < 0:
            nY[i] = 0

    return nY
