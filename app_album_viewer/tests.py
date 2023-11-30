from django.test import TestCase


class AlbumsIndexPageTests(TestCase):

    """Test whether our albums index view page"""

    def setUp(self):
        # Will be used to do any set up before test cases
        return

    def test_album_page(self):
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, 200)
