from pytopo import azimuth

def pi():
    return 3.1415926535897932384626433832795


def rad2grad(rads):
    return rads * 200 / pi()


def azimuth_centesimales(vector):
    az_rads = azimuth((0,0), vector)
    return round(rad2grad(az_rads),4)


print(azimuth_centesimales([-1,-1]))

