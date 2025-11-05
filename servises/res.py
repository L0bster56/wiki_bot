import wikipedia


def get_wiki_kb(pageid:int, leng:str):
    wikipedia.set_lang(leng)
    page = wikipedia.page(pageid=pageid)
    text = f"{page.original_title}\n\n{page.summary}"
    return text, page.url