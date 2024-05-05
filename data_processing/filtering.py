def filter_by_words_in_title(items, condition):
    return [item for item in items if condition(count_words(item['title']))]

def count_words(text):
    return len(text.split())
