import math
import csv
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt

def metersFromLong(x,unit='RAD'):
    d2r = degOrGradToRad(unit, x)
    return((111415.13 * math.cos(d2r))- (94.55 * math.cos(3.0*d2r)) + (0.12 * math.cos(5.0*d2r)))

def metersFromLat(x,unit='RAD'):
    print('x',x,'type',type(x))
    d2r = degOrGradToRad(unit, x)
    print('d2r',d2r,'type',type(d2r))
    return(111132.09 - (566.05 * math.cos(2.0*d2r))+ (1.20 * math.cos(4.0*d2r)) - (0.002 * math.cos(6.0*d2r)))


def degOrGradToRad(unit, x):
    if unit == 'DEG':
        d2r = x * 2 * math.pi / 360
    elif unit == 'GRAD':
        d2r = x * 2 * math.pi / 400
    elif unit == 'RAD':
        d2r = x
    return d2r

#lecture du csv, conversion en liste
gps_liste=[]
with open('../tour de la bourse GPS.csv', newline='') as csvfile:
    gpsreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in gpsreader:
        #print(', '.join(row))
        gps_liste.append(row)

gps_liste = np.asarray(gps_liste)
# gps_liste = gps_liste.astype(np.float)

vmflat = np.vectorize(metersFromLat)
vmflng = np.vectorize(metersFromLong)
latData = vmflat(np.asarray(gps_liste)[:,1].astype(np.float))
lngData = vmflng(np.asarray(gps_liste)[:,2].astype(np.float))
latLngData = np.column_stack((latData.T, lngData.T))

plt.xlabel('x')
plt.ylabel('y')
x, y = latLngData.T
plt.plot(x,y)
plt.show()
