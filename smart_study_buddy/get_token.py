import requests
import uuid

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload = 'scope=GIGACHAT_API_PERS'

request_id = str(uuid.uuid4())

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': request_id,
    'Authorization': 'Basic OGI1ZDJhNTktZmUxNi00MTI1LTg1MzgtMTU4NGI1MzI3ZDZmOjczNjkxMGVjLTdiNzItNDZkZC04Y2U4LWU5ZmI4ZjhiM2YyNw=='
}

response = requests.post(url, headers=headers, data=payload, verify=False)

print(response.text)
