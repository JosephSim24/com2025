from django.core.management.base import BaseCommand
from app_album_viewer.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        Album.objects.all().delete()
        Comment.objects.all().delete()
        Song.objects.all().delete()
        Profile.objects.all().delete()

        a1=Album(title="Dripping Stereo (Deluxe Edition)", artist="Jonathan Rocs", cover="media/dripping-stereo.png", description="A very unique album from JRocs!", price=5, format="Vinyl", release_date="2023-06-06")
        a1.save()

        a2=Album(title="Music for Cats", artist="MyCatMusicCo", cover="media/music-for-cats.png", description="Your cats will enjoy", price=35, format="Digital Download", release_date="2023-06-06")
        a2.save()

        a3=Album(title="My Red House", artist="Agnes Merrello", cover="media/my-red-house.png", description="The soulful audio experience from Agnes Merrello", price=3, format="CD", release_date="2023-06-06")
        a3.save()

        a4=Album(title="My Red House", artist="Agnes Merrello", cover="media/my-red-house.png", description="The soulful audio experience from Agnes Merrello, now on Vinyl!", price=12, format="Vinyl", release_date="2023-06-06")
        a4.save()

        a5=Album(title="OUR TECHNICOLOUR (world)", artist="pippumpkin", cover="media/our-technicolour-world.png", price=1.99, format="Digital Download", release_date="2023-06-06")
        a5.save()

        a6=Album(title="sealife part II reprise EP", artist="Tom Turle and Friends", cover="media/sealife.png", price=0, release_date="2023-06-06")
        a6.save()
        a7=Album(title="Biggest Hits Compilation", artist="Songster", price=1.99, format="Digital Download", release_date="2023-06-06")
        a7.save()

        self.stdout.write('Albums done')

        s=Song(title="its too loud", runtime=294, albums=a1)
        s.save()
        s=Song(title="oh actually its fine", runtime=231, albums=a1)
        s.save()
        s=Song(title="nope too loud", runtime=127, albums=a1)
        s.save()
        s=Song(title="Running without a care at 4am", runtime=1000, albums=a2)
        s.save()
        s=Song(title="Snoozing all day", runtime=1505, albums=a2)
        s.save()
        s=Song(title="My bowl is empty (again) (sad version)", runtime=340, albums=a2)
        s.save()
        s=Song(title="The dog is back", runtime=134, albums=a2)
        s.save()
        s=Song(title="BRICKS ARE FALLING", runtime=180, albums=(a3, a4))
        s.save()
        s=Song(title="THE HEARTH AND HOME", runtime=182, albums=(a3, a4, a7))
        s.save()
        s=Song(title="LEAKY ROOF", runtime=189, albums=(a3, a4, a7))
        s.save()

        self.stdout.write('Songs done')

        #TODO seed the database with profiles and users



        #TODO change the parameters of Comment to accomodate the user

        c1=Comment(user_display_name="AnnaB93", message="Not a fan to be honest")
        c2=Comment(user_display_name="AnnaB93", message="Actually, it's pretty good")
        c3=Comment(user_display_name="jc2", message="Best album yet!!!!")
        c1.save()
        c2.save()
        c3.save()

        c4=Comment(user_display_name="jonManco", message="My cats and I love it")
        c5=Comment(user_display_name="AnnaB93", message="Is this for cats or humans?? Kind of liking it")
        c6=Comment(user_display_name="jc2", message="Far too expensive :-(")
        c4.save()
        c5.save()
        c6.save()

        c7=Comment(user_display_name="jonManco", message="CD isn't worth it, go for vinyl one")
        c8=Comment(user_display_name="jc2", message="Arrived scratched :'-(")
        c7.save()
        c8.save()

        c9=Comment(user_display_name="jonManco", message="Vinyl is the best version!")
        c9.save()

        c10=Comment(user_display_name="someguy", message="first")
        c10.save()