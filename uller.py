import os
import requests
from bs4 import BeautifulSoup

url_list = ['https://portoalegre-airport.com.br/pt/',
            'https://www.ahnegao.com.br/', 'https://openai.com/blog/chatgpt/']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.104 Safari/537.3"
}
count = 0

for url in url_list:

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        images = soup.find_all("img")

        if not os.path.exists("images"):
            os.makedirs("images")

        for i, image in enumerate(images):
            try:
                img_url = image["src"]
                if not img_url:
                    # ou qualquer outro atributo que possa ser usado para identificar a URL da imagem
                    img_url = image["class"]
                if 'https' in img_url:
                    response = requests.get(img_url, headers=headers)
                    open(f"images/{count}.jpg", "wb").write(response.content)
                else:
                    response = requests.get(url+img_url, headers=headers)
                    open(f"images/{count}.jpg", "wb").write(response.content)
            except (KeyError, requests.exceptions.RequestException) as e:
                if not img_url:
                    img_url = image["class"]
                if 'https' in img_url:
                    response = requests.get(img_url, headers=headers)
                    open(f"images/{count}.jpg", "wb").write(response.content)
                else:
                    response = requests.get(url+img_url, headers=headers)
                    open(f"images/{count}.jpg", "wb").write(response.content)
            count = count + 1
