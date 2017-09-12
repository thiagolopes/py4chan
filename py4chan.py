from bs4 import BeautifulSoup

# config for debug
# logger = loggin.basicConfig(format='''\033[1m%(asctime)s\033[0m
                                    # \033[92m%(message)s \033[0m''',
                             # datefmt='%m/%d/%Y %I:%M:%S %p',
                             # level=logging.DEBUG)


def get_boards(context: str, just_code=False) -> dict:
    if isinstance(context, str):
        soup_chan = BeautifulSoup(context, 'html5lib')

        # find all links for boards
        links = soup_chan.find_all('a', class_='boardlink')

        # dict comprehension for create all links and remove popular threads
        if just_code:
            boards = dict((name.string, '{}'.format(
                          url['href'].split('/')[-2]))
                          for name, url in zip(links, links)
                          if name.string is not None)
        # full link
        else:
            boards = dict((name.string, 'https:' + url['href'])
                          for name, url in zip(links, links)
                          if name.string is not None)

        return boards
    else:
        return dict()


# TODO implemente all pages threads
def get_threads(context: str, preview=True, length=50) -> list:
    if isinstance(context, str):
        # parse html
        soup_threads = BeautifulSoup(context, 'html5lib')
        # just a filter for a listcomps
        list_threads = soup_threads.find_all('div', class_='thread')
        # a tuple comps -> (('id', 'description')...)
        threads = list((int(thread['id'][1:]),
                        thread.find(class_='postMessage').get_text()[:length])

                       for thread in list_threads)
        return threads


def get_images_links(context: str, thumbs=False) -> tuple:
    if isinstance(context, str):
        soup_images = BeautifulSoup(context, 'html5lib')
        list_links = soup_images.find_all('a', class_='fileThumb')
        # change //.i to //.t, not to receive 403
        if thumbs:
            links = tuple('https:' +
                          x['href'].replace('//i.', '//t.')[:-4] +
                          's.jpg'
                          for x in list_links)
        else:
            links = tuple('https:' + x['href'].replace('//i.', '//t.')
                          for x in list_links)

        """
        the link for thumnais is //.t and xxxxxxxxs.jpg
        """
        return links
