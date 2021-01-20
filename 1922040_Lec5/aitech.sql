CREATE TABLE spot_time_table(
    id SERIAL PRIMARY KEY,
    loc TEXT,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    fun INTEGER,
    history INTEGER,
    view INTEGER,
    nature INTEGER,
    open_time INTEGER,
    close_time INTEGER,
    stay_time INTEGER
);

INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('バンナ公園',24.375031,124.160795,1,0,1,1,9,21,60);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('石垣島鍾乳洞',24.361743,124.154466,1,1,0,1,9,18,90);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('石垣やいま村',24.40489,124.144636,1,0,1,1,9,17,90);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('米原ビーチ',24.453028,124.185614,1,0,1,1,0,24,30);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('玉取崎展望台',24.490633,124.278908,1,0,1,1,9,20,30);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('八重山漁協',24.347778,124.145328,0,0,0,1,5,19,10);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('新栄公園',24.340933,124.153402,1,0,1,1,9,21,10);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('南ぬ浜町緑地公園',24.330883,124.157031,1,0,1,1,9,21,20);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('サザンゲート公園',24.330794,124.156776,1,0,1,1,9,21,20);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('舟蔵公園',24.354722,124.136667,1,0,1,1,9,21,30);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('沖縄県石垣市真栄里公園',24.332877,124.167249,1,0,1,1,9,21,20);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('崎原公園',24.345461,124.200597,1,0,1,1,9,21,20);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('新川公園',24.351662,124.146805,1,0,1,1,9,21,10);
INSERT INTO spot_time_table(loc,lat,lng,fun,history,view,nature,open_time,close_time,stay_time) VALUES ('大浜海岸',24.344964,124.201176,0,0,1,1,0,24,30);