import timeit
from PyPDF2 import PdfReader

from utils import download_pdf, logger, fetch_information
from io_helper import read_config, write_to_json


def main():
    """
    Driver function
    """
    try:
        start_time = timeit.default_timer()

        # get data fetched from configuration file
        urls, page_count = read_config.read_config()

        # list to store dictionaries for each URL
        info_list = []
        for url in urls:

            # last element in URL is the PDF name
            pdf_name = url.split("/")[-1]

            # download pdf and get its pages
            download_pdf.download_file(url=url)

            reader = PdfReader(pdf_name)

            info_list.append(fetch_information.fetch_information(
                url=url, pages=reader.pages[0:page_count]))
            
        write_to_json.write_to_json(info_list=info_list)
        elapsed_time = timeit.default_timer() - start_time
        logger.log_message(
            message=f"Elapsed time: {elapsed_time}", level=0)

    except Exception as e:
        logger.log_message(
                            message=str(e.args), level=1)


if __name__ == '__main__':
    main()
