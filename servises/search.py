import requests


def get_wikw_results(query: str, lang: str = 'ru'):
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)
    print(response.json())

    data = response.json()["query"].get("search")
    return data



print(get_wikw_results("python"))

text = {'batchcomplete': '', 'continue': {'sroffset': 10, 'continue': '-||'},
        'query': {'searchinfo': {'totalhits': 1868}, 'search': [
            {'ns': 0, 'title': 'Python', 'pageid': 2705},
            {'ns': 0, 'title': 'Python (значения)', 'pageid': 768120},
            {'ns': 0, 'title': 'Colt Python', 'pageid': 3684251},
            {'ns': 0, 'title': 'Rafael Python 3', 'pageid': 1548777},
            {'ns': 0, 'title': 'Монти Пайтон', 'pageid': 156203},
            {'ns': 0, 'title': 'Python Software Foundation', 'pageid': 1768334},
            {'ns': 0, 'title': 'ActivePython', 'pageid': 613593},
            {'ns': 0, 'title': 'PythonAnywhere', 'pageid': 6827704},
            {'ns': 0, 'title': 'История языка программирования Python', 'pageid': 4165579},
            {'ns': 0, 'title': 'Дзен Пайтона', 'pageid': 9985573}]}}
