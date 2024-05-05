from parsing import parse_news_data


def test_parse_news_data():

    html = f'''
        <table border="0" cellpadding="0" cellspacing="0">
        {news_item_template(123, 1, "Title one", 123, 5)}
        {news_item_template(432, 2, "Title two", 55, 6)}
        {news_item_template(789, 3, "Title three", 2, 7)}
        </table>
    '''
    parsed_data = parse_news_data(html)
    assert parsed_data == [
        expected_news_data_item(1, "Title one", 123, 5),
        expected_news_data_item(2, "Title two", 55, 6),
        expected_news_data_item(3, "Title three", 2, 7)
    ]

def test_parse_news_data_with_too_many_items():

    news_items_html = '\n'.join([news_item_template(123, 1, "Title one", 123, 5)]*40)
    html = f'''
        <table border="0" cellpadding="0" cellspacing="0">
        {news_items_html}
        </table>
    '''
    parsed_data = parse_news_data(html)
    assert parsed_data == [
        expected_news_data_item(1, "Title one", 123, 5)
    ]*30

def expected_news_data_item(order, title, points, comments_count):
    return {
        'order': order,
        'title': title,
        'points': points,
        'comments_count': comments_count
    }

def news_item_template(news_id, order, title, points, comments_count):
    return f'''
        <tr class='athing' news_id='{news_id}'>
            <td align="right" valign="top" class="title">
                <span class="rank">{order}.</span>
            </td>
            <td valign="top" class="votelinks">
                <center>
                    <a news_id='up_{news_id}'href='vote?news_id={news_id}&amp;how=up&amp;goto=news'>
                        <div class='votearrow' title='upvote'></div>
                    </a>
                </center>
            </td>
            <td class="title">
                <span class="titleline">
                    <a href="https://exmaple.com">
                    {title}
                    </a>
                    <span class="sitebit comhead">
                        (<a href="from?site=bandmatch.app"><span class="sitestr">bandmatch.app</span></a>)
                    </span>
                </span>
            </td>
        </tr>
        <tr>
            <td colspan="2"></td>
            <td class="subtext">
                <span class="subline">
                    <span class="score" news_id="score_{news_id}">{points} points</span>
                    by <a href="user?news_id=pg5" class="hnuser">pg5</a>
                    <span class="age" title="2024-05-03T18:11:25">
                        <a href="item?news_id={news_id}">2 hours ago</a>
                    </span>
                    <span news_id="unv_{news_id}"></span> |
                    <a href="hnews_ide?news_id={news_id}&amp;goto=news">hnews_ide</a> |
                    <a href="item?news_id={news_id}">{comments_count}&nbsp;comments</a>
                </span>
            </td>
        </tr>
        <tr class="spacer" style="height:5px"></tr>
    '''
