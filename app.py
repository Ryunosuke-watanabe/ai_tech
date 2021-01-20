from dataaccess import DataAccess

da = DataAccess()
spot_list = da.get_spots()
for spot in spot_list:
    print(spot)
print("----")
spot_list = da.get_spots_by_area("東京")
for spot in spot_list:
    print(spot)
print("----")
spot_list = da.get_latlng_by_spot_name("皇居")
for spot in spot_list:
    print(spot)
print("----")

spot_list = da.get_openclose_by_spot_name("皇居")
for spot in spot_list:
    print(spot)
print("----")
spot_list = da.get_spot_by_features(1, 0, 1, 1, 0)
for spot in spot_list:
    print(spot)
print("----")
spot_list = da.get_spot_by_branch(22)
for spot in spot_list:
    print(spot)