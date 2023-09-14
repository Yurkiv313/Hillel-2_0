def parse_cookie(query: str) -> dict:
    cookies = {}
    parts = query.split(';')
    for part in parts:
        key_value = part.strip().split('=', 1)
        if len(key_value) == 2:
            key, value = key_value
            cookies[key] = value
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima; age=28; city=New York') == {'name': 'Dima', 'age': '28', 'city': 'New York'}
    assert parse_cookie('name=Діма;city=Київ') == {'name': 'Діма', 'city': 'Київ'}
    assert parse_cookie('name=Dima; name=Ivan') == {'name': 'Ivan'}
    assert parse_cookie('  name=Dima; age=28  ') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('user-name=Dima-123; product-id=456;') == {'user-name': 'Dima-123', 'product-id': '456'}
    assert parse_cookie('items=one,two;quantity=3,4;') == {'items': 'one,two', 'quantity': '3,4'}
