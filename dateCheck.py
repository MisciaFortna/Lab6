import speRead as sp

intF = './TXT_Files/Acq300sec_'
endF = '.txt'

for i in range(10):
    fileName = intF + '00' + str(i) + endF
    print(str(sp.date(fileName)) + ' : ' + str(sp.time(fileName, 15000, 15, 15, 15)))
    print('\n')

for i in range(10, 100):
    fileName = intF + '0' + str(i) + endF
    print(str(sp.date(fileName)) + ' : ' + str(sp.time(fileName, 15000, 15, 15, 15)))
    print('\n')

for i in range(100, 110):
    fileName = intF + str(i) + endF
    print(str(sp.date(fileName)) + ' : ' + str(sp.time(fileName, 15000, 15, 15, 15)))
    print('\n')
