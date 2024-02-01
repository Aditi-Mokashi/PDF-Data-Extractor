import os
from PyPDF2 import PdfReader

from utils import download_pdf, regex_utils, logger, fetch_information
from io_ops import read_config, write_to_json

path = os.path.dirname(os.path.abspath('__file__'))

urls, page_count = read_config.read_config()


def main():
    """
    Driver function
    """
    try:
        # list to store dictionaries for each URL
        info_list = []
        for url in urls:
            download_pdf.download_file(url, path)

            # last element in the URL is the PDF name
            reader = PdfReader(url.split("/")[-1])
            info_list.append(fetch_information.fetch_information(
                url=url, pages=reader.pages, page_count=page_count))

        write_to_json.write_to_json(dictionary=info_list)

    except Exception as e:
        logger.log_message(
                            message=str(e.args), level=1)


if __name__ == '__main__':
    main()
