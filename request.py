import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'distance':2, 'medical_score':9, 'overall_score':6})

print(r.json())