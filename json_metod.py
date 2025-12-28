import json

# json_data = {
#     "name": "Миша Ivanov",
#     "age": 20,
#     "city": "Moscow",
#     "skils": ["SQL", "Python"],
# }

# json_string = json.dumps(json_data)

# print(json_string)

# python_dict = json.loads(json_string)

# print(python_dict["name"])

user_profile = {
    "user_id": 123,
    "username": "coder2025",
    "settings": {"theme": "dark", "notifications": True},
}


with open("users.json", "w", encoding="utf-8") as f:
    json.dump(user_profile, f)

print("Файл json создан")

with open("users.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Тема оформления {data['settings']['theme']}")
