import requests
from bs4 import BeautifulSoup
from pprint import pprint

# ссылка на страницу блога с превью статей
url = 'https://evo-lutio.livejournal.com/'
response = requests.get(url)

# варим суп из страницы с превьюшками и берем оттуда ссылки на каждую полную статью
soup_blog_page = BeautifulSoup(response.text, 'html.parser')
links = []
for link in soup_blog_page.find_all('a', class_='subj-link'):
    links.append(link.get('href'))

# варим суп уже отдельно из страницы с полной статьей
for link in links[1:3]:
    new_url = link
    new_response = requests.get(new_url)
    soup_article_page = BeautifulSoup(new_response.text, 'html.parser')
# берем название
    title = soup_article_page.find('h1').text
# берем текст статьи, в тексте хочу сохранить все переносы и ссылки, но убрать теги, актуальные только
# для жж
    article = soup_article_page.find('article', class_='b-singlepost-body entry-content e-content')

# ищем внутри тега с текстом статьи все теги, у которых есть имя и класс
    def has_name_or_class(tag):
        return tag.has_attr('class') or tag.has_attr('name')
# убираем их, чтобы остались только общие теги, характерные для любой html страницы
    for tag in article.find_all(has_name_or_class):
        tag.decompose()
# выводим название, дату и статью, которую можно прочитать с консоли и может быть куда-то потом пихнуть
    date = soup_article_page.find('time').text
    print(f'{title} {date}')
    pprint(article.contents)
