from data_processing.parsing import parse_news_data
from data_processing.web_crawling import get_source_code


def main():
    html = get_source_code('https://news.ycombinator.com/')
    parsed_data = parse_news_data(html)
    return parsed_data

if __name__ == "__main__":
    data = main()
    print(data)
