import app as project
import unittest


class TestAppWeb(unittest.TestCase):

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
        # images
        images = self.app.get('/g/51971506/')
        self.assertEqual(images.status_code, 200)

    def test_get_404(self):
        # threads
        threads = self.app.get('/xxx/')
        self.assertEqual(threads.status_code, 404)
        # images
        # TODO more tests


if __name__ == '__main__':
    unittest.main()
