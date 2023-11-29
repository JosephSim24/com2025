from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import datetime


def validate_release_date(value):
    if value.year > datetime.date.today().year + 3:
        raise ValidationError(_("ReleaseDateTooFar"))
    elif value.year > datetime.date.today().year + 1:
        Album.release_date = [value.year + "-" + 1
                            + "-" + value.day]


class Album(models.Model):
    class Comment(models.Model):
        user_display_name = models.CharField(max_length=50)
        message = models.TextField()

    class Format(models.TextChoices):
        DD = "DD", _("DigitalDownload")
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
    #assocSongs
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE,
                            null=True, blank=True)

    def __str__(self):
        return self.artist + self.title + self.price

class Song(models.Model):
    title = models.CharField(max_length=200)
    runtime = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


#class User(models.Model):
    #email = models.CharField(max_length=250)
    #username = models.CharField(max_length=100)
    #password = "password"
    #user_display_name = models.CharField(max_length=100)
    #message = models.CharField(max_length=1000)
