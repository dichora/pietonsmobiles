import math
def metersFromLong(x,unit):
    d2r = degOrGradToRad(unit, x)
    return((111415.13 * math.cos(d2r))- (94.55 * math.cos(3.0*d2r)) + (0.12 * math.cos(5.0*d2r)))

def metersFromLat(x,unit):
    d2r = degOrGradToRad(unit, x)
    return(111132.09 - (566.05 * math.cos(2.0*d2r))+ (1.20 * math.cos(4.0*d2r)) - (0.002 * math.cos(6.0*d2r)))


def degOrGradToRad(unit, x):
    if unit == 'DEG':
        d2r = x * 2 * math.pi / 360
    elif unit == 'GRAD':
        d2r = x * 2 * math.pi / 400
    elif unit == 'RAD':
        d2r = x
    return d2r

