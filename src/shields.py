import requests


def download_image(count: str) -> bytes:
    url = f"https://img.shields.io/badge/thanks-{count}-c.svg"

    response = requests.get(url)
    image = response.content
    return image
