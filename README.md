# PDF Data Extractor

This Python script is designed to download a file from a URL and to extract information from PDF file using regex. The output/fetched information is saved in JSON format.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Prerequisites

- Python 3.x
- Required Python libraries (install via `pip install -r requirements.txt`):
  - `PyPDF2`
  - `selenium`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NotShrirang/News-Web-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PDF-Data-Extractor
   ```
3. Setup virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate virtual environment:
   ```bash
   source venv/Scripts/activate
   ```
   
6. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Edit the `config.json` file to configure the URL and Number of pages to extract information from.

2. Run the main script:

   ```bash
   python main.py
   ```

3. The extracted information will be stored in `output.json` file in the project directory.

## Configuration

- **config.json**: This file contains the input configuration for the script i.e. URL of the PDF file and number of pages to extract information from.

## Author
- Aditi Mokashi
