import json
from pprint import pprint

sur_data_list = []
sur_data = {}

response_name = input("What is your name? ")
sur_data['name'] = response_name

response_age = input("What is your age? ")
sur_data['age'] = response_age

response_city = input("What is your city? ")
sur_data['city'] = response_city

print(sur_data)
sur_data_list.append(sur_data)

f = open("data.json", "r")
olddata = json.load(f)
sur_data_list.extend(olddata)
f.close()


with open('data.json', 'w+') as outfile:
    json.dump(sur_data_list, outfile,)



