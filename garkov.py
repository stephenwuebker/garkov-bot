import requests
from bs4 import BeautifulSoup
import imgkit
from urllib.parse import urljoin

def GetComic():
    base_url = 'http://joshmillard.com/garkov/'

    #get updated css (if any)
    response_css = requests.get(base_url + "style.css")
    with open("style.css",'wb') as output_file:
        output_file.write(response_css.content)

    #get page html
    response = requests.get(base_url)
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        content = response.content

    soup = BeautifulSoup(content,'html.parser')

    #get the actual comic strip data
    div_bs4 = soup.find('div',class_="comicborder")

    #modify image src url to use absolute url
    for image in div_bs4.findAll('img'):
        image["src"] = urljoin(base_url, image["src"])

    for cb in div_bs4.findAll('div',class_="commentblock"):
        cb["style"] = cb["style"].replace("url(","url(" + base_url)

    #save resulting html as jpg
    imgkit.from_string(str(div_bs4),'garkov.jpg',css='style.css',options={'crop-x':'206', 'crop-w':'612'})