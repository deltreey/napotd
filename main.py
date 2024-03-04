from bs4 import BeautifulSoup
from requests import get
from starlette.responses import RedirectResponse
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(main())


def main():
    url = "https://apod.nasa.gov/apod/"
    response = get(url)
    html = response.text
    soup = BeautifulSoup(html, features="html.parser")
    img = soup.find('img')
    image_url = img['src']
    return url + image_url
    # with open('img.png', 'wb') as out_file:
    #     response = get(url + image_url, stream=True)
    #     for chunk in response:
    #         out_file.write(chunk)
