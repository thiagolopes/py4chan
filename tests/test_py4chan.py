from py4chan import get_images_links, get_boards, get_threads
import unittest
import requests

# links 4chan
LINK_CHAN = 'https://www.4chan.org/'
LINK_THREAD = 'https://boards.4chan.org/{0}/thread/{1}'
LINK_BOARD = 'https://boards.4chan.org/{0}/'


class TestGetBoards(unittest.TestCase):

    def setUp(self):
        self.context = requests.get(LINK_CHAN)

    def test_get_boards_instance(self):
        self.assertIsInstance(get_boards(self.context.text), dict)

    def test_get_boards_instance_len(self):
        self.assertGreaterEqual(len(get_boards(self.context.text)), 70)

    def test_get_boards_none(self):
        self.assertIsInstance(get_boards(''), dict)

    def test_error_keyerror(self):
        self.assertEqual(get_boards(0), None)

    def test_get_boards_just_code(self):
        self.assertEqual(get_boards(self.context.text, True)['Random'], 'b')


class TestGetThreads(unittest.TestCase):
    def setUp(self):
        self.context = requests.get(LINK_BOARD.format('g'))
        self.get = get_threads(self.context.text)

    def test_get_threads_contains_number(self):
        self.assertEqual(self.get[0][0], 51971506)

    def test_get_threads_contains_string(self):
        self.assertEqual(len(self.get[0][1]), 50)

    def test_get_threads_instance(self):
        self.assertIsInstance(self.get, tuple)

    def test_get_threads_none(self):
        self.assertEqual(get_threads(''), ())

    def test_get_threads_is_int(self):
        self.assertIsInstance(self.get[0][0], int)


class TestGetImagesLinks(unittest.TestCase):
    def setUp(self):
        self.context = requests.get(LINK_THREAD.format('g', '51971506'))
        self.get = get_images_links(self.context.text)

    def test_get_images(self):
        self.assertIsInstance(self.get, tuple)
        self.assertEqual(len(self.get), 1)
        self.assertEqual(self.get[0], 'https://t.4cdn.org/g/1450659832892.png')


if __name__ == '__main__':
    unittest.main()
