# AWS Durham News Sentiment Analysis
Leveraging AWS cloud technologies for news sentiment analysis

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


## Architecture
|![AWS-DNSA drawio-2](https://user-images.githubusercontent.com/58488209/134609857-737f763a-f58e-4177-9ab1-89370dc5b020.png)|
|---|
| Architecture of the application |
