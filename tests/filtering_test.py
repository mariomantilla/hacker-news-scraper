from data_processing.filtering import filter_by_words_in_title, sort_items


def test_filter_by_words():

    items = [
        {'title': "1"},
        {'title': "2 words"},
        {'title': "this has 3"},
        {'title': "this has four 4"},
    ]
    assert filter_by_words_in_title(items, lambda c: c > 5) == []
    assert filter_by_words_in_title(items, lambda c: c >= 1) == items
    assert filter_by_words_in_title(items, lambda c: c >= 3) == items[2:]
    assert filter_by_words_in_title(items, lambda c: c <= 3) == items[:3]

def test_order_list_with_none():

    items = [
        {'points': None},
        {'points': 5},
        {'points': 4},
        {'points': 0},
        {'points': None},
    ]
    assert sort_items(items, 'points') == [
        {'points': 0},
        {'points': 4},
        {'points': 5},
        {'points': None},
        {'points': None},
    ]
