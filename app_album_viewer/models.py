from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import datetime


valid_formats = ["Digital download", "CD", "Vinyl"]

def validate_format(value):
    if not valid_formats.__contains__(value):
        raise ValidationError(_("InvalidFormat"))


def h():


class Album(models.Model):
    #cover
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    artist = models.CharField(max_length=60)
    price = models.DecimalField()
    format = models.CharField(validators=[validate_format])
    #release_date
    #assocSongs
    #comments
