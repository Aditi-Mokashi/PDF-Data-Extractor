import re
from utils import logger

def get_cin(text: str) -> list:
    """
    extracts Corporate Identification Number (CIN) from given input

    Args:
        text (str): input to search pattern in

    Returns:
        list (str): list of matches found
    """

    try:
        return re.findall(r'[UL]\d{5}[a-zA-Z]{2}\d{4}[a-zA-Z]{3}\d{6}', text)
    except Exception as e:
        logger.log_message(
                            message='Error while fetching CIN: ' + str(e.args), level=1)


def get_email(text: str) -> list:
    """
    Email from given input

    Args:
        text (str): input to search pattern in

    Returns:
        list (str): list of matches found
    """

    try:
        return re.findall(r'[\w\.-]+@[\w-]+\.[\w-]+', text)
    except Exception as e:
        logger.log_message(
                            message='Error while fetching email: ' + str(e.args), level=1)


def get_phone_number(text: str) -> list:
    """
    extracts Phone numbers from given input

    Args:
        text (str): input to search pattern in

    Returns:
        list (str): list of matches found
    """

    try:
        phone_number_with_std = re.findall(r'\+\d{12}', text)
        landline = re.findall(r'\d{11}', text)
        phone_number = re.findall(r'\d{10}$', text)

        return phone_number_with_std, landline, phone_number
    except Exception as e:
        logger.log_message(
                            message='Error while fetching phone number: ' + str(e.args), level=1)


def get_pan(text: str) -> list:
    """
    extracts Permanent Account Number from given input

    Args:
        text (str): input to search pattern in

    Returns:
        list (str): list of matches found
    """

    try:
        return re.findall(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}', text)
    except Exception as e:
        logger.log_message(
                            message='Error while fetching PAN: ' + str(e.args), level=1)


def get_website(text: str) -> list:
    """
    extracts Website URL from given input

    Args:
        text (str): input to search pattern in

    Returns:
        list (str): list of matches found
    """

    try:
        return re.findall(r'www[.]\w*[.]\w*', text)
    except Exception as e:
        logger.log_message(
                            message='Error while fetching website: ' + str(e.args), level=1)


def get_date(text: str) -> str:
    """
    extracts Dates in specified format (DD/MM/YYYY) from given input

    Args:
        text (str): input to search pattern in

    Returns:
        list (str): list of matches found
    """

    try:
        return re.findall(r'\d{2}[/]\d{2}[/]\d{4}', text)
    except Exception as e:
        logger.log_message(
                            message='Error while fetching date: ' + str(e.args), level=1)