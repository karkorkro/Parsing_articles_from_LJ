import requests
from random import choice
from bs4 import BeautifulSoup

blogger = 'evo-lutio'


def find_random_evo_article():
    month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
                  'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    years = list(range(2013, 2024))
    year = choice(years)
    url = f'https://{blogger}.livejournal.com/{year}'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    months = []
    for i in soup.find_all('a', class_='month'):
        if i.text == 'Jan':
            pass
        else:
            months.append(i.text)

    month = month_dict.get(choice(months))
    url = f'https://{blogger}.livejournal.com/{year}/{month}'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'{year}, {month}')

    posts = []
    for i in soup.find('div', class_='entry-text').find_all('dd'):
        posts.append(i.contents[1].get('href'))
    article = choice(posts)
    return article


def show_tags():
    url = f'https://{blogger}.livejournal.com/tag/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags_list = soup.find('div', class_='content-tags').text
    return tags_list


def check_tag(tag):
    return tag in show_tags().strip('\n').split(', ')


def tag_random(tag):
    if not check_tag():
        return "Некорректный тег, попробуйте посмотреть список тегов с помощью команды /showtags"
    else:
        url = f'https://{blogger}.livejournal.com/tag/{tag}'
        return url




