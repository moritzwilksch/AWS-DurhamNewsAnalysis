# %%
import requests
from bs4 import BeautifulSoup
import time
import json


# %%
headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# %%


def _fetch_headlines_with_links(url: str = None) -> list[dict[str, str]]:
    if url is None:
        url = "https://abc11.com/durham/"

    print(f"[INFO] Initialized with {url =}")

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        print(f"[ERROR] Failed fetching {url} and parsing HTML.")

    anchor_links = soup.find_all('a', {'class': 'AnchorLink'})

    result_list = []
    for al in anchor_links:
        contained_headline = al.find('div', 'headline')

        if contained_headline is not None:
            result_list.append(
                {
                    'headline': contained_headline.text,
                    'link': al.get('href')
                }
            )

    return result_list





# %%
def scrape_story_links(headlines_with_links: list[dict[str, str]] = None, sleep: float = 0.5):
    if headlines_with_links is None:
        headlines_with_links = _fetch_headlines_with_links()
    
    result_list = []
    for story in headlines_with_links:
        current_story = {
            'headline': story['headline'],
            'link': story['link'],
        }

        print(f"[INFO] Fetching {current_story['link']}...")

        try:
            response = requests.get(current_story['link'], headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
        except:
            print(f"[ERROR] Fetching story {current_story['link']}")

        story = soup.find('div', 'body-text')

        if story is not None:
            current_story['text'] = story.text
            result_list.append(current_story)
            print(f"--> Got it!")
        else:
            print(f"--> [WARN] Did not find a story")

        time.sleep(sleep)

    with open("dump.json", "w") as f:
        json.dump(result_list, f)
        
    return result_list


if __name__ == "__main__":
    results = scrape_story_links()


