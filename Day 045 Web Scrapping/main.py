from bs4 import BeautifulSoup
# import lxml <- required for xml sites
import requests

response = requests.get('https://news.ycombinator.com/')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

# first_news = soup.find(class_='titleline', name='a')
# first_news = soup.select_one('.titleline a')
# first_score = soup.find(name='span', class_='score')

# print(first_news.get_attribute_list('href'))
# print(first_score.text)
# print(int(first_score.text.split()[0]))

# article_text = first_news.text
# article_link = first_news.get('href')
# article_upvote = int(first_score.text.split()[0])

# articles = soup.find_all(name='a', class_='titleline')
# articles = soup.select('span .titleline a')

articles= soup.find_all(name='span', class_='titleline')
article_texts = []
article_links = []
for article_tag in articles:
    news = article_tag.find_next('a')
    article_texts.append(news.getText())
    article_links.append(news.get('href'))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

highest_score = max(article_upvotes)
score_index = article_upvotes.index(highest_score)

print(article_texts[score_index])
print(article_links[score_index])
print(article_upvotes[score_index])



"""
# for encoding use the charset specified in the html
with open('website.html', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, lxml') <- for xml sites
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.string)
print(soup.prettify())
print(soup.a)
print(soup.li)
print(soup.p)

# all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get('href'))

heading = soup.find(id='name')
print(heading)

section_heading = soup.find(class_='heading')
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get('class'))

company_url = soup.select_one(selector='p a')  # an 'a' tag sitting inside a 'p' tag
print(company_url)

name = soup.select_one(selector='#name')  # an id 'name'
print(name)

my_headings = soup.select('.heading') # all 'heading' class items
print(my_headings)
"""

# === END === #
