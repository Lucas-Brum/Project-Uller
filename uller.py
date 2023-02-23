import os
import requests
from bs4 import BeautifulSoup


def get_html(url, headers):
    response = requests.get(url, headers=headers)
    return response.content if response.status_code == 200 else None


def get_image_url(image):
    img_url = image.get("src")
    if not img_url:
        img_url = image.get("class")
    return img_url


def download_image(url, img_url, count, headers):
    if 'https' in img_url:
        response = requests.get(img_url, headers=headers)
        open(f"{url.split('/')[-2]}/{count}.jpg", "wb").write(response.content)
    else:
        response = requests.get(f"{url}{img_url}", headers=headers)
        open(f"{url.split('/')[-2]}/{count}.jpg", "wb").write(response.content)


def download_images(url_list):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.104 Safari/537.3"
    }
    count = 0
    for url in url_list:
        html = get_html(url, headers)
        if not html:
            continue

        soup = BeautifulSoup(html, "html.parser")
        images = soup.find_all("img")

        if not os.path.exists(url.split('/')[-2]):
            os.makedirs(url.split('/')[-2])

        for image in images:
            try:
                img_url = get_image_url(image)
                download_image(url, img_url, count, headers)
            except (KeyError, requests.exceptions.RequestException) as e:
                img_url = get_image_url(image)
                download_image(url, img_url, count, headers)

            count += 1


if __name__ == "__main__":
    url_list = ['https://portoalegre-airport.com.br/pt/',
                'https://www.ahnegao.com.br/', 'https://openai.com/blog/chatgpt/']
    download_images(url_list)
