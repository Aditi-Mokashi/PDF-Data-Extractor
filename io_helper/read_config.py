import json
from utils import logger
import aiofiles

async def read_config():
    """
    reads configuration file containing input parameters
    (URL, Number of pages)

    Returns:
        URL (str): Link to the PDF
        page_count (int): Number of pages to extract information from
    """

    try:
        async with aiofiles.open("config.json", 'r') as f:
            contents = await f.read()
        data = json.loads(contents)
        return data['urls'], data['page_count']
    except Exception as e:
        logger.log_message(
                        message="Could not read JSON file " + str(e.args), level=1)