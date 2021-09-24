# %%
import json
from scraper import scrape_story_links

# %%

LOAD_FROM_DISK = True

if LOAD_FROM_DISK:
    with open("dump.json") as f:
        results = json.load(f)
else:
    results = scrape_story_links()

print(results)
