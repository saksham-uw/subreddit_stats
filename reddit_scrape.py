# Importing libraries
import requests
import time
from bs4 import BeautifulSoup

# Website to be scraped
subreddit = "datascience"  # Global
result = []  # Global
url = "https://old.reddit.com/r/{}/".format(subreddit)

# Headers to mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}  # Global

# Returns a requests.models.Response object
page = requests.get(url, headers=headers)

# Preparing Soup
soup = BeautifulSoup(page.text, 'html.parser')

# Finding posts that are of the given subreddit
attrs = {'class': 'thing',
         'data-domain': 'self.{}'.format(subreddit)}  # Global
counter = 1  # Global
posts = 100  # Global

while (counter <= posts):
    for post in soup.find_all('div', attrs=attrs):
        title = post.find('p', class_="title").text

        try:
            author = post.find('a', class_='author').text
        except:
            author = "[deleted]"

        comments = post.find('a', class_='comments').text.split()[0]
        if comments == "comment":
            comments = 0

        likes = post.find("div", attrs={"class": "score likes"}).text
        if likes == "•":
            likes = "None"

        post_line = [counter, title, author, likes, comments]
        result.append(post_line)

        counter += 1

    next_button = soup.find("span", class_="next-button")
    next_page_link = next_button.find("a").attrs['href']
    time.sleep(1)
    page = requests.get(next_page_link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

print(result)
