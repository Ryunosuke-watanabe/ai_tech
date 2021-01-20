CREATE TABLE location_sensitivity(
    id SERIAL PRIMARY KEY,
    loc TEXT,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    balloon TEXT,
    fun INTEGER,
    history INTEGER,
    view INTEGER,
    nature INTEGER,
    open_time INTEGER,
    close_time INTEGER
);

INSERT INTO location_sensitivity(
    loc, lat, lng, balloon, fun, history, view, nature, open_time, close_time
) VALUES(
    'バンナ公園', 
    24.37501, 
    124.160795, 
    '石垣島中央に位置する標高230mのバンナ岳。バンナ公園はバンナ岳にある海の見える山の公園なのです。石垣島の透き通った海が見える展望台や異国情緒を思わせる南国の木々、子供が大自然の中でのびのびと遊べる広場など、市民の生活には欠かせない場所になっています。',
    1,
    0,
    1,
    1,
    9,
    21
);

INSERT INTO location_sensitivity(
    loc, lat, lng, balloon, fun, history, view, nature, open_time, close_time
) VALUES(
    '石垣島鍾乳洞',
    24.361743,
    124.154466,
    '２０万年の時をかけて自然が造り出した石垣島最大の鍾乳洞。キラキラ光る鍾乳石、鍾乳洞イルミネーションの幻想的な輝き、水の音を楽しむ水琴窟、トトロの鍾乳石など見所がいっぱいです。',
    1,
    1,
    0,
    1,
    9,
    18
);

INSERT INTO location_sensitivity(
    loc, lat, lng, balloon, fun, history, view, nature, open_time, close_time
) VALUES(
    '石垣やいま村',
    24.40489,
    124.144636,
    '石垣島の名所「名蔵湾」を一望する丘にある「石垣やいま村」は、豊かな自然を背景に旧き良き八重山の家並みを再現したテーマパークです。',
    1,
    0,
    0,
    0,
    9,
    17
);
