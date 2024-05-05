from parsing import parse_news_data
from web_crawling import get_source_code


def main():
    html = get_source_code('https://news.ycombinator.com/')
    parsed_data = parse_news_data(html)
    return parsed_data

if __name__ == "__main__":
    data = main()
    print(data)
