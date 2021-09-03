import requests

balance = requests.post('http://localhost:5001/api/v1/balance', json={'account': '17PBfmGiEUt8diTd3fD8idpnFPXiiiX4FacfzL'}).json()
print(balance["data"])
