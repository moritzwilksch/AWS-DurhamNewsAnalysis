# %%
import boto3
import json
from scraper import scrape_story_links

# %%

LOAD_FROM_DISK = False

if LOAD_FROM_DISK:
    with open("dump.json") as f:
        results = json.load(f)
else:
    results = scrape_story_links()

print(results)

# %%
comprehend = boto3.client(
    'comprehend',
    region_name="us-east-2"
)

# %%

for story in results:
    print(f"[INFO] Fetching sentiment for {story['link']}...", end=" ")
    try:
        sentiment = comprehend.detect_sentiment(Text=story['text'], LanguageCode='en')
        print("[DONE]")
    except:
        sentiment = {'Sentiment': 'Error calling comprehend', 'Text': story['text']}
        print("[ERROR]")
    
    story['sentiment'] = json.dumps(sentiment)
    
    


# %%

dynamodb = boto3.resource(
    'dynamodb',
    region_name="us-east-2",
)

table = dynamodb.Table('durhamnews')

# %%
for item in results:
    table.put_item(Item=item)
    # print(item)

# %%
table.item_count
