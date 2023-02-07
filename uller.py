import requests

response = requests.get('https://www.ahnegao.com.br/')
print(response.status_code)  # 200 significa requisição OK

print(len(response.content))

print(response.content[:100])  # imprimindo só os 100 primeiros chars  