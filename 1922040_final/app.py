from dataaccess import DataAccess
from dist import Graph
from dist_GA import DIST_GA
import numpy as np
from math import sin, cos, acos, radians

num = input("1→空間的に近い場所を検索, 2→２点間の移動時間, 3→感性が近い場所への時間, 4→遺伝的アルゴリズムによる巡回経路")

da = DataAccess()

if num == "1":
    loc = input("検索したい場所を入力してください。")
    spot_list = da.get_lat_lng(loc)
    spot_list2 = da.get_lat_lng2(loc)

    base = np.array([])
    b = np.array([])
    kekka = np.array([])

    ### 大円距離のための関数

    def latlng_to_xyz(lat, lng):
        rlat, rlng = radians(lat), radians(lng)
        coslat = cos(rlat)
        return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

    def dist_on_sphere(pos0lat, pos0lng, pos1lat, pos1lng, radius=6378.137):
        xyz0, xyz1 = latlng_to_xyz(pos0lat, pos0lng), latlng_to_xyz(pos1lat, pos1lng)
        return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius

    ### ここまで

    if len(spot_list) != 0:
        for spot in spot_list:
            base = np.append(base, list(spot))
        for spots in spot_list2:
            b = np.append(b, list(spots), axis=0)
        b = b.reshape(len(spot_list2), int(len(b) / len(spot_list2)))

        for item in b:
            # ans = np.linalg.norm(base - np.array([item[1:]], dtype=float))
            ans = dist_on_sphere(base[0], base[1], float(item[1]), float(item[2]))
            if len(kekka) == 0 or float(kekka[1]) > ans:
                kekka = np.array([])
                kekka = np.append(kekka, [item[0],ans])
        print(kekka[0], kekka[1]+'km')
    else:
        print("検索結果はありませんでした。バンナ公園、石垣島鍾乳洞、石垣やいま村を入力してみてください。")

if num == "2":
    loc = input("検索したい場所を入力してください。")
    loc2 = input("もう一つ入力してください。")
    spot_list = da.get_lat_lng(loc)
    spot_list2 = da.get_lat_lng(loc2)

    base = np.array([])
    b = np.array([])
    kekka = np.array([])

    ### 大円距離のための関数

    def latlng_to_xyz(lat, lng):
        rlat, rlng = radians(lat), radians(lng)
        coslat = cos(rlat)
        return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

    def dist_on_sphere(pos0lat, pos0lng, pos1lat, pos1lng, radius=6378.137):
        xyz0, xyz1 = latlng_to_xyz(pos0lat, pos0lng), latlng_to_xyz(pos1lat, pos1lng)
        return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius

    ### ここまで

    if len(spot_list) != 0 or len(spot_list2) != 0:
        for spot in spot_list:
            base = np.append(base, list(spot))
        for spots in spot_list2:
            b = np.append(b, list(spots))

        print(loc, 'から', loc2, 'までの距離は', dist_on_sphere(base[0], base[1], b[0], b[1]), 'kmです。')
        print('時速4kmで移動する場合,かかる時間は', dist_on_sphere(base[0], base[1], b[0], b[1])/4, '時間です。')

    else:
        print("検索結果はありませんでした。")

