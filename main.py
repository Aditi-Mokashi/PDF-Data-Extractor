import os
from PyPDF2 import PdfReader

from utils import download_pdf, logger, fetch_information
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
            # last element in URL is the PDF name
            pdf_name = url.split("/")[-1]

            # if file already exists, remove it and download again
            if os.path.exists(path=os.path.join(path, pdf_name)):
                os.remove(os.path.join(path,pdf_name))
            download_pdf.download_file(url, path)

            # last element in the URL is the PDF name
            reader = PdfReader(pdf_name)
            info_list.append(fetch_information.fetch_information(
                url=url, pages=reader.pages, page_count=page_count))
            
        write_to_json.write_to_json(info_list=info_list)

    except Exception as e:
        logger.log_message(
                            message=str(e.args), level=1)


if __name__ == '__main__':
    main()
