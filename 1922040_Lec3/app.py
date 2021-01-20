from dataaccess import DataAccess
import numpy as np

num = input("0→感性が似ている場所を検索, 1→空間的に近い場所を検索, 2→営業時間が似ている場所を検索")

da = DataAccess()

if num == "0":
    loc = input('検索したい場所を入力してください。')
    spot_list = da.get_spots_sensitivity(loc)
    spot_list2 = da.get_spots_sensitivity2(loc)

    base = np.array([])
    b = np.array([])
    kekka = np.array([])

    if len(spot_list) != 0:
        for spot in spot_list:
            base = np.append(base, list(spot))
        for spots in spot_list2:
            b = np.append(b, list(spots), axis=0)
        b = b.reshape(len(spot_list2), int(len(b) / len(spot_list2)))
        # print(base)
        # print(b)
        for item in b:
            ans = np.sum(base * np.array([item[1:]], dtype=int))
            if len(kekka) == 0 or float(kekka[1]) < ans:
                kekka = np.array([])
                kekka = np.append(kekka, [item[0], ans])
        
        print('一番近い場所は', kekka[0], 'です。内積結果は', kekka[1], 'です。')
    else:
        print("その場所はありませんでした。バンナ公園、石垣島鍾乳洞、石垣やいま村を入力してみてください。")

if num == "1":
    loc = input("検索したい場所を入力してください。")
    spot_list = da.get_lat_lng(loc)
    spot_list2 = da.get_lat_lng2(loc)

    base = np.array([])
    b = np.array([])
    kekka = np.array([])

    if len(spot_list) != 0:
        for spot in spot_list:
            base = np.append(base, list(spot))
        for spots in spot_list2:
            b = np.append(b, list(spots), axis=0)
        b = b.reshape(len(spot_list2), int(len(b) / len(spot_list2)))

        for item in b:
            ans = np.linalg.norm(base - np.array([item[1:]], dtype=float))
            if len(kekka) == 0 or float(kekka[1]) > ans:
                kekka = np.array([])
                kekka = np.append(kekka, [item[0], ans])
        print('一番近い場所は', kekka[0], 'です。ユークリッド距離は', kekka[1], 'です。')
    else:
        print("検索結果はありませんでした。バンナ公園、石垣島鍾乳洞、石垣やいま村を入力してみてください。")

if num == "2":
    loc = input("検索したい場所を入力してください。")
    spot_list = da.get_open_close(loc)
    spot_list2 = da.get_open_close2(loc)

    base = np.array([])
    b = np.array([])
    kekka = np.array([])

    if len(spot_list) != 0:
        for spot in spot_list:
            base = np.append(base, list(spot))
        for spots in spot_list2:
            b = np.append(b, list(spots), axis=0)
        b = b.reshape(len(spot_list2), int(len(b) / len(spot_list2)))

        for item in b:
            ans = np.sum(np.abs(base - np.array([item[1:]], dtype=float)))
            if len(kekka) == 0 or float(kekka[1]) > ans:
                kekka = np.array([])
                kekka = np.append(kekka, [item[0], ans])
        print('一番営業時間が近いのは', kekka[0], 'です。計算結果は', kekka[1], 'です。')
    else:
        print("検索結果はありませんでした。バンナ公園、石垣島鍾乳洞、石垣やいま村を入力してみてください。")

if num != "0" and num != "1" and num != "2":
    print('0か1か2を入力してください。')