if num == "3":
    loc = input("検索したい場所を入力してください。")
    spot_list = da.get_spots_sensitivity(loc)
    spot_list2 = da.get_spots_sensitivity2(loc)

    base = np.array([])
    b = np.array([])
    kekka = np.empty((0,2))
    lat_lng = np.empty((0,2))
    base_2 = np.array([])


    def latlng_to_xyz(lat, lng):
        rlat, rlng = radians(lat), radians(lng)
        coslat = cos(rlat)
        return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

    def dist_on_sphere(pos0lat, pos0lng, pos1lat, pos1lng, radius=6378.137):
        xyz0, xyz1 = latlng_to_xyz(pos0lat, pos0lng), latlng_to_xyz(pos1lat, pos1lng)
        return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius

    if len(spot_list) != 0:
        for spot in spot_list:
            base = np.append(base, list(spot))
        for spots in spot_list2:
            b = np.append(b, list(spots), axis=0)
        b = b.reshape(len(spot_list2), int(len(b) / len(spot_list2)))

        for item in b:
            ans = np.sum(base * np.array([item[1:]], dtype=float))
            kekka = np.append(kekka, np.array([[item[0], ans]]), axis=0)
        kekka_ = np.sort(kekka, axis=0)[-5:]
        # print(kekka_)

        spot_list = da.get_lat_lng(loc)
        for spot in spot_list:
            base_2 = np.append(base_2, spot)

        for loca in kekka_[:, 0]:
            spot_list = da.get_lat_lng(loca)
            for spot in spot_list:
                lat_lng = np.append(lat_lng, np.array([spot]), axis=0)

        lat_lng = np.insert(lat_lng, 0, base_2, axis=0)
        # print(lat_lng, lat_lng.shape[0])

        time_spot = np.empty((0, lat_lng.shape[0]))
        for alpha in lat_lng:
            theta = np.array([])
            for beta in lat_lng:
                if alpha[0]==beta[0] and alpha[1]==beta[1]:
                    ans = 0
                else:
                    ans = dist_on_sphere(float(alpha[0]), float(alpha[1]), float(beta[0]), float(beta[1])) / 4

                theta = np.append(theta, ans)
            time_spot = np.append(time_spot, np.array([theta]), axis=0)

        # print(time_spot)

        for l in range(len(time_spot)):
            time_spot[l] = np.where(time_spot[l] > sorted(time_spot[l].ravel())[-2], 0, time_spot[l])
            time_spot[:, l] = time_spot[l]

        # time_spot = np.where(time_spot > sorted(time_spot.ravel())[-10], 0, time_spot)
        # print(time_spot)

        gl = Graph(lat_lng.shape[0])
        gl.graph = time_spot
        dist = gl.dijkstra(0)
        kekka_ = np.insert(kekka_, 0, np.array([loc, 0]), axis=0)
        for i in range(len(dist)):
            print(kekka_[i][0], 'まで', dist[i], '時間')
        # print(time_spot)

    else:
        print("検索結果はありませんでした。")

if num == "4":
    loc = input('検索したい場所を入力てください。')
    spot_list = da.get_lat_lng_sense(loc)
    spot_list2 = da.get_lat_lng_sense2(loc)

    base = np.array([])
    base2 = np.array([])

    for spot in spot_list:
        base = np.append(base, list(spot))
    for spots in spot_list2:
        base2 = np.append(base2, list(spots), axis=0)
    base2 = base2.reshape(len(spot_list2), int(len(base2) / len(spot_list2)))

    # 感性が近いものを抽出
    sense_list = np.empty([0, 4])
    for item in base2:
        ans = np.array([])
        tmp = np.sum(np.array([base[3:]], dtype=float) * np.array([item[3:]], dtype=float))
        ans = np.append(ans, tmp)
        ans = np.append(ans, item[:3])
        sense_list = np.append(sense_list, np.array([ans]), axis=0)

    # 今回は感性が近い4つを採用する
    sense_list = np.sort(sense_list, axis=0)[-4:]
    base_del = np.array([])
    base_del = np.append(base_del, 'base')
    base_del = np.append(base_del, base[:3])
    sense_list = np.append(sense_list, np.array([base_del]), axis=0)
    # print(sense_list)
    result = []
    for item in sense_list:
        tmp = item[-2:]
        tmp = list(np.float_(tmp))
        result.append(tuple(tmp))
    # print(result)
    ga = DIST_GA(len(result), result)
    result_ga = ga.main()

    print('遺伝的アルゴリズムによる最短経路')
    for i in result_ga[0]:
        print(sense_list[i][1])
        print('↓')

    print('合計距離：', result_ga[1])

if num != "1" and num != "2" and num != "3" and num != "4":
    print('0か1か2か3を入力してください。')