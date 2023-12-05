from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app_album_viewer.models import *
from datetime import date

class Command(BaseCommand):

    def handle(self, *args, **options):
        Album.objects.all().delete()

        a1=Album(title="Dripping Stereo (Deluxe Edition)", artist="Jonathan Rocs", cover="media/dripping-stereo.png", description="A very unique album from JRocs!", price=5, format="Vinyl", release_date=date(2023, 6, 6))
        a1.save() 

        a2=Album(title="Music for Cats", artist="MyCatMusicCo", cover="media/music-for-cats.png", description="Your cats will enjoy", price=35, format="Digital Download", release_date=date(2023, 6, 6))
        a2.save()

        a3=Album(title="My Red House", artist="Agnes Merrello", cover="media/my-red-house.png", description="The soulful audio experience from Agnes Merrello", price=3, format="CD", release_date=date(2023, 6, 6))
        a3.save()

        a4=Album(title="My Red House", artist="Agnes Merrello", cover="media/my-red-house.png", description="The soulful audio experience from Agnes Merrello, now on Vinyl!", price=12, format="Vinyl", release_date=date(2023, 6, 6))
        a4.save()

        a5=Album(title="OUR TECHNICOLOUR (world)", artist="pippumpkin", cover="media/our-technicolour-world.png", price=1.99, format="Digital Download", release_date=date(2023, 6, 6))
        a5.save()

        a6=Album(title="sealife part II reprise EP", artist="Tom Turle and Friends", cover="media/sealife.png", price=0, release_date=date(2023, 6, 6))
        a6.save()
        a7=Album(title="Biggest Hits Compilation", artist="Songster", price=1.99, format="Digital Download", release_date=date(2023, 6, 6))
        a7.save()

        self.stdout.write('Albums done')

        Song.objects.all().delete()

        s=Song.objects.create(title="its too loud", runtime=294)
        s.albums.add(a1)

        s=Song.objects.create(title="oh actually its fine", runtime=231)
        s.albums.add(a1)

        s=Song.objects.create(title="nope too loud", runtime=127)
        s.albums.add(a1)

        s=Song.objects.create(title="Running without a care at 4am", runtime=1000)
        s.albums.add(a2)

        s=Song.objects.create(title="Snoozing all day", runtime=1505)
        s.albums.add(a2)

        s=Song.objects.create(title="My bowl is empty (again) (sad version)", runtime=340)
        s.albums.add(a2)

        s=Song.objects.create(title="The dog is back", runtime=134)
        s.albums.add(a2)

        s=Song.objects.create(title="BRICKS ARE FALLING", runtime=180)
        s.albums.add(a3, a4)

        s=Song.objects.create(title="THE HEARTH AND HOME", runtime=182)
        s.albums.add(a3, a4, a7)

        s=Song.objects.create(title="LEAKY ROOF", runtime=189)
        s.albums.add(a3, a4, a7)

        self.stdout.write('Songs done')

        User.objects.all().delete()
        Profile.objects.all().delete()

        user_data = [
            {"username": "anna.baston", "email": "AnnaB39@example.com", "display_name": "AnnaB39"},
            {"username": "james.cole", "email": "jc2@example.com", "display_name": "jc2"},
            {"username": "jon.manco", "email": "jonManco@example.com", "display_name": "jonManco"},
            {"username": "someguy", "email": "someguy@example.com", "display_name": "someguy"}
        ]
        password = "password"

        for data in user_data:
            username = data['username']
            email = data['email']
            display_name = data['display_name']
            
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password(password)
                user.save()
            
            profile, created = Profile.objects.get_or_create(user=user, defaults={'display_name': display_name})
            if not created:
                profile.display_name = display_name
                profile.save()

        self.stdout.write('Profiles done')

        Comment.objects.all().delete()

        u1=Profile.objects.get(display_name="AnnaB39")
        u2=Profile.objects.get(display_name="jc2")
        u3=Profile.objects.get(display_name="jonManco")
        u4=Profile.objects.get(display_name="someguy")

        c1=Comment(user=u1, message="Not a fan to be honest", album=a1)
        c2=Comment(user=u1, message="Actually, it's pretty good", album=a1)
        c3=Comment(user=u2, message="Best album yet!!!!", album=a1)
        c1.save()
        c2.save()
        c3.save()

        c4=Comment(user=u3, message="My cats and I love it", album=a2)
        c5=Comment(user=u1, message="Is this for cats or humans?? Kind of liking it", album=a2)
        c6=Comment(user=u2, message="Far too expensive :-(", album=a2)
        c4.save()
        c5.save()
        c6.save()

        c7=Comment(user=u3, message="CD isn't worth it, go for vinyl one", album=a3)
        c8=Comment(user=u2, message="Arrived scratched :'-(", album=a3)
        c7.save()
        c8.save()

        c9=Comment(user=u3, message="Vinyl is the best version!", album=a4)
        c9.save()

        c10=Comment(user=u4, message="first", album=a5)
        c10.save()

        self.stdout.write('Comments done')