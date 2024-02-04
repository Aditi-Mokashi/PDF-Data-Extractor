from utils import logger, regex_utils


def fetch_information(url:str, pages: list) -> dict:
    """
    extracts information from each page
    (CIN, PAN, Email, Website, Contact, Date)

    Args:
        url (str): Link of the PDF
        pages (list): pages in a PDF as a list

    Returns:
        dict: extracted information as key value pairs
    """
    
    try:
        # extract information for each page in PDF
        count = 1
        info_dict = {url: {}}
        for page in pages:
            info_dict[url]['Page ' + str(count)] = {}
            # replace newlines with spaces
            text = " ".join(page.extract_text().split('\n'))

            # get Corporate Identification Number (CIN) and its count,
            # Email, Permanent Identification Number (PAN), Date,
            # Website, Contact Number and save it in a ditionary in format:
            # url: {Page 1: {CIN: cin, Email: email}, {Page2: ...}}
            cin = regex_utils.get_cin(text)
            info_dict[url]['Page ' + str(count)]['CIN_count'] = len(cin)
            info_dict[url]['Page ' + str(count)]['CIN'] = cin
            
            email = regex_utils.get_email(text)
            info_dict[url]['Page ' + str(count)]['Email'] = email
            
            pan = regex_utils.get_pan(text)
            info_dict[url]['Page ' + str(count)]['PAN'] = pan
            
            date = regex_utils.get_date(text)
            info_dict[url]['Page ' + str(count)]['Date'] = date
            
            website = regex_utils.get_website(text)
            info_dict[url]['Page ' + str(count)]['Website'] = website

            phone_number_with_std, landline, phone_number = regex_utils.get_phone_number(text)
            # for each fetched number store STD code and number seperately
            phone_number_list = []
            for number in phone_number_with_std:
                phone_number_list.append({
                    "STD Code": number[:3],
                    "Number": number[3:]
                })
            info_dict[url]['Page ' + str(count)]['Phone numbers with STD'] = phone_number_list
            
            # for each fetched number store STD code and number seperately
            landline_list = []
            for number in landline:
                landline_list.append({
                    "STD Code": number[:3],
                    "Number": number[3:]
                })
            info_dict[url]['Page ' + str(count)]['Landline'] = landline_list
            info_dict[url]['Page ' + str(count)]['Phone numbers'] = phone_number
            
            count += 1
        
        return info_dict
    except Exception as e:
        logger.log_message(
            f"Error while reading PDF: {str(e.args)}", level=1)