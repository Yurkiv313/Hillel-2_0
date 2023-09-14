from urllib.parse import urlparse, parse_qs


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_parameters = parse_qs(parsed_url.query)
    query_parameters = {key: value[0] for key, value in query_parameters.items()}
    return query_parameters


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/Dima') == {}
    assert parse('http://example.com/?name=Ivan%20Ivanov&age=30') == {'name': 'Ivan Ivanov', 'age': '30'}
    assert parse('https://example.com/?name1=Ivan1&name2=Artem2&name1=Andrii3') == {'name1': 'Ivan1',
                                                                                    'name2': 'Artem2'}
    assert parse('https://example.com/?longtext=This%20is%20a%20very%20long%20text%20with%20spaces') == {
        'longtext': 'This is a very long text with spaces'}
    assert parse('https://example.com/?user-name=johndoe&product-id=12345') == {'user-name': 'johndoe',
                                                                                'product-id': '12345'}
