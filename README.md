# Web Scraping Movies Information

## Overview
This project is a Python script (`scraping.py`) and a Jupyter Notebook implementation (`scraping.ipynb`) for web scraping movie information from the Rotten Tomatoes website. The scraper fetches data from the specified webpage, processes it, and provides tools for exporting the data into formats like CSV. It focuses on extracting data such as movie titles, ratings, genres, and release dates, which can be used for analysis or recommendation systems.

## Features
- Extracts information about movies, including titles, ratings, genres, and release dates.
- Outputs scraped data in structured formats such as CSV or pandas DataFrame.
- Uses Python libraries for efficient and scalable web scraping.

## Requirements
- Python 3.7 or higher.
- Libraries: BeautifulSoup, Requests, Pandas.
- Internet access to fetch data from the website.

## How the Script Works
1. **Specify the URL**:
   - The script starts by defining the target URL to scrape data from.
   - Current target: `https://editorial.rottentomatoes.com/guide/best-new-movies/`.

2. **Fetch Webpage Data**:
   - The script uses the `requests` library to send an HTTP GET request to the target URL.

3. **Parse the HTML Content**:
   - BeautifulSoup processes the HTML content to extract movie data.

4. **Structure Data**:
   - Extracted data is organized into a pandas DataFrame for further processing.

5. **Export Data**:
   - The final structured data is saved into a CSV file for easy analysis.

## Website Link
- The project currently scrapes data from: [Rotten Tomatoes - Best New Movies](https://editorial.rottentomatoes.com/guide/best-new-movies/)

## Code Overview
The script is divided into several key sections:
1. **Library Imports**:
   - Imports required libraries for scraping and data handling.
2. **Define URL and Send Request**:
   - Sets the target URL and sends a GET request.
3. **Parse HTML with BeautifulSoup**:
   - Navigates and extracts specific tags containing movie information.
4. **Data Cleaning and Structuring**:
   - Organizes the raw scraped data into a pandas DataFrame.
5. **Data Export**:
   - Saves the processed data into a CSV file.

## Directory Structure
```
web_scraping_project/
│
├── images/                     # Directory to store downloaded images
│   ├── 0.jpg
│   ├── 1.jpg
│   └── ...
│
├── scraping.py        # Python script containing the scraping logic
├── scraping.ipynb     # Jupyter Notebook for interactive exploration 
└── README.md                   # This README file
```

## Input
- The URL of the webpage to scrape. In this implementation, the target URL is:
  ```
  https://editorial.rottentomatoes.com/guide/best-new-movies/
  ```

## Output
- A CSV file containing structured data about movies. Example data includes:
  | Title              | Rating | Genre        | Release Date |
  |--------------------|--------|--------------|--------------|
  | Movie Title 1      | 95%    | Comedy, Drama| 2024-01-01   |
  | Movie Title 2      | 88%    | Action       | 2023-12-15   |

## Example Usage
1. **Scraping Data**:
   - Run the Python script (`scraping.py`) or the Jupyter Notebook (`scraping.ipynb`) to fetch and parse the webpage content.

2. **Processing Data**:
   - The script processes the scraped data into a pandas DataFrame for further analysis.

3. **Saving Data**:
   - Export the data to a CSV file for offline use or integration with other tools.

---
