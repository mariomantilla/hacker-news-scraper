from data_processing.filtering import filter_by_words_in_title


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
