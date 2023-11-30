from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def validate_release_date(value):
    if value.year > datetime.date.today().year + 3:
        raise ValidationError(_("ReleaseDateTooFar"))
    elif value.year > datetime.date.today().year + 1:
        Album.release_date = [value.year + "-" + 1
                            + "-" + value.day]


class Comment(models.Model):
    user_display_name = models.CharField(max_length=50)
    message = models.TextField()


class Album(models.Model):
    class Format(models.TextChoices):
        DD = "DIGDL", _("Digital Download")
        CD = "CD", _("CD")
        VINYL = "VINYL", _("Vinyl")

    cover = models.ImageField(default="media/default-cover.png",
                            upload_to="media")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,
                                blank=True)
    artist = models.CharField(max_length=60)
    price = models.DecimalField(default=0.00,
                                max_digits=5,
                                decimal_places=2)
    format = models.CharField(max_length=5,
                            choices=Format.choices, 
                            default=Format.DD)
    release_date = models.DateField(null=True,
                        validators=[validate_release_date])
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE,
                            null=True, blank=True)

    def __str__(self):
        return self.artist + self.title


class Song(models.Model):
    title = models.CharField(max_length=200)
    runtime = models.IntegerField()
    albums = models.ManyToManyField(Album)


class Tracklist(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    songs = models.ForeignKey(Song, on_delete=models.CASCADE)
