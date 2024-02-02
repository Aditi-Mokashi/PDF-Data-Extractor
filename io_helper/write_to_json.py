import json
from utils import logger


def write_to_json(info_list: list):
    """
    writes input list to a file in JSON format

    Args:
        info_list (list): list of dictionaries containing extracted information
    """
    try:
        with open("output.json",'w') as f:
            f.write(json.dump(info_list, f, indent=4))
        logger.log_message(
                        message='Output saved to JSON file', level=0)
    except Exception as e:
        logger.log_message(
                        message="Could not write to JSON file " + str(e.args), level=1)