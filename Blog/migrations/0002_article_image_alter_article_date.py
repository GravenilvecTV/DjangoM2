# Generated by Django 5.0.3 on 2024-04-02 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.TextField(default='https://resize-elle.ladmedia.fr/rcrop/638,,forcex/img/var/plain_site/storage/images/elle-a-table/les-dossiers-de-la-redaction/dossier-de-la-redac/blog-cuisine/68970235-2-fre-FR/Quels-sont-les-10-blogs-de-cuisine-les-plus-influents.jpg'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 4, 2, 13, 41, 3, 205520, tzinfo=datetime.timezone.utc)),
        ),
    ]
