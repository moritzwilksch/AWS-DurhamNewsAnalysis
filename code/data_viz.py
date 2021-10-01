# %%
import pandas as pd
import boto3
import json
import seaborn as sns


# %%

dynamodb = boto3.resource(
    'dynamodb',
    region_name="us-east-2",
)

table = dynamodb.Table('durhamnews')

# %%
content = table.scan()


# %%
df = pd.json_normalize(content['Items'])
df = pd.merge(
    df,
    pd.json_normalize(json.loads(x) for x in df['sentiment']),
    left_index=True,
    right_index=True
)

#%%
sns.countplot(data=df, x='Sentiment')
sns.despine()

#%%
print(df.query("Sentiment == 'POSITIVE'")['headline'].values)
