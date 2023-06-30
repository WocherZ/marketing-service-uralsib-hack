import requests

res = requests.post("https://f721-46-172-32-24.eu.ngrok.io/predict",
                    json={"text": "Дебетовая карта с бесплатным снятием наличных в банкоматах по всему миру."})

json = res.json()

title = json.get('title')

advertisement = json.get('advertisement')

print(title)

print(advertisement)