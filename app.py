import helpers.helper as helper
import modules.reading_module as read


def main():
    def printGreeting():
        print('This program was created for scraping web-sites.')
    printGreeting()
    try:
        article = read.readData()
        article.download()
        # print(a)
        article.parse()
        article.saveArticle()
    except helper.ArticleException:
        print('You need to input a correct website. \nCheck your input data.')
        exit()


main()
