# Importing libraries
import requests
import time
from bs4 import BeautifulSoup

def scrape(subreddit):
    result = []
    url = "https://old.reddit.com/r/{}/".format(subreddit)

    # Headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Returns a requests.models.Response object
    page = requests.get(url, headers=headers)

    # Preparing Soup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Finding posts that are of the given subreddit
    attrs = {'class': 'thing',
             'data-domain': 'self.{}'.format(subreddit)}
    counter = 1
    posts = 50

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
                likes = "0"

            post_line = [counter, title, author, int(likes), comments]
            result.append(post_line)

            counter += 1

        next_button = soup.find("span", class_="next-button")
        next_page_link = next_button.find("a").attrs['href']
        page = requests.get(next_page_link, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')


    result = sorted(result, key = lambda x: x[3])

    return result[-1]



    