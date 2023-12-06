from django.test import TestCase
from django.utils import timezone
from .models import Album


class AlbumsIndexPageTests(TestCase):

    """Test whether our albums index view page"""

    def setUp(self):
        # Will be used to do any set up before test cases
        return

    def test_album_page(self):
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, 200)


class AlbumModelTest(TestCase):
    def test_release_date_month(self):
        # Create an album with a release date more than 1 year away
        future_release_date = timezone.now().date() + timezone.timedelta(days=400)
        album = Album.objects.create(title='Test Album', release_date=future_release_date)

        # Refresh the album instance from the database to get the updated release_date
        album.refresh_from_db()

        # Check if the month of the release_date is 1
        self.assertEqual(album.release_date.month, 1)


