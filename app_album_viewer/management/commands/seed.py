from django.core.management.base import BaseCommand
from app_album_viewer.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        Album.objects.all().delete()
        a=Album(title="Dripping Stereo (Deluxe Edition)", artist="Jonathan Rocs", cover="media/dripping-stereo.png", description="A very unique album from JRocs!", price=5, format="Vinyl", release_date="2023-06-06")
        a.save()
        a=Album(title="Music for Cats", artist="MyCatMusicCo", cover="media/music-for-cats.png", description="Your cats will enjoy", price=35, format="Digital Download", release_date="2023-06-06")
        a.save()
        a=Album(title="My Red House", artist="Agnes Merrello", cover="media/my-red-house.png", description="The soulful audio experience from Agnes Merrello", price=3, format="CD", release_date="2023-06-06")
        a.save()
        a=Album(title="My Red House", artist="Agnes Merrello", cover="media/my-red-house.png", description="The soulful audio experience from Agnes Merrello, now on Vinyl!", price=12, format="Vinyl", release_date="2023-06-06")
        a.save()
        a=Album(title="OUR TECHNICOLOUR (world)", artist="pippumpkin", cover="media/our-technicolour-world.png", price=1.99, format="Digital Download", release_date="2023-06-06")
        a.save()
        a=Album(title="sealife part II reprise EP", artist="Tom Turle and Friends", cover="media/sealife.png", price=0, release_date="2023-06-06")
        a.save()
        a=Album(title="Biggest Hits Compilation", artist="Songster", price=1.99, format="Digital Download", release_date="2023-06-06")
        a.save()

        self.stdout.write('done.')