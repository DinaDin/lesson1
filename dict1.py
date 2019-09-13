dict = {"city":"Москва","temperature":20}
print(dict.get("city"))
dict["temperature"] = dict["temperature"]-5
print(dict)
print(dict.get("country"))
print(dict.get("country","Россия"))
dict["date"]="27.05.2019"
print(dict)
print(len(dict))