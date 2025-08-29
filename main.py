import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import re
import openpyxl
import csv
import json

def get_columns_from_dictionary(file_url):
    """
    Downloads an XLSX file, intelligently finds the start of the main data table,
    and extracts variable names and descriptions from the first two columns.
    """
    try:
        response = requests.get(file_url, timeout=20)
        response.raise_for_status()
        file_content = io.BytesIO(response.content)
        workbook = openpyxl.load_workbook(file_content)
        sheet = workbook.active
        start_row = 0
        for row_num, row in enumerate(sheet.iter_rows(), 1):
            if row[0].value and row[1].value:
                start_row = row_num
                break
        if start_row == 0:
            return None
        file_content.seek(0)
        df = pd.read_excel(file_content, engine='openpyxl', skiprows=start_row - 1)
        df = df.dropna(subset=[df.columns[0]])
        if df.empty:
            return None
        return dict(zip(df.iloc[:, 0].astype(str), df.iloc[:, 1].astype(str)))
    except Exception as e:
        print(f"  [Error] Failed to process Excel dictionary {file_url}: {e}")
        return None

def get_columns_from_csv(file_url):
    """
    Downloads a CSV file, automatically detects the delimiter, reads only the header,
    and returns column names.
    """
    try:
        response = requests.get(file_url, timeout=20)
        response.raise_for_status()
        sample = response.text[:2048]
        delimiter = ','
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=',;')
            delimiter = dialect.delimiter
        except csv.Error:
            pass
        df = pd.read_csv(io.StringIO(response.text), nrows=0, sep=delimiter)
        return {col.strip(): "N/A" for col in df.columns}
    except Exception as e:
        print(f"  [Error] Failed to read CSV header for {file_url}: {e}")
        return {}

def scrape_metadata_table(soup):
    """Scrapes the 'Dataset Info' table into a dictionary."""
    metadata = {}
    table = soup.find('section', class_='group_additional')
    if not table:
        return metadata

    for row in table.find_all('tr'):
        header = row.find('th')
        value = row.find('td')
        if header and value:
            metadata[header.get_text(strip=True)] = value.get_text(strip=True)

    return metadata


def scrape_page_details(page_url, hackathon_title):
    """
    Scrapes a single detail page and returns ONE dictionary for the whole page,
    with resources nested inside.
    """
    print(f"\n-> Processing Page: {page_url}")
    try:
        response = requests.get(page_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  [Error] Could not fetch page {page_url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape main page information
    soup.find('h1', class_='page-header').get_text(strip=True) if soup.find('h1', class_='page-header') else hackathon_title
    description_div = soup.find('div', class_='field-name-body')
    description_div.get_text(strip=True) if description_div else "No description available."
    scrape_metadata_table(soup)

    # Scrape all downloadable resources on the page
    resources_div = soup.find('div', id='data-and-resources')
    if not resources_div:
        return None

    resource_list_items = resources_div.find_all('li')

    all_resources = []
    dictionary_url = None

    # First pass: identify resources and find the dictionary
    for item in resource_list_items:
        link_tag = item.find('a', class_='heading')
        download_tag = item.find('a', class_='data-link')
        format_tag = item.find('span', class_='format-label')

        if not all([link_tag, download_tag, format_tag]):
            continue

        title = link_tag.get_text(strip=True)
        download_url = download_tag['href']
        file_format = format_tag.get('data-original-title', '').lower()

        if download_url.lower().endswith(('.xlsx', '.xls')):
            file_format = 'xlsx'

        resource_info = {
            # 'title': title,
            'download_link': download_url,
            'format': file_format
        }
        all_resources.append(resource_info)

        if file_format in ['xlsx', '.xlsx', 'excel'] and re.search(r'diccionario|metadatos', title, re.IGNORECASE):
            dictionary_url = download_url
            print(f"  [Info] Found data dictionary: {title}")

    # Second pass: get column info for each resource
    dataset_columns_from_dict = None
    if dictionary_url:
        dataset_columns_from_dict = get_columns_from_dictionary(dictionary_url)

    for resource in all_resources:
        if resource['format'] == 'csv':
            if dataset_columns_from_dict:
                resource['columns'] = dataset_columns_from_dict
            else:
                # print(f"  [Info] No dictionary found. Reading header from CSV: {resource['title']}")
                resource['columns'] = get_columns_from_csv(resource['download_link'])
        else:
            resource['columns'] = None


    page_data = {
        'source_title': hackathon_title,
        'page_url': page_url,
        # 'page_title': page_title,
        # 'description': description,
        # 'metadata': metadata,
        'resources': all_resources
    }

    return page_data

def scrape_hackathon_listings(start_url):
    """
    Main function to scrape all pages of hackathon listings and then
    scrape the details for each entry.
    """
    all_pages_data = []
    current_url = start_url

    while current_url:
        print(f"\nScraping listing page: {current_url}")
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching listing URL: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('div', class_='view-content')
        if not content:
            break

        articles = content.find_all('article', class_='node-search-result')
        for article in articles:
            title_element = article.find('h2', class_='node-title')
            if title_element and title_element.a:
                hackathon_title = title_element.a.get_text(strip=True)
                hackathon_link = "https://datosabiertos.gob.pe" + title_element.a['href']

                page_details = scrape_page_details(hackathon_link, hackathon_title)
                if page_details:
                    all_pages_data.append(page_details)

        next_page_element = soup.find('li', class_='pager-next')
        current_url = "https://datosabiertos.gob.pe" + next_page_element.a['href'] if next_page_element and next_page_element.a else None

    return all_pages_data


if __name__ == '__main__':
    START_URL = 'https://datosabiertos.gob.pe/search/field_topic/educaci%C3%B3n-28/field_topic/datat%C3%B3n-2025-2077?sort_by=changed'

    scraped_data = scrape_hackathon_listings(START_URL)

    if scraped_data:
        output_filename = 'hackathons.json'
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(scraped_data, f, ensure_ascii=False, indent=4)
        print(f"\n\nScraping complete. All data saved to {output_filename}")
    else:
        print("\nNo data was scraped.")
