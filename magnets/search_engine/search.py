html = '<div class="udacity float-left"><a href="http://udacity.com">'


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url, end_pos = get_next_target(page)
        if url:
            links.append(url)
            page = page[end_pos:]
        else:
            break
    return links

# print get_page()
print get_next_target(html)
print get_all_links(html)
