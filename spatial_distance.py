import numpy as np
from math import sin, cos, acos, radians

# 那覇空港
ø1 = 26.2064
lam1 = 127.6465
# 首里城
ø2 = 26.2183
lam2 = 127.7154

del_ø = abs(ø1-ø2)
del_lam = abs(lam1-lam2)

theta = 2*np.arcsin(np.sqrt(np.sin(radians(del_ø/2))**2 + np.cos(radians(ø1))*np.cos(radians(ø2))*np.sin((radians(del_lam)/2)**2)))
# theta = np.arctan2(np.sqrt((np.cos(ø2)*np.sin(del_lam))**2 + (np.cos(ø1)*np.sin(ø2) - np.sin(ø1)*np.cos(ø2)*np.cos(del_lam))**2) / np.sin(ø1)*np.sin(ø2) + np.cos(ø1)*np.cos(ø2)*np.cos(del_lam))
er = 6378.137
d = er * theta

print(d)

def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

def dist_on_sphere(pos0lat, pos0lng, pos1lat, pos1lng, radius=6378.137):
    xyz0, xyz1 = latlng_to_xyz(pos0lat, pos0lng), latlng_to_xyz(pos1lat, pos1lng)
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius

print(dist_on_sphere(ø1, lam1, ø2, lam2))


# from geopy.distance import great_circle
# NahaAirport = (26.2064, 127.6465)
# SyuriCastle = (26.2183, 127.7154)

# dis = great_circle(NahaAirport, SyuriCastle).km
# print(dis)
# # 6.999682077880665 (道のりで8kmくらいなため正しい)