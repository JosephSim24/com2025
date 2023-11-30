# Generated by Django 4.2.6 on 2023-11-30 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_album_viewer', '0002_alter_album_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='albums',
            field=models.ManyToManyField(to='app_album_viewer.album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='format',
            field=models.CharField(choices=[('DIGDL', 'Digital Download'), ('CD', 'CD'), ('VINYL', 'Vinyl')], default='DIGDL', max_length=5),
        ),
        migrations.CreateModel(
            name='Tracklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_album_viewer.album')),
                ('songs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_album_viewer.song')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
