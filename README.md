# AWS Durham News Sentiment Analysis
Leveraging AWS cloud technologies for news sentiment analysis

## Architecture
|![AWS-DNSA drawio-3](https://user-images.githubusercontent.com/58488209/134623331-322f66d5-89a3-415d-8e2f-a8c37e5c8af0.png)|
|---|
| Architecture of the application |

## Project Setup
1) Create and activate a virtual environment
```bash
python -m venv .env
source .env/bin/activate
```

2) Install required libraries
```bash
make install
# OR:
# pip install -r requirements.txt
```

3) AWS Authentication
To enable boto3 to access the DynamoDB, add the following lines to your.env/bin/activate script
```bash
export AWS_ACCESS_KEY_ID=AKIAXXXXXXXXXXXX
export AWS_SECRET_ACCESS_KEY=eo8CdXXXXXXXXXXXXXXXXXXXXXXXX
```
replacing them with your IAM account tokens.
