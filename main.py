from data_processing.filtering import filter_by_words_in_title, sort_items
from data_processing.parsing import parse_news_data
from data_processing.web_crawling import get_source_code


def main():
    html = get_source_code('https://news.ycombinator.com/')
    parsed_data = parse_news_data(html)
    long_titles_items = filter_by_words_in_title(parsed_data, lambda c: c > 5)
    short_titles_items = filter_by_words_in_title(parsed_data, lambda c: c <= 5)
    long_titles_items_by_comments = sort_items(long_titles_items, 'comments_count')
    short_titles_items_by_points = sort_items(short_titles_items, 'points')
    return parsed_data, long_titles_items_by_comments, short_titles_items_by_points

if __name__ == "__main__":
    data = main()
    print(data)
