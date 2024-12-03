import logging, os

from dotenv import load_dotenv
load_dotenv()

access_key = os.getenv('ACCESS_KEY')
base_url = os.getenv('BASE_URL')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not access_key:
    logger.warning("\nAccess key is not set in the environment variables.\n")
if not base_url:
    logger.warning("\nBase url is not set in the environment variables.\n")