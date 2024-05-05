def filter_by_words_in_title(items, condition):
    return [item for item in items if title_meets_condition(item, condition)]

def sort_items(items, order):
    return sorted(items, key=lambda item: (item[order] is None, item[order]))

def title_meets_condition(item, condition):
    return condition(count_words(item['title']))

def count_words(text):
    return len(text.split())
