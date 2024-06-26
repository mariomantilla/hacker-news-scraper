import re
from bs4 import BeautifulSoup


def parse_news_data(html):
    parsed_html = BeautifulSoup(html, 'html.parser')
    news_items = parsed_html.find_all("tr", class_="athing", limit=30)
    parsed_data = [format_news_item_data(item) for item in news_items]
    return parsed_data

def format_news_item_data(item):
    return {
        'order': find_order(item),
        'title': find_title(item),
        'points': find_points(item),
        'comments_count': find_comments(item)
    }

def find_order(item):
    order_tag = item.find("span", class_="rank")
    return extract_int(order_tag.string)

def find_title(item):
    title_tag = item.find("span", class_="titleline")
    return title_tag.a.string.strip()

def find_points(item):
    ''' Returns the number of points or None if it is a job offer '''
    points_tag = item.find_next_sibling('tr').find("span", class_="score")
    return extract_int(points_tag.string) if points_tag else None

def find_comments(item):
    ''' Returns 0 if there are no comments or None if it is a job offer '''
    comments_tag = item.find_next_sibling('tr').find("a", string=re.compile(r"comments"))
    if not comments_tag:
        discuss_tag = item.find_next_sibling('tr').find("a", string="discuss")
        return 0 if discuss_tag else None
    return extract_int(comments_tag.string)

def extract_int(string):
    return int(re.compile(r"(\d+)").match(string).group(1))
