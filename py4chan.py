from bs4 import BeautifulSoup

# config for debug
# logger = logging.basicConfig(format='''\033[1m%(asctime)s\033[0m
                                    # \033[92m%(message)s \033[0m''',
                             # datefmt='%m/%d/%Y %I:%M:%S %p',
                             # level=logging.DEBUG)


def get_boards(context: str) -> dict:
    if isinstance(context, str):
        soup_chan = BeautifulSoup(context, 'html5lib')

        # find all links for boards
        links = soup_chan.find_all('a', class_='boardlink')

        # dict comprehension for create all links and remove popular threads
        boards = dict((name.string, 'https:'+url['href'])
                      for name, url in zip(links, links)
                      if name.string is not None)

        return boards
    else:
        return None



def get_threads(context: str, preview=50) -> tuple:
    if isinstance(context, str):
        # parse html
        soup_threads = BeautifulSoup(context, 'html5lib')
        # just a filter for a listcomps
        list_threads = soup_threads.find_all('div', class_='thread')
        # a tuple comps -> (('id', 'description')...)
        threads = tuple((int(thread['id'][1:]),
                        thread.find(class_='postMessage').get_text()[:preview])
                        for thread in list_threads)

        return threads


def get_images_links(context: str) -> tuple:
    if isinstance(context, str):
        soup_images = BeautifulSoup(context, 'html5lib')
        list_links = soup_images.find_all('a', class_='fileThumb')
        links = tuple('https:'+x['href'] for x in list_links)
        return links
