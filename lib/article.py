from lib import helper


class MyArticle(helper.Article):

    def __checkTitle(self):
        if self.title is not '':
            fileName = self.title + '.docx'
        else:
            fileName = 'untitled_article_' + \
                helper.strftime("%Y-%m-%d %H:%M:%S", helper.gmtime()) + '.docx'
        return fileName

    def __checkIfThereIsImage(self):
        if self.top_image is not '':
            return True
        else:
            return False

    def __saveImage(self):
        # sys.path.insert(0, './lib')
        image_url = self.top_image
        image_name = self.top_image.split('/')[-1]
        path = helper.pjoin("images", image_name)
        helper.ImageSaver(image_url, path)
        return path

    def __checkIfThereAreVideosInArticle(self):
        if self.movies:
            return True

        else:
            return False

    def __processVideos(self, document):
        if(self.__checkIfThereAreVideosInArticle()):
            print('was here too but idk why')
            document.add_paragraph(
                'Videos from this webpage are available: ' + str(self.movies))

    def __processImage(self, document):
        if(self.__checkIfThereIsImage()):
            image_name = self.__saveImage()
            document.add_picture(image_name, width=helper.Inches(3.25))

    def saveArticle(self):
        path = helper.pjoin("articles", self.__checkTitle())
        document = self.__processArticle()
        print('Saving a file ' + self.__checkTitle() + ' to /articles/')
        document.save(path)

    def __processArticle(self):
        document = helper.Document()
        document.add_heading(self.title)
        self.__processImage(document)
        document.add_paragraph(self.text)
        self.__processVideos(document)
        # print(self.html)
        # self.__findLinks()
        return document
