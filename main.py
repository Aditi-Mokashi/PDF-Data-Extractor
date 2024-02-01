import os
import timeit
from PyPDF2 import PdfReader

from utils import download_pdf, logger, fetch_information
from io_ops import read_config, write_to_json


path = os.path.dirname(os.path.abspath('__file__'))
urls, page_count = read_config.read_config()

def main():
    start_time = timeit.default_timer()
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

            # read pages and extract information
            reader = PdfReader(pdf_name)
            info_list.append(fetch_information.fetch_information(
                url=url, pages=reader.pages, page_count=page_count))
            
        write_to_json.write_to_json(info_list=info_list)
        elapsed_time = timeit.default_timer() - start_time
        logger.log_message(
            message=f"Completed: Elapsed time: {elapsed_time}", level=0)

    except Exception as e:
        logger.log_message(
                            message=str(e.args), level=1)


if __name__ == '__main__':
    main()
