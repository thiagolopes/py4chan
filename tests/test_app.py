import app as project
import unittest


class TestAppWeb(unittest.TestCase):
    # TODO more tests

    def setUp(self):
        project.app.testing = True
        self.app = project.app.test_client()

    def test_get_responses(self):
        # boards
        boards = self.app.get('/')
        self.assertEqual(boards.status_code, 200)
        # threads
        threads = self.app.get('/g/')
        self.assertEqual(threads.status_code, 200)
        # page
        page = self.app.get('/g/?page=2')
        self.assertEqual(page.status_code, 200)
        # images
        images = self.app.get('/g/51971506/')
        self.assertEqual(images.status_code, 200)

    def test_get_404(self):
        # threads
        threads = self.app.get('/xxx/')
        self.assertEqual(threads.status_code, 404)
        # images
        images = self.app.get('/g/66666666/')
        self.assertEqual(images.status_code, 404)
        # pages
        page = self.app.get('/g/?page=11')
        self.assertEqual(page.status_code, 404)


if __name__ == '__main__':
    unittest.main()
