# Hacker News Scraper

## Overview
This project is a web crawler developed in Python that extracts information from the [Hacker News webpage](https://news.ycombinator.com/) using scraping techniques. It retrieves the titles, order numbers, number of comments, and points of the entries from the provided URL. Additionally, it implements some filtering operations of the extracted entries based on specific criteria.

## Features
- Fetches webpage content and extracts relevant information (titles, order numbers, number of comments, and points).
- Handles up to the first 30 entries in the web page
- Offers two filtering options:
    - Entries with more than 5 words in the title, ordered by number of comments (fewer comments first)
    - Entries with 5 or less words in the title, ordered by number of points (fewer points first)
- Outputs the data in json format via stdout with the following properties:
    - `all_entries`: A list of all extracted entries.
    - `more_than_five_words_in_title_by_comments`: Entries with more than five words in the title, ordered by number of comments.
    - `less_than_five_words_in_title_by_points`: Entries with less than or equal to five words in the title, ordered by points.
- Each entry is displayed as an object with the following properties:
    - `order` (int): A number representing the rank in the Hacker News list (as displayed in the web, could be different from the actual order in the list).
    - `title` (string): The title of the entry.
    - `points` (int): A number showing the number of points given to that entry. Takes the value `null` if the entry is job offer.
    - `comments_count` (int): A number showing the count of comments in that entry. Takes the value `null` if the entry is job offer.

## JSON Schema example
The JSON output returned by the script follows this schema:

```json
{
  "all_entries": [
    {
      "order": "1",
      "title": "Sample Title",
      "points": 100,
      "comments_count": 50
    },
    {
      "order": "2",
      "title": "Another Title",
      "points": 80,
      "comments_count": 30
    },
    ...
  ],
  "more_than_five_words_in_title_by_comments": [
    {
      "order": "3",
      "title": "Title with more than five words",
      "points": 120,
      "comments_count": 70
    },
    ...
  ],
  "less_than_five_words_in_title_by_points": [
    {
      "order": "4",
      "title": "Short Title",
      "points": 150,
      "comments_count": 40
    },
    ...
  ]
}
```

## Dependencies
- Python 3.10 (it should work in different versions but has only been tested in that one)
- requests library (for fetching webpage content)
- beautifulsoup4 library (for HTML parsing and data extraction)
- pytest library (for writing and running tests)

The specific versions and other indirect dependencies can be checked in the `requirements.txt` file.

## Installation
1. Clone the repository:
```bash
git clone git@github.com:mariomantilla/hacker-news-scraper.git
```
2. Navigate to the project directory:
```bash
cd hacker-news-scraper
```
3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
4. Activate the virtual environment (if you created it):
```bash
source venv/bin/activate
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the main script to extract entries from the Hacker News webpage:

    ```bash
    python main.py
    ```
    This will fetch entries from the https://news.ycombinator.com/ and display them in the terminal. Alternatively, you can create a json file with the data using:
    ```bash
    python main.py >> data.json
    ```

## Testing
1. Run the test suite to ensure correct behaviour:
```bash
pytest -v
```
This command will run all test cases in verbose mode, providing detailed output.

## Contributing
Contributions are welcome! If you encounter any bugs or have suggestions for improvements, please open an issue or submit a pull request.