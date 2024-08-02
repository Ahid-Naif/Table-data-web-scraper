# Web Scraping Project

## Overview

This project is a web scraping tool that logs into a website, navigates through paginated data in a table form, and exports the data to an Excel file. It uses Python libraries to handle HTTP requests, parse HTML content, and manage Excel files. The script is compatible with Python 3.8.0, and has not been tested with other Python versions.

## Features

- **Login**: Handles login with CSRF token and credentials.
- **Pagination**: Automatically navigates through paginated data.
- **Data Extraction**: Extracts data from HTML tables.
- **Export**: Saves the extracted data to an Excel file.

## Requirements

To run this project, you need Python 3.8.0 and the following libraries:

- `requests`
- `beautifulsoup4`
- `pandas`
- `python-dotenv`
- `openpyxl`

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install the Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project with the following content:

   ```plaintext
   LOGIN_EMAIL=your-email@example.com
   LOGIN_PASSWORD=your-password
   LOGIN_URL=Login-page-url
   DATA_URL_TEMPLATE=<data-page-url>?page={}
   ```

## Usage

1. **Run the Script**

   ```bash
   python scrape_data.py
   ```

   This will log in to the website, scrape the data from the paginated tables, and save it to `data.xlsx`.

2. **Check the Output**

   After running the script, you will find the exported data in `data.xlsx`.

## Troubleshooting

- **Login Issues**: Ensure that your credentials and CSRF token handling are correct.
- **Data Not Found**: Verify the structure of the web page and ensure that your scraping logic matches the HTML structure.
- **Installation Issues**: Ensure that all required libraries are installed and that there are no version conflicts.
- **Python Version**: This script has been tested and is confirmed to work with Python 3.8.0. Other versions may require adjustments.

## Acknowledgments

- **Libraries**: This project uses [requests](https://docs.python-requests.org/), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), [pandas](https://pandas.pydata.org/), and [openpyxl](https://openpyxl.readthedocs.io/en/stable/).