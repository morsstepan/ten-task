import helpers.helper as helper


def readData():
    if len(helper.sys.argv) == 1:
        print('You need to specify the web-site')
        exit()
    elif len(helper.sys.argv) >= 1:
        data = processUrl()
    return data


def processUrl():
    for arg in helper.sys.argv[1:]:
        print('Scraping from ' + str(arg) + '...')
        article = helper.MyArticle(arg, language='ru')
    return article


def processPage(soup, arg):
    title = soup.title.text
    text = ''
    for tag in soup.findAll('p'):
        try:
            print('--------------------')
            print(tag.contents[0])
            text += str(tag.contents[0])
        except IndexError:
            return
    link = arg
    article = helper.Article(title, text, link)
    return article
