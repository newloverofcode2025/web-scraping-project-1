# web-scraping-project-1
 # Web Scraping Project 1

## Overview
This project demonstrates a basic web scraping task using Python, requests, and BeautifulSoup. It scrapes links from a given website and saves them to a CSV file.

## Project Structure
web-scraping-project-1/
├── src/
│   └── main.py
├── data/
│   └── output.csv
└── README.md

## Dependencies
- Python
- requests
- beautifulsoup4
- pandas

## Setup
1. Clone the repository.
2. Install the required libraries using `pip install requests beautifulsoup4 pandas`.
3. Run the script using `python src/main.py`.

## Usage
- The script scrapes all the `<a>` tags from the specified URL and saves the text and href attributes to `data/output.csv`.

## Notes
- Replace the URL in `main.py` with the website you want to scrape.
- Ensure you have permission to scrape the website and comply with its `robots.txt` file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
