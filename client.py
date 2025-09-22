import requests

body = {
    "materials_gathered": 800,
    "materials_used": 700,
    "damage_to_structures": 1500,
    "damage_to_players": 200
}

response = requests.post("http://127.0.0.1:8000/predict", json=body)
print(response.json())
