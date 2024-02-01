from utils import logger, regex_utils
from io_ops import write_to_json


def fetch_information(url:str, pages: list, page_count: int):
    try:
        # extract information for each page in PDF
        count = 1
        info_dict = {url: {}}
        for page in pages[0:page_count]:
            info_dict[url]['Page ' + str(count)] = {}
            text = " ".join(page.extract_text().split('\n'))

            cin = regex_utils.get_cin(text)
            if len(cin) != 0:
                info_dict[url]['Page ' + str(count)]['CIN_count'] = len(cin)
                info_dict[url]['Page ' + str(count)]['CIN'] = cin
            
            email = regex_utils.get_email(text)
            if len(email) != 0:
                info_dict[url]['Page ' + str(count)]['Email'] = email
            
            pan = regex_utils.get_pan(text)
            if len(pan) != 0:
                info_dict[url]['Page ' + str(count)]['PAN'] = pan
            
            date = regex_utils.get_date(text)
            if len(date) != 0:
                info_dict[url]['Page ' + str(count)]['Date'] = date
            
            website = regex_utils.get_website(text)
            if len(website) != 0:
                info_dict[url]['Page ' + str(count)]['Website'] = website

            phone_number_std, landline, phone_number = regex_utils.get_phone_number(text)
            if len(phone_number_std) != 0:
                info_dict[url]['Page ' + str(count)]['Phone number STD'] = phone_number_std
            if len(landline) != 0:
                info_dict[url]['Page ' + str(count)]['Landline'] = landline
            if len(phone_number) != 0:
                info_dict[url]['Page ' + str(count)]['Phone number'] = phone_number
            
            count += 1
        
        return info_dict
    except Exception as e:
        logger.log_message(
                        message=str(e.args), level=1)