import json

def read_config():
    """
    reads configuration file containing input parameters
    (URL, Number of pages)
    """

    try:
        from utils import logger
        with open("config.json", 'r') as f:
            data = json.load(f)
        return data['url'], data['page_count']
    except Exception as e:
        logger.log_message(
                        message="Could not read JSON file " + str(e.args), level=1)