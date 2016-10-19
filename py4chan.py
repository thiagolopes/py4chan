import requests
import os
from clint.textui import progress

class Py4chan(object):

    def __init__(self, board, number):
        self.__board = board
        self.__number = number
        self.__Text = 'href="//i.4cdn.org/'+self.__board+'/'
        self.__Links= []
        self.__Url = None

    def __str__(self):
        if self.__Url == None:
            return "Dont have valid thread"
        else:
            if not self.__Links:
                msg = "Board: /{}/ \nThread: {} \nUrl: {}".format(self.__board,self.__number,self.__Url)
            else:
                msg = "Board: /{}/ \nThread: {} \nUrl: {} \nI found {} images in Thread".format(
                    self.__board,self.__number,self.__Url,len(self.__Links))

            return msg

    def verific_url(self):
        self.__Url = 'https://boards.4chan.org/'+self.__board+'/thread/'+self.__number
        self.link = requests.get(self.__Url)
        if self.link.status_code == requests.codes.ok:
            self.__Url = self.__Url
            return self.__Url
        else:
            self.__Url = None
            return "Error url"

    def get_links_content(self):
        self.requesthttp = requests.get(self.__Url)
        self.content = str(self.requesthttp.content)

        for n in self.content.split():
            if n.find(self.__Text) != -1:
                if self.__Links.count(n) == 0:
                    self.__Links.append(n)

        self.__creat_dir()
        self.__clear_Link()

    def __creat_dir(self):
        if not os.path.exists(self.__number):
            os.mkdir(self.__number)

    def __clear_Link(self):
        for n in range(0,len(self.__Links)):
            # security for dont remove last letter
            if self.__Links[n][-1] == '"':
                self.__Links[n] = self.__Links[n][:-1]
            # remove href
            removehref = self.__Links[n]
            self.__Links[n] = removehref.replace('href="','https:')

    def download_images(self):
        for n in self.__Links:
            image_link = n
            image_name = n.split('/')[4]
            r = requests.get(image_link, stream = True)

            with open(self.__number+'/'+image_name, 'wb') as f:
                length = int(r.headers.get('content-length'))
                print(image_name+' ')
                for chunk in progress.bar(r.iter_content(chunk_size=1024),expected_size=(length/1024) + 1):
                    f.write(chunk)
                    f.flush()
    @property
    def Links(self):
        return self.__Links

    @property
    def Url(self):
        return self.__Url

    @property
    def Board(self):
        return self.__board

    @property
    def Thread(self):
        return self.__number
