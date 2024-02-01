import os
from PyPDF2 import PdfReader
import json

from utils import download_pdf, fetch_information, logger

path = os.path.dirname(os.path.abspath('__file__'))

with open("config.json", 'r') as f:
    data = json.load(f)
url = data['url']
page_count = data['page_count']


def main():
    try:
        dictionary = {}
        download_pdf.download_file(url, path)

        reader = PdfReader(url.split("/")[-1])

        count = 1
        for page in reader.pages[0:page_count]:
            dictionary['Page ' + str(count)] = {}
            text = " ".join(page.extract_text().split('\n'))

            cin = fetch_information.get_cin(text)
            if len(cin) != 0:
                dictionary['Page ' + str(count)]['CIN'] = cin
            
            email = fetch_information.get_email(text)
            if len(email) != 0:
                dictionary['Page ' + str(count)]['Email'] = email
            
            pan = fetch_information.get_pan(text)
            if len(pan) != 0:
                dictionary['Page ' + str(count)]['PAN'] = pan
            
            date = fetch_information.get_date(text)
            if len(date) != 0:
                dictionary['Page ' + str(count)]['Date'] = date
            
            website = fetch_information.get_website(text)
            if len(website) != 0:
                dictionary['Page ' + str(count)]['Website'] = website

            phone_number_std, landline, phone_number = fetch_information.get_phone(text)
            if len(phone_number_std) != 0:
                dictionary['Page ' + str(count)]['Phone number STD'] = phone_number_std
            if len(landline) != 0:
                dictionary['Page ' + str(count)]['Landline'] = landline
            if len(phone_number) != 0:
                dictionary['Page ' + str(count)]['Phone number'] = phone_number
            
            count += 1
        
        json_object = json.dumps(dictionary, indent=4)
        with open("output.json",'w') as f:
            f.write(json_object)
        logger.log_message(
                            message='Output saved to JSON file', level=0)
    except Exception as e:
        logger.log_message(
                            message=str(e.args), level=1)


if __name__ == '__main__':
    main()
