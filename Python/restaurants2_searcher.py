# restaurants_searcher.py

import csv
import json
import requests

# 初期設定
KEYID = "ac0bdde9d64add0a"
COUNT = 100
PREF = "Z011"
FREEWORD = "渋谷駅"
FORMAT = "json"

PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, 
"keyword":FREEWORD, "format":FORMAT}


def write_data_to_csv(params):
    restaurants = []
    json_res = requests.get(
        "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/",
        params=params).text
    response = json.loads(json_res)
    if "eroor" in response["results"]:
        return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        restaurant_name = restaurant["name"]
        restaurants.append(restaurant_name)
        
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(restaurants)
    
    return print(restaurants)
    
write_data_to_csv(PARAMS)

