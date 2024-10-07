from bs4 import BeautifulSoup
import requests

URL = 'https://randompoem.fun/'
URL = 'https://www.poetrysoup.com/famous/poems/random_famous_poem.aspx'


def get_poem(url: 'string') -> 'poem':
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_soup = soup.find('pre')
    poem = new_soup.text.strip()
    return poem


def get_writer(url: 'string') -> 'writer':
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_soup = soup.find('div', class_ = 'byline')
    writer = new_soup.text.strip()
    return writer[11:]


def send_poem():
    print(get_writer('https://www.poetrysoup.com/famous/poems/random_famous_poem.aspx'))
    print("---------------------")
    print(get_poem('https://www.poetrysoup.com/famous/poems/random_famous_poem.aspx'))


# def get_poem(html: 'html')

def main() -> None:
    send_poem()


if __name__ == "__main__":
    main()
