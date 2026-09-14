# %%
import pandas as pd

data = {
    'student_id': [101, 102, 103, 104, 105],
    'database_score': [85, 76, 92, 63, 88],
    'cloudcomputing_score': [78, 82, 95, 70, 84],
    'python_score': [92, 78, 85, 75, 91],
    'watch_rate': [0.95, 0.87, 0.99, 0.80, 0.93]
}

df = pd.DataFrame(data)

df.to_csv("data.csv", encoding="utf-8")

# %%
import json
data22 = {
    "이름":"하시준",
    "나이": [8, 9, 12],
    "거주지": "서울숲",
    "관심사": ["요리","그림","장난","프로그래밍"]
}

with open ("data22.json", "w", encoding="utf-8") as f:
    json.dump(data22, f, indent=4, ensure_ascii=False)
# %%
import pandas as pd

data3 = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터학", "경영학", "농학", "교육학", "영어영문학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
    }

df3 = pd.DataFrame(data3)
print(df)
print(df.index)
print(df.columns)
print(df.values.tolist())
print(df.values.flatten())


# %%

df4 = pd.DataFrame(data3)

df4.to_csv("data33.csv")
df4.to_json("data33.json", indent=4,orient="records", force_ascii=False)
df4.to_html("data33.html")
# %%

import requests

url = "https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
api_key ="af0QZng7h0Yrix8MM9SoxXCWNquWeuiXyWCO5r/RUfVQ4LRpeJhgN5KClOBkZ8icqmK0RyZ1C4pGZEVAB2ViEw=="

params = {
    "serviceKey":api_key,
    "returnType":"json",
    "numOfRows":"100",
    "pageNo":"1",
    "sidoName":"서울",
    "ver":"1.0",
}

response = requests.get(url, params=params,verify=False)

# %%
with open("json_air.json","w",encoding="utf-8") as j:
    json.dump(response.json(), j, indent=4, ensure_ascii=False)

print(response.json())


# %%

json_air=response.json()["response"]["body"]["items"]
air_df = pd.DataFrame(json_air)
air_df[["dataTime","stationName","pm10Grade"]]
# %%

air_df.to_json("air_df.json", indent=4, force_ascii=False, orient="records")

air_df.to_csv("air_df.csv", encoding="utf-8", index=False)

air_df.to_excel("air_df.xlsx", index=False)

air_df.to_html("air_df.html", encoding="utf-8", index=False)
# %
# %%
air_df_csv = pd.read_csv("air_df.csv")
air_df_csv
# %%
