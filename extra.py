import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials and URLs from environment variables
email = os.getenv('LOGIN_EMAIL')
password = os.getenv('LOGIN_PASSWORD')
login_url = os.getenv('LOGIN_URL')
profile_url = os.getenv('PROFILE_URL')
data_url_template = os.getenv('DATA_URL_TEMPLATE')

# Start a session
session = requests.Session()

# GET the login page to retrieve the CSRF token
login_page_response = session.get(login_url)
login_page_soup = BeautifulSoup(login_page_response.text, 'html.parser')

# Extract the CSRF token from the meta tag
csrf_token = login_page_soup.find('meta', {'name': 'csrf-token'})['content']

# Credentials and CSRF token
payload = {
    'authenticity_token': csrf_token,
    'user[email]': email,
    'user[password]': password
}

# POST the login form with the CSRF token
login_response = session.post(login_url, data=payload)

# Check if login was successful
if login_response.status_code == 200:
    print("Login successful")

    # GET the profile page to select the profile
    profile_response = session.get(profile_url)
    profile_response.raise_for_status()  # Check if the GET request was successful
    print("Profile page loaded")

    all_rows = []
    page_number = 1
    while True:
        # GET the data page with pagination
        data_url = data_url_template.format(page_number)
        data_response = session.get(data_url)
        data_soup = BeautifulSoup(data_response.text, 'html.parser')

        # Find the table in the page
        table = data_soup.find('table')
        
        # Break the loop if no table is found (indicating no more data)
        if not table:
            break

        # Extract table headers on the first page
        if page_number == 1:
            headers = [th.text.strip() for th in table.find_all('th')]

        # Extract table rows
        rows = []
        for tr in table.find_all('tr')[1:]:  # Skip header row
            cells = [td.text.strip() for td in tr.find_all('td')]
            if len(cells) > 0:
                rows.append(cells)

        if not rows:
            break

        all_rows.extend(rows)
        page_number += 1

    # Create DataFrame
    df = pd.DataFrame(all_rows, columns=headers)

    # Save to Excel
    df.to_excel('data.xlsx', index=False)
    print("Data exported to data.xlsx")
else:
    print("Login failed")
