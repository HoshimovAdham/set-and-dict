users = [
    {
        "first_name": "Angeline",
        "last_name":"Timothy",
        "email":"atimothy0@geocities.com",
        "gender":"Female",
        "ip_address":"48.93.26.14",
        "age": 12
    },
    {
        "first_name":"Shandy",
        "last_name":"Kierans",
        "email":"skierans1@surveymonkey.com",
        "gender":"Female",
        "ip_address":"164.225.85.37",
        "age": 15
    },
    {
        "first_name":"Scott",
        "last_name":"Ketton",
        "email":"sketton2@sogou.com",
        "gender":"Male",
        "ip_address":"71.70.178.85",
        "age": 10
    },
]

males = 0
females = 0
n = len(users)

for user in users:
    if user['gender'] == "Male":
        males += 1
    elif user['gender'] == "Female":
        females += 1

percent_male = round(males / n * 100, 2)
percent_female = round(females / n * 100, 2)

print(f"Hisobor:\n\tErkaklar: {males}, {percent_male}%\n\tAyollar: {females}, {percent_female}%")
