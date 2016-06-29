import requests
import os
from clint.textui import progress

class chandownloader:

    def __init__(self, board, number):
        self.board = board
        self.number = number
        self.Text = 'href="//i.4cdn.org/'+self.board+'/'
        self.Links= []
        self.Url = None

    def __str__(self):
        if self.Url == None:
            return "Dont have valid thread"
        else:
            if not self.Links:
                msg = "Board: /{}/ \nThread: {} \nUrl: {}".format(self.board,self.number,self.Url)
            else:
                msg = "Board: /{}/ \nThread: {} \nUrl: {} \nI found {} images in Thread".format(
                    self.board,self.number,self.Url,len(self.Links))

            return msg

    def verific_url(self):
        self.url = 'https://boards.4chan.org/'+self.board+'/thread/'+self.number
        self.link = requests.get(self.url)
        if self.link.status_code == requests.codes.ok:
            self.Url = self.url
            return self.Url
        else:
            self.Url = None
            return "Error url"

    def get_links_content(self):
        self.requesthttp = requests.get(self.Url)
        self.content = str(self.requesthttp.content)

        for n in self.content.split():
            if n.find(self.Text) != -1:
                if self.Links.count(n) == 0:
                    self.Links.append(n)

    def creat_dir(self):
        if not os.path.exists(self.number):
            os.mkdir(self.number)

    def clear_Link(self):
        for n in range(0,len(self.Links)):
            # security for dont remove last letter
            if self.Links[n][-1] == '"':
                self.Links[n] = self.Links[n][:-1]
            # remove href
            removehref = self.Links[n]
            self.Links[n] = removehref.replace('href="','https:')

    def download_images(self):
        for n in self.Links:
            image_link = n
            image_name = n.split('/')[4]
            r = requests.get(image_link, stream = True)

            with open(self.number+'/'+image_name, 'wb') as f:
                length = int(r.headers.get('content-length'))
                print(image_name+' ')
                for chunk in progress.bar(r.iter_content(chunk_size=1024),expected_size=(length/1024) + 1):
                    f.write(chunk)
                    f.flush()
