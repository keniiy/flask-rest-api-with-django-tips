import ssl
import os
from dotenv import load_dotenv
load_dotenv()

# TWITTER API KEYS - Get these keys from your twitter app
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

databasename = "tipdatabase.db"


LOCAL_CSV = 'daily-python-tip.csv'  # for testing
REMOTE_CSV = 'https://t.co/oARrOmrin7'
FIELDS = 'time code name email admin1 admin2 published'.split()
CONTEXT = ssl._create_unverified_context()
TEST = False


