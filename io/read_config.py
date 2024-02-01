import json
from utils import logger

def read_config():
    try:
        with open("config.json", 'r') as f:
            data = json.load(f)
        return data['url'], data['page_count']
    except Exception as e:
        logger.log_message(
                        message="Could not read JSON file " + str(e.args), level=1)