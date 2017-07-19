import helpers.helper as helper
# import modules.reading_module as read


def main():
	def printGreeting():
		print('This program was created for scraping web-sites.')
	printGreeting()

	def readData():
		if len(helper.sys.argv) == 1:
			print('You need to specify the web-site')
			exit()
		elif len(helper.sys.argv) >= 1:
			processUrl()

	def processUrl():
		for arg in helper.sys.argv[1:]:
			print('Scraping from ' + str(arg) + '...')
			article = helper.MyArticle(arg, language='ru')
			article.download()
			# print(article)
			article.parse()
			article.saveArticle()

	try:
		readData()
	except helper.ArticleException:
		print('You need to input a correct website. \nCheck your input data.')
		exit()


main()
