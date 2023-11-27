from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import datetime


valid_formats = ["Digital download", "CD", "Vinyl"]

def validate_format(value):
    if not valid_formats.__contains__(value):
        raise ValidationError(_("InvalidFormat"))


def validate_release_date(value):
    if value.year > datetime.date.today().year + 3:
        raise ValidationError(_("ReleaseDateTooFar"))
    elif value.year > datetime.date.today().year + 1:
        value.month = 1


class Album(models.Model):
    class Comments(models.Model):
        user_display_name = "" #TODO
        message = "" #TODO

    cover = models.ImageField(default="/media/default-cover.png",
                            upload_to="media")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    artist = models.CharField(max_length=60)
    price = models.DecimalField()
    format = models.CharField(validators=[validate_format])
    release_date = models.DateField(validators=[validate_release_date])
    #assocSongs
    comments = models.Aggregate(Comments.user_display_name
                            + Comments.message) #TODO Double check this works


class Song(models.Model):
    title = models.CharField(max_length=200)
    runtime = models.IntegerField()
    album = models.Aggregate() #TODO


class User(models.Model):
    email = models.CharField(max_length=250)
    username = models.CharField(max_length=100)
    password = "password"
    user_display_name = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
