# %%
import pandas as pd
df = pd.read_csv("data.csv")
print(df)

# %%
import json
df_1=pd.read_json("students.json")
print(df_1)

# %%
import re
with open('callcenter20250301.log',"r",encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(\d{6})-(\d{7})')
masked_content = pattern.sub(r'\1-*******', content)

with open('masked_callcenter20250301.log',"w") as f:
    f.write(masked_content)

# %%
with open("data.json","r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.read_json("data.json",orient="records")

df

# %%
import requests
import json

url="https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":"37.58638333",
    "longitude":"127.0203333",
    "current":"temperature_2m"
}




try:
    response = requests.get(url, verify=False, params=params)
    response.raise_for_status()
    data = response.json()

    print(data)


    print("API 응답:", data)
    print("서울시의 현재 온도는 : {0}{1} 입니다".format(data["current"]["temperature_2m"], data["current_units"]["temperature_2m"]))


except requests.exceptions.RequestException as e: 
    print(f'API 호출 실패: {e}')
except json.JSONDecodeError as e:
    print(f'JSON 파싱 실패: {e}')

# %%
import requests

url = "https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
api_key= "af0QZng7h0Yrix8MM9SoxXCWNquWeuiXyWCO5r/RUfVQ4LRpeJhgN5KClOBkZ8icqmK0RyZ1C4pGZEVAB2ViEw=="

params = {
    "serviceKey":api_key,
    "returnType":"JSON",
    "numOfRows":"100",
    "pageNo":"1",
    "sidoName":"서울",
    "ver":"1.0"
}

response_1 = requests.get(url, verify=False, params=params).json()


print(json.dumps(response_1,indent=4,ensure_ascii=False))


# %%
vrty_code = ["01", "02", "03", "06"]
output=""

for i in vrty_code:

    url_hw = "https://apis.data.go.kr/B552845/perDay/price"

    params_hw ={
    "serviceKey":api_key,
    "returnType":"JSON",
    "pageNo":"1",
    "numOfRows":"400",
    "cond[exmn_ymd::LTE]":"20151231",
    "cond[exmn_ymd::GTE]":"20150101",
    "cond[se_cd::EQ]":"02",
    "cond[ctgry_cd::EQ]":"200",
    "cond[item_cd::EQ]":"211",
    "cond[grd_cd::EQ]":"04",
    "cond[sgg_cd::EQ]":"1101",
    "cond[mrkt_cd::EQ]":"0110211",
    "cond[vrty_cd::EQ]":i
    }
    response_hw = requests.get(url_hw,verify=False,params=params_hw).json()

    with open(f"output_{i}.json","w",encoding="utf-8") as f:
        json.dump(response_hw, f, indent=4, ensure_ascii=False)

# %%
