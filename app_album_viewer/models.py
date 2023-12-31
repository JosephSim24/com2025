from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Album(models.Model):
    class Format(models.TextChoices):
        DD = "Digital Download", _("Digital Download")
        CD = "CD", _("CD")
        VINYL = "Vinyl", _("Vinyl")

    cover = models.ImageField(default="media/default-cover.png",
                            upload_to="media/")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,
                                blank=True)
    artist = models.CharField(max_length=200)
    price = models.DecimalField(default=0,
                                max_digits=7,
                                decimal_places=2)
    format = models.CharField(max_length=16,
                            choices=Format.choices, 
                            default=Format.DD)
    release_date = models.DateField(default=models.DateField(auto_now_add=True))

    def save(self, *args, **kwargs):
        from datetime import timedelta
        import pytz

        if self.release_date > timezone.now().date() + timedelta(days=365):
            self.release_date = self.release_date.replace(month = 1)
        super().save(*args, **kwargs)

    def add_song(self, song):
        self.songs.add(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=200)
    runtime = models.PositiveIntegerField()
    albums = models.ManyToManyField(Album, related_name='songs')

    def format_runtime(self):
        mins = self.runtime // 60
        secs = self.runtime % 60
        format_runtime = "{:02d}".format(secs)
        return f"{mins}:{format_runtime}"

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200)

    def __str__(self):
        return self.display_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE,
                            related_name='comments')

