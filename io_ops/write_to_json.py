import json
from utils import logger

def write_to_json(info_list: list):
    try:
        for object in info_list:
            json_object = json.dump(object, indent=4)
            with open("output.json",'w') as f:
                f.write(json_object)
            logger.log_message(
                            message='Output saved to JSON file', level=0)
    except Exception as e:
        logger.log_message(
                        message="Could not write to JSON file " + str(e.args), level=1)