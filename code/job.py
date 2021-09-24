# %%
import boto3
import json
import os
from scraper import scrape_story_links

# %%

LOAD_FROM_DISK = True

if LOAD_FROM_DISK:
    with open("dump.json") as f:
        results = json.load(f)
else:
    results = scrape_story_links()

print(results)

# %%

dynamodb = boto3.resource(
    'dynamodb',
    region_name="us-east-2",

)

table = dynamodb.Table('durhamnews')

#%%
for item in results:
    table.put_item(Item=item)
    break
    # print(item)

#%%
table.item_count