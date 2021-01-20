from dataaccess import DataAccess

num = input("0→全体, 1→検索")

da = DataAccess()

if num == "0":
    spot_list = da.get_spots()
    for spot in spot_list:
        print(spot)

if num == "1":
    loc = input("検索したい場所を入力してください。")
    spot_list = da.get_lat_lng(loc)
    if len(spot_list) == 0:
        print("検索結果はありませんでした。バンナ公園、石垣島鍾乳洞、石垣やいま村を入力してみてください。")
    else:
        for spot in spot_list:
            print(spot)

if num != "0" and num != "1":
    print('0か1を入力してください。')