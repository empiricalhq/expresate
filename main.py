import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import re
import openpyxl
import csv


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
            print(
                f"  [Warning] Could not find a plausible data table in dictionary: {file_url}"
            )
            return None

        print(
            f"  [Info] Found table header at row {start_row}. Reading data from that point."
        )

        file_content.seek(0)
        df = pd.read_excel(file_content, engine="openpyxl", skiprows=start_row - 1)

        df = df.dropna(subset=[df.columns[0]])
        if df.empty:
            return None

        columns = dict(zip(df.iloc[:, 0].astype(str), df.iloc[:, 1].astype(str)))
        return columns

    except Exception as e:
        print(f"  [Error] Failed to process Excel dictionary {file_url}: {e}")
        return None


def get_columns_from_csv(file_url):
    """
    Downloads a CSV file, automatically detects the delimiter, reads only the header,
    and returns column names.
    """
    columns = {}
    try:
        response = requests.get(file_url, timeout=20)
        response.raise_for_status()

        sample = response.text[:1024]
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;")
            delimiter = dialect.delimiter
            print(f"  [Info] Sniffer detected delimiter: '{delimiter}'")
        except csv.Error:
            print("  [Warning] CSV Sniffer failed. Falling back to comma delimiter.")
            delimiter = ","

        file_content_str = response.text
        file_content = io.StringIO(file_content_str)

        # Read only the first row to get the header using the detected delimiter
        df = pd.read_csv(file_content, nrows=0, sep=delimiter)

        columns = {col: "N/A" for col in df.columns}

    except UnicodeDecodeError:
        try:
            file_content = io.StringIO(response.content.decode("latin-1"))
            df = pd.read_csv(file_content, nrows=0, sep=delimiter)
            columns = {col: "N/A" for col in df.columns}
        except Exception as e:
            print(
                f"  [Error] Failed to read CSV header with fallback encoding for {file_url}: {e}"
            )

    except Exception as e:
        print(f"  [Error] Failed to read CSV header for {file_url}: {e}")

    return columns


def scrape_dataset_details(page_url):
    """
    Scrapes a single dataset page to find downloadable resources and their columns.
    """
    print(f"\n-> Visiting page: {page_url}")
    try:
        response = requests.get(page_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  [Error] Could not fetch page {page_url}: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    resources_div = soup.find("div", id="data-and-resources")
    if not resources_div:
        print("  [Info] No 'data-and-resources' section found.")
        return []

    resource_list_items = resources_div.find_all("li")

    all_resources = []
    dictionary_url = None

    for item in resource_list_items:
        link_tag = item.find("a", class_="heading")
        download_tag = item.find("a", class_="data-link")
        format_tag = item.find("span", class_="format-label")

        if not all([link_tag, download_tag, format_tag]):
            continue

        title = link_tag.get_text(strip=True)
        download_url = download_tag["href"]
        file_format = format_tag.get("data-original-title", "").lower()

        if download_url.lower().endswith((".xlsx", ".xls")):
            file_format = "xlsx"  # Standardize to xlsx for our logic

        resource_info = {
            "dataset_title": title,
            "dataset_download_link": download_url,
            "dataset_format": file_format,
            "columns": "Not a data file",
        }
        all_resources.append(resource_info)

        if file_format in ["xlsx", ".xlsx", "excel"] and re.search(
            r"diccionario|metadatos", title, re.IGNORECASE
        ):
            dictionary_url = download_url
            print(f"  [Info] Found data dictionary: {title}")

    dataset_columns = None
    if dictionary_url:
        dataset_columns = get_columns_from_dictionary(dictionary_url)

    final_resource_list = []
    for resource in all_resources:
        if resource["dataset_format"] == "csv":
            if dataset_columns:
                column_str = " | ".join(
                    [f"{k}: {v}" for k, v in dataset_columns.items()]
                )
                resource["columns"] = column_str
            else:
                print(
                    f"  [Info] No dictionary found/parsed. Reading header from: {resource['dataset_title']}"
                )
                csv_columns = get_columns_from_csv(resource["dataset_download_link"])
                column_str = " | ".join(
                    [f"{k.strip()}: {v}" for k, v in csv_columns.items()]
                )
                resource["columns"] = (
                    column_str if column_str else "Could not read header"
                )

        final_resource_list.append(resource)

    return final_resource_list


def scrape_hackathon_listings(start_url):
    """
    Main function to scrape all pages of hackathon listings and then
    scrape the details for each entry.
    """
    all_datasets = []
    current_url = start_url

    while current_url:
        # current_page += 1
        print(f"\nScraping listing page: {current_url}")
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching listing URL: {e}")
            break

        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find("div", class_="view-content")
        if not content:
            print("Could not find the main content area on the listing page.")
            break

        articles = content.find_all("article", class_="node-search-result")

        for article in articles:
            title_element = article.find("h2", class_="node-title")
            if title_element and title_element.a:
                hackathon_title = title_element.a.get_text(strip=True)
                hackathon_link = (
                    "https://datosabiertos.gob.pe" + title_element.a["href"]
                )

                datasets_info = scrape_dataset_details(hackathon_link)

                for dataset in datasets_info:
                    dataset["hackathon_title"] = hackathon_title
                    dataset["hackathon_link"] = hackathon_link
                    all_datasets.append(dataset)

        next_page_element = soup.find("li", class_="pager-next")
        if next_page_element and next_page_element.a:
            current_url = "https://datosabiertos.gob.pe" + next_page_element.a["href"]
        else:
            current_url = None

    return all_datasets


if __name__ == "__main__":
    START_URL = "https://datosabiertos.gob.pe/search/field_topic/educaci%C3%B3n-28/field_topic/datat%C3%B3n-2025-2077?sort_by=changed"

    scraped_data = scrape_hackathon_listings(START_URL)

    if scraped_data:
        df = pd.DataFrame(scraped_data)
        df = df[
            [
                "hackathon_title",
                "hackathon_link",
                "dataset_title",
                "dataset_download_link",
                "dataset_format",
                "columns",
            ]
        ]

        df.to_csv("hackathons.csv", index=False, encoding="utf-8-sig")
        print("\nScraping complete. Data saved to hackathons.csv")
    else:
        print("\nNo data was scraped.")